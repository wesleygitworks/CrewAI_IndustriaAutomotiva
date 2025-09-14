import os
# Importa as classes que representam os "agentes"
from agents.coletor_dados_agente import ColetorDados
from agents.analista_eficiencia_agente import AnalistaEficiencia
from agents.monitor_fluxo_agente import MonitorFluxo
from agents.qualidade_agente import Qualidade
from agents.relatorio_visualizacao_agente import RelatorioVisualizacao

print("### Iniciando o Programa de Automação Industrial ###")

# 1. Instancia os agentes
coletor_agente = ColetorDados()
analista_eficiencia_agente = AnalistaEficiencia()
monitor_fluxo_agente = MonitorFluxo()
qualidade_agente = Qualidade()
relatorio_visualizacao_agente = RelatorioVisualizacao()

# 2. Execução sequencial das tarefas
dados_producao_df = coletor_agente.executar_tarefa()
if dados_producao_df is None or dados_producao_df.empty:
    print("Erro: Não foi possível obter os dados de produção. Encerrando o projeto.")
    exit()

kpis = analista_eficiencia_agente.executar_tarefa(dados_producao_df)
gargalo = monitor_fluxo_agente.executar_tarefa(dados_producao_df)
analise_qualidade = qualidade_agente.executar_tarefa(kpis)
resultado_final = relatorio_visualizacao_agente.executar_tarefa(kpis, gargalo, dados_producao_df)

print("\n--- Processo Concluído ---")
print(f"Relatórios gerados com sucesso na pasta 'outputs/'.")
print("--------------------------")