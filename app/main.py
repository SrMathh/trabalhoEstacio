from cloud import Cloud
from processamento import calcular_medias
from visualizacao import plot_medias

if __name__ == '__main__':
    # Coleta dos dados
    df_microdados = Cloud.get_data_teresopolis()

    # Processamento dos dados
    medias_diarias = calcular_medias(df_microdados)

    # Visualização dos dados
    plot_medias(medias_diarias)
