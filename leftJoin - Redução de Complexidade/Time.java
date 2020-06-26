public class Time {

    String id;
    String nome_time;

    public Time(String id, String id_time){

        this.id = id;
        this.nome_time = id_time;

    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNome_time() {
        return nome_time;
    }

    public void setNome_time(String nome_time) {
        this.nome_time = nome_time;
    }
}
