import com.fasterxml.jackson.core.JsonProcessingException;

import java.io.File;
import java.io.IOException;
import java.util.*;


public class leftJoin {


    public static ArrayList<String[]> readcsv(String filepath) throws JsonProcessingException, IOException {

        Scanner scan = new Scanner(new File(filepath));
        ArrayList<String[]> records = new ArrayList<String[]>();
        String[] record = new String[2];
        while (scan.hasNext()) {
            record = scan.nextLine().split(",");
            records.add(record);
        }

        return records;
    }


    public void leftJoinTwoFor(ArrayList<String[]> dados1, ArrayList<String[]> dados2){

        ArrayList<TorcedorTimeLeftJoin> match = new ArrayList<>();

        for (int i = 1; i < (long) dados1.size(); i++) {
            for (int j = 1; j < (dados2.size()); j++) {

                String idTimeTabela1 = (dados1.get(i))[1];
                String idTimeTabela2 = (dados2.get(j))[0];

                if (idTimeTabela1.equals(idTimeTabela2)){

                    String[] dadosx1 = dados1.get(i);
                    String[] dadosx2 = dados2.get(j);

                    match.add(new TorcedorTimeLeftJoin( dadosx1[0],
                            dadosx1[1],
                            dadosx2[1],
                            dadosx1[2]
                    ));
                }
            }
        }
        for (TorcedorTimeLeftJoin pojoLinhaJoin : match) {
            System.out.println(pojoLinhaJoin.getId() + " " + pojoLinhaJoin.getId_time() + " " + pojoLinhaJoin.getId_time_nome() + " " + pojoLinhaJoin.getNome());
        }
    }


    public void leftJoinOneFor(ArrayList<String[]> listaTorcedores, ArrayList<String[]> listaTimes){


        Map<String, Time> timesMap = new HashMap<>();
        List<TorcedorTimeLeftJoin> torcedorTimeLeftJoins = new ArrayList<>();

        for (int i=0; i < listaTimes.size(); i++){
            timesMap.put(String.valueOf(i), new Time(listaTimes.get(i)[0], listaTimes.get(i)[1]));
        }

        for (String[] torcedor:listaTorcedores
        ) {
            if(timesMap.containsKey(torcedor[1])) {
                torcedorTimeLeftJoins.add(new TorcedorTimeLeftJoin(torcedor[0], torcedor[2], timesMap.get(torcedor[1]).getId(), timesMap.get(torcedor[1]).getNome_time()));
            }
            else {
                torcedorTimeLeftJoins.add(new TorcedorTimeLeftJoin(torcedor[0], torcedor[2], null, null));
            }
        }

        for (TorcedorTimeLeftJoin pojoLinhaJoin : torcedorTimeLeftJoins) {
            System.out.println(pojoLinhaJoin.getId() + " " + pojoLinhaJoin.getId_time() + " " + pojoLinhaJoin.getId_time_nome() + " " + pojoLinhaJoin.getNome());
        }



    }

}

