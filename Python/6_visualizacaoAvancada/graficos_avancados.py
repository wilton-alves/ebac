import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

# Histograma
def cria_g_histograma(df):
    fig1 = px.histogram(df, x='salario', nbins=30, title='Distrtribuição de salários')
    return fig1

# Pizza / Rosquinha
def cria_g_pizza(df):
    fig2 = px.pie(df, names='area_atuacao', color='area_atuacao', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)
    return fig2

# Gráfico de Bolhas
def cria_g_bolhas(df):
    fig3 = px.scatter(df, x='idade', y='salario', size='anos_experiencia', color='area_atuacao', hover_name='estado', size_max=60)
    fig3.update_layout(title='Salário por idade e anos de experiência')
    return fig3

# Gráfico de linhas
def cria_g_linhas(df):
    fig4 = px.line(df, x='idade', y='salario', color='area_atuacao', facet_col='nivel_educacao')
    fig4.update_layout(
        title='Salário por idade e Área de Atuação por Nível de Educação',
        xaxis_title='Idade',
        yaxis_title='Salário',
    )
    return fig4

# Gráfico 3D
def cria_g_3d(df):
    fig5 = px.scatter_3d(df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')
    return fig5

# Gráfico de barras
def cria_g_barras(df):
    fig6 = px.bar(df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group', color_discrete_sequence=px.colors.qualitative.Alphabet)
    fig6.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='rgba(222, 255, 255, 1)',  # Fundo Interno
        paper_bgcolor='rgba(186, 245, 241, 1)',  # Fundo Externo
    )
    return fig6


def gera_graficos(df):
    fig1 = cria_g_histograma(df)
    fig2 = cria_g_pizza(df)
    fig3 = cria_g_bolhas(df)
    fig4 = cria_g_linhas(df)
    fig5 = cria_g_3d(df)
    fig6 = cria_g_barras(df)
    return fig1, fig2, fig3, fig4, fig5, fig6


# Criar o aplicativo Dash
def cria_app(df):
    fig1, fig2, fig3, fig4, fig5, fig6 = gera_graficos(df)

    app = Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
    ])
    return app


# Carregar os dados
df = pd.read_csv('..\\..\\Python\\clientes-v3-preparado.csv')


# Executar o aplicativo
if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)