package Tarefa7;

public class Triangulo implements ITriangulo{
    //Atributos

    private double base;
    private double altura;
    private double area;

    //Métodos
    // Setters e Getters

    public void setBase(double base) {
        this.base = base;
    }
   
    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double getBase() {
        return base;
    }

    public double getAltura() {
        return altura;
    }

    // Calculo da área

    public double getArea() {
        this.area = ((this.base * this.altura) / 2);
        return this.area;
    }
}
