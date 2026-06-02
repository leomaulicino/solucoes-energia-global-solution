# ==============================================================================
# FIAP - GLOBAL SOLUTION 2026
# DISCIPLINA: SOLUÇÕES EM ENERGIAS RENOVÁVEIS E SUSTENTABILIDADE (SERS)
# PROJETO: ECO-ORBITER ENERGY SMART GRID (EOSG)
# ==============================================================================

import time

def exibir_cabecalho():
    print("=" * 75)
    print("     ECO-ORBITER ENERGY SMART GRID (EOSG) - MONITORAMENTO AUTOMATIZADO")
    print("=" * 75)
    time.sleep(0.5)

def analisar_modulo_termico(temperatura):
    """Analisa a eficiência do sistema de dissipação térmica e inversores."""
    if temperatura < 15 or temperatura > 45:
        return "CRÍTICO", "Risco de degradação das células fotovoltaicas. Ativar refrigeração ativa."
    elif temperatura < 20 or temperatura > 35:
        return "ALERTA", "Temperatura oscilando. Eficiência de conversão energética reduzida."
    return "NORMAL", "Temperatura nominal. Dissipação térmica eficiente."

def analisar_potencia_transmissao(comunicacao):
    """Analisa o consumo de potência elétrica do subsistema de telecomunicações."""
    if comunicacao < 40:
        return "CRÍTICO", "Atenuação severa. Amplificadores exigindo pico crítico de potência (W)."
    elif comunicacao < 70:
        return "ALERTA", "Sinal instável. Modulando taxa de dados para economizar energia."
    return "NORMAL", "Link estável. Consumo de transmissão otimizado."

def analisar_banco_baterias(bateria):
    """Métrica vital: Nível de armazenamento de energia nas baterias recarregáveis."""
    if bateria < 25:
        return "CRÍTICO", "Esgotamento iminente. Iniciar protocolo de corte de cargas não essenciais!"
    elif bateria < 55:
        return "ALERTA", "Geração solar insuficiente para a carga. Ativar modo econômico."
    return "NORMAL", "Banco de baterias carregado. Matriz energética estável."

def analisar_suporte_vida(oxigenio):
    """Mede a eficiência energética do sistema de reciclagem ambiental (ECLSS)."""
    if oxigenio < 50:
        return "CRÍTICO", "Subsistema ambiental operando com sobrecarga elétrica. Risco de blackout."
    elif oxigenio < 75:
        return "ALERTA", "Demanda de potência acima da média para reciclagem de gases."
    return "NORMAL", "Módulo ecológico operando com alta eficiência energética."

def analisar_estabilidade_rede(estabilidade):
    """Avalia a flutuação de tensão e a eficiência da distribuição elétrica na nave."""
    # CORRIGIDO: Removido o bug da variável 'distribuicao' inexistente
    if estabilidade < 60:
        return "CRÍTICO", "Flutuação severa na rede de distribuição (Smart Grid instável)."
    elif estabilidade < 80:
        return "ALERTA", "Micro-oscilações de corrente detectadas nos barramentos principais."
    return "NORMAL", "Fator de potência ideal. Distribuição elétrica linear."

def calcular_indice_risco(alertas, criticos):
    """Calcula o risco matemático do ciclo com base na gravidade das falhas energéticas."""
    total_pontos = (alertas * 1) + (criticos * 2)
    if total_pontos == 0:
        return 0, "NULO"
    elif total_pontos <= 2:
        return 1, "BAIXO"
    elif total_pontos <= 4:
        return 2, "MÉDIO"
    return 3, "ALTO / CRÍTICO"

