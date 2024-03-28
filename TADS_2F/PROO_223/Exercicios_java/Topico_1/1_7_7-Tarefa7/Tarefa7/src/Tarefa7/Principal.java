package Tarefa7;
import java.util.Scanner;

public class Principal {

    public static void main(String args[]) {
        //Objeto para a entrada de dados
        Scanner scanner = new Scanner(System.in);
        
        //Declara e instância um objeto chamado tri1 da classe Triângulo
        Triangulo tri1 = new Triangulo();
        
        //Realiza a leitura da base e altura
        System.out.println("Digite a base:");
        tri1.setBase(scanner.nextDouble());
        
        System.out.println("Digite a altura:");
        tri1.setAltura(scanner.nextDouble());
        
        //Escreve a área do triângulo
        System.out.println("A área é " + tri1.getArea());
    }
}