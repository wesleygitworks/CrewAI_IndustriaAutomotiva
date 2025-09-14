### agents/monitor_fluxo_agente.py
from tasks.calculos_producao_tasks import detectar_gargalos

class MonitorFluxo:
    """
    Agente responsável por identificar gargalos na linha de produção.
    """
    def __init__(self):
        self.nome = "Monitor de Fluxo"
        self.descricao = "Detecta gargalos na linha de produção."

    def executar_tarefa(self, dados_producao):
        print(f"[{self.nome}] Identificando possíveis gargalos...")
        return detectar_gargalos(dados_producao)