def processar_ciclos_energeticos(matriz_dados):
    """Processa a matriz de dados simulados (6 ciclos x 5 parâmetros)."""
    relatorio_ciclos = []
    contagem_afetadas = {"Térmico": 0, "Transmissão": 0, "Baterias": 0, "Ambiental": 0, "Rede Elétrica": 0}
    
    # INOVAÇÃO: Atuadores automatizados de resposta a crises (Tomada de Decisão Real)
    sistemas_contingencia = {
        "Refrigeração Ativa": "DESATIVADO",
        "Corte de Cargas (Load Shedding)": "INATIVO",
        "Modulação de Dados": "DESATIVADO"
    }
    
    for i, ciclo in enumerate(matriz_dados):
        print(f"\n>>> PROCESSANDO CICLO OPERACIONAL TEMPORAL: {i + 1} <<<")
        print("-" * 55)
        
        alertas_ciclo = 0
        criticos_ciclo = 0
        
        temp, com, bat, oxig, estab = ciclo

        print("\n[DADOS MONITORADOS]")
        print(f"Temperatura: {temp} °C")
        print(f"Comunicação: {com}%")
        print(f"Bateria: {bat}%")
        print(f"Oxigênio: {oxig}%")
        print(f"Estabilidade da Rede: {estab}%")
        
        status_t, msg_t = analisar_modulo_termico(temp)
        status_c, msg_c = analisar_potencia_transmissao(com)
        status_b, msg_b = analisar_banco_baterias(bat)
        status_o, msg_o = analisar_suporte_vida(oxig)
        status_e, msg_e = analisar_estabilidade_rede(estab)
        
        mapeamento_status = [
            (status_t, "Térmico", msg_t), 
            (status_c, "Transmissão", msg_c), 
            (status_b, "Baterias", msg_b), 
            (status_o, "Ambiental", msg_o), 
            (status_e, "Rede Elétrica", msg_e)
        ]
        
        for status, area, msg in mapeamento_status:
            if status == "ALERTA":
                alertas_ciclo += 1
                contagem_afetadas[area] += 1
                print(f"[{status}] {area}: {msg}")
                
                # Resposta automatizada básica para Alertas
                if area == "Transmissão":
                    sistemas_contingencia["Modulação de Dados"] = "ATIVADO (Economia de Energia)"
                    
            elif status == "CRÍTICO":
                criticos_ciclo += 1
                contagem_afetadas[area] += 2
                print(f"[{status}] {area} !!! {msg}")
                
                # TOMADA DE DECISÃO AUTOMATIZADA (Respostas sistêmicas automáticas)
                if area == "Térmico":
                    sistemas_contingencia["Refrigeração Ativa"] = "LIGADA (Potência Máxima)"
                if area == "Baterias":
                    sistemas_contingencia["Corte de Cargas (Load Shedding)"] = "EXECUTANDO PROTOCOLO CRÍTICO"

        # Exibição do estado atual dos atuadores inteligentes da Smart Grid
        print("\n[STATUS DOS ATUADORES AUTOMÁTICOS DE CONTINGÊNCIA]")
        for atuador, estado in sistemas_contingencia.items():
            print(f"  -> {atuador}: {estado}")
        
        peso_risco, nivel_risco = calcular_indice_risco(alertas_ciclo, criticos_ciclo)
        print(f"\n--> Nível de Risco do Ciclo {i+1}: {nivel_risco} (Fator: {peso_risco})")
        
        relatorio_ciclos.append({
            "ciclo": i + 1,
            "peso_risco": peso_risco,
            "status_geral": nivel_risco
        })
        time.sleep(0.3)
        
        # Reset de contingências temporárias simuladas pós-ciclo para a próxima leitura
        sistemas_contingencia = {
            "Refrigeração Ativa": "DESATIVADO",
            "Corte de Cargas (Load Shedding)": "INATIVO",
            "Modulação de Dados": "DESATIVADO"
        }
        
    return relatorio_ciclos, contagem_afetadas

def gerar_diagnostico_final(relatorio, anomalias):
    """Gera o balanço de sustentabilidade e a tendência operacional do sistema."""
    print("\n" + "=" * 75)
    print("                 RELATÓRIO FINAL DE EFICIÊNCIA ENERGÉTICA")
    print("=" * 75)
    
    area_mais_afetada = max(anomalias, key=anomalias.get)
    
    risco_inicial = relatorio[0]["peso_risco"]
    risco_final = relatorio[-1]["peso_risco"]
    
    if risco_final > risco_inicial:
        tendencia = "DEGRADANTE (Risco de colapso energético a longo prazo. Requer intervenção)."
    elif risco_final < risco_inicial:
        tendencia = "OTIMIZADA (Algoritmo de Smart Grid controlou as flutuações com sucesso)."
    else:
        tendencia = "ESTÁVEL (Consumo e geração em equilíbrio dinâmico sustentável)."
        
    print(f"• Matriz de Risco Geral da Missão: {tendencia}")
    print(f"• Subsistema Crítico com Maior Desperdício/Risco: {area_mais_afetada.upper()}")
    print("-" * 75)
    print(f"Recomendação do Sistema: Priorizar a manutenção preditiva no subsistema de {area_mais_afetada}")
    print("e recalibrar o direcionamento dos painéis fotovoltaicos automáticos.")
    print("=" * 75)

# Matriz de Dados Simulados Exigida: 6 Ciclos (Linhas) x 5 Parâmetros (Colunas)
dados_simulados_missao = [
    [25, 85, 90, 80, 95],  # Ciclo 1: Nominal total (Sustentável)
    [32, 75, 70, 70, 85],  # Ciclo 2: Pequenas flutuações térmicas
    [40, 50, 52, 60, 75],  # Ciclo 3: Alertas de armazenamento (Bateria baixando)
    [46, 35, 40, 45, 55],  # Ciclo 4: Entrada em zona de eclipse solar (Crítico)
    [28, 60, 48, 65, 70],  # Ciclo 5: Recuperação energética gradual
    [22, 80, 65, 82, 88]   # Ciclo 6: Estabilização pós-alocação inteligente de carga
]

if __name__ == "__main__":
    exibir_cabecalho()
    historico, metricas_anomalias = processar_ciclos_energeticos(dados_simulados_missao)
    gerar_diagnostico_final(historico, metricas_anomalias)