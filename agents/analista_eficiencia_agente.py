### agents/analista_eficiencia_agente.py
from tasks.calculos_producao_tasks import calcular_kpis

class AnalistaEficiencia:
    """
    Agente responsável por calcular os principais KPIs de eficiência.
    """
    def __init__(self):
        self.nome = "Analista de Eficiência"
        self.descricao = "Calcula KPIs como OEE, Takt Time e Taxa de Defeitos."

    def executar_tarefa(self, dados_producao):
        print(f"[{self.nome}] Analisando dados e calculando KPIs...")
        return calcular_kpis(dados_producao)