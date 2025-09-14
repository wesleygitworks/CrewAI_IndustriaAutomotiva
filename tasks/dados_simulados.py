### tasks/dados_simulados.py
import pandas as pd
import random
from datetime import datetime

def gerar_dados_producao():
    data_atual = datetime.now().strftime('%Y-%m-%d')
    turnos = ['1', '2', '3']
    produtos = ['Carro A', 'Carro B']
    estacoes = ['Estacao 1', 'Estacao 2', 'Estacao 3']

    dados_producao = []

    for turno in turnos:
        for produto in produtos:
            for estacao in estacoes:
                tempo_ciclo = random.randint(55, 75)
                volume_produzido = random.randint(100, 130)
                unidades_defeitos = random.randint(1, 10)
                tempo_parada_min = random.randint(5, 20)
                demanda_diaria = random.randint(450, 600)

                dados_producao.append({
                    'data': data_atual,
                    'turno': turno,
                    'produto': produto,
                    'estacao_trabalho': estacao,
                    'tempo_ciclo_seg': tempo_ciclo,
                    'volume_produzido': volume_produzido,
                    'unidades_defeitos': unidades_defeitos,
                    'tempo_parada_min': tempo_parada_min,
                    'demanda_diaria': demanda_diaria
                })

    dados = pd.DataFrame(dados_producao)
    print("Dados de produção simulados e gerados com sucesso para o dia de hoje.")
    return dados