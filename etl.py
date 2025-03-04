import pandas as pd
import os
import glob
from utilis_log import log_decorator
# uma funcao de extract que le e consolida os json

@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta,"*.json")) # retorna uma lista com os nomes dos arquivos na pasta
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] 
    df_total = pd.concat(df_list,ignore_index=True) # realiza a uniao dos tres dataset em um unico agrupado
    return df_total
@log_decorator
# uma funcao que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# um função que da load em csv ou parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)


# extrair_dados_e_consolidar()
# @extrair_dados_e_consolidar
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)

# uma funcao que da load em csv ou parquet