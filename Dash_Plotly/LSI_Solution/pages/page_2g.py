import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import create_dropdown, create_range_slider, Initialize_band, update_band_and_graph


def initialize_2g(dict_2g):
    df_PRX_Gain_2G = dict_2g["RXGain"]
    df_Ripple_2G = dict_2g["RXRipp"]

    band_opt = [{"label": "", "value": ""}]

    drop_2GRXGain_rat = create_dropdown("2GRXGain_RAT", "G", [{"label": "2G", "value": "G"}])
    drop_2GRXRipp_rat = create_dropdown("2GRXRipp_RAT", "G", [{"label": "2G", "value": "G"}])

    drop_2GRXGain_band = create_dropdown("2GRXGain_band", "", band_opt)
    drop_2GRXRipp_band = create_dropdown("2GRXRipp_band", "", band_opt)

    layout = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.H2("2G RX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_2GRXGain_rat, width=1),
                    dbc.Col(drop_2GRXGain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2GRXGain_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2GRXGain_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_2GRXGain_scat", df_PRX_Gain_2G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(html.H2("2G RX Ripple", className="display-7"), width="auto"),
                    dbc.Col(drop_2GRXRipp_rat, width=1),
                    dbc.Col(drop_2GRXRipp_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2GRXRipp_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2GRXRipp_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_2GRXRipp_scat", df_Ripple_2G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    @callback(Output("2GRXGain_band", "value"), Input("2GRXGain_RAT", "value"))
    def RXGain_2G(Sel_rat):
        return Initialize_band(Sel_rat, df_PRX_Gain_2G)

    @callback(
        [
            Output("2GRXGain_band", "options"),
            Output("2GRXGain_grp_scatt", "figure"),
            Output("2GRXGain_grp_histo", "figure"),
        ],
        [Input("2GRXGain_RAT", "value"), Input("2GRXGain_band", "value"), Input("sld_2GRXGain_scat", "value")],
    )
    def update_2GRXGain(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_PRX_Gain_2G, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    @callback(Output("2GRXRipp_band", "value"), Input("2GRXRipp_RAT", "value"))
    def RXRipp_2G(Sel_rat):
        return Initialize_band(Sel_rat, df_Ripple_2G)

    @callback(
        [
            Output("2GRXRipp_band", "options"),
            Output("2GRXRipp_grp_scatt", "figure"),
            Output("2GRXRipp_grp_histo", "figure"),
        ],
        [Input("2GRXRipp_RAT", "value"), Input("2GRXRipp_band", "value"), Input("sld_2GRXRipp_scat", "value")],
    )
    def update_3GFBRXFreq(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_Ripple_2G, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/GSM", name="GSM", title="GSM", layout=layout)

    return layout
