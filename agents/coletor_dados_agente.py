### agents/coletor_dados_agente.py
from tasks.dados_simulados import gerar_dados_producao

class ColetorDados:
    """
    Agente responsável por coletar ou gerar os dados brutos de produção.
    """
    def __init__(self):
        self.nome = "Coletor de Dados"
        self.descricao = "Coleta e prepara dados de produção."

    def executar_tarefa(self):
        print(f"[{self.nome}] Iniciando coleta e geração de dados...")
        return gerar_dados_producao()