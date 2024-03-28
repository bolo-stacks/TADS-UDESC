package Tarefa5;

public class Funcionario implements IFuncionario{
    private int matricula;
    private String nome;
    
    //Construtor sem parâmetros   

    public Funcionario() {
        this.matricula = 0;
        this.nome = "";
    }
  
    //Construtor com parâmetros

    public Funcionario(int matricula, String nome) {
        this.matricula = matricula;
        this.nome = nome;
    }
        
    //set’s
    public void setMatricula(int matricula){
      this.matricula = matricula;
    }
    public void setNome(String nome){
      this.nome = nome;
    }
    //gets’s
    public int getMatricula(){
      return matricula;
    }
    public String getNome(){
      return nome;
    }
 }
