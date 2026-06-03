# ==============================================================================
# FIAP - GLOBAL SOLUTION 2026
# DISCIPLINA: SOLUÇÕES EM ENERGIAS RENOVÁVEIS E SUSTENTABILIDADE (SERS)
# PROJETO: ECO-ORBITER ENERGY SMART GRID (EOSG)
# ==============================================================================

import time
from typing import Dict, List, Tuple

# ------------------------------------------------------------------------------
# CONFIGURAÇÕES DOS MÓDULOS (REQUISITOS TÉCNICOS)
# ------------------------------------------------------------------------------

CONFIG_MODULOS = {
    "Térmico": {
        "indice": 0,
        "critico": lambda x: x < 15 or x > 45,
        "alerta": lambda x: x < 20 or x > 35,
        "msg_critico": "CRÍTICO: Risco de degradação severa das células fotovoltaicas.",
        "msg_alerta": "ALERTA: Temperatura oscilando. Eficiência dos painéis reduzida.",
        "msg_normal": "Nominal: Temperatura interna controlada."
    },
    "Transmissão": {
        "indice": 1,
        "critico": lambda x: x < 40,
        "alerta": lambda x: x < 70,
        "msg_critico": "CRÍTICO: Atenuação severa do sinal de telemetria.",
        "msg_alerta": "ALERTA: Link de comunicação instável com a base.",
        "msg_normal": "Nominal: Link estável com largura de banda ideal."
    },
    "Baterias": {
        "indice": 2,
        "critico": lambda x: x < 25,
        "alerta": lambda x: x < 55,
        "msg_critico": "CRÍTICO: Esgotamento iminente do banco de armazenamento.",
        "msg_alerta": "ALERTA: Geração solar insuficiente para a demanda.",
        "msg_normal": "Nominal: Banco de baterias operando em regime seguro."
    },
    "Ambiental": {
        "indice": 3,
        "critico": lambda x: x < 50,
        "alerta": lambda x: x < 75,
        "msg_critico": "CRÍTICO: Sobrecarga crítica no sistema de suporte à vida.",
        "msg_alerta": "ALERTA: Pico de consumo energético no módulo de oxigênio.",
        "msg_normal": "Nominal: Eficiência ambiental e suporte à vida ideais."
    },
    "Rede Elétrica": {
        "indice": 4,
        "critico": lambda x: x < 60,
        "alerta": lambda x: x < 80,
        "msg_critico": "CRÍTICO: Flutuação severa e instabilidade na Smart Grid.",
        "msg_alerta": "ALERTA: Micro-oscilações de tensão detectadas na distribuição.",
        "msg_normal": "Nominal: Distribuição elétrica estabilizada na malha."
    }
}

# ------------------------------------------------------------------------------
# IA INTRODUTÓRIA: FILTRAGEM E PREVISÃO POR REGRESSÃO LINEAR
# ------------------------------------------------------------------------------

def prever_colapso_bateria(historico_bateria: List[int]) -> Tuple[str, float]:
    """
    Aplica o algoritmo estatístico de Regressão Linear (Mínimos Quadrados) para
    calcular a taxa de variação (inclinação m) do nível da bateria ao longo do tempo.
    Constitui uma abordagem matemática de IA preditiva puramente em Python Standard.
    """
    n = len(historico_bateria)
    if n < 2:
        return "Dados analíticos insuficientes para predição.", 0.0

    # Cálculo das médias das coordenadas x (tempo) e y (carga %)
    x_medio = (n - 1) / 2.0
    y_medio = sum(historico_bateria) / n

    # Aplicação das fórmulas de regressão linear para obter a inclinação (m)
    numerador = sum((i - x_medio) * (v - y_medio) for i, v in enumerate(historico_bateria))
    denominador = sum((i - x_medio) ** 2 for i in range(n))

    if denominador == 0:
        return "Banco de energia perfeitamente estável.", 0.0

    inclinacao = numerador / denominador

    # Tomada de decisão baseada na tendência calculada pelo modelo matemático
    if inclinacao < -4.0:
        return f"CRÍTICO: Queda severa de {abs(inclinacao):.1f}% por ciclo. Risco de colapso energético!", inclinacao
    elif inclinacao < 0:
        return f"ALERTA: Tendência de descarga moderada ({inclinacao:+.1f}% por ciclo). Monitorar cargas.", inclinacao
    else:
        return f"OTIMIZADO: Recuperação/Estabilização energética detectada ({inclinacao:+.1f}% por ciclo).", inclinacao

# ------------------------------------------------------------------------------
# SIMULAÇÃO DINÂMICA (NARRATIVA TELEMÉTRICA COERENTE)
# ------------------------------------------------------------------------------

