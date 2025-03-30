package javaapplication1;

public class Refrigerante {
   public int get_Refrigerante() throws InterruptedException {
      System.out.println("Pegando o copo");
      Thread.sleep(5000);
      System.out.println("Pegou o refrigerante");
      return 1;
   }
}
    
