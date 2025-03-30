package javaapplication1;

public class Pipoca {
   int qtd_pacote = 0;

   public Pipoca() {
      this.qtd_pacote = 0;
   }

   private int fazerPipoca() throws InterruptedException {
      System.out.println("Fazendo pipoca");
      this.qtd_pacote = 0;
      Thread.sleep(10000);
      System.out.println("Pipoca feita");
      return 1;
   }

   public int getPipoca() throws InterruptedException {
      if (this.qtd_pacote == 1) {
         this.fazerPipoca();
      }

      System.out.println("Empacotando pipoca");
      Thread.sleep(7000);
      System.out.println("Pipoca empacotada");
      ++this.qtd_pacote;
      return 1;
   }
}

