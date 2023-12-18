import os
import dash
from dash import html
import dash_bootstrap_components as dbc
from LSI_Solution.pages.page_cf import initialize_cf
from LSI_Solution.pages.page_2g import initialize_2g
from LSI_Solution.pages.page_3g import initialize_3g
from LSI_Solution.pages.page_nr import initialize_nr

# from pages import page_2G


def MultiPageApp(
    df_TXDC,
    df_IIP2,
    df_Cable,
    df_3GTXCP,
    df_fbrxgm_3G,
    df_fbrxgc_3G,
    df_fbrxfm_3G,
    df_fbrxfm_3G_ch,
    df_fbrxgm_NR,
    df_fbrxgc_NR,
    df_fbrxfm_NR,
    df_fbrxfc_NR,
    df_PRX_Gain_2G,
    df_Ripple_2G,
    df_RXGain_3G,
    df_RXComp_3G,
    df_RXGain_sub6,
    df_RXRSRP_sub6,
    df_RXComp_sub6,
    df_RXMixer_sub6,
    df_APT_Meas_3G,
    df_APT_Meas_sub6,
    df_3G_ETSAPT_Pst,
    df_3G_ETSAPT_Power,
    df_NR_ETSAPT_Psat,
    df_NR_ETSAPT_Pgain,
    df_NR_ETSAPT_Power,
    df_NR_ETSAPT_Freq,
):
    # app = dash.Dash(__name__, use_pages=True, pages_folder=pages_folder, external_stylesheets=[dbc.themes.COSMO])
    app = dash.Dash(__name__, use_pages=True, pages_folder="", external_stylesheets=[dbc.themes.COSMO])
    # app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.COSMO])

    initialize_cf(df_TXDC, df_IIP2, df_Cable)
    initialize_2g(df_PRX_Gain_2G, df_Ripple_2G)
    initialize_3g(
        df_3GTXCP,
        df_fbrxgm_3G,
        df_fbrxgc_3G,
        df_fbrxfm_3G,
        df_fbrxfm_3G_ch,
        df_RXGain_3G,
        df_RXComp_3G,
        df_APT_Meas_3G,
        df_3G_ETSAPT_Pst,
        df_3G_ETSAPT_Power,
    )
    initialize_nr(
        df_fbrxgm_NR,
        df_fbrxgc_NR,
        df_fbrxfm_NR,
        df_fbrxfc_NR,
        df_RXGain_sub6,
        df_RXRSRP_sub6,
        df_RXComp_sub6,
        df_RXMixer_sub6,
        df_APT_Meas_sub6,
        df_NR_ETSAPT_Psat,
        df_NR_ETSAPT_Pgain,
        df_NR_ETSAPT_Power,
        df_NR_ETSAPT_Freq,
    )

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
            dbc.Row([dbc.Col(html.Div("Dashboard [Model name] RF Cal Data", style={"fontSize": 50, "textAlign": "center"}))]),
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
