from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')

def cria_graficos():
    # Histograma
    fig1 = px.histogram(df, x='Preço', nbins=20, title='Distribuição de Preços')
    fig1.update_layout(xaxis_title='Preço', yaxis_title='Frequência')

    # Gráfico de dispersão
    fig2 = px.scatter(df, x='Qtd_Vendidos_Cod', y='Temporada_Cod')
    fig2.update_layout(
        title='Relação entre Quantidade Vendida e Temporada',
        xaxis_title='Quantidade Vendida',
        yaxis_title='Temporada'
    )
    
    # Mapa de calor
    df_corr = df[['Nota', 'N_Avaliações', 'Qtd_Vendidos_Cod', 'Preço', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod']].corr()
    rotulos = df_corr.columns
    fig3 = px.imshow(df_corr, labels=dict(color="Correlation"), x=rotulos, y=rotulos, text_auto=False)
    fig3.update_layout(title='Correlação entre variáveis do Dataframe')
    fig3.update_traces(
        texttemplate='%{z:.2f}',
        text=df_corr.values
    )
    
    # Gráfico de barras
    fig4 = px.bar(df, x='Nota', y='N_Avaliações', color='Temporada_Cod', color_discrete_sequence=px.colors.qualitative.Bold_r)
    fig4.update_layout(
    title='Notas Por Número de Avaliações por Temporada',
    xaxis_title='Nota',
    yaxis_title='Número de Avaliações',
    legend_title='Temporada'
    )

    # Gráfico de pizza
    fig5 = px.pie(df, names='Gênero', color='Gênero', color_discrete_sequence=px.colors.sequential.RdBu)
    
    # Gráfico de Densidade
    # Não há uma função específica para criar gráfico de densidade no Plotly, então utilizei o seaborn como apoio
    import plotly.graph_objects as go
    import seaborn as sns
    kde = sns.kdeplot(df['Preço'], bw_adjust=0.5)  # Ajuste a largura de banda (bw_adjust)
    x_vals = kde.get_lines()[0].get_xdata()
    y_vals = kde.get_lines()[0].get_ydata()

    fig6 = go.Figure()
    fig6.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', fill='tozeroy', line=dict(color='#863e9c')))
    fig6.update_layout(title="Densidade de Preço", xaxis_title="Preço", yaxis_title="Densidade")

    # Gráfico de Regressão
    fig7 = px.scatter(df, x='Preço', y='Desconto', opacity=0.6, trendline='ols', trendline_color_override='DarkBlue')
    fig7.update_layout(
    title='Relação entre Preço e Desconto (Com OLS)',
    xaxis_title='Preço',
    yaxis_title='Desconto'
    )

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7


def cria_app():
    app = Dash(__name__)
    fig1, fig2, fig3, fig4, fig5, fig6, fig7 = cria_graficos()

    app.layout = html.Div([
        html.H1('Projeto 3 - Vizualização avançada com Plotly'),
        html.Br(),
        html.H2('Gráficos'),
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7)
    ])

    return app



if __name__ == '__main__':
    app = cria_app()
    app.run_server(debug=True)

