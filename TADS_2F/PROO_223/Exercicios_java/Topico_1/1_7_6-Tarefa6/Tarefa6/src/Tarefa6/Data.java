package Tarefa6;
public class Data {
    //Atributos
    private int dia;
    private int mes;
    private int ano;

    //Construtor sem parâmetros
    public Data() {
        this.dia = 0;
        this.mes = 0;
        this.ano = 0;
    }
    //Construtor com parâmetros
    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }
    //gets e sets
    public int getDia() {
        return dia;
    }

    public void setDia(int dia) {
        this.dia = dia;
    }

    public int getMes() {
        return mes;
    }

    public void setMes(int mes) {
        this.mes = mes;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }
    
    //Verifica se o ano é bissexto
    public boolean getBissexto(){
        boolean resultado = (getAno() % 400 == 0) || ((getAno() % 4 == 0) && (getAno() % 100 != 0));
        return resultado;
    }
}

