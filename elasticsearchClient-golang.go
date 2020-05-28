//Elasticsearch client example using golang.

//Default config: elasticsearch server service running on localhosta:9200 <-> elastic:changeme

//Create a JSON file and name as 'query.json'. Inside the file, paste de query to performe the search 
//									  |
//									  |__ You can forge a query using Kibana!!! 

package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"strings"

	"github.com/elastic/go-elasticsearch"
)

func main() {

	// Create a context object for the API calls
	ctx := context.Background()

	// Declare an Elasticsearch configuration
	cfg := elasticsearch.Config{
		Addresses: []string{"http://localhost:9200"},
		Username: "elastic",
		Password: "changeme",
	}

	// Instantiate a new Elasticsearch client object instance
	client, err := elasticsearch.NewClient(cfg)

	// Exit the system if connection raises an error
	if err != nil {
		log.Fatalf("Elasticsearch connection error:", err)
	}

	var buf bytes.Buffer

	//Read Json Query
	query, err := ioutil.ReadFile("./query.json")
	queryS := string(query)
	if err != nil {
		fmt.Print(err)
	}

	var b strings.Builder
	b.WriteString(queryS)
	read := strings.NewReader(b.String())


	// Attempt to encode the JSON query and look for errors
	err = json.NewEncoder(&buf).Encode(read)
	if err != nil {
		log.Println("Error encoding query: %s", err)

	} else {
		fmt.Println("json.NewEncoder encoded query:", read, "\n")

		// Pass the JSON query to the Golang client's Search() method
		res, err := client.Search(client.Search.WithContext(ctx),client.Search.WithBody(read))
		if err != nil {
			log.Println("Elasticsearch API ERROR:", err)

		} else {

			bodyBytes, err := ioutil.ReadAll(res.Body)
			if err != nil {
				log.Fatal(err)
			}
			bodyString := string(bodyBytes)
			fmt.Println(bodyString)

			defer res.Body.Close()
		}

	}
}
