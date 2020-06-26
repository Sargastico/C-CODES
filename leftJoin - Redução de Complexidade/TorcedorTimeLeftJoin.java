import java.util.ArrayList;

public class TorcedorTimeLeftJoin {

    String id;
    String id_time;
    String id_time_nome;
    String nome;

    public TorcedorTimeLeftJoin(String id, String id_time, String id_time_nome, String nome){

        this.id = id;
        this.id_time = id_time;
        this.id_time_nome = id_time_nome;
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

    public String getId_time_nome() {
        return id_time_nome;
    }

    public void setId_time_nome(String id_time_nome) {
        this.id_time_nome = id_time_nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}
