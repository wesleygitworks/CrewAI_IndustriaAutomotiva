### agents/relatorio_visualizacao_agente.py
from tasks.relatorio_tasks import gerar_relatorio_html, gerar_relatorio_pdf, gerar_planilha_excel

class RelatorioVisualizacao:
    """
    Agente responsável por consolidar os resultados e gerar os relatórios finais.
    """
    def __init__(self):
        self.nome = "Gerador de Relatórios"
        self.descricao = "Consolida informações e gera relatórios finais."

    def executar_tarefa(self, kpis, gargalo, dados_producao):
        print(f"[{self.nome}] Consolidando informações e gerando relatórios...")
        # A ordem de geração é importante para o PDF
        gerar_relatorio_html(kpis, gargalo)
        gerar_planilha_excel(kpis, gargalo, dados_producao)
        gerar_relatorio_pdf()
        return "Relatórios gerados com sucesso."