def gerar_dados_simulados() -> List[List[int]]:
    """
    Gera uma telemetria estruturada que narra o comportamento real de uma missão:
    Ciclo 1: Condições Nominais
    Ciclo 2: Entrada em zona de radiação/aquecimento (Anomalia Térmica)
    Ciclo 3: Degradação em cascata (Bateria e Rede afetadas)
    Ciclo 4: Ápice crítico e atuação emergencial dos sistemas autônomos
    Ciclo 5: Início do reestabelecimento e controle da Smart Grid
    Ciclo 6: Estabilização completa pós-intervenção
    """
    return [
        # Temp(°C), Com(%), Bat(%), Oxigênio(%), Estabilidade SmartGrid(%)
        [25, 95, 85, 90, 92],  # Ciclo 1: Estabilidade total
        [38, 72, 70, 88, 81],  # Ciclo 2: Alerta térmico inicial
        [48, 55, 50, 74, 65],  # Ciclo 3: Crise térmica, reflexo nas baterias
        [42, 38, 22, 48, 52],  # Ciclo 4: Ápice crítico (Shedding ativo)
        [32, 68, 45, 76, 78],  # Ciclo 5: Resposta eficiente e resfriamento
        [24, 88, 65, 89, 90]   # Ciclo 6: Missão salva e grid reestabelecida
    ]

# ------------------------------------------------------------------------------
# INTERFACE E PROCESSAMENTO
# ------------------------------------------------------------------------------

def exibir_cabecalho() -> None:
    print("=" * 80)
    print("                 ECO-ORBITER ENERGY SMART GRID (EOSG)")
    print("         Sistema Inteligente de Monitoramento e Telemetria Espacial")
    print("=" * 80)

def analisar_modulo(nome: str, valor: int) -> Tuple[str, str]:
    config = CONFIG_MODULOS[nome]
    if config["critico"](valor):
        return "CRÍTICO", config["msg_critico"]
    if config["alerta"](valor):
        return "ALERTA", config["msg_alerta"]
    return "NORMAL", config["msg_normal"]

def calcular_indice_risco(alertas: int, criticos: int) -> Tuple[int, str]:
    pontos = alertas + (criticos * 2)
    if pontos == 0:
        return 0, "NULO (Operação Segura)"
    if pontos <= 2:
        return 1, "BAIXO (Flutuações Aceitáveis)"
    if pontos <= 5:
        return 2, "MÉDIO (Atenção Operacional)"
    return 3, "ALTO / CRÍTICO (Intervenção Automática Requerida)"

# ------------------------------------------------------------------------------
# CORE LOOP (PROCESSAMENTO DE SINAIS)
# ------------------------------------------------------------------------------

def processar_ciclos(dados: List[List[int]]):
    historico_peso = []
    historico_bateria = []
    
    ocorrencias = {modulo: 0 for modulo in CONFIG_MODULOS}
    severidade = {modulo: 0 for modulo in CONFIG_MODULOS}
    
    atuadores = {
        "Refrigeração Ativa": False,
        "Load Shedding (Corte de Cargas)": False,
        "Modulação de Sinal de Dados": False
    }

    for numero, ciclo in enumerate(dados, start=1):
        print(f"\n{'=' * 80}")
        print(f" TRANSMISSÃO DE TELEMETRIA - CICLO OPERACIONAL 0{numero}")
        print(f"{'=' * 80}")

        temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo
        historico_bateria.append(bateria)

        print(f"[DADOS DE SENSORES RECEBIDOS]:")
        print(f"  -> Temperatura Sistema Fotovoltaico : {temperatura} °C")
        print(f"  -> Intensidade do Link de Sinal     : {comunicacao} %")
        print(f"  -> Capacidade Banco de Baterias     : {bateria} %")
        print(f"  -> Concentração de Oxigênio (S.V)  : {oxigenio} %")
        print(f"  -> Estabilidade da Smart Grid       : {estabilidade} %")

        alertas = 0
        criticos = 0

        print("\n[ANÁLISE DE SUBSISTEMAS]:")
        for modulo, config in CONFIG_MODULOS.items():
            valor = ciclo[config["indice"]]
            status, mensagem = analisar_modulo(modulo, valor)

            if status != "NORMAL":
                ocorrencias[modulo] += 1
                if status == "ALERTA":
                    alertas += 1
                    severidade[modulo] += 1
                    print(f"  {mensagem}")
                elif status == "CRÍTICO":
                    criticos += 1
                    severidade[modulo] += 2
                    print(f" {mensagem}")
            else:
                print(f"{modulo}: {mensagem}")

        # LOGICA AUTÔNOMA DE TOMADA DE DECISÃO (ATUADORES SIMULADOS)
        if temperatura > 35:
            atuadores["Refrigeração Ativa"] = True
        elif temperatura <= 35:
            atuadores["Refrigeração Ativa"] = False

        if bateria < 55:
            atuadores["Load Shedding (Corte de Cargas)"] = True
        elif bateria >= 55:
            atuadores["Load Shedding (Corte de Cargas)"] = False

        if comunicacao < 70:
            atuadores["Modulação de Sinal de Dados"] = True
        elif comunicacao >= 70:
            atuadores["Modulação de Sinal de Dados"] = False

        # EXIBIÇÃO DAS REPOSTAS DOS ATUADORES DA NAVE
        print("\n[MATRIZ DE RESPOSTA AUTOMATIZADA (ATUADORES)]:")
        for atuador, estado in atuadores.items():
            status_text = "[ATIVADO - MITIGANDO ANOMALIA]" if estado else "[INATIVO - NOMINAL]"
            print(f"  * {atuador:<35}: {status_text}")

        # INSIGHT DA IA PREDITIVA DURANTE O LOOP
        msg_ia, _ = prever_colapso_bateria(historico_bateria)
        print(f"\n[IA INTRODUTÓRIA - MODELO DE TENDÊNCIA DE ENERGIA]:")
        print(f"  {msg_ia}")

        peso, nivel = calcular_indice_risco(alertas, criticos)
        print(f"\n[RISCO INTEGRADO DA MISSÃO]:\n  Nível: {nivel}")
        
        historico_peso.append({"ciclo": numero, "peso": peso})
        time.sleep(0.4)

    return historico_peso, ocorrencias, severidade, historico_bateria

