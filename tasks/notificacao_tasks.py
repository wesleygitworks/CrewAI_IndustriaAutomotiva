### tasks/notificacao_tasks.py
def enviar_alerta(mensagem: str, canal: str = "email"):
    print(f"\n[ALERTA DE SISTEMA] Enviando notificação via {canal.upper()}:")
    print("----------------------------------------------------------------")
    print(f"{mensagem}")
    print("----------------------------------------------------------------\n")