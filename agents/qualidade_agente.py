### agents/qualidade_agente.py
from tasks.notificacao_tasks import enviar_alerta

class Qualidade:
    """
    Agente responsável por analisar a qualidade da produção e gerar alertas.
    """
    def __init__(self):
        self.nome = "Especialista em Qualidade"
        self.descricao = "Verifica indicadores de qualidade e gera alertas."

    def executar_tarefa(self, kpis):
        print(f"[{self.nome}] Analisando taxa de defeitos para gerar alertas...")
        taxa_defeitos = kpis.get("Taxa_Defeitos", 0)
        mensagem_alerta = None
        if taxa_defeitos > 5.0:
            mensagem_alerta = f"ALERTA: A taxa de defeitos atual de {taxa_defeitos}% excede o limite aceitável de 5%. Ação imediata é necessária."
            enviar_alerta(mensagem_alerta)
        else:
            print("Nenhum alerta de qualidade necessário. A taxa está dentro do limite.")
        return {"taxa_defeitos": taxa_defeitos, "mensagem_alerta": mensagem_alerta}