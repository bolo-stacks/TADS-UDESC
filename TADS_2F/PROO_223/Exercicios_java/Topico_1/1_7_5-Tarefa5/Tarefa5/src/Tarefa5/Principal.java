package Tarefa5;
import java.util.Scanner;

public class Principal {
    
    public static void main(String args[]) {
        //Objeto para a entrada de dados
        Scanner scanner = new Scanner(System.in);
        
        //******** Leitura do objeto 1
        
        //Declara e instância um objeto chamado obj1 da classe Funcionário
        Funcionario obj1 = new Funcionario();
        
        //******** Leitura do objeto 2
        
        //Realiza a leitura da matrícula e nome do funcionário para o objeto 2
        System.out.println("Digite a matricula:");
        int matricula = Integer.parseInt(scanner.nextLine());
        System.out.println("Digite o nome:");
        String nome = scanner.nextLine();
        
        //Declara e instância um objeto chamado obj2 da classe Funcionário usando o construtor com parâmetros
        Funcionario obj2 = new Funcionario(matricula, nome);
        
        //Saída de dados
        
        //Escreve os dados default do objeto 1
        System.out.println("Matricula:"+obj1.getMatricula());
        System.out.println("Nome:"+obj1.getNome());
        
        //Escreve os dados lidos objeto 2
        System.out.println("Matricula:"+obj2.getMatricula());
        System.out.println("Nome:"+obj2.getNome());
    }    
}
