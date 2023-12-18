import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import create_dropdown, create_range_slider, Initialize_band, update_band_and_graph


def initialize_3g(dict_3g):
    df_3GTXCP = dict_3g["TxP_CC"]
    df_RXGain_3G = dict_3g["RX_Gain"]
    df_RXComp_3G = dict_3g["RX_Comp"]
    df_fbrxgm_3G = dict_3g["FBRX_GM"]
    df_fbrxgc_3G = dict_3g["FBRX_GC"]
    df_fbrxfm_3G = dict_3g["FBRX_FM"]
    df_fbrxfm_3G_ch = dict_3g["FBRX_FM_Ch"]
    df_APT_Meas_3G = dict_3g["APT_Meas"]
    df_3G_ETSAPT_Pst = dict_3g["ET_Psat"]
    df_3G_ETSAPT_Power = dict_3g["ET_Pgain"]

    band_opt = [{"label": "", "value": ""}]

    drop_TXCP_rat = create_dropdown("3G_TXCP_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_FBRXGain_rat = create_dropdown("3G_FBRXGain_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_FBRXFreq_rat = create_dropdown("3G_FBRXFreq_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_FBRXFreq_ch_rat = create_dropdown("3G_FBRXFreq_ch_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_RXGain_rat = create_dropdown("3G_RXGain_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_RXComp_rat = create_dropdown("3G_RXComp_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_APTMeas_rat = create_dropdown("3G_APTMeas_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_ETPsat_rat = create_dropdown("3G_ETPsat_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_ETPower_rat = create_dropdown("3G_ETPower_RAT", "B", [{"label": "3G", "value": "B"}])

    drop_TXCP_band = create_dropdown("3G_TXCP_band", "", band_opt)
    drop_FBRXGain_band = create_dropdown("3G_FBRXGain_band", "", band_opt)
    drop_FBRXFreq_band = create_dropdown("3G_FBRXFreq_band", "", band_opt)
    drop_FBRXFreq_ch_band = create_dropdown("3G_FBRXFreq_ch_band", "", band_opt)
    drop_RXGain_band = create_dropdown("3G_RXGain_band", "", band_opt)
    drop_RXComp_band = create_dropdown("3G_RXComp_band", "", band_opt)
    drop_APTMeas_band = create_dropdown("3G_APTMeas_band", "", band_opt)
    drop_ETPsat_band = create_dropdown("3G_ETPsat_band", "", band_opt)
    drop_ETPower_band = create_dropdown("3G_ETPower_band", "", band_opt)

    layout = html.Div(
        [
            # ! 3G TX Channel Components
            dbc.Row(
                [
                    dbc.Col(html.H2("3G_ TX Channel Components", className="display-7"), width="auto"),
                    dbc.Col(drop_TXCP_rat, width=1),
                    dbc.Col(drop_TXCP_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_TXCP_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_TXCP_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GTXCP_scat", df_3GTXCP, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! 3G FBRX Gain Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("3G FBRX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_FBRXGain_rat, width=1),
                    dbc.Col(drop_FBRXGain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_FBRX_GM_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_FBRX_GM_grp_histo"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_FBRX_GC_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_FBRX_GC_grp_histo"), width={"size": 3, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GFBRX_GM_scat", df_fbrxgm_3G, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        create_range_slider("sld_3GFBRX_GC_scat", df_fbrxgc_3G, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Hr(),
            # ! 3G FBRX Freq Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("3G FBRX Freq Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_FBRXFreq_rat, width=1),
                    dbc.Col(drop_FBRXFreq_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_FBRX_FM_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_FBRX_FM_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GFBRX_FM_scat", df_fbrxfm_3G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! 3G FBRX Freq Cal - Channel
            # dbc.Row(
            #     [
            #         dbc.Col(html.H2("3G FBRX Freq Cal Channel Data", className="display-7"), width="auto"),
            #         dbc.Col(drop_FBRXFreq_ch_rat, width=1),
            #         dbc.Col(drop_FBRXFreq_ch_band, width=1),
            #     ],
            #     align="center",
            # ),
            # html.Br(),
            # dbc.Row(
            #     [
            #         dbc.Col(
            #             dcc.Graph(id=f"3G_FBRX_FM_CH_1", figure={"layout": {"height": 1000}}), width={"size": 6, "offset": 0}
            #         ),
            #         dbc.Col(
            #             dcc.Graph(id=f"3G_FBRX_FM_CH_2", figure={"layout": {"height": 1000}}), width={"size": 6, "offset": 0}
            #         ),
            #     ],
            #     align="center",
            # ),
            # dbc.Row(
            #     [
            #         [dcc.Graph(id=f"3G_FBRX_FM_CH_{i}", figure={"layout": {"height": 1000}})]
            #         for i in df_fbrxfm_3G_ch.index
            #     ]
            # ),
            # html.Hr(),
            # ! 3G RX Gain Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("3G RX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RXGain_rat, width=1),
                    dbc.Col(drop_RXGain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_RXGain_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_RXGain_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GRXGain_scat", df_RXGain_3G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! 3G RX Comp Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("3G RX Comp Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RXComp_rat, width=1),
                    dbc.Col(drop_RXComp_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_RXComp_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_RXComp_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GRXComp_scat", df_RXComp_3G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! 3G APT Measurement
            dbc.Row(
                [
                    dbc.Col(html.H2("3G APT Measuremnet", className="display-7"), width="auto"),
                    dbc.Col(drop_APTMeas_rat, width=1),
                    dbc.Col(drop_APTMeas_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_APTMeas_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_APTMeas_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GAPTMeas_scat", df_APT_Meas_3G, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! 3G ET Psat
            dbc.Row(
                [
                    dbc.Col(html.H2("3G ET Psat", className="display-7"), width="auto"),
                    dbc.Col(drop_ETPsat_rat, width=1),
                    dbc.Col(drop_ETPsat_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_ETPsat_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_ETPsat_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GETPsat_scat", df_3G_ETSAPT_Pst, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! 3G ET Power
            dbc.Row(
                [
                    dbc.Col(html.H2("3G ET Power", className="display-7"), width="auto"),
                    dbc.Col(drop_ETPower_rat, width=1),
                    dbc.Col(drop_ETPower_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_ETPower_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_ETPower_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_3GETPower_scat", df_3G_ETSAPT_Power, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ! 3G TxP Channel Components
    @callback(Output("3G_TXCP_band", "value"), Input("3G_TXCP_RAT", "value"))
    def TXCP_3G(Sel_rat):
        return Initialize_band(Sel_rat, df_3GTXCP)

    @callback(
        [
            Output("3G_TXCP_band", "options"),
            Output("3G_TXCP_grp_scatt", "figure"),
            Output("3G_TXCP_grp_histo", "figure"),
        ],
        [Input("3G_TXCP_RAT", "value"), Input("3G_TXCP_band", "value"), Input("sld_3GTXCP_scat", "value")],
    )
    def update_3GTXCP(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_3GTXCP, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    # ! 3G FBRX Gain Cal
    @callback(Output("3G_FBRXGain_band", "value"), Input("3G_FBRXGain_RAT", "value"))
    def FBRXGain_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxgm_3G)

    @callback(
        [
            Output("3G_FBRXGain_band", "options"),
            Output("3G_FBRX_GM_grp_scatt", "figure"),
            Output("3G_FBRX_GM_grp_histo", "figure"),
            Output("3G_FBRX_GC_grp_scatt", "figure"),
            Output("3G_FBRX_GC_grp_histo", "figure"),
        ],
        [
            Input("3G_FBRXGain_RAT", "value"),
            Input("3G_FBRXGain_band", "value"),
            Input("sld_3GFBRX_GM_scat", "value"),
            Input("sld_3GFBRX_GC_scat", "value"),
        ],
    )
    def update_3GFBRXGain(Sel_rat, Sel_band, scatt_range1, scatt_range2):
        band_opt, scatt_fig1, histo_fig1 = update_band_and_graph(df_fbrxgm_3G, Sel_rat, Sel_band, scatt_range1)
        band_opt, scatt_fig2, histo_fig2 = update_band_and_graph(df_fbrxgc_3G, Sel_rat, Sel_band, scatt_range2)
        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ! 3G FBRX Freq Cal
    @callback(Output("3G_FBRXFreq_band", "value"), Input("3G_FBRXFreq_RAT", "value"))
    def FBRXFreq_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxfm_3G)

    @callback(
        [
            Output("3G_FBRXFreq_band", "options"),
            Output("3G_FBRX_FM_grp_scatt", "figure"),
            Output("3G_FBRX_FM_grp_histo", "figure"),
        ],
        [Input("3G_FBRXFreq_RAT", "value"), Input("3G_FBRXFreq_band", "value"), Input("sld_3GFBRX_FM_scat", "value")],
    )
    def update_3GFBRXFreq(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_fbrxfm_3G, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    # ! 3G FBRX Freq Cal - Channel
    @callback(Output("3G_FBRXFreq_ch_band", "value"), Input("3G_FBRXFreq_ch_RAT", "value"))
    def FBRXFreq_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxfm_3G_ch)

    @callback(
        [
            Output("3G_FBRXFreq_ch_band", "options"),
            Output("3G_FBRX_FM_CH_1", "figure"),
            Output("3G_FBRX_FM_CH_2", "figure"),
        ],
        [Input("3G_FBRXFreq_ch_RAT", "value"), Input("3G_FBRXFreq_ch_band", "value")],
    )
    def update_3GFBRXFreq(Sel_rat, Sel_band):
        band_opt, scatter_fig1, scatter_fig2 = update_band_and_graph(df_fbrxfm_3G_ch, Sel_rat, Sel_band, None)
        return band_opt, scatter_fig1, scatter_fig2

    # ! 3G RX Gain Cal
    @callback(Output("3G_RXGain_band", "value"), Input("3G_RXGain_RAT", "value"))
    def RXGain_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_RXGain_3G)

    @callback(
        [
            Output("3G_RXGain_band", "options"),
            Output("3G_RXGain_grp_scatt", "figure"),
            Output("3G_RXGain_grp_histo", "figure"),
        ],
        [Input("3G_RXGain_RAT", "value"), Input("3G_RXGain_band", "value"), Input("sld_3GRXGain_scat", "value")],
    )
    def update_3GRXGain(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_RXGain_3G, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    # ! 3G RX Channel components
    @callback(Output("3G_RXComp_band", "value"), Input("3G_RXComp_RAT", "value"))
    def RXComp_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_RXComp_3G)

    @callback(
        [
            Output("3G_RXComp_band", "options"),
            Output("3G_RXComp_grp_scatt", "figure"),
            Output("3G_RXComp_grp_histo", "figure"),
        ],
        [Input("3G_RXComp_RAT", "value"), Input("3G_RXComp_band", "value"), Input("sld_3GRXComp_scat", "value")],
    )
    def update_3GRXComp(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_RXComp_3G, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    # ! 3G APT Measuremnet
    @callback(Output("3G_APTMeas_band", "value"), Input("3G_APTMeas_RAT", "value"))
    def RXComp_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_APT_Meas_3G)

    @callback(
        [
            Output("3G_APTMeas_band", "options"),
            Output("3G_APTMeas_grp_scatt", "figure"),
            Output("3G_APTMeas_grp_histo", "figure"),
        ],
        [Input("3G_APTMeas_RAT", "value"), Input("3G_APTMeas_band", "value"), Input("sld_3GAPTMeas_scat", "value")],
    )
    def update_3GRXComp(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_APT_Meas_3G, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    # ! 3G ET Psat
    @callback(Output("3G_ETPsat_band", "value"), Input("3G_ETPsat_RAT", "value"))
    def ETPsat_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_3G_ETSAPT_Pst)

    @callback(
        [
            Output("3G_ETPsat_band", "options"),
            Output("3G_ETPsat_grp_scatt", "figure"),
            Output("3G_ETPsat_grp_histo", "figure"),
        ],
        [Input("3G_ETPsat_RAT", "value"), Input("3G_ETPsat_band", "value"), Input("sld_3GETPsat_scat", "value")],
    )
    def update_3GETPsat(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_3G_ETSAPT_Pst, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    # ! 3G ET Psat
    @callback(Output("3G_ETPower_band", "value"), Input("3G_ETPower_RAT", "value"))
    def ETPower_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_3G_ETSAPT_Power)

    @callback(
        [
            Output("3G_ETPower_band", "options"),
            Output("3G_ETPower_grp_scatt", "figure"),
            Output("3G_ETPower_grp_histo", "figure"),
        ],
        [Input("3G_ETPower_RAT", "value"), Input("3G_ETPower_band", "value"), Input("sld_3GETPower_scat", "value")],
    )
    def update_ETPower(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(
            df_3G_ETSAPT_Power, Sel_rat, Sel_band, scatt_range
        )
        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    return layout
