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

## Questão 02

Uma Universidade precisa saber quais são os alunos que estão se formando no semestre para enviar estas informações para:  
- A empresa de eventos (organização da festa de formatura);  
- A impressão dos diplomas.  

Para isso, o setor de Tecnologia da Informação da Universidade preparou um arquivo (no formato `.txt`) para cada curso de graduação contendo os dados de todos os alunos do curso.  

- **Universidade**: possui 15 cursos de graduação.  
- **Arquivo Base**: Cada arquivo contém os seguintes dados:  
  - Matrícula;  
  - Nome do aluno;  
  - Curso;  
  - **Flag** (status do aluno):  
    - `CURSANDO`;  
    - `CONCLUÍDO`.  

---

### Contexto
O objetivo é listar todos os alunos formandos (flag como `CONCLUÍDO`) a partir da busca nos arquivos dos cursos de graduação.

---

### Requisitos

1. **Gerar um Código**:  
   - Desenvolver um código utilizando **programação concorrente** para processar as informações.

2. **Base de Dados**:  
   - Deve ser criada pelo grupo, seguindo o modelo apresentado: `{matrícula, nome do aluno, curso, flag}`.

3. **Processamento Concorrente**:  
   - O código deve ser capaz de buscar as informações em todos os arquivos de maneira eficiente e listar os alunos formandos.

---

## Questão 03

### Contexto
O cinema do Shopping ABC deseja implementar uma **solução concorrente** no processo de pedidos de lanches, incluindo pipoca e refrigerante. O funcionamento segue as etapas abaixo:

1. **Pedido**:  
   - O cliente faz o pedido de uma pipoca e um refrigerante no balcão.  

2. **Preparação do Pedido**:  
   - A atendente solicita a execução para sua equipe;  
   - Um membro da equipe prepara a pipoca;  
   - Outro membro prepara o refrigerante;  
   - Ambas as tarefas acontecem simultaneamente.  

3. **Entrega do Pedido**:  
   - O pedido só é considerado totalmente realizado quando ambas as tarefas forem concluídas;  
   - Os membros da equipe entregam os itens à atendente;  
   - O cliente recebe e pode desfrutar do lanche.  

---

### Requisitos

1. **Desenvolver o Código**:  
   - Implementar uma solução concorrente para atender à situação descrita.

2. **Dica**:
   - Utilize a API `CompletableFuture` para implementar os seguintes métodos:  
     - `getPipoca()`: retorna um “future” com a string `Pipoca Pronta`;  
     - `getRefrigerante()`: retorna um “future” com a string `Refrigerante Pronto`;  
     - `lanchePronto()`: retorna uma string informando que o lanche está pronto.  

   > **Nota:** O método `lanchePronto()` só deve ser chamado após a pipoca e o refrigerante estarem disponíveis.

3. **Concorrência**:
   - Tanto `getPipoca()` quanto `getRefrigerante()` devem ser executados de forma concorrente.  
   - Uma vez concluídos, as informações devem ser retornadas, permitindo a execução de `lanchePronto()`.

---

## Questão 04

### Contexto
O cálculo da soma de números inteiros armazenados em um grande vetor é necessário em várias situações práticas, como:

- **Análise de dados**: Soma de vendas para calcular o total em determinado período.  
- **Processamento de imagens**: Determinação da intensidade média ou total de luz.  
- **Simulação de Monte Carlo**: Avaliação de incertezas, como cálculo de médias ou desvios padrões.  
- **Aprendizado de Máquina**: Treinamento de modelos ou previsões usando grandes vetores.  
- **Criptografia**: Algoritmos que dependem de somas de valores para processos de encriptação/desencriptação.

---

### Problema
Dado um vetor de 1 milhão de números inteiros, é necessário calcular a soma total:

- **Abordagem Sequencial**:  
  - Percorre o vetor somando cada número, o que pode ser lento.  

