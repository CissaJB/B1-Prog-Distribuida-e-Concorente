# **Questão 5** <br>
O processamento concorrente é essencial em sistemas modernos para melhorar a eficiência e a capacidade
de resposta. Muitas aplicações precisam executar várias tarefas simultaneamente, como sistemas de
simulação, jogos e serviços em nuvem.<br>
Uma área onde o uso de threads se destaca é a simulação de tráfego urbano. Em cidades inteligentes, é
fundamental monitorar e otimizar o fluxo de veículos, reduzindo congestionamentos e melhorando a
mobilidade. Exemplos de potenciais aplicações que usam recursos de concorrência são: <br>
  • <sub>**Sistemas de semáforos inteligentes:**</sub> Sensores de tráfego enviam dados para servidores que ajustam
    os tempos dos semáforos dinamicamente, reduzindo congestionamentos. <br>
  • <sub>**Aplicativos de navegação:**</sub> Apps como Google Maps ou Waze processam dados de milhares de
    usuários simultaneamente para calcular rotas otimizadas. <br>
  • <sub>**Simulações para planejamento urbano:**</sub> Cidades usam simulações para prever o impacto de novas
    vias, mudanças de sentido ou obras na fluidez do trânsito. <br>
Dentro deste contexto pede-se: Desenvolver uma aplicação que simule um sistema de tráfego urbano
utilizando threads para representar veículos que transitam por um conjunto de ruas e cruzamentos. A
simulação deve permitir a movimentação dos veículos de maneira concorrente, respeitando regras básicas,
como a espera em cruzamentos e a liberação por semáforos. <br>
# **Requisitos** <br>
• <sub>**Criação de veículos:**</sub> Cada veículo deve ser representado por uma thread e deve seguir uma rota específica.<br>
• <sub>**Sistema de cruzamentos:**</sub> Os veículos devem parar e aguardar a liberação dos semáforos antes de prosseguir.<br>
• <sub>**Sincronização:**</sub> Utilizar mecanismos como, por exemplo, synchronized ou locks para garantir que múltiplos veículos não
ocupem o mesmo cruzamento ao mesmo tempo.<br>
• <sub>**Relatórios:**</sub> Ao final da simulação, exibir estatísticas, como número total de veículos processados. Sugira outras 
informações, por exemplo, informações sobre os tempos de espera, etc.<br>
