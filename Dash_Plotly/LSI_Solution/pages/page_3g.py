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


def Initialize_3g(dict_3g):
    df_TXCP = df_strip(dict_3g["TxP_CC"])
    df_RXGain = df_strip(dict_3g["RX_Gain"])
    df_RXComp = df_strip(dict_3g["RX_Comp"])
    df_fbrxgm = df_strip(dict_3g["FBRX_GM"])
    df_fbrxgc = df_strip(dict_3g["FBRX_GC"])
    df_fbrxfm = df_strip(dict_3g["FBRX_FM"])
    df_fbrxfm_ch = df_strip(dict_3g["FBRX_FM_Ch"])
    df_APT_Meas = df_strip(dict_3g["APT_Meas"])
    df_ET_Pst = df_strip(dict_3g["ET_Psat"])
    df_ET_Power = df_strip(dict_3g["ET_Pgain"])

    band_opt = [{"label": "", "value": ""}]

    drop_TxP_CC_r = Create_dropdown("3G_TxP_CC_r", "B", [{"label": "3G", "value": "B"}])
    drop_FBRX_Gain_r = Create_dropdown("3G_FBRX_Gain_r", "B", [{"label": "3G", "value": "B"}])
    drop_FBRX_Freq_r = Create_dropdown("3G_FBRX_Freq_r", "B", [{"label": "3G", "value": "B"}])
    drop_FBRX_Freq_ch_r = Create_dropdown("3G_FBRX_Freq_ch_r", "B", [{"label": "3G", "value": "B"}])
    drop_RX_Gain_r = Create_dropdown("3G_RX_Gain_r", "B", [{"label": "3G", "value": "B"}])
    drop_RX_Comp_r = Create_dropdown("3G_RX_Comp_r", "B", [{"label": "3G", "value": "B"}])
    drop_APT_Meas_r = Create_dropdown("3G_APT_Meas_r", "B", [{"label": "3G", "value": "B"}])
    drop_ET_Psat_r = Create_dropdown("3G_ET_Psat_r", "B", [{"label": "3G", "value": "B"}])
    drop_ET_Power_r = Create_dropdown("3G_ET_Power_r", "B", [{"label": "3G", "value": "B"}])

    drop_TxP_CC_b = Create_dropdown("3G_TxP_CC_b", "", band_opt)
    drop_FBRX_Gain_b = Create_dropdown("3G_FBRX_Gain_b", "", band_opt)
    drop_FBRX_Freq_b = Create_dropdown("3G_FBRX_Freq_b", "", band_opt)
    drop_FBRX_Freq_ch_b = Create_dropdown("3G_FBRX_Freq_ch_b", "", band_opt)
    drop_RX_Gain_b = Create_dropdown("3G_RX_Gain_b", "", band_opt)
    drop_RX_Comp_b = Create_dropdown("3G_RX_Comp_b", "", band_opt)
    drop_APT_Meas_b = Create_dropdown("3G_APT_Meas_b", "", band_opt)
    drop_ET_Psat_b = Create_dropdown("3G_ET_Psat_b", "", band_opt)
    drop_ET_Power_b = Create_dropdown("3G_ET_Power_b", "", band_opt)

    layout = html.Div(
        [
            # ** ============================== 3G TX Channel Components ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G TxP Channel Components", className="display-7"), width="auto"),
                    dbc.Col(drop_TxP_CC_r, width=1),
                    dbc.Col(drop_TxP_CC_b, width=1),
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
                    dbc.Col(drop_FBRX_Gain_r, width=1),
                    dbc.Col(drop_FBRX_Gain_b, width=1),
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
                    dbc.Col(drop_FBRX_Freq_r, width=1),
                    dbc.Col(drop_FBRX_Freq_b, width=1),
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
            #         dbc.Col(drop_FBRX_Freq_ch_r, width=1),
            #         dbc.Col(drop_FBRX_Freq_ch_b, width=1),
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
                    dbc.Col(drop_RX_Gain_r, width=1),
                    dbc.Col(drop_RX_Gain_b, width=1),
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
                    dbc.Col(drop_RX_Comp_r, width=1),
                    dbc.Col(drop_RX_Comp_b, width=1),
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
                    dbc.Col(drop_APT_Meas_r, width=1),
                    dbc.Col(drop_APT_Meas_b, width=1),
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
                    dbc.Col(drop_ET_Psat_r, width=1),
                    dbc.Col(drop_ET_Psat_b, width=1),
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
                    dbc.Col(drop_ET_Power_r, width=1),
                    dbc.Col(drop_ET_Power_b, width=1),
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
    @callback(Output("3G_TxP_CC_b", "value"), Input("3G_TxP_CC_r", "value"))
    def TxP_CC_3G(selected_r):
        return Initialize_band(selected_r, df_TXCP)

    @callback(
        [
            Output("3G_TxP_CC_b", "options"),
            Output("3G_TxP_CC_grp_scatt", "figure"),
            Output("3G_TxP_CC_grp_histo", "figure"),
        ],
        [Input("3G_TxP_CC_r", "value"), Input("3G_TxP_CC_b", "value"), Input("sld_TxP_CC_scat", "value")],
    )
    def update_TxP_CC(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_TXCP, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_TXCP, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G FBRX Gain Cal ==============================
    @callback(Output("3G_FBRX_Gain_b", "value"), Input("3G_FBRX_Gain_r", "value"))
    def FBRXGain_3G(selected_r):
        return Initialize_band(selected_r, df_fbrxgm)

    @callback(
        [
            Output("3G_FBRX_Gain_b", "options"),
            Output("3G_FBRX_GM_grp_scatt", "figure"),
            Output("3G_FBRX_GM_grp_histo", "figure"),
            Output("3G_FBRX_GC_grp_scatt", "figure"),
            Output("3G_FBRX_GC_grp_histo", "figure"),
        ],
        [
            Input("3G_FBRX_Gain_r", "value"),
            Input("3G_FBRX_Gain_b", "value"),
            Input("sld_FBRX_GM_scat", "value"),
            Input("sld_FBRX_GC_scat", "value"),
        ],
    )
    def update_FBRXGain(selected_r, selected_b, scatt_range1, scatt_range2):
        scatt_fig1, histo_fig1 = Update_band_and_graph(df_fbrxgm, selected_r, selected_b, scatt_range1)
        scatt_fig2, histo_fig2 = Update_band_and_graph(df_fbrxgc, selected_r, selected_b, scatt_range2)
        band_opt = Band_list(df_fbrxgm, selected_r)

        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ** ============================== 3G FBRX Freq Cal ==============================
    @callback(Output("3G_FBRX_Freq_b", "value"), Input("3G_FBRX_Freq_r", "value"))
    def FBRXFreq_3G(selected_r):
        return Initialize_band(selected_r, df_fbrxfm)

    @callback(
        [
            Output("3G_FBRX_Freq_b", "options"),
            Output("3G_FBRX_FM_grp_scatt", "figure"),
            Output("3G_FBRX_FM_grp_histo", "figure"),
        ],
        [Input("3G_FBRX_Freq_r", "value"), Input("3G_FBRX_Freq_b", "value"), Input("sld_FBRX_FM_scat", "value")],
    )
    def update_FBRXFreq(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_fbrxfm, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_fbrxfm, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G FBRX Freq Cal - Channel ==============================
    # @callback(Output("3G_FBRX_Freq_ch_b", "value"), Input("3G_FBRX_Freq_ch_r", "value"))
    # def FBRXFreq_Ch_3G(selected_r):
    #     return Initialize_band(selected_r, df_fbrxfm_ch)

    # @callback(
    #     [
    #         Output("3G_FBRX_Freq_ch_b", "options"),
    #         Output("3G_FBRX_FM_CH_1", "figure"),
    #         Output("3G_FBRX_FM_CH_2", "figure"),
    #     ],
    #     [Input("3G_FBRX_Freq_ch_r", "value"), Input("3G_FBRX_Freq_ch_b", "value")],
    # )
    # def update_FBRX_Freq_ch(selected_r, selected_b):
    #     scatter_fig1, scatter_fig2 = Update_band_and_graph(df_fbrxfm_ch, selected_r, selected_b, None)
    #     band_opt = Band_list(df_fbrxfm_ch)

    #     return band_opt, scatter_fig1, scatter_fig2

    # ** ============================== 3G RX Gain Cal ==============================
    @callback(Output("3G_RX_Gain_b", "value"), Input("3G_RX_Gain_r", "value"))
    def RXGain_3G(selected_r):
        return Initialize_band(selected_r, df_RXGain)

    @callback(
        [
            Output("3G_RX_Gain_b", "options"),
            Output("3G_RX_Gain_grp_scatt", "figure"),
            Output("3G_RX_Gain_grp_histo", "figure"),
        ],
        [Input("3G_RX_Gain_r", "value"), Input("3G_RX_Gain_b", "value"), Input("sld_RX_Gain_scat", "value")],
    )
    def update_RXGain(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_RXGain, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_RXGain, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G RX Channel components ==============================
    @callback(Output("3G_RX_Comp_b", "value"), Input("3G_RX_Comp_r", "value"))
    def RXComp_3G(selected_r):
        return Initialize_band(selected_r, df_RXComp)

    @callback(
        [
            Output("3G_RX_Comp_b", "options"),
            Output("3G_RX_Comp_grp_scatt", "figure"),
            Output("3G_RX_Comp_grp_histo", "figure"),
        ],
        [Input("3G_RX_Comp_r", "value"), Input("3G_RX_Comp_b", "value"), Input("sld_RX_Comp_scat", "value")],
    )
    def update_RXComp(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_RXComp, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_RXComp, selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    # ** ============================== 3G APT Measuremnet ==============================
    @callback(Output("3G_APT_Meas_b", "value"), Input("3G_APT_Meas_r", "value"))
    def APT_Meas_3G(selected_r):
        return Initialize_band(selected_r, df_APT_Meas)

    @callback(
        [
            Output("3G_APT_Meas_b", "options"),
            Output("3G_APT_Meas_grp_scatt", "figure"),
            Output("3G_APT_Meas_grp_histo", "figure"),
        ],
        [Input("3G_APT_Meas_r", "value"), Input("3G_APT_Meas_b", "value"), Input("sld_APT_Meas_scat", "value")],
    )
    def update_APT_Meas(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_APT_Meas, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_APT_Meas, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Psat ==============================
    @callback(Output("3G_ET_Psat_b", "value"), Input("3G_ET_Psat_r", "value"))
    def ETPsat_3G(selected_r):
        return Initialize_band(selected_r, df_ET_Pst)

    @callback(
        [
            Output("3G_ET_Psat_b", "options"),
            Output("3G_ET_Psat_grp_scatt", "figure"),
            Output("3G_ET_Psat_grp_histo", "figure"),
        ],
        [Input("3G_ET_Psat_r", "value"), Input("3G_ET_Psat_b", "value"), Input("sld_ET_Psat_scat", "value")],
    )
    def update_ETPsat(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_ET_Pst, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_ET_Pst, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Power ==============================
    @callback(Output("3G_ET_Power_b", "value"), Input("3G_ET_Power_r", "value"))
    def ETPower_3G(selected_r):
        return Initialize_band(selected_r, df_ET_Power)

    @callback(
        [
            Output("3G_ET_Power_b", "options"),
            Output("3G_ET_Power_grp_scatt", "figure"),
            Output("3G_ET_Power_grp_histo", "figure"),
        ],
        [Input("3G_ET_Power_r", "value"), Input("3G_ET_Power_b", "value"), Input("sld_ET_Power_scat", "value")],
    )
    def update_ETPower(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_ET_Power, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_ET_Power, selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    return layout
