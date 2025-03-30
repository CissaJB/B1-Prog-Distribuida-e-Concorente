# TrabalhoB1 Programação Distribuída e Concorrente

## Questão 01

### A) Criação de uma aplicação
Deve-se criar uma aplicação que modele o funcionamento de sua conta bancária. Esta conta será o recurso compartilhado e deverá ser acessada/modificada por três threads: a thread **AEsperta**, a thread **AEconomica** e a thread **AGastadora**, concorrentemente.

1. **AGastadora**:  
   - Esta thread (de atitude voraz) deverá, a cada 3000 milissegundos, verificar se há saldo suficiente e retirar 10 reais da sua conta.  
   - Deve disputar por dinheiro com as demais threads, concorrentemente.

2. **AEsperta**:  
   - Mais comedida que a anterior, esta thread verificará o saldo apenas a cada 6000 milissegundos.  
   - Caso haja saldo suficiente, retirará 50 reais da sua conta.  
   - Deve disputar com outras threads, concorrentemente.

3. **AEconomica**:  
   - Preza mais por você e suas finanças. Verificará o saldo apenas a cada 12000 milissegundos.  
   - Caso haja fundos, tentará retirar apenas 5 reais da conta.  
   - Deve disputar com outras threads, concorrentemente.

---

### B) Classe Conta (recurso compartilhado)

A classe deve conter pelo menos:  
- **Atributos**:
  - Número da conta;
  - Titular da conta;
  - Saldo.

- **Regras básicas de integridade**:
  - Tratar valores inválidos (por exemplo, números de conta negativos).  

- **Métodos principais**:
  - `deposito`: para adicionar saldo;
  - `saque`: para retirar saldo.

> **Nota:** Inicie o saldo (recurso compartilhado) da conta depositando uma quantia de R$ 1.000,00.

> **Dica:** Faça um esboço de um diagrama inicial de classes para visualizar melhor quantas classes serão necessárias e como elas se relacionam.

---

### IMPORTANTE

Sempre que uma thread movimentar fundos da sua conta, o sistema deve:  
- Informar qual thread efetuou a operação (saque ou depósito);  
- Informar o saldo atual final (após o saque), permitindo acompanhar a situação financeira em tempo real.

> **Lembre-se:**  
> - Não defina prioridades (todas as threads devem ter as mesmas chances);  
> - Não permita corrupção de dados (use `synchronized` ou outro modelo apropriado).  

---

### C) Conta com saldo zerado
- Quando a conta estiver com saldo zero:  
  - Todas as threads devem ser colocadas em estado de espera.  
  - Ao serem colocadas em espera, cada thread deve imprimir:  
    - A quantidade de saques efetuados;  
    - O valor total retirado da conta.  

Execute e veja os resultados.

---

### D) Acrescentar a thread **APatrocinadora**
- Essa thread deve:  
  - Depositar 100 reais sempre que a conta estiver zerada.  
  - Ser uma “produtora”, enquanto as demais são “consumidoras”.  
  - Avaliar o uso de `wait` e `notifyAll` ou outro modelo apropriado.

---

### E) Uso de GUI
- Fica a critério do grupo decidir se usará ou não uma interface gráfica (GUI).
