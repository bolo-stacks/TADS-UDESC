package Tarefa2;
public class Retangulo {
    //Atributos 
    private double altura;
    private double base;
   
    //Construtor sem parâmetros
    public Retangulo() {
        setBase(0);
        setAltura(0);
    }
    
    //Construtor com parâmetros
    public Retangulo(double base, double altura) {
        setBase(base);
        setAltura(altura);
    }
    
    //Get de altura
    public double getAltura() {
        return altura;
    }
    
    //Get de base
    public double getBase() {
        return base;
    }
    
    //Set de altura
    public void setAltura(double altura) {
        this.altura = altura;
        
    }
    
    //Set de base
    public void setBase(double base) {
        this.base = base;
        
    }
}