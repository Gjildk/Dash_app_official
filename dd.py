from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd 
import plotly.express as px

# Lien vers le fichier CSV
url = "https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv"

# Créez un DataFrame en utilisant on_bad_lines
df = pd.read_csv(url, on_bad_lines='skip')

app = Dash(__name__)

# Layout de base
app.layout = html.Div([
    dcc.Dropdown(
        id='book-dropdown',
        options=[{'label': title, 'value': title} for title in df['title']],
        value=df['title'].iloc[0],  # Valeur par défaut
    ),
    dcc.Graph(id='graph-example')
])

# Callback pour mettre à jour le graphique en fonction de la sélection
@app.callback(
    Output('graph-example', 'figure'),
    [Input('book-dropdown', 'value')]
)
def update_graph(selected_book):
    selected_data = df[df['title'] == selected_book]
    figure = px.bar(
        selected_data,
        x='title',
        y='  num_pages',
        labels={'  num_pages': 'Nombre de Pages'},
        title=f'Graphique à Barres pour "{selected_book}"'
    )
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
