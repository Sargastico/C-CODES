import java.util.ArrayList;

public class Torcedor {

    String id;
    String id_time;
    String nome;

    public Torcedor(String id, String id_time, String nome){

        this.id = id;
        this.id_time = id_time;
        this.nome = nome;

    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getId_time() {
        return id_time;
    }

    public void setId_time(String id_time) {
        this.id_time = id_time;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}
