package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {

	gateway := gin.Default()

	gateway.LoadHTMLGlob("templates/*.html")

	gateway.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "home.html", nil)
	})

	gateway.GET("/wannacry.exe", func(c *gin.Context) {
		c.HTML(http.StatusOK, "wannacry.html", nil)
	})

	gateway.GET("/myIP", func(c *gin.Context) {

		c.JSON(200, gin.H{
			"message": c.ClientIP(),
		})
	})

	gateway.GET("/IsMyComputerOn?", func(c *gin.Context) {

		c.JSON(200, gin.H{
			"message": "yes",
		})
	})

	gateway.GET("/ReadPessoa", func(c *gin.Context) {

		nome := c.Query("nome")
		permissao := c.Query("permissao")
		id := c.Query("id")

		c.JSON(200, gin.H{

			"id":        id,
			"nome":      nome,
			"permissao": permissao,
		})
	})

	gateway.DELETE("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "not_allow.html", nil)
	})

	gateway.PUT("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "not_allow.html", nil)
	})

	gateway.Run(":80")
}
