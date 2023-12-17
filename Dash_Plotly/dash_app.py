# dash_app.py

import dash
from dash import html
import dash_bootstrap_components as dbc
from pages.page_CF import initialize_cf
from pages.page_3G import initialize_3g
from pages.page_NR import initialize_nr

# from pages import page_2G


class MultiPageApp:
    def __init__(
        self,
        df_TXDC,
        df_IIP2,
        df_Cable,
        df_3GTXCP,
        df_fbrxgm_3G,
        df_fbrxgc_3G,
        df_fbrxfm_3G,
        df_fbrxgm_NR,
        df_fbrxgc_NR,
        df_fbrxfm_NR,
        df_fbrxfc_NR,
    ):
        self.app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
        self.server = self.app.server

        # 페이지 초기화 및 등록
        initialize_cf(df_TXDC, df_IIP2, df_Cable)
        initialize_3g(df_3GTXCP, df_fbrxgm_3G, df_fbrxgc_3G, df_fbrxfm_3G)
        initialize_nr(df_fbrxgm_NR, df_fbrxgc_NR, df_fbrxfm_NR, df_fbrxfc_NR)
        # initialize_2g(df_TXDC, df_IIP2, df_Cable)

        self.sidebar = dbc.Nav(
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

        self.app.layout = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                "Dashboard [Model name] RF Cal Data", style={"fontSize": 50, "textAlign": "center"}
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([self.sidebar], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
                        dbc.Col([dash.page_container], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10),
                    ]
                ),
            ],
            fluid=True,
        )

    def run(self):
        self.app.run(debug=True)
