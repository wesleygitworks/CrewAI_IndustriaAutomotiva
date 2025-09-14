import os
import sys
import pandas as pd
import pdfkit

# --- SOLUÇÃO DO PROBLEMA: Encontrar o caminho da pasta de saída ---
# Verifica se o programa está sendo executado como um executável de PyInstaller
if getattr(sys, 'frozen', False):
    # Se for um executável, o caminho base é o diretório onde o .exe está
    base_path = os.path.dirname(sys.executable)
else:
    # Se for um script Python, o caminho base é o diretório do script
    base_path = os.path.dirname(os.path.abspath(__file__))

# Define o caminho completo da pasta de saída
output_folder = os.path.join(base_path, 'outputs')

# Garante que a pasta de saída exista
os.makedirs(output_folder, exist_ok=True)
# -------------------------------------------------------------------

def gerar_relatorio_html(kpis, gargalo):
    print("Gerando relatório HTML...")
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Relatório de Produção</title>
        <style>
            body {{ font-family: sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            .container {{ width: 80%; margin: 0 auto; }}
            .kpi-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            .kpi-table th, .kpi-table td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            .kpi-table th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Relatório Diário de Produção</h1>
            <h2>Indicadores de Desempenho (KPIs)</h2>
            <table class="kpi-table">
                <tr><th>KPI</th><th>Valor</th></tr>
                <tr><td>OEE (Eficiência Geral do Equipamento)</td><td>{oee:.2f}%</td></tr>
                <tr><td>Takt Time</td><td>{takt_time:.2f}s/peça</td></tr>
                <tr><td>Taxa de Defeitos</td><td>{taxa_defeitos:.2f}%</td></tr>
            </table>
            <h2>Análise de Gargalo</h2>
            <p>O gargalo do dia foi detectado na **{gargalo_estacao}** com um tempo de ciclo médio de {gargalo_tempo:.2f} segundos.</p>
            <p>Este é o ponto que requer mais atenção para melhorar a eficiência geral da linha de produção.</p>
        </div>
    </body>
    </html>
    """
    html_content = template.format(
        oee=kpis.get('OEE', 0.0),
        takt_time=kpis.get('Takt_Time', 0.0),
        taxa_defeitos=kpis.get('Taxa_Defeitos', 0.0),
        gargalo_estacao=gargalo.get('estacao', 'N/A'),
        gargalo_tempo=gargalo.get('tempo_medio', 0.0)
    )
    
    html_file_path = os.path.join(output_folder, 'relatorio_producao.html')
    with open(html_file_path, "w") as f:
        f.write(html_content)

    print(f"Relatório HTML gerado em: {html_file_path}")

def gerar_planilha_excel(kpis, gargalo, dados_producao):
    print("Gerando planilha Excel...")
    excel_file_path = os.path.join(output_folder, 'relatorio_producao.xlsx')
    
    with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
        # Adiciona a aba com os dados brutos
        dados_producao.to_excel(writer, sheet_name='Dados Brutos', index=False)
        
        # Adiciona a aba com os KPIs
        kpis_df = pd.DataFrame(list(kpis.items()), columns=['KPI', 'Valor'])
        kpis_df.to_excel(writer, sheet_name='KPIs', index=False)
        
        # Adiciona a aba com os gargalos
        gargalo_df = pd.DataFrame([gargalo])
        gargalo_df.to_excel(writer, sheet_name='Gargalo', index=False)

    print(f"Planilha Excel gerada em: {excel_file_path}")

def gerar_relatorio_pdf():
    print("Gerando relatório PDF...")
    
    # Caminhos completos para os arquivos de entrada e saída
    html_file_path = os.path.join(output_folder, 'relatorio_producao.html')
    pdf_file_path = os.path.join(output_folder, 'relatorio_producao.pdf')
    
    try:
        # Tenta gerar o PDF a partir do HTML
        pdfkit.from_file(html_file_path, pdf_file_path)
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")
        print("Certifique-se de que o wkhtmltopdf está instalado corretamente e acessível via PATH.")
        
    print(f"Relatório PDF gerado em: {pdf_file_path}")