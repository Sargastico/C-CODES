import java.util.HashMap;
import java.util.Map;

public class Pizza {

    static int  numIngredientesAll;
    int numIngredientes;

    HashMap<String, Integer> ingredientes = new HashMap<String, Integer>();

    public void adicionaIngrediente(String ingrediente){

        contabilizaIngrediente(ingrediente);
        numIngredientesAll++;
        numIngredientes++;
    }

    public void contabilizaIngrediente(String ingrediente){
            ingredientes.merge(ingrediente, 1, Integer::sum);
    }
}
