# Eco-Orbiter Energy Smart Grid (EOSG) 
### Sistema Inteligente de Monitoramento e Telemetria Energética Espacial

---

## Integrantes do Grupo
* **Enzo Caruso Peter** - RM: 570908
* **Leonardo Robert Maulicino** - RM: 570329
* **Lucas Ramos de Sousa** - RM: 573901

**Curso:** Ciência da Computação  
**Turma:** 1CCPG  
**Instituição:** FIAP (Global Solution 2026)

---

## Visão Geral do Projeto
O **Eco-Orbiter Energy Smart Grid (EOSG)** é uma solução computacional desenvolvida para o monitoramento inteligente de microrredes de energia renovável e sistemas críticos em missões aeroespaciais experimentais. Em cenários de exploração espacial, a eficiência energética e a resiliência de sistemas de suporte à vida são fundamentais.

O software foi projetado para receber telemetrias simuladas e, de forma autônoma, interpretar dados operacionais, gerar alertas em tempo real, acionar atuadores de mitigação de riscos e rodar um algoritmo preditivo estatístico de Inteligência Artificial para antecipar falhas de armazenamento de energia.

---

## Requisitos Técnicos Implementados

O projeto atende a 100% dos requisitos mínimos exigidos no escopo da **Global Solution 2026**:

* **Monitoramento de Dados Simulados:** Acompanhamento dinâmico de 5 eixos críticos da missão: Temperatura do Sistema Fotovoltaico, Intensidade do Link de Sinal (Comunicação), Capacidade do Banco de Baterias (Energia), Concentração de Oxigênio (Módulo Ambiental) e Estabilidade da Smart Grid.
* **Geração Automática de Alertas:** Lógica em tempo real para identificação de estados de `ALERTA` e `CRÍTICO`, com mensagens customizadas de engenharia para cada anomalia detectada.
* **Tomada de Decisão Básica (Atuadores Coerentes):** Resposta automatizada acionando sistemas de proteção da nave como *Refrigeração Ativa*, *Load Shedding* (corte de cargas não essenciais) e *Modulação de Sinal*.
* **Inteligência Artificial Introdutória:** Implementação nativa (Python Standard) do algoritmo estatístico preditivo de **Regressão Linear por Mínimos Quadrados** para calcular a tendência de variação de carga da bateria, prevendo colapsos energéticos antes que eles aconteçam.
* **Visualização de Dados (Usabilidade):** Interface organizada via terminal com a geração de um relatório de diagnóstico final contendo estatísticas volumétricas e um gráfico de barras em modo texto (`#`).

---

## Arquitetura da IA Preditiva
Para cumprir o critério de **Inovação**, o sistema foge de meras estruturas de decisão fixas (`if/else`) para avaliar a integridade energética. O algoritmo calcula dinamicamente o coeficiente angular ($m$) da reta de regressão com base no histórico de ciclos passados:

$$m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$

Onde:
* $x$ representa a progressão temporal dos ciclos operacionais.
* $y$ representa o percentual de carga restante no banco de baterias.

Se a inclinação calculada pela IA for excessivamente negativa ($m < -4.0$), o sistema dispara uma predição antecipada de colapso energético iminente, permitindo o planejamento preventivo de controle de danos.

---

## Estrutura do Código

O script principal está estruturado de forma modular e fortemente tipada:

* `CONFIG_MODULOS`: Dicionário de configuração contendo funções anônimas (`lambda`) para validação de limites físicos e strings de diagnóstico.
* `prever_colapso_bateria()`: Core do modelo estatístico de IA preditiva.
* `gerar_dados_simulados()`: Matriz telemetria estruturada em formato de narrativa espacial (Estado Nominal $\rightarrow$ Stress Térmico $\rightarrow$ Crise Cascata $\rightarrow$ Mitigação Autônoma $\rightarrow$ Recuperação).
* `processar_ciclos()`: Loop de processamento de sinais, tratamento de estados e controle dos atuadores.
* `gerar_relatorio_final()`: Consolidação analítica do desempenho da missão, diretrizes sugeridas de engenharia e renderização do gráfico de falhas.

---

## Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado.
* Nenhuma biblioteca externa é necessária (Construído 100% com a biblioteca padrão do Python).

### Passos para Execução
1. Abra o terminal do seu sistema operacional.
2. Clone este repositório utilizando a URL abaixo (substitua pelo link do seu repositório):
```bash
git clone https://github.com/leomaulicino/solucoes-energia-global-solution.git
3.  Acesse a pasta do projeto descarregada: cd solucoes-energia-global-solution
4. Execute o script principal do monitor: main.py

##Exemplo de Saída no Terminal

================================================================================
 TRANSMISSÃO DE TELEMETRIA - CICLO OPERACIONAL 03
================================================================================
[DADOS DE SENSORES RECEBIDOS]:
  -> Temperatura Sistema Fotovoltaico : 48 °C
  -> Intensidade do Link de Sinal     : 55 %
  -> Capacidade Banco de Baterias     : 50 %
  -> Concentração de Oxigênio (S.V)  : 74 %
  -> Estabilidade da Smart Grid       : 65 %

[ANÁLISE DE SUBSISTEMAS]:
  CRÍTICO: Risco de degradação severa das células fotovoltaicas.
  ALERTA: Link de comunicação instável com a base.
  ALERTA: Geração solar insuficiente para a demanda.
  ALERTA: Pico de consumo energético no módulo de oxigênio.
  ALERTA: Micro-oscilações de tensão detectadas na distribuição.

[MATRIZ DE RESPOSTA AUTOMATIZADA (ATUADORES)]:
  * Refrigeração Ativa                 : [ATIVADO - MITIGANDO ANOMALIA]
  * Load Shedding (Corte de Cargas)    : [ATIVADO - MITIGANDO ANOMALIA]
  * Modulação de Sinal de Dados        : [ATIVADO - MITIGANDO ANOMALIA]

[IA INTRODUTÓRIA - MODELO DE TENDÊNCIA DE ENERGIA]:
  ALERTA: Tendência de descarga moderada (-17.5% por ciclo). Monitorar cargas.

[RISCO INTEGRADO DA MISSÃO]:
  Nível: ALTO / CRÍTICO (Intervenção Automática Requerida)