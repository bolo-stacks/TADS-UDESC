package Tarefa4;
public class Calculadora implements ICalculadora {
    //Atributos 
    private double numero1;
    private double numero2;
   
    //Construtor sem parâmetros
    public Calculadora() {
        setNumero1(0);
        setNumero2(0);
    }
    
    //Construtor com parâmetros
    public Calculadora(double numero1, double numero2) {
        setNumero1(numero1);
        setNumero2(numero2);
    }
    
    //Get de numero1
    public double getNumero1() {
        return numero1;
    }
    
    //Get de numero2
    public double getNumero2() {
        return numero2;
    }
    
    //Set de numero1
    public void setNumero1(double numero1) {
        this.numero1 = numero1;
    }
    
    //Set de numero2
    public void setNumero2(double numero2) {
        this.numero2 = numero2;
    }
    
    //Implementação dos métodos da interface ICalculadora
    public double getSoma() {
        return numero1 + numero2;
    }

    public double getDiferenca() {
        return numero1 - numero2;
    }

    public double getProduto() {
        return numero1 * numero2;
    }

    public double getQuociente() {
        return numero1 / numero2;
    }
}


