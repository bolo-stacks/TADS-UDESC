package Tarefa3;
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
    
    //Get da altura
    public double getAltura() {
        return altura;
    }
    
    //Get da base
    public double getBase() {
        return base;
    }
    
    //Set da altura
    public void setAltura(double altura) {
        this.altura = altura;
    }
    
    //Set da base
    public void setBase(double base) {
        this.base = base;
    }
    
    //Get Area
    public double getArea() {
        return this.base * this.altura;
    }
}
