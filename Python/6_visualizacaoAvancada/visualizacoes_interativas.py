from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('..\\..\\Python\\clientes-v3-preparado.csv')

lista_nivel_educacao = df['nivel_educacao'].unique()
options = [{'label': nivel, 'value': nivel} for nivel in lista_nivel_educacao]

def cria_graficos(selecao_nivel_educacao):
    # Gráfico de Barras:
    filtro_df = df[df['nivel_educacao'].isin(selecao_nivel_educacao)]

    fig1 = px.bar(filtro_df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group', color_discrete_sequence=px.colors.sequential)
    fig1.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='rgba(222, 255, 253, 1)',
        paper_bgcolor='rgba(186, 245, 241, 1)'
        )

    fig2 = px.scatter_3d(filtro_df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')
    fig2.update_layout(
        title='Salario X Idade X Anos de Experiencia',
        scene= dict(
            xaxis_title='Idade',
            yaxis_title='Salario',
            zaxis_title='Anos de Experiencia'
        )
    )

    return fig1, fig2

def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dashboard Interativo'),
        html.Div('''Interatividade entre os dados'''),
        html.Br(),
        html.H2('Gráfico de Salários por Estado Civil'),
        dcc.Checklist(
            id='id_selecao_nivel_educacao',
            options=options,
            value=[lista_nivel_educacao[0]],
        ),
        dcc.Graph(id='id_grafico_barras'),
        dcc.Graph(id='id_grafico_3d')
    ])
    return app

if __name__ == '__main__':
    app = cria_app()

    @app.callback(
        [
            Output('id_grafico_barras', 'figure'),
            Output('id_grafico_3d', 'figure')
        ]
        [Input('id_selecao_nivel_educacao', 'value')]
    )

    def atualiza_graficos(selecao_nivel_educacao):
        fig1, fig2 = cria_graficos(selecao_nivel_educacao)
        return [fig1, fig2]

    app.run_server(debug=True, port=8050)