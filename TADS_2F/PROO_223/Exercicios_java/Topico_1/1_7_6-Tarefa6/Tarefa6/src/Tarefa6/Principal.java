package Tarefa6;
import java.util.Scanner;

public class Principal {

    public static void main(String args[]) {
        //Objeto para a entrada de dados
        Scanner scanner = new Scanner(System.in);
        
        //Declara e instância um objeto chamado d1 da classe Data
        Data d1 = new Data();
        
        //Realiza a leitura do dia, mês e ano        
        System.out.println("Digite o dia:");
        d1.setDia(scanner.nextInt());
        System.out.println("Digite o mes:");
        d1.setMes(scanner.nextInt());
        System.out.println("Digite o ano:");
        d1.setAno(scanner.nextInt());
        
        //Escreve a data
        System.out.println("A data " + d1.getDia() + "/" + d1.getMes() + "/" + d1.getAno());
        //Verifica se o ano é bissexto
        if (d1.getBissexto()){
            System.out.println("O ano é bissexto");
        } else {
            System.out.println("O ano não é bissexto");
        }
    }
}