# ------------------------------------------------------------------------------
# DIAGNÓSTICO FINAL EXCLUSIVO (MÁXIMA USABILIDADE)
# ------------------------------------------------------------------------------

def gerar_relatorio_final(historico, ocorrencias, severidade, historico_bateria):
    print("\n" + "=" * 80)
    print("               RELATÓRIO DE DIAGNÓSTICO FINAL DA MISSÃO (EOSG)")
    print("=" * 80)

    area_mais_afetada = max(ocorrencias, key=ocorrencias.get)
    area_maior_risco = max(severidade, key=severidade.get)

    risco_inicial = historico[0]["peso"]
    risco_final = historico[-1]["peso"]

    if risco_final > risco_inicial:
        tendencia = "DEGRADANTE (Anomalias finais exigem revisão de hardware)."
        conclusao = "ATENÇÃO: A sonda encerrou o ciclo em estado severo. Recomenda-se recalibrar os painéis fotovoltaicos."
    elif risco_final < risco_inicial or (risco_final == 0 and risco_inicial > 0):
        tendencia = "OTIMIZADA (Os algoritmos de Smart Grid controlaram as flutuações com sucesso)."
        conclusao = "SUCESSO: Os atuadores inteligentes contiveram as anomalias climáticas do espaço profundo."
    else:
        tendencia = "ESTÁVEL (Padrão energético contínuo mantido)."
        conclusao = "NOTA: Sistemas operando dentro da margem de amortecimento estático."

    # Processamento final do modelo estatístico de IA
    _, inclinacao_final = prever_colapso_bateria(historico_bateria)

    print(f" Tendência Operacional Global : {tendencia}")
    print(f" Subsistema Mais Instável     : {area_mais_afetada} ({ocorrencias[area_mais_afetada]} falhas detectadas)")
    print(f" Vetor de Maior Severidade    : {area_maior_risco} (Impacto crítico acumulado)")
    print(f" Coeficiente Angular da IA    : {inclinacao_final:+.2f}% de variação média de carga/ciclo")
    print(f"\n[ANÁLISE DE VOLUMETRIA DE FALHAS]:")
    for modulo, qtd in ocorrencias.items():
        bar = "#" * qtd
        print(f"  - {modulo:<15} : {qtd} ocorrência(s) {bar}")

    print("\n[DIRETRIZES DE ENGENHARIA RECOMENDADAS]:")
    if area_maior_risco == "Térmico":
        print("  -> Priorizar manutenção preditiva nos revestimentos de isolamento multicamadas (MLI).")
    if area_maior_risco == "Baterias" or inclinacao_final < -2.0:
        print("  -> Alocar rotina de desacoplamento de telemetrias secundárias para evitar colapso na Smart Grid.")
    if ocorrencias["Rede Elétrica"] > 0:
        print("  -> Executar purga harmônica nos inversores estáticos da rede de distribuição acoplada.")
        
    print(f"\n{conclusao}\n" + "=" * 80)

# ------------------------------------------------------------------------------
# PONTO DE ENTRADA DO SCRIPT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    exibir_cabecalho()
    dados_simulados = gerar_dados_simulados()
    historico, ocorrencias, severidade, hist_bat = processar_ciclos(dados_simulados)
    gerar_relatorio_final(historico, ocorrencias, severidade, hist_bat)