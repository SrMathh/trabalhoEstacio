import pandas as pd

def calcular_medias(df):
    """Calcula as médias de temperatura, umidade e precipitação."""
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['temperatura_media'] = (df['temperatura_max'] + df['temperatura_min']) / 2
    
    # Calcular médias diárias
    medias_diarias = df.groupby(df['data'].dt.date).agg({
        'temperatura_media': 'mean',
        'precipitacao_total': 'mean'
    }).reset_index()
    
    # Renomear a coluna de precipitação
    medias_diarias.rename(columns={'precipitacao_total': 'precipitacao_media'}, inplace=True)

    # Calcular médias mensais para umidade
    df['mes'] = df['data'].dt.to_period('M')  # Criar uma coluna de período mensal
    medias_mensais = df.groupby('mes').agg({
        'umidade_rel_hora': 'mean'  # Calcular a média de umidade
    }).reset_index()

    # Renomear coluna para corresponder ao formato
    medias_mensais['mes'] = medias_mensais['mes'].dt.to_timestamp()  # Converter de período para timestamp

    return medias_diarias, medias_mensais
