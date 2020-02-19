package main

import (
	"database/sql"
	"fmt"
	"github.com/casbin/casbin"
	"github.com/cychiuae/casbin-pg-adapter"
	"os"
	"strconv"
	"time"
)

const (
	host     = ""
	port     = 5432
	user     = "postgres"
	password = ""
	dbname   = ""
)

func validateCheck(lista [][]string) bool{


	indexTime, err := time.Parse("2-Jan-2006_15:04",([]string{lista[0][3]})[0]) 	//Converte a string "index" em um objeto do tipo "Time"
	if err != nil{
		panic(err)
	}

	sinceTime := (time.Since(indexTime).Hours())/24 				//Calcula o Tempo em "dias" desde "indexTime"

	indexTimeP, err := strconv.ParseFloat(([]string{lista[0][4]})[0],8) 		//Converte string em variável do tipo float64
	if err != nil{
		panic(err)
	}


	if sinceTime > indexTimeP {							//Verifica se o tempo de criação da política já atingiu o prazo estabelecido.
		return false
	}

	return true
}

func SetPolicyTime() string {

	t := time.Now().Format("2-Jan-2006_15:04")
	return t
}

func formatList(lista [][]string){

	for i := range lista{
		fmt.Println(lista[i])
	}
}

func main(){

	postgresql := fmt.Sprintf("host=%s port=%d user=%s "+"password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)

	db, err := sql.Open("postgres", postgresql)
	defer db.Close()
	if err != nil{
		fmt.Print("\n[-] Erro ao abrir conexão com o DB")
		panic(err)
	}

	err = db.Ping()
	if err != nil{

		panic(err)

	} else {

		fmt.Print("\n[+] Conectado.")

	}

	tableName := "casbin"

	adapter, err := casbinpgadapter.NewAdapter(db, tableName)
	if err != nil {

		fmt.Print("\n Erro")
		panic(err)

	}

	enforcer, err := casbin.NewEnforcer("model.conf", adapter)
	if err != nil {
		panic(err)
	}

	err = enforcer.LoadPolicy()
	if err != nil{

		fmt.Print("\n[-]Erro ao carregar politicas.")
		panic(err)

	}else {

		fmt.Println("\n[+] Politicas carregadas com sucesso.")

	}

	if os.Args[1] == "add"{

		_, err = enforcer.AddPolicy(os.Args[2], os.Args[3], os.Args[4], SetPolicyTime(), os.Args[5])
		if err != nil{

			fmt.Print("\n[-] Erro ao adicionar nova politica.")
			panic(err)

		} else {

			fmt.Print("\n[+] Politica adicionada!")

		}

	} else if os.Args[1] == "remove"{

		_, err = enforcer.RemoveFilteredPolicy(0,os.Args[2])
		if err != nil{

			fmt.Print("\n[-] Erro ao remover politica.")
			panic(err)

		} else {

			fmt.Print("\n[+] Politica removida!")
		}

	} else if os.Args[1] == "check" {

		msg, err := enforcer.Enforce(os.Args[2], os.Args[3], os.Args[4], os.Args[5], os.Args[6])

		if err != nil{
			fmt.Print("\n[-] Erro ao checar politica.")
			panic(err)

		}else {

			validate := validateCheck(enforcer.GetFilteredPolicy(0, os.Args[2],os.Args[3],os.Args[4], os.Args[5]))

			fmt.Println("\nCheck:")
			fmt.Println(">>> Exist: ", msg)
			fmt.Println(">>> Valid: ", validate)
		}

	} else if os.Args[1] == "list"{

		fmt.Print("\n")
		formatList(enforcer.GetFilteredPolicy(0, os.Args[2]))

	}

	enforcer.SavePolicy()

}




