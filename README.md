# Soluções em Energia - Global Solution

> **FIAP - Global Solution 2026**  
> **Disciplina:** Soluções em Energias Renováveis e Sustentáveis 
> **Integrantes:** Enzo Caruso Peter, RM: 570908/Leonardo Robert Maulicino, RM: 570329/Lucas Ramos de Sousa, RM:573901 
> **Curso:** Ciência da Computação (1CCPG)  
> **Repositório:** solucoes-energia-global-solution  

---

## Resumo do Projeto
Na exploração aeroespacial contemporânea, a sustentabilidade e a resiliência energética são os fatores limítrofes entre o sucesso de uma missão e o colapso operacional. O **Eco-Orbiter Energy Smart Grid (EOSG)** é um sistema inteligente de monitoramento e controle automatizado de matrizes energéticas projetado para naves e módulos espaciais experimentais de longa duração.

Utilizando os pilares do Pensamento Computacional e arquitetura limpa em Python, o sistema funciona como uma malha inteligente (*Smart Grid*), recebendo dados simulados de geração, armazenamento e dissipação para prever riscos, otimizar o fator de potência, mitigar o desperdício elétrico e garantir que os sistemas de suporte à vida operem dentro do escopo ecológico ideal através de fontes de energia renováveis.

---

## Funcionalidades e Escopo Técnico

O software foi modelado para cumprir rigorosamente as métricas de análise de dados estruturados através de uma matriz multidimensional de **6 ciclos temporais** e **5 parâmetros de relevância física e sustentável**:

| Parâmetro | Módulo Relacionado | Descrição Sustentável |
| :--- | :--- | :--- |
| **Temperatura** | Módulo Térmico | Monitora inversores e painéis para evitar perdas por efeito Joule. |
| **Potência %** | Transmissão / Telecom | Evita picos desnecessários de consumo de corrente no link de rádio. |
| **Bateria %** | Armazenamento Central | Eixo central de controle. Evita esgotamento de energia limpa armazenada. |
| **ECLSS %** | Suporte à Vida | Mede a eficiência ambiental e custo ecológico da reciclagem de gases. |
| **Estabilidade %**| Rede Elétrica / Distribuição| Avalia micro-oscilações de tensão nas Smart Grids internas. |

---

## Lógica de Decisão e Resposta Automatizada

O algoritmo processa a matriz de dados aplicando regras lógicas baseadas em limiares operacionais (`NORMAL`, `ALERTA` e `CRÍTICO`). 

* **Tomada de Decisão Automatizada:** Diante de dados críticos detectados em tempo real, o sistema altera o status operacional de atuadores da nave autonomamente (ex: ativando a *Refrigeração Ativa* ou iniciando o protocolo de *Corte de Cargas Não-Essenciais* para preservar as baterias).
* **Cálculo de Risco Dinâmico:** Cada anomalia possui um peso matemático associado. O sistema calcula o nível cumulativo de risco por ciclo e gera uma **Tendência Operacional da Missão** ao final do processamento.

---

## Estrutura do Repositório

* `main.py`: Código-fonte principal em Python, estruturado com funções modulares e lógica de decisão para Smart Grid.
* `README.md`: Documentação técnica detalhada das diretrizes de sustentabilidade do projeto.

---

## Como Executar o Sistema

### Pré-requisitos
* Python 3.x instalado localmente.

### Execução
1. Clone este repositório ou baixe o arquivo `main.py`.
2. Abra o terminal na pasta correspondente e execute:
```bash
python main.py