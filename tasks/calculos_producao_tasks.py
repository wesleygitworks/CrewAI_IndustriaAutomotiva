### tasks/calculos_producao_tasks.py
import pandas as pd

def calcular_kpis(dados: pd.DataFrame):
    if dados is None or dados.empty:
        return {"OEE": 0, "Takt_Time": 0, "Taxa_Defeitos": 0}

    tempo_disponivel_total_min = 480
    tempo_parada_total = dados['tempo_parada_min'].sum()
    volume_total = dados['volume_produzido'].sum()
    unidades_defeitos_total = dados['unidades_defeitos'].sum()
    demanda_total = dados['demanda_diaria'].sum()

    disponibilidade = (tempo_disponivel_total_min - tempo_parada_total) / tempo_disponivel_total_min
    takt_time_seg = (tempo_disponivel_total_min * 60) / demanda_total
    tempo_ciclo_medio = dados['tempo_ciclo_seg'].mean()
    performance = takt_time_seg / tempo_ciclo_medio if tempo_ciclo_medio > 0 else 0
    qualidade = (volume_total - unidades_defeitos_total) / volume_total if volume_total > 0 else 0
    oee = disponibilidade * performance * qualidade
    taxa_defeitos = (unidades_defeitos_total / volume_total) * 100 if volume_total > 0 else 0

    print("KPIs calculados: OEE, Takt Time e Taxa de Defeitos.")
    return {
        "OEE": round(oee * 100, 2),
        "Takt_Time": round(takt_time_seg, 2),
        "Taxa_Defeitos": round(taxa_defeitos, 2)
    }

def detectar_gargalos(dados: pd.DataFrame):
    if dados is None or dados.empty:
        return None

    media_tempo_ciclo = dados.groupby('estacao_trabalho')['tempo_ciclo_seg'].mean()
    estacao_gargalo = media_tempo_ciclo.idxmax()
    tempo_ciclo_gargalo = media_tempo_ciclo.max()
    print(f"Gargalo detectado na estação: {estacao_gargalo} com tempo de ciclo médio de {tempo_ciclo_gargalo}s.")
    return {"estacao": estacao_gargalo, "tempo_ciclo_medio": tempo_ciclo_gargalo}