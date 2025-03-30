package javaapplication1;

import java.util.Scanner;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Balcao {
   String filme = "teste filme";
   int pedido = 0;
   Pipoca pipoca = new Pipoca();


   public String escolherPedido() throws InterruptedException {
      CompletableFuture<String> future1 = CompletableFuture.supplyAsync(() -> {
         try {
            this.pipoca.getPipoca();
         } catch (InterruptedException var1) {
            Logger.getLogger(JavaApplication1.class.getName()).log(Level.SEVERE, (String)null, var1);
         }

         return "Pegou a pipoca";
      });
      CompletableFuture<String> future2 = CompletableFuture.supplyAsync(() -> {
         try {
            Refrigerante refri = new Refrigerante();
            refri.get_Refrigerante();
         } catch (InterruptedException var1) {
            Logger.getLogger(JavaApplication1.class.getName()).log(Level.SEVERE, (String)null, var1);
         }

         return "Pegou o refrigerante";
      });

      // The completion of the resulting objects is dependent on the completion of all subsequent Futures
      // allOf() is not a blocking method  Wait for all the CompleteFuture to complete
      // thenApply() =>  we can concatenate the values of the three futures and continue the non-blocking flow with the resulting String:
      //CompletableFuture<String> allFutures = CompletableFuture.allOf(future1, future2).thenApply(__ -> future1.join() + "," + future2.join()); 
      CompletableFuture<String> allFutures = CompletableFuture.allOf(future1, future2).thenApply(__ -> "Pedido Pronto"); 
      // método garante que as tarefas sejam executadas de maneira assíncrona, ou seja, em paralelo, sem bloquear a execução do programa. 
      
      // join() => é um método bloqueante
      System.out.println(allFutures.join()); // aguarda até que todas as tarefas assíncronas estejam concluídas e, então, retorna o resultado da execução

      
      
      return "Pedido pronto";
   }
}

