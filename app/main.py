from cloud import Cloud
from processamento import calcular_medias
from visualizacao import plot_medias_e_precipitacao

if __name__ == '__main__':
    # Coleta dos dados
    df_microdados = Cloud.get_data_teresopolis()

    # Processamento dos dados
    medias_diarias, medias_mensais = calcular_medias(df_microdados)
    
    # Extração dos dados de precipitação
    dados_precipitacao = df_microdados['precipitacao_total']  # Isso está correto

    # Visualização dos dados
    plot_medias_e_precipitacao(medias_diarias, medias_mensais, dados_precipitacao)
