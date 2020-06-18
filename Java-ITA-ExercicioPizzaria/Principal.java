public class Principal {

    public static void main(String[] args){

    Pizza pizza1 = new Pizza();
    Pizza pizza2 = new Pizza();
    Pizza pizza3 = new Pizza();

    CarrinhoDeCompras carrinho = new CarrinhoDeCompras();

    pizza1.adicionaIngrediente("queijo");


    pizza2.adicionaIngrediente("frango");
    pizza2.adicionaIngrediente("Catupiry");
    pizza2.adicionaIngrediente("oregano");


    pizza3.adicionaIngrediente("Calabresa");
    pizza3.adicionaIngrediente("Calabresa");
    pizza3.adicionaIngrediente("Queijo");
    pizza3.adicionaIngrediente("Macarrão");
    pizza3.adicionaIngrediente("sorvete");
    pizza3.adicionaIngrediente("caviar");
    pizza3.adicionaIngrediente("cebola");

    System.out.println("-------------------------------------------------------------------");
    System.out.println("Pizza 1: \n");
    carrinho.addCarrinho(pizza1);


    System.out.println("Pizza 1: \n");
    carrinho.addCarrinho(pizza2);

    System.out.println("-------------------------------------------------------------------");
    System.out.println("Pizza 3: \n");
    carrinho.addCarrinho(pizza3);


    System.out.println("-------------------------------------------------------------------");
    System.out.println("Preço total das pizzas: "+ CarrinhoDeCompras.getTotalPizzasValue());

    }
}
