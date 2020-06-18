import java.util.HashMap;
import java.util.Map;

public class CarrinhoDeCompras {

    HashMap<String, Integer> ingredientesUnidade = new HashMap<String, Integer>();

    static int  precoAll;
    int preco, qtd;

    public CarrinhoDeCompras(){

        precoAll = 0;

    }

    public void addCarrinho(Pizza pizza) {

        if (pizza.numIngredientes == 0) {
            System.out.println("[!!] Não é possível adicionar pizzas sem ingredientes!");
        } else {
            this.ingredientesUnidade = pizza.ingredientes;
            getPreco();
            getIngredientes();

        }
    }

    public void getIngredientes() {
        for (Map.Entry<String,Integer> i : ingredientesUnidade.entrySet()) {
            if (i.getValue() != null) {
                System.out.println("Ingrediente: "+ i.getKey() + " | Qtd: " + i.getValue());
            }
        }
        System.out.println("\n");
    }

    public void getPreco(){
        preco = 0;
        for (Map.Entry<String,Integer> i : ingredientesUnidade.entrySet()) {
            if (i.getValue() != null) {
                qtd += i.getValue();
            }
        }
        if (qtd <= 2) {
            preco += 15;
        } else if (qtd >= 3 && qtd <= 5) {
            preco += 20;
        } else {
            preco += 23;
        }
        System.out.println("Preço da pizza: "+preco+"\n");
        precoAll += preco;
    }

    public static int getTotalPizzasValue(){
           return precoAll;
    }
}


