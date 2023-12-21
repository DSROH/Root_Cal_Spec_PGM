import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input, State
from LSI_Solution.pages.page_cf import (
    Create_dropdown,
    Create_range_slider,
    Initialize_band,
    Band_list,
    Update_band_and_graph,
    tweet_callback,
    Drawing_pcc,
    Drawing_scc,
)


def Initialize_nr(dict_nr):
    df_RX_Gain = dict_nr["RX_Gain"]
    df_RX_RSRP = dict_nr["RX_RSRP"]
    df_RX_Comp = dict_nr["RX_Comp"]
    df_RX_Mixer = dict_nr["RX_Mix"]
    df_FBRX_GM = dict_nr["FBRX_GM"]
    df_FBRX_GC = dict_nr["FBRX_GC"]
    df_FBRX_FM = dict_nr["FBRX_FM"]
    df_FBRX_FC = dict_nr["FBRX_FC"]
    df_APT_Meas = dict_nr["APT_Meas"]
    df_ET_Psat = dict_nr["ET_Psat"]
    df_ET_Pgain = dict_nr["ET_Pgain"]
    df_ET_Power = dict_nr["ET_Power"]
    df_ET_Freq = dict_nr["ET_Freq"]

    band_opt = [{"label": "", "value": ""}]

    drop_RX_Gain_rat = Create_dropdown("NR_RX_Gain_rat", "n", [{"label": "NR", "value": "n"}])
    drop_RX_RSRP_rat = Create_dropdown("NR_RX_RSRP_rat", "n", [{"label": "NR", "value": "n"}])
    drop_RX_Comp_rat = Create_dropdown("NR_RX_Comp_rat", "n", [{"label": "NR", "value": "n"}])
    drop_RX_Mixer_rat = Create_dropdown("NR_RX_Mixer_rat", "n", [{"label": "NR", "value": "n"}])
    drop_FBRX_Gain_rat = Create_dropdown("NR_FBRX_Gain_rat", "n", [{"label": "NR", "value": "n"}])
    drop_FBRX_Freq_rat = Create_dropdown("NR_FBRX_Freq_rat", "n", [{"label": "NR", "value": "n"}])
    drop_APT_Meas_rat = Create_dropdown("NR_APT_Meas_rat", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Psat_rat = Create_dropdown("NR_ET_Psat_rat", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Pgain_rat = Create_dropdown("NR_ET_Pgain_rat", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Power_rat = Create_dropdown("NR_ET_Power_rat", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Freq_rat = Create_dropdown("NR_ET_Freq_rat", "n", [{"label": "NR", "value": "n"}])

    drop_RX_Gain_band = Create_dropdown("NR_RX_Gain_band", "", band_opt)
    drop_RX_RSRP_band = Create_dropdown("NR_RX_RSRP_band", "", band_opt)
    drop_RX_Comp_band = Create_dropdown("NR_RX_Comp_band", "", band_opt)
    drop_RX_Mixer_band = Create_dropdown("NR_RX_Mixer_band", "", band_opt)
    drop_FBRX_Gain_band = Create_dropdown("NR_FBRX_Gain_band", "", band_opt)
    drop_FBRX_Freq_band = Create_dropdown("NR_FBRX_Freq_band", "", band_opt)
    drop_APT_Meas_band = Create_dropdown("NR_APT_Meas_band", "", band_opt)
    drop_ET_Psat_band = Create_dropdown("NR_ET_PSat_band", "", band_opt)
    drop_ET_Pgain_band = Create_dropdown("NR_ET_Pgain_band", "", band_opt)
    drop_ET_Power_band = Create_dropdown("NR_ET_Power_band", "", band_opt)
    drop_ET_Freq_band = Create_dropdown("NR_ET_Freq_band", "", band_opt)

    layout = html.Div(
        [
            # ** ================================= Sub6 FBRX Gain Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "FBRX", "Gain Cal"), id="head_fbrx_gm", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_FBRX_Gain_rat, width=1),
                    dbc.Col(drop_FBRX_Gain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_FBRX_GM_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_FBRX_GM_grp_histo"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_FBRX_GC_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_FBRX_GC_grp_histo"), width={"size": 3, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_FBRX_GM_scat", df_FBRX_GM, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_FBRX_GC_scat", df_FBRX_GC, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Div(id="fbrx_gm_scc", children=[]),
            html.Hr(),
            # ** ================================= Sub6 FBRX Freq Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "FBRX", "Freq Cal"), id="head_fbrx_fm", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_FBRX_Freq_rat, width=1),
                    dbc.Col(drop_FBRX_Freq_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_FBRX_FM_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_FBRX_FM_grp_histo"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_FBRX_FC_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_FBRX_FC_grp_histo"), width={"size": 3, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_FBRX_FM_scat", df_FBRX_FM, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_FBRX_FC_scat", df_FBRX_FC, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Div(id="fbrx_fm_scc", children=[]),
            html.Hr(),
            # ** ================================= Sub6 RX Gain Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "RX", "Gain Cal"), id="head_rx_gain", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_RX_Gain_rat, width=1),
                    dbc.Col(drop_RX_Gain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RX_Gain_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RX_Gain_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_RX_Gain_scat", df_RX_Gain, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 RX RSRP Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "RX", "RSRP Cal"), id="head_rx_rsrp", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_RX_RSRP_rat, width=1),
                    dbc.Col(drop_RX_RSRP_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RX_RSRP_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RX_RSRP_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_RX_RSRP_scat", df_RX_RSRP, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 RX Freq Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "RX", "Freq Cal"), id="head_rx_comp", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_RX_Comp_rat, width=1),
                    dbc.Col(drop_RX_Comp_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RX_Comp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RX_Comp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_RX_Comp_scat", df_RX_Comp, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 RX Mixer Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            children=tweet_callback("NR", "RX", "Mixer Cal"),
                            id="head_rx_mixer",
                            className="display-7",
                        ),
                        width="auto",
                    ),
                    dbc.Col(drop_RX_Mixer_rat, width=1),
                    dbc.Col(drop_RX_Mixer_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RX_Mixer_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RX_Mixer_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_RX_Mixer_scat", df_RX_Mixer, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 APT Measuremnt =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            children=tweet_callback("NR", "APT", "Measurement"),
                            id="head_apt_measure",
                            className="display-7",
                        ),
                        width="auto",
                    ),
                    dbc.Col(drop_APT_Meas_rat, width=1),
                    dbc.Col(drop_APT_Meas_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_APT_Meas_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_APT_Meas_histo"), width={"size": 6, "offset": 0}),
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
            html.Div(id="apt_measure_scc", children=[]),
            html.Hr(),
            # ** ================================= Sub6 ET Psat =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "ET-SAPT", "Psat"), id="head_et_psat", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_ET_Psat_rat, width=1),
                    dbc.Col(drop_ET_Psat_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ET_Psat_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ET_Psat_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_ET_Psat_scat", df_ET_Psat, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Div(id="et_psat_scc", children=[]),
            html.Hr(),
            # ** ================================= Sub6 ET Pgain =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "ET-SAPT", "Pgain"), id="head_et_pgain", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_ET_Pgain_rat, width=1),
                    dbc.Col(drop_ET_Pgain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ET_Pgain_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ET_Pgain_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_ET_Pgain_scat", df_ET_Pgain, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Div(id="et_pgain_scc", children=[]),
            html.Hr(),
            # ** ================================= Sub6 ET Power =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "ET-SAPT", "Power"), id="head_et_power", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_ET_Power_rat, width=1),
                    dbc.Col(drop_ET_Power_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ET_Power_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ET_Power_histo"), width={"size": 6, "offset": 0}),
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
            html.Div(id="et_power_scc", children=[]),
            html.Hr(),
            # ** ================================= Sub6 ET Freq =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "ET-SAPT", "Freq Cal"), id="head_et_freq", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(drop_ET_Freq_rat, width=1),
                    dbc.Col(drop_ET_Freq_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ET_Freq_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ET_Freq_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_ET_Freq_scat", df_ET_Freq, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Div(id="et_freq_scc", children=[]),
            html.Hr(),
        ]
    )

    # ** ======================================================================================
    # **
    # **
    # **
    # **
    # **
    # **
    # **                                   Call Back Function
    # **
    # **
    # **
    # **
    # **
    # **
    # ** ================================= Sub6 FBRX Gain Cal =================================

    @callback(Output("NR_FBRX_Gain_band", "value"), Input("NR_FBRX_Gain_rat", "value"))
    def FBRXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_FBRX_GM)

    @callback(
        [
            Output("NR_FBRX_Gain_band", "options"),
            Output("NR_FBRX_GM_grp_scatt", "figure"),
            Output("NR_FBRX_GM_grp_histo", "figure"),
            Output("NR_FBRX_GC_grp_scatt", "figure"),
            Output("NR_FBRX_GC_grp_histo", "figure"),
            Output("fbrx_gm_scc", "children"),
        ],
        [
            Input("NR_FBRX_Gain_rat", "value"),
            Input("NR_FBRX_Gain_band", "value"),
            Input("sld_FBRX_GM_scat", "value"),
            Input("sld_FBRX_FC_scat", "value"),
            State("fbrx_gm_scc", "children"),
        ],
    )
    def update_FBRX_Gain(selected_rat, selected_band, scatt_range1, scatt_range2, children):
        band_opt = Band_list(df_ET_Psat, selected_rat)
        filtered_df = df_ET_Psat[df_ET_Psat["Band"] == selected_band].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2 = Drawing_pcc(
                selected_rat, selected_band, filtered_df, scatt_range1, scatt_range2
            )
            children = [layout for layout in children if "scc_scatt" not in str(layout)]
            children = Drawing_scc(selected_rat, selected_band, filtered_df, "ET-SAPT", children, scatt_range1, scatt_range2)

            return band_opt, scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2, children
        else:
            scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2 = Drawing_pcc(
                selected_rat, selected_band, filtered_df, scatt_range1, scatt_range2
            )
            children = [layout for layout in children if f"FBRX_scc_scatt" not in str(layout)]

            return band_opt, scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2, children

    # ** ================================= Sub6 FBRX Freq Cal =================================
    @callback(Output("NR_FBRX_Freq_band", "value"), Input("NR_FBRX_Freq_rat", "value"))
    def FBRXFreq_NR(selected_rat):
        return Initialize_band(selected_rat, df_FBRX_FM)

    @callback(
        [
            Output("NR_FBRX_Freq_band", "options"),
            Output("NR_FBRX_FM_grp_scatt", "figure"),
            Output("NR_FBRX_FM_grp_histo", "figure"),
            Output("NR_FBRX_FC_grp_scatt", "figure"),
            Output("NR_FBRX_FC_grp_histo", "figure"),
        ],
        [
            Input("NR_FBRX_Freq_rat", "value"),
            Input("NR_FBRX_Freq_band", "value"),
            Input("sld_FBRX_FM_scat", "value"),
            Input("sld_FBRX_FC_scat", "value"),
        ],
    )
    def update_FBRXFreq(selected_rat, selected_band, scatt_range1, scatt_range2):
        scatt_fig1, histo_fig1 = Update_band_and_graph(df_FBRX_FM, selected_rat, selected_band, scatt_range1)
        scatt_fig2, histo_fig2 = Update_band_and_graph(df_FBRX_FC, selected_rat, selected_band, scatt_range2)
        band_opt = Band_list(df_FBRX_FM, selected_rat)

        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ** ================================= Sub6 RX Gain Cal =================================
    @callback(Output("NR_RX_Gain_band", "value"), Input("NR_RX_Gain_rat", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RX_Gain)

    @callback(
        [
            Output("NR_RX_Gain_band", "options"),
            Output("NR_RX_Gain_scatt", "figure"),
            Output("NR_RX_Gain_histo", "figure"),
        ],
        [
            Input("NR_RX_Gain_rat", "value"),
            Input("NR_RX_Gain_band", "value"),
            Input("sld_RX_Gain_scat", "value"),
        ],
    )
    def update_RX_Gain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_RX_Gain, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RX_Gain, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX RSRP Cal =================================
    @callback(Output("NR_RX_RSRP_band", "value"), Input("NR_RX_RSRP_rat", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RX_RSRP)

    @callback(
        [
            Output("NR_RX_RSRP_band", "options"),
            Output("NR_RX_RSRP_scatt", "figure"),
            Output("NR_RX_RSRP_histo", "figure"),
        ],
        [
            Input("NR_RX_RSRP_rat", "value"),
            Input("NR_RX_RSRP_band", "value"),
            Input("sld_RX_RSRP_scat", "value"),
        ],
    )
    def update_RX_Gain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_RX_RSRP, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RX_RSRP, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Freq Cal =================================
    @callback(Output("NR_RX_Comp_band", "value"), Input("NR_RX_Comp_rat", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RX_Comp)

    @callback(
        [
            Output("NR_RX_Comp_band", "options"),
            Output("NR_RX_Comp_scatt", "figure"),
            Output("NR_RX_Comp_histo", "figure"),
        ],
        [
            Input("NR_RX_Comp_rat", "value"),
            Input("NR_RX_Comp_band", "value"),
            Input("sld_RX_Comp_scat", "value"),
        ],
    )
    def update_RX_Gain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_RX_Comp, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RX_Comp, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Mixer Cal =================================
    @callback(Output("NR_RX_Mixer_band", "value"), Input("NR_RX_Mixer_rat", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RX_Mixer)

    @callback(
        [
            Output("NR_RX_Mixer_band", "options"),
            Output("NR_RX_Mixer_scatt", "figure"),
            Output("NR_RX_Mixer_histo", "figure"),
        ],
        [
            Input("NR_RX_Mixer_rat", "value"),
            Input("NR_RX_Mixer_band", "value"),
            Input("sld_RX_Mixer_scat", "value"),
        ],
    )
    def update_RX_Gain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_RX_Mixer, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RX_Mixer, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 APT Measuremnt =================================
    @callback(Output("NR_APT_Meas_band", "value"), Input("NR_APT_Meas_rat", "value"))
    def APTMeas_NR(selected_rat):
        return Initialize_band(selected_rat, df_APT_Meas)

    @callback(
        [
            Output("NR_APT_Meas_band", "options"),
            Output("NR_APT_Meas_scatt", "figure"),
            Output("NR_APT_Meas_histo", "figure"),
        ],
        [
            Input("NR_APT_Meas_rat", "value"),
            Input("NR_APT_Meas_band", "value"),
            Input("sld_APT_Meas_scat", "value"),
        ],
    )
    def update_APTMeas(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_APT_Meas, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_APT_Meas, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Psat =================================
    @callback(Output("NR_ET_PSat_band", "value"), Input("NR_ET_Psat_rat", "value"))
    def ET_Psat_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Psat)

    @callback(
        [
            Output("NR_ET_PSat_band", "options"),
            Output("NR_ET_Psat_scatt", "figure"),
            Output("NR_ET_Psat_histo", "figure"),
        ],
        [
            Input("NR_ET_Psat_rat", "value"),
            Input("NR_ET_PSat_band", "value"),
            Input("sld_ET_Psat_scat", "value"),
        ],
    )
    def update_ET_Psat(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_ET_Psat, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Psat, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Pgain =================================
    @callback(Output("NR_ET_Pgain_band", "value"), Input("NR_ET_Pgain_rat", "value"))
    def ET_Pgain_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Pgain)

    @callback(
        [
            Output("NR_ET_Pgain_band", "options"),
            Output("NR_ET_Pgain_scatt", "figure"),
            Output("NR_ET_Pgain_histo", "figure"),
        ],
        [
            Input("NR_ET_Pgain_rat", "value"),
            Input("NR_ET_Pgain_band", "value"),
            Input("sld_ET_Pgain_scat", "value"),
        ],
    )
    def update_ET_Pgain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_ET_Pgain, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Pgain, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Power =================================
    @callback(Output("NR_ET_Power_band", "value"), Input("NR_ET_Power_rat", "value"))
    def ET_Power_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Power)

    @callback(
        [
            Output("NR_ET_Power_band", "options"),
            Output("NR_ET_Power_scatt", "figure"),
            Output("NR_ET_Power_histo", "figure"),
        ],
        [
            Input("NR_ET_Power_rat", "value"),
            Input("NR_ET_Power_band", "value"),
            Input("sld_ET_Power_scat", "value"),
        ],
    )
    def update_ET_Power(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_ET_Power, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Power, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Freq =================================
    @callback(Output("NR_ET_Freq_band", "value"), Input("NR_ET_Freq_rat", "value"))
    def ET_Freq_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Freq)

    @callback(
        [
            Output("NR_ET_Freq_band", "options"),
            Output("NR_ET_Freq_scatt", "figure"),
            Output("NR_ET_Freq_histo", "figure"),
        ],
        [
            Input("NR_ET_Freq_rat", "value"),
            Input("NR_ET_Freq_band", "value"),
            Input("sld_ET_Freq_scat", "value"),
        ],
    )
    def update_ET_Freq(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = Update_band_and_graph(df_ET_Freq, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Freq, selected_rat)

        return band_opt, scatt_fig, histo_fig

    dash.register_page(__name__, path="/NR", name="NR_ Sub6", title="NR_ Sub6", layout=layout)

    return layout
