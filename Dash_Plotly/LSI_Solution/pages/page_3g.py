import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import Create_dropdown, Create_range_slider, Initialize_band, Band_list, Update_band_and_graph


def Initialize_3g(dict_3g):
    df_TXCP = dict_3g["TxP_CC"]
    df_RXGain = dict_3g["RX_Gain"]
    df_RXComp = dict_3g["RX_Comp"]
    df_fbrxgm = dict_3g["FBRX_GM"]
    df_fbrxgc = dict_3g["FBRX_GC"]
    df_fbrxfm = dict_3g["FBRX_FM"]
    df_fbrxfm_ch = dict_3g["FBRX_FM_Ch"]
    df_APT_Meas = dict_3g["APT_Meas"]
    df_ET_Pst = dict_3g["ET_Psat"]
    df_ET_Power = dict_3g["ET_Pgain"]

    band_opt = [{"label": "", "value": ""}]

    drop_TxP_CC_rat = Create_dropdown("3G_TxP_CC_rat", "B", [{"label": "3G", "value": "B"}])
    drop_FBRX_Gain_rat = Create_dropdown("3G_FBRX_Gain_rat", "B", [{"label": "3G", "value": "B"}])
    drop_FBRX_Freq_rat = Create_dropdown("3G_FBRX_Freq_rat", "B", [{"label": "3G", "value": "B"}])
    drop_FBRX_Freq_ch_rat = Create_dropdown("3G_FBRX_Freq_ch_rat", "B", [{"label": "3G", "value": "B"}])
    drop_RX_Gain_rat = Create_dropdown("3G_RX_Gain_rat", "B", [{"label": "3G", "value": "B"}])
    drop_RX_Comp_rat = Create_dropdown("3G_RX_Comp_rat", "B", [{"label": "3G", "value": "B"}])
    drop_APT_Meas_rat = Create_dropdown("3G_APT_Meas_rat", "B", [{"label": "3G", "value": "B"}])
    drop_ET_Psat_rat = Create_dropdown("3G_ET_Psat_rat", "B", [{"label": "3G", "value": "B"}])
    drop_ET_Power_rat = Create_dropdown("3G_ET_Power_rat", "B", [{"label": "3G", "value": "B"}])

    drop_TxP_CC_band = Create_dropdown("3G_TxP_CC_band", "", band_opt)
    drop_FBRX_Gain_band = Create_dropdown("3G_FBRX_Gain_band", "", band_opt)
    drop_FBRX_Freq_band = Create_dropdown("3G_FBRX_Freq_band", "", band_opt)
    drop_FBRX_Freq_ch_band = Create_dropdown("3G_FBRX_Freq_ch_band", "", band_opt)
    drop_RX_Gain_band = Create_dropdown("3G_RX_Gain_band", "", band_opt)
    drop_RX_Comp_band = Create_dropdown("3G_RX_Comp_band", "", band_opt)
    drop_APT_Meas_band = Create_dropdown("3G_APT_Meas_band", "", band_opt)
    drop_ET_Psat_band = Create_dropdown("3G_ET_Psat_band", "", band_opt)
    drop_ET_Power_band = Create_dropdown("3G_ET_Power_band", "", band_opt)

    layout = html.Div(
        [
            # ** ============================== 3G TX Channel Components ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G TxP Channel Components", className="display-7"), width="auto"),
                    dbc.Col(drop_TxP_CC_rat, width=1),
                    dbc.Col(drop_TxP_CC_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_TxP_CC_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_TxP_CC_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_TxP_CC_scat", df_TXCP, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G FBRX Gain Cal ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G FBRX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_FBRX_Gain_rat, width=1),
                    dbc.Col(drop_FBRX_Gain_band, width=1),
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
                        Create_range_slider("sld_FBRX_GM_scat", df_fbrxgm, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_FBRX_GC_scat", df_fbrxgc, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G FBRX Freq Cal ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G FBRX Freq Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_FBRX_Freq_rat, width=1),
                    dbc.Col(drop_FBRX_Freq_band, width=1),
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
                        Create_range_slider("sld_FBRX_FM_scat", df_fbrxfm, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G FBRX Freq Cal - Channel ==============================
            # dbc.Row(
            #     [
            #         dbc.Col(html.H2("3G FBRX Freq Cal Channel Data", className="display-7"), width="auto"),
            #         dbc.Col(drop_FBRX_Freq_ch_rat, width=1),
            #         dbc.Col(drop_FBRX_Freq_ch_band, width=1),
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
            #         for i in df_fbrxfm_ch.index
            #     ]
            # ),
            # html.Hr(),
            # ** ============================== 3G RX Gain Cal ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G RX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RX_Gain_rat, width=1),
                    dbc.Col(drop_RX_Gain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_RX_Gain_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_RX_Gain_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_RX_Gain_scat", df_RXGain, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G RX Comp Cal ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G RX Comp Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RX_Comp_rat, width=1),
                    dbc.Col(drop_RX_Comp_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_RX_Comp_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_RX_Comp_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_RX_Comp_scat", df_RXComp, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G APT Measurement ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G APT Measuremnet", className="display-7"), width="auto"),
                    dbc.Col(drop_APT_Meas_rat, width=1),
                    dbc.Col(drop_APT_Meas_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_APT_Meas_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_APT_Meas_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_APT_Meas_scat", df_APT_Meas, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G ET Psat ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G ET Psat", className="display-7"), width="auto"),
                    dbc.Col(drop_ET_Psat_rat, width=1),
                    dbc.Col(drop_ET_Psat_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_ET_Psat_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_ET_Psat_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_ET_Psat_scat", df_ET_Pst, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G ET Power ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G ET Power", className="display-7"), width="auto"),
                    dbc.Col(drop_ET_Power_rat, width=1),
                    dbc.Col(drop_ET_Power_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3G_ET_Power_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="3G_ET_Power_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_ET_Power_scat", df_ET_Power, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ** ============================== 3G TxP Channel Components ==============================
    @callback(Output("3G_TxP_CC_band", "value"), Input("3G_TxP_CC_rat", "value"))
    def TxP_CC_3G(selected_rat):
        return Initialize_band(selected_rat, df_TXCP)

    @callback(
        [
            Output("3G_TxP_CC_band", "options"),
            Output("3G_TxP_CC_grp_scatt", "figure"),
            Output("3G_TxP_CC_grp_histo", "figure"),
        ],
        [Input("3G_TxP_CC_rat", "value"), Input("3G_TxP_CC_band", "value"), Input("sld_TxP_CC_scat", "value")],
    )
    def update_TxP_CC(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_TXCP, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_TXCP, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G FBRX Gain Cal ==============================
    @callback(Output("3G_FBRX_Gain_band", "value"), Input("3G_FBRX_Gain_rat", "value"))
    def FBRXGain_3G(selected_rat):
        return Initialize_band(selected_rat, df_fbrxgm)

    @callback(
        [
            Output("3G_FBRX_Gain_band", "options"),
            Output("3G_FBRX_GM_grp_scatt", "figure"),
            Output("3G_FBRX_GM_grp_histo", "figure"),
            Output("3G_FBRX_GC_grp_scatt", "figure"),
            Output("3G_FBRX_GC_grp_histo", "figure"),
        ],
        [
            Input("3G_FBRX_Gain_rat", "value"),
            Input("3G_FBRX_Gain_band", "value"),
            Input("sld_FBRX_GM_scat", "value"),
            Input("sld_FBRX_GC_scat", "value"),
        ],
    )
    def update_FBRXGain(selected_rat, selected_band, scatt_range1, scatt_range2):
        scatt_fig1, histo_fig1 = Update_band_and_graph(df_fbrxgm, selected_rat, selected_band, scatt_range1)
        scatt_fig2, histo_fig2 = Update_band_and_graph(df_fbrxgc, selected_rat, selected_band, scatt_range2)
        band_opt = Band_list(df_fbrxgm, selected_rat)

        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ** ============================== 3G FBRX Freq Cal ==============================
    @callback(Output("3G_FBRX_Freq_band", "value"), Input("3G_FBRX_Freq_rat", "value"))
    def FBRXFreq_3G(selected_rat):
        return Initialize_band(selected_rat, df_fbrxfm)

    @callback(
        [
            Output("3G_FBRX_Freq_band", "options"),
            Output("3G_FBRX_FM_grp_scatt", "figure"),
            Output("3G_FBRX_FM_grp_histo", "figure"),
        ],
        [Input("3G_FBRX_Freq_rat", "value"), Input("3G_FBRX_Freq_band", "value"), Input("sld_FBRX_FM_scat", "value")],
    )
    def update_FBRXFreq(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_fbrxfm, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_fbrxfm, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G FBRX Freq Cal - Channel ==============================
    # @callback(Output("3G_FBRX_Freq_ch_band", "value"), Input("3G_FBRX_Freq_ch_rat", "value"))
    # def FBRXFreq_Ch_3G(selected_rat):
    #     return Initialize_band(selected_rat, df_fbrxfm_ch)

    # @callback(
    #     [
    #         Output("3G_FBRX_Freq_ch_band", "options"),
    #         Output("3G_FBRX_FM_CH_1", "figure"),
    #         Output("3G_FBRX_FM_CH_2", "figure"),
    #     ],
    #     [Input("3G_FBRX_Freq_ch_rat", "value"), Input("3G_FBRX_Freq_ch_band", "value")],
    # )
    # def update_FBRX_Freq_ch(selected_rat, selected_band):
    #     scatter_fig1, scatter_fig2 = Update_band_and_graph(df_fbrxfm_ch, selected_rat, selected_band, None)
    #     band_opt = Band_list(df_fbrxfm_ch)

    #     return band_opt, scatter_fig1, scatter_fig2

    # ** ============================== 3G RX Gain Cal ==============================
    @callback(Output("3G_RX_Gain_band", "value"), Input("3G_RX_Gain_rat", "value"))
    def RXGain_3G(selected_rat):
        return Initialize_band(selected_rat, df_RXGain)

    @callback(
        [
            Output("3G_RX_Gain_band", "options"),
            Output("3G_RX_Gain_grp_scatt", "figure"),
            Output("3G_RX_Gain_grp_histo", "figure"),
        ],
        [Input("3G_RX_Gain_rat", "value"), Input("3G_RX_Gain_band", "value"), Input("sld_RX_Gain_scat", "value")],
    )
    def update_RXGain(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_RXGain, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RXGain, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G RX Channel components ==============================
    @callback(Output("3G_RX_Comp_band", "value"), Input("3G_RX_Comp_rat", "value"))
    def RXComp_3G(selected_rat):
        return Initialize_band(selected_rat, df_RXComp)

    @callback(
        [
            Output("3G_RX_Comp_band", "options"),
            Output("3G_RX_Comp_grp_scatt", "figure"),
            Output("3G_RX_Comp_grp_histo", "figure"),
        ],
        [Input("3G_RX_Comp_rat", "value"), Input("3G_RX_Comp_band", "value"), Input("sld_RX_Comp_scat", "value")],
    )
    def update_RXComp(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_RXComp, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RXComp, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    # ** ============================== 3G APT Measuremnet ==============================
    @callback(Output("3G_APT_Meas_band", "value"), Input("3G_APT_Meas_rat", "value"))
    def APT_Meas_3G(selected_rat):
        return Initialize_band(selected_rat, df_APT_Meas)

    @callback(
        [
            Output("3G_APT_Meas_band", "options"),
            Output("3G_APT_Meas_grp_scatt", "figure"),
            Output("3G_APT_Meas_grp_histo", "figure"),
        ],
        [Input("3G_APT_Meas_rat", "value"), Input("3G_APT_Meas_band", "value"), Input("sld_APT_Meas_scat", "value")],
    )
    def update_APT_Meas(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_APT_Meas, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_APT_Meas, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Psat ==============================
    @callback(Output("3G_ET_Psat_band", "value"), Input("3G_ET_Psat_rat", "value"))
    def ETPsat_3G(selected_rat):
        return Initialize_band(selected_rat, df_ET_Pst)

    @callback(
        [
            Output("3G_ET_Psat_band", "options"),
            Output("3G_ET_Psat_grp_scatt", "figure"),
            Output("3G_ET_Psat_grp_histo", "figure"),
        ],
        [Input("3G_ET_Psat_rat", "value"), Input("3G_ET_Psat_band", "value"), Input("sld_ET_Psat_scat", "value")],
    )
    def update_ETPsat(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_ET_Pst, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Pst, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Power ==============================
    @callback(Output("3G_ET_Power_band", "value"), Input("3G_ET_Power_rat", "value"))
    def ETPower_3G(selected_rat):
        return Initialize_band(selected_rat, df_ET_Power)

    @callback(
        [
            Output("3G_ET_Power_band", "options"),
            Output("3G_ET_Power_grp_scatt", "figure"),
            Output("3G_ET_Power_grp_histo", "figure"),
        ],
        [Input("3G_ET_Power_rat", "value"), Input("3G_ET_Power_band", "value"), Input("sld_ET_Power_scat", "value")],
    )
    def update_ETPower(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_ET_Power, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Power, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    return layout