- **Abordagem Paralela**:  
  - Dividir o vetor em partes (ex.: 10 partes);  
  - Calcular a soma de cada parte em threads separadas, utilizando múltiplos núcleos.

---

### Requisitos

1. **Desenvolver Códigos**:  
   - Implementar duas abordagens para o cálculo da soma:
     1. Sequencial;
     2. Concorrente.  

2. **Dica**:  
   - Criar uma classe `SomaThread` que implementa a interface `Runnable` e recebe:
     - O vetor de números inteiros;  
     - Índices de início e fim da parte a ser somada;  
     - Um objeto `AtomicInteger` para armazenar o resultado parcial.  

   > **Nota:** Utilize o método `addAndGet(int delta)` para adicionar atomicamente o valor ao resultado atual.

---

## Questão 05

### Contexto
O processamento concorrente é essencial em sistemas modernos para melhorar a eficiência e a capacidade de resposta. Muitas aplicações utilizam concorrência, especialmente na simulação de tráfego urbano em cidades inteligentes, com objetivos como:

- **Sistemas de semáforos inteligentes**: Ajustar dinamicamente os tempos dos semáforos com base em dados de sensores de tráfego.  
- **Aplicativos de navegação**: Processar dados de milhares de usuários simultaneamente para calcular rotas otimizadas.  
- **Simulações para planejamento urbano**: Antecipar o impacto de mudanças de vias, sentidos ou obras no fluxo do trânsito.  

---

### Objetivo
Desenvolver uma aplicação que simule um **sistema de tráfego urbano** utilizando threads para representar veículos transitando por um conjunto de ruas e cruzamentos. A simulação deve permitir movimentação concorrente, respeitando regras básicas como espera em cruzamentos e liberação por semáforos.

---

### Requisitos

1. **Criação de Veículos**:  
   - Cada veículo deve ser representado por uma **thread**.  
   - Cada veículo deve seguir uma rota específica.  

2. **Sistema de Cruzamentos**:  
   - Os veículos devem parar e aguardar a liberação dos semáforos antes de prosseguir.  

3. **Sincronização**:  
   - Utilizar mecanismos como `synchronized` ou `locks` para garantir que múltiplos veículos não ocupem o mesmo cruzamento ao mesmo tempo.  

4. **Relatórios**:  
   - Exibir estatísticas ao final da simulação, como:  
     - Número total de veículos processados;  
     - Informações sobre tempos de espera;  
     - Outros dados relevantes sugeridos.  

---

## Questão 06

### Contexto
Nos sistemas modernos, a programação concorrente é essencial para garantir desempenho e escalabilidade. Muitas aplicações precisam integrar dados de diferentes fontes e processá-los em tempo real. Exemplos de possíveis aplicações incluem:

- **Serviços de previsão do tempo**: Aplicações como Weather.com e Climatempo agregam dados de múltiplas fontes para oferecer previsões precisas.  
- **Integração de sensores em cidades inteligentes**: Estações meteorológicas distribuem dados em tempo real para monitoramento climático eficiente.  
- **Análises climáticas na agricultura**: Fazendas utilizam dados de várias fontes para prever secas e planejar a irrigação.  

---

### Objetivo
Desenvolver uma aplicação que simule um **agregador de informações meteorológicas**, coletando dados de diferentes bases de dados simuladas, processando-os de forma concorrente e consolidando-os em um relatório final.

---

### Requisitos

1. **Bases de Dados Simuladas**:  
   - Armazenar os dados meteorológicos em listas ou mapas, simulando bancos de dados distintos.  

2. **Coleta Assíncrona**:  
   - Buscar os dados das diferentes fontes de forma concorrente.  
   - Utilizar APIs como `CompletableFuture` para facilitar a execução assíncrona.  

3. **Processamento de Dados**:  
   - Calcular a média da temperatura coletada.  
   - Sugerir informações adicionais, como:  
     - Localizações das bases de dados;  
     - Outras análises relevantes.  

---




