import matplotlib.pyplot as plt
import seaborn as sns

def plot_medias_e_precipitacao(medias_diarias, dados_precipitacao, limite_perigo=15):
    """Gera gráficos das médias diárias de temperatura e umidade e destaca precipitações perigosas."""
    
    # Definir o tamanho da figura e criar os subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 16))

    # Gráfico de linhas para temperatura
    sns.lineplot(data=medias_diarias, x='data', y='temperatura_media', label='Temperatura Média (°C)', 
                 color='orange', ax=ax1)
    
    # Personalizar o gráfico de temperatura
    ax1.set_title('Médias Diárias de Temperatura em Teresópolis', fontsize=16)
    ax1.set_xlabel('Data', fontsize=14)
    ax1.set_ylabel('Temperatura (°C)', fontsize=14)
    ax1.set_ylim(5, 35)  # Definir limites de temperatura
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True)
    ax1.legend(loc='upper left')

    # Gráfico de linhas para umidade 
    sns.lineplot(data=medias_diarias, x='data', y='umidade_media', label='Umidade Relativa (%)', 
                 color='green', ax=ax2)
    
   # Personalizar o gráfico de umidade
    ax2.set_title('Umidade Relativa em Teresópolis', fontsize=16)
    ax2.set_xlabel('Data', fontsize=14)
    ax2.set_ylabel('Umidade Relativa (%)', fontsize=14)
    ax2.set_ylim(50, 100)  # Definir limites de umidade
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True)
    ax2.legend(loc='upper left')

    # Gráfico de linhas para precipitação total
    sns.lineplot(data=dados_precipitacao, x='data', y='precipitacao_total', label='Precipitação Total (mm)', 
                 color='blue', ax=ax3)
    
    # Destacar os dias com precipitação acima do limite de perigo
    perigosos = dados_precipitacao[dados_precipitacao['precipitacao_total'] > limite_perigo]
    
    # Se houver dias perigosos, destacar com pontos
    if not perigosos.empty:
        ax3.scatter(perigosos['data'], perigosos['precipitacao_total'], color='red', s=100, zorder=25, 
                    label='Precipitação Perigosa')

    # Adicionar uma linha de referência para o limite de perigo
    ax3.axhline(y=limite_perigo, color='red', linestyle='--', label=f'Limite de Perigo: {limite_perigo} mm')

    # Ajustar a escala do eixo y para exibir até 50 mm
    ax3.set_ylim(0, 50)

    # Personalizar o gráfico de precipitação
    ax3.set_title('Precipitação Total Diária em Teresópolis com Destaque para Períodos Críticos', fontsize=16)
    ax3.set_xlabel('Data', fontsize=14)
    ax3.set_ylabel('Precipitação Total (mm)', fontsize=14)
    ax3.tick_params(axis='x', rotation=45)
    ax3.grid(True)
    ax3.legend(loc='upper left')

    # Ajustar o layout para evitar sobreposição
    plt.tight_layout()

    # Mostrar o gráfico final
    plt.show()