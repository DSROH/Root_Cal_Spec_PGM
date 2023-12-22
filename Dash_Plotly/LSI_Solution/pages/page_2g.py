import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import (
    df_strip,
    Create_dropdown,
    Create_range_slider,
    Initialize_band,
    Band_list,
    Update_band_and_graph,
)


def Initialize_2g(dict_2g):
    df_PRX_Gain_2G = df_strip(dict_2g["RXGain"])
    df_Ripple_2G = df_strip(dict_2g["RXRipp"])
    df_GMSK_Mean = df_strip(dict_2g["GMSK"])
    df_GMSK_TxL_Mean = df_strip(dict_2g["GMSK_TxL"])
    df_GMSK_Code_Mean = df_strip(dict_2g["GMSK_Code"])
    df_EPSK_Mean = df_strip(dict_2g["EPSK"])
    df_EPSK_TxL_Mean = df_strip(dict_2g["EPSK_TxL"])
    df_EPSK_Code_Mean = df_strip(dict_2g["EPSK_Code"])

    band_opt = [{"label": "", "value": ""}]

    drop_2GRXGain_rat = Create_dropdown("2G_RXGain_RAT", "G", [{"label": "2G", "value": "G"}])
    drop_2GRXRipp_rat = Create_dropdown("2G_RXRipp_RAT", "G", [{"label": "2G", "value": "G"}])

    drop_2G_GMSK_rat = Create_dropdown("2G_GMSK_RAT", "G", [{"label": "2G", "value": "G"}])
    drop_2G_GMSKTxL_rat = Create_dropdown("2G_GMSKTxL_RAT", "G", [{"label": "2G", "value": "G"}])
    drop_2G_GMSKCode_rat = Create_dropdown("2G_GMSKCode_RAT", "G", [{"label": "2G", "value": "G"}])

    drop_2G_EPSK_rat = Create_dropdown("2G_EPSK_RAT", "G", [{"label": "2G", "value": "G"}])
    drop_2G_EPSKTxL_rat = Create_dropdown("2G_EPSKTxL_RAT", "G", [{"label": "2G", "value": "G"}])
    drop_2G_EPSKCode_rat = Create_dropdown("2G_EPSKCode_RAT", "G", [{"label": "2G", "value": "G"}])

    drop_2GRXGain_band = Create_dropdown("2G_RXGain_band", "", band_opt)
    drop_2GRXRipp_band = Create_dropdown("2G_RXRipp_band", "", band_opt)

    drop_2G_GMSK_band = Create_dropdown("2G_GMSK_band", "", band_opt)
    drop_2G_GMSKTxL_band = Create_dropdown("2G_GMSKTxL_band", "", band_opt)
    drop_2G_GMSKCode_band = Create_dropdown("2G_GMSKCode_band", "", band_opt)

    drop_2G_EPSK_band = Create_dropdown("2G_EPSK_band", "", band_opt)
    drop_2G_EPSKTxL_band = Create_dropdown("2G_EPSKTxL_band", "", band_opt)
    drop_2G_EPSKCode_band = Create_dropdown("2G_EPSKCode_band", "", band_opt)

    layout = html.Div(
        [
            # ** ============================== 2G RX Cain cal ==============================
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
                    dbc.Col(dcc.Graph(id="2G_RXGain_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_RXGain_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_RXGain_scat", df_PRX_Gain_2G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 2G RX Ripple cal ==============================
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
                    dbc.Col(dcc.Graph(id="2G_RXRipp_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_RXRipp_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_RXRipp_scat", df_Ripple_2G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 2G TX GMSK Index ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("2G TX GMSK Index", className="display-7"), width="auto"),
                    dbc.Col(drop_2G_GMSK_rat, width=1),
                    dbc.Col(drop_2G_GMSK_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2G_GMSK_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_GMSK_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_GMSK_scat", df_GMSK_Mean, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 2G TX GMSK TxL ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("2G TX GMSK TxL", className="display-7"), width="auto"),
                    dbc.Col(drop_2G_GMSKTxL_rat, width=1),
                    dbc.Col(drop_2G_GMSKTxL_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2G_GMSKTxL_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_GMSKTxL_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_GMSKTxL_scat", df_GMSK_TxL_Mean, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 2G TX GMSK Code ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("2G TX GMSK Code", className="display-7"), width="auto"),
                    dbc.Col(drop_2G_GMSKCode_rat, width=1),
                    dbc.Col(drop_2G_GMSKCode_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2G_GMSKCode_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_GMSKCode_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_GMSKCode_scat", df_GMSK_Code_Mean, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 2G TX EPSK Index ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("2G TX EPSK Index", className="display-7"), width="auto"),
                    dbc.Col(drop_2G_EPSK_rat, width=1),
                    dbc.Col(drop_2G_EPSK_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2G_EPSK_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_EPSK_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_EPSK_scat", df_EPSK_Mean, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 2G TX EPSK TxL ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("2G TX EPSK TxL", className="display-7"), width="auto"),
                    dbc.Col(drop_2G_EPSKTxL_rat, width=1),
                    dbc.Col(drop_2G_EPSKTxL_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2G_EPSKTxL_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_EPSKTxL_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_EPSKTxL_scat", df_EPSK_TxL_Mean, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 2G TX EPSK Code ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("2G TX EPSK Code", className="display-7"), width="auto"),
                    dbc.Col(drop_2G_EPSKCode_rat, width=1),
                    dbc.Col(drop_2G_EPSKCode_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="2G_EPSKCode_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="2G_EPSKCode_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_2G_EPSKCode_scat", df_EPSK_Code_Mean, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ** ============================== 2G RX Cain cal ==============================
    @callback(Output("2G_RXGain_band", "value"), Input("2G_RXGain_RAT", "value"))
    def RXGain_2G(selected_r):
        return Initialize_band(selected_r, df_PRX_Gain_2G)

    @callback(
        [
            Output("2G_RXGain_band", "options"),
            Output("2G_RXGain_grp_scatt", "figure"),
            Output("2G_RXGain_grp_histo", "figure"),
        ],
        [Input("2G_RXGain_RAT", "value"), Input("2G_RXGain_band", "value"), Input("sld_2G_RXGain_scat", "value")],
    )
    def update_2G_RXGain(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_PRX_Gain_2G, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_PRX_Gain_2G, selected_r)
        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G RX Ripple cal ==============================
    @callback(Output("2G_RXRipp_band", "value"), Input("2G_RXRipp_RAT", "value"))
    def RXRipp_2G(selected_r):
        return Initialize_band(selected_r, df_Ripple_2G)

    @callback(
        [
            Output("2G_RXRipp_band", "options"),
            Output("2G_RXRipp_grp_scatt", "figure"),
            Output("2G_RXRipp_grp_histo", "figure"),
        ],
        [Input("2G_RXRipp_RAT", "value"), Input("2G_RXRipp_band", "value"), Input("sld_2G_RXRipp_scat", "value")],
    )
    def update_2G_RXRipp(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_Ripple_2G, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_Ripple_2G, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX GMSK Index ==============================
    @callback(Output("2G_GMSK_band", "value"), Input("2G_GMSK_RAT", "value"))
    def GMSK_2G(selected_r):
        return Initialize_band(selected_r, df_GMSK_Mean)

    @callback(
        [
            Output("2G_GMSK_band", "options"),
            Output("2G_GMSK_grp_scatt", "figure"),
            Output("2G_GMSK_grp_histo", "figure"),
        ],
        [Input("2G_GMSK_RAT", "value"), Input("2G_GMSK_band", "value"), Input("sld_2G_GMSK_scat", "value")],
    )
    def update_2G_GMSK(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_GMSK_Mean, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_GMSK_Mean, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX GMSK TxL ==============================
    @callback(Output("2G_GMSKTxL_band", "value"), Input("2G_GMSKTxL_RAT", "value"))
    def GMSKTxL_2G(selected_r):
        return Initialize_band(selected_r, df_GMSK_TxL_Mean)

    @callback(
        [
            Output("2G_GMSKTxL_band", "options"),
            Output("2G_GMSKTxL_grp_scatt", "figure"),
            Output("2G_GMSKTxL_grp_histo", "figure"),
        ],
        [Input("2G_GMSKTxL_RAT", "value"), Input("2G_GMSKTxL_band", "value"), Input("sld_2G_GMSKTxL_scat", "value")],
    )
    def update_2G_GMSKTxL(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_GMSK_TxL_Mean, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_GMSK_TxL_Mean, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX GMSK Code ==============================
    @callback(Output("2G_GMSKCode_band", "value"), Input("2G_GMSKCode_RAT", "value"))
    def GMSKCode_2G(selected_r):
        return Initialize_band(selected_r, df_GMSK_Code_Mean)

    @callback(
        [
            Output("2G_GMSKCode_band", "options"),
            Output("2G_GMSKCode_grp_scatt", "figure"),
            Output("2G_GMSKCode_grp_histo", "figure"),
        ],
        [Input("2G_GMSKCode_RAT", "value"), Input("2G_GMSKCode_band", "value"), Input("sld_2G_GMSKCode_scat", "value")],
    )
    def update_2G_GMSKCode(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_GMSK_Code_Mean, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_GMSK_Code_Mean, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX EPSK Index ==============================
    @callback(Output("2G_EPSK_band", "value"), Input("2G_EPSK_RAT", "value"))
    def EPSK_2G(selected_r):
        return Initialize_band(selected_r, df_EPSK_Mean)

    @callback(
        [
            Output("2G_EPSK_band", "options"),
            Output("2G_EPSK_grp_scatt", "figure"),
            Output("2G_EPSK_grp_histo", "figure"),
        ],
        [Input("2G_EPSK_RAT", "value"), Input("2G_EPSK_band", "value"), Input("sld_2G_EPSK_scat", "value")],
    )
    def update_2G_EPSK(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_EPSK_Mean, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_EPSK_Mean, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX EPSK TxL ==============================
    @callback(Output("2G_EPSKTxL_band", "value"), Input("2G_EPSKTxL_RAT", "value"))
    def EPSKTxL_2G(selected_r):
        return Initialize_band(selected_r, df_EPSK_TxL_Mean)

    @callback(
        [
            Output("2G_EPSKTxL_band", "options"),
            Output("2G_EPSKTxL_grp_scatt", "figure"),
            Output("2G_EPSKTxL_grp_histo", "figure"),
        ],
        [Input("2G_EPSKTxL_RAT", "value"), Input("2G_EPSKTxL_band", "value"), Input("sld_2G_EPSKTxL_scat", "value")],
    )
    def update_2G_EPSKTxL(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_EPSK_TxL_Mean, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_EPSK_TxL_Mean, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX EPSK Code ==============================
    @callback(Output("2G_EPSKCode_band", "value"), Input("2G_EPSKCode_RAT", "value"))
    def EPSKCode_2G(selected_r):
        return Initialize_band(selected_r, df_EPSK_Code_Mean)

    @callback(
        [
            Output("2G_EPSKCode_band", "options"),
            Output("2G_EPSKCode_grp_scatt", "figure"),
            Output("2G_EPSKCode_grp_histo", "figure"),
        ],
        [Input("2G_EPSKCode_RAT", "value"), Input("2G_EPSKCode_band", "value"), Input("sld_2G_EPSKCode_scat", "value")],
    )
    def update_2G_EPSKCode(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_EPSK_Code_Mean, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_EPSK_Code_Mean, selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/GSM", name="GSM", title="GSM", layout=layout)

    return layout
