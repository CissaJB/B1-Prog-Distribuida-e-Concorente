import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.ArrayList;
import java.util.List;

class Semaforo {
    private Lock lock = new ReentrantLock(); //previne o deadlock

    public void entrarNoCruzamento() {
        lock.lock(); //garantir que apenas um veículo tenha acesso ao cruzamento usando .lock
    }

    public void sairDoCruzamento() {
        lock.unlock(); //liberar o cruzamento usando o .unlock
    }
}

class Relatorio {
    private List<String> registros = new ArrayList<>(); //lista que vai armazenar os registros

    public synchronized void adicionarRegistro(String registro) {
        registros.add(registro); //adiciona registros ao relatório, usando o synchronized para não ter problema de corrida
    }

    public synchronized void imprimir() {
        System.out.println("\n=================== Relatório Final ===================");
        for (String registro : registros) {
            System.out.println(registro);
        }
        System.out.println("Simulação finalizada.");
    }
}

class Veiculo extends Thread {
    private int id;
    private Semaforo semaforo;
    private Relatorio relatorio;
    private long inicioEspera;

    //adiciona as informações do veículo
    public Veiculo(int id, Semaforo semaforo, Relatorio relatorio) {
        this.id = id;
        this.semaforo = semaforo;
        this.relatorio = relatorio;
        this.inicioEspera = System.currentTimeMillis();
    }

    @Override //garante que está sendo executado o run
    public void run() {
        //ao iniciar o veículo aguarda sua vez no cruzamento 
        try {
            
            System.out.println("Veículo " + id + " esperando para entrar no cruzamento.");
            long tempoInicio = System.currentTimeMillis();
            semaforo.entrarNoCruzamento();
            
            long tempoEspera = System.currentTimeMillis() - tempoInicio;
            System.out.println("Veículo " + id + " entrou no cruzamento.");
            
            Thread.sleep(3000); //ms
            long tempoCruzamento = System.currentTimeMillis() - tempoInicio - tempoEspera;
            System.out.println("Veículo " + id + " saiu do cruzamento.");
            
            semaforo.sairDoCruzamento();
            
            relatorio.adicionarRegistro("Veículo " + id + ": Espera " + tempoEspera + " ms, Tempo no cruzamento " + tempoCruzamento + " ms");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int numVeiculos = 5;
        //instancias: 
        Semaforo semaforo = new Semaforo();
        Relatorio relatorio = new Relatorio();
        List<Veiculo> veiculos = new ArrayList<>();
        
        //enquanto o numero de veiculos foi menor ou igual a 5 faça:
        for (int i = 1; i <= numVeiculos; i++) {
            Veiculo v = new Veiculo(i, semaforo, relatorio);
            veiculos.add(v);
            v.start(); //inicia a execusão da thread de forma assincrona
        }
        
        for (Veiculo v : veiculos) {
            v.join(); //permite que a thread espere outra terminar antes de continuar sua execusão
        }
        
        relatorio.imprimir();
        System.out.println("\nTotal de veículos processados: " + numVeiculos);
    }
}
