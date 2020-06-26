import java.io.IOException;
import java.util.ArrayList;

class main {

    public static <string> void main(String[] args) throws IOException {

        ArrayList<String[]> listaTorcedores = leftJoin.readcsv("\\tabelaOne.csv");
        ArrayList<String[]> listaTimes = leftJoin.readcsv("\\tabelaTwo.csv");

        leftJoin join = new leftJoin();

        System.out.println("\nExecutando leftJoin com 2 FORs Loops\n");
        join.leftJoinTwoFor(listaTorcedores, listaTimes);

        System.out.println("\nExecutando leftJoin com 1 FOR Loop\n");
        join.leftJoinOneFor(listaTorcedores, listaTimes);


    }

}

