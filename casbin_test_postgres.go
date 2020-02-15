package main

import (
	"database/sql"
	"fmt"
	"github.com/casbin/casbin"
	"github.com/cychiuae/casbin-pg-adapter"
	"os"
)

const (
	host     = ""
	port     = 5432
	user     = "postgres"
	password = ""
	dbname   = ""
)


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
		fmt.Print("\n[+] Politicas carregadas com sucesso.")
	}

	if os.Args[1] == "add"{
		_, err = enforcer.AddPolicy(os.Args[2], os.Args[3], os.Args[4])
		if err != nil{
			fmt.Print("\n[-] Erro ao adicionar nova politica.")
			panic(err)
		} else {
			fmt.Print("\n[+] Politica adicionada!")
		}
	} else if os.Args[1] == "remove"{
		_, err = enforcer.RemovePolicy(os.Args[2],os.Args[3],os.Args[4])
		if err != nil{
			fmt.Print("\n[-] Erro ao remover politica.")
			panic(err)
		} else {
			fmt.Print("\n[+] Politica removida!")
		}
	} else if os.Args[1] == "check" {
		msg, err := enforcer.Enforce(os.Args[2],os.Args[3],os.Args[4])
		if err != nil{
			fmt.Print("\n[-] Erro ao checar politica.")
		}else {
			fmt.Print("\n[+] Check: ", msg)
		}
	}

	enforcer.SavePolicy()

}



