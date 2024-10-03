from google.cloud import bigquery
import pandas as pd
import os

class Cloud:
    
    def set_credentials():
        """Define o caminho para o arquivo JSON de credenciais do Google Cloud."""
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/noclaf/Documentos/pyton/bigData/json/bigdata-436913-05b3d371b5d4.json"

    def get_info_tere():
        """Busca informações gerais sobre as estações meteorológicas de Teresópolis."""
        # Configurar as credenciais
        Cloud.set_credentials()

        # Criar cliente BigQuery
        client = bigquery.Client()

        # Definir a query para buscar informações das estações de Teresópolis
        query = """
        SELECT
            dados.id_municipio,
            dados.id_estacao,
            dados.estacao,
            dados.data_fundacao,
            dados.latitude,
            dados.longitude,
            dados.altitude,
            diretorio_id_municipio.nome as nome_municipio
        FROM `basedosdados.br_inmet_bdmep.estacao` AS dados
        LEFT JOIN `basedosdados.br_bd_diretorios_brasil.municipio` AS diretorio_id_municipio
        ON dados.id_municipio = diretorio_id_municipio.id_municipio
        WHERE diretorio_id_municipio.nome = 'Teresópolis'
        """

        # Executar a consulta e converter para DataFrame
        df = client.query(query).to_dataframe()

        # Exibir as primeiras linhas do DataFrame
        print("Informações das estações meteorológicas de Teresópolis:")
        print(df.head())

        return df

    def get_data_teresopolis(id_estacao='A618'):
        """Busca microdados meteorológicos de uma estação específica de Teresópolis."""
        # Configurar as credenciais
        Cloud.set_credentials()

        # Criar cliente BigQuery
        client = bigquery.Client()

        # Definir a query para buscar microdados da estação específica
        query = f"""
        SELECT *
        FROM `basedosdados.br_inmet_bdmep.microdados`
        WHERE id_estacao = '{id_estacao}'
        """

        # Executar a consulta e armazenar o resultado em um DataFrame
        df = client.query(query).to_dataframe()

        # Remover valores NaN e converter a coluna 'data' para datetime
        df = df.dropna()
        # Garantir que a coluna 'data' esteja no formato datetime
        df['data'] = pd.to_datetime(df['data'], errors='coerce')

        # Ordenar os dados pela data
        df_sorted = df.sort_values(by='data', ascending=True)
        
        # Formatar a coluna de data para mostrar apenas dia, mês e ano
        df_sorted['data'] = df_sorted['data'].dt.strftime('%d-%m-%Y')

        # Salvar os dados em um arquivo Excel
        df_sorted.to_excel('dados_ordenados.xlsx', index=False, engine='openpyxl')

        # Exibir as primeiras linhas dos microdados da estação específica
        print("Microdados da estação específica:")
        print(df_sorted.head())

        return df_sorted
