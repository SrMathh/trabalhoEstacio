import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates

def plot_medias_e_precipitacao(medias_diarias, medias_mensais, dados_precipitacao, limite_perigo=15):
    """Gera gráficos das médias diárias de temperatura e umidade e destaca precipitações perigosas."""
    
    # Definir o tamanho da figura e criar os subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 16))

    # Gráfico de linhas para temperatura
    sns.lineplot(data=medias_diarias, x='data', y='temperatura_media', label='Temperatura Média (°C)', color='orange', ax=ax1)
    
    # Personalizar o gráfico de temperatura
    ax1.set_title('Médias Diárias de Temperatura em Teresópolis', fontsize=16)
    ax1.set_ylabel('Temperatura (°C)', fontsize=14)
    ax1.set_ylim(5, 35)  # Definir limites de temperatura
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True)
    ax1.legend(loc='upper left')

    # Gráfico de linhas para umidade 
    sns.lineplot(data=medias_mensais, x='mes', y='umidade_rel_hora', label='Umidade Relativa (%)', color='green', ax=ax2)
    
    # Personalizar o gráfico de umidade
    ax2.set_title('Umidade Relativa em Teresópolis', fontsize=16)
    ax2.set_ylabel('Umidade Relativa (%)', fontsize=14)
    ax2.set_ylim(60, 100)  # Definir limites de umidade
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True)
    ax2.legend(loc='upper left')

    # Criar o DataFrame com os dados de precipitação
    dados_precipitacao_df = pd.DataFrame({'data': medias_diarias['data'], 'precipitacao_total': dados_precipitacao})

    # Converter a coluna 'data' para formato datetime (se ainda não estiver)
    dados_precipitacao_df['data'] = pd.to_datetime(dados_precipitacao_df['data'])

    # Filtrar os dados para o intervalo de 2006 a 2024
    dados_precipitacao_df = dados_precipitacao_df[
        (dados_precipitacao_df['data'] >= pd.to_datetime('2006-05-01')) & 
        (dados_precipitacao_df['data'] <= pd.to_datetime('2024-12-31'))
    ]

    # Gráfico de linhas para precipitação total
    sns.lineplot(data=dados_precipitacao_df, x='data', y='precipitacao_total', label='Precipitação Total (mm)', 
                 color='blue', ax=ax3)

    # Linha pontilhada para o limite de perigo
    ax3.axhline(y=limite_perigo, color='red', linestyle='--', label=f'Limite de Perigo: {limite_perigo} mm')

    # Ajustar a escala do eixo y
    ax3.set_ylim(0, 50)  # Definir limites do eixo y de 0 a 50

    # Definir o intervalo do eixo x para exibir os anos de 2006 a 2024
    ax3.set_xlim(pd.to_datetime('2006-05-01'), pd.to_datetime('2024-12-31'))

    # Ajustar os ticks do eixo x para mostrar um tick por ano
    ax3.xaxis.set_major_locator(mdates.YearLocator())  # Tick a cada ano
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Mostrar o ano no formato YYYY
    ax3.tick_params(axis='x', rotation=45)

    # Destacar os pontos acima do limite de perigo
    perigosos = dados_precipitacao_df[dados_precipitacao_df['precipitacao_total'] > limite_perigo]
    
    # Adicionar os pontos vermelhos no gráfico para os dias com precipitação acima do limite de perigo
    ax3.scatter(perigosos['data'], perigosos['precipitacao_total'], color='red', label='Precipitação Perigosa', zorder=5)

    # Personalizar o gráfico
    ax3.set_title('Precipitação Total Diária em Teresópolis com Destaque para Períodos Críticos', fontsize=16)
    ax3.set_ylabel('Precipitação Total (mm)', fontsize=14)
    ax3.grid(True)
    ax3.legend(loc='upper left')

    # Ajustar o layout para evitar sobreposição
    plt.tight_layout()

    # Mostrar o gráfico final
    plt.show()
