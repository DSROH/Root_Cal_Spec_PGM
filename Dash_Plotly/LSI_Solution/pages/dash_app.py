import os
import dash
from dash import html
import dash_bootstrap_components as dbc
from LSI_Solution.pages.page_cf import initialize_cf
from LSI_Solution.pages.page_2g import initialize_2g
from LSI_Solution.pages.page_3g import initialize_3g
from LSI_Solution.pages.page_nr import initialize_nr


def MultiPageApp(dict_cf, dict_2g, dict_3g, dict_nr):

    print(os.getcwd())
    # app = dash.Dash(__name__, use_pages=True, pages_folder=pages_folder, external_stylesheets=[dbc.themes.COSMO])
    # app = dash.Dash(__name__, use_pages=True, pages_folder="LSI_Solution/pages", external_stylesheets=[dbc.themes.COSMO])
    # app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.COSMO])
    # app = dash.Dash(__name__, use_pages=True, pages_folder="/Users/dsroh/Python/Multipage_dash/LSI_Solution/pages", external_stylesheets=[dbc.themes.COSMO])

    current_directory = os.path.dirname(__file__)  # 현재 파일의 디렉토리 경로
    app = dash.Dash(__name__, use_pages=True, pages_folder=current_directory, external_stylesheets=[dbc.themes.COSMO])


    initialize_cf(dict_cf)
    initialize_2g(dict_2g)
    initialize_3g(dict_3g)
    initialize_nr(dict_nr)

    sidebar = dbc.Nav(
        [
            dbc.NavLink(
                [
                    html.Div(page["name"], className="ms-2"),
                ],
                href=page["path"],
                active="exact",
            )
            for page in dash.page_registry.values()
        ],
        vertical=True,
        pills=True,
        className="bg-light",
    )

    app.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Div("Dashboard [Model name] RF Cal Data", style={"fontSize": 50, "textAlign": "center"})
                    )
                ]
            ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col([sidebar], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
                    dbc.Col([dash.page_container], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10),
                ]
            ),
        ],
        fluid=True,
    )

    app.run(debug=True, use_reloader=False, port=8050)
