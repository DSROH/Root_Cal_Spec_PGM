import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input, State
from LSI_Solution.pages.page_cf import (
    Initialize_dropdowns,
    Create_range_slider,
    Initialize_band,
    Band_list,
    Update_band_and_graph,
    tweet_callback,
    Drawing_pcc,
    Drawing_scc,
)


def Initialize_nr(dict_nr):
    dropdown_keys = [
        "RX_Gain",
        "RX_RSRP",
        "RX_Comp",
        "RX_Mix",
        "FBRX_GM",
        "FBRX_GC",
        "FBRX_FM",
        "FBRX_FC",
        "APT_Meas",
        "ET_Psat",
        "ET_Pgain",
        "ET_Power",
        "ET_Freq",
    ]
    dropdowns, data_frame = Initialize_dropdowns(dict_nr, dropdown_keys)

    layout = html.Div(
        [
            # ** ================================= Sub6 RX Gain Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "RX", "Gain Cal"), id="head_rx_gain", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(dropdowns["RX_Gain_r"], width=1),
                    dbc.Col(dropdowns["RX_Gain_b"], width=1),
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
                        Create_range_slider("sld_RX_Gain_scat", data_frame["RX_Gain"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_RX_Gain_hist", data_frame["RX_Gain"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
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
                    dbc.Col(dropdowns["RX_RSRP_r"], width=1),
                    dbc.Col(dropdowns["RX_RSRP_b"], width=1),
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
                        Create_range_slider("sld_RX_RSRP_scat", data_frame["RX_RSRP"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_RX_RSRP_hist", data_frame["RX_RSRP"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
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
                    dbc.Col(dropdowns["RX_Comp_r"], width=1),
                    dbc.Col(dropdowns["RX_Comp_b"], width=1),
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
                        Create_range_slider("sld_RX_Comp_scat", data_frame["RX_Comp"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_RX_Comp_hist", data_frame["RX_Comp"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
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
                    dbc.Col(dropdowns["RX_Mix_r"], width=1),
                    dbc.Col(dropdowns["RX_Mix_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RX_Mix_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RX_Mix_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_RX_Mix_scat", data_frame["RX_Mix"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_RX_Mix_hist", data_frame["RX_Mix"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 FBRX Gain Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "FBRX", "Gain Cal"), id="head_fbrx_gm", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(dropdowns["FBRX_GM_r"], width=1),
                    dbc.Col(dropdowns["FBRX_GM_b"], width=1),
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
                        Create_range_slider("sld_FBRX_GM_scat", data_frame["FBRX_GM"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_FBRX_GM_hist", data_frame["FBRX_GM"], use_min_max=False),
                        width={"size": 6, "offset": 0},
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
                    dbc.Col(dropdowns["FBRX_FM_r"], width=1),
                    dbc.Col(dropdowns["FBRX_FM_b"], width=1),
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
                        Create_range_slider("sld_FBRX_FM_scat", data_frame["FBRX_FM"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_FBRX_FM_hist", data_frame["FBRX_FM"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                ],
                align="center",
            ),
            html.Div(id="fbrx_fm_scc", children=[]),
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
                    dbc.Col(dropdowns["APT_Meas_r"], width=1),
                    dbc.Col(dropdowns["APT_Meas_b"], width=1),
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
                        Create_range_slider("sld_APT_Meas_scat", data_frame["APT_Meas"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_APT_Meas_hist", data_frame["APT_Meas"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
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
                    dbc.Col(dropdowns["ET_Psat_r"], width=1),
                    dbc.Col(dropdowns["ET_Psat_b"], width=1),
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
                        Create_range_slider("sld_ET_Psat_scat", data_frame["ET_Psat"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_ET_Psat_hist", data_frame["ET_Psat"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
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
                    dbc.Col(dropdowns["ET_Pgain_r"], width=1),
                    dbc.Col(dropdowns["ET_Pgain_b"], width=1),
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
                        Create_range_slider("sld_ET_Pgain_scat", data_frame["ET_Pgain"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_ET_Pgain_hist", data_frame["ET_Pgain"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
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
                    dbc.Col(dropdowns["ET_Power_r"], width=1),
                    dbc.Col(dropdowns["ET_Power_b"], width=1),
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
                        Create_range_slider("sld_ET_Power_scat", data_frame["ET_Power"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_ET_Power_hist", data_frame["ET_Power"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                ],
                align="center",
            ),
            html.Div(id="et_power_scc", children=[]),
            html.Hr(),
            # ** ================================= Sub6 ET Freq =================================
            html.Div(
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H2(
                                    children=tweet_callback("NR", "ET-SAPT", "Freq Cal"),
                                    id="head_et_freq",
                                    className="display-7",
                                ),
                                width="auto",
                            ),
                            dbc.Col(dropdowns["ET_Freq_r"], width=1),
                            dbc.Col(dropdowns["ET_Freq_b"], width=1),
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
                                Create_range_slider("sld_ET_Freq_scat", data_frame["ET_Freq"], use_min_max=False),
                                width={"size": 6, "offset": 0},
                            ),
                            dbc.Col(
                                Create_range_slider("sld_ET_Freq_hist", data_frame["ET_Freq"], use_min_max=False),
                                width={"size": 6, "offset": 0},
                            ),
                        ],
                        align="center",
                    ),
                ]
            ),
            html.Div(id="et_freq_scc", children=[]),
            html.Hr(),
        ]
    )

    # ** ======================================================================================
    # **
    # **                                   Call Back Function
    # **
    # ** ======================================================================================

    @callback(Output("NR_RX_Gain_b", "value"), Input("NR_RX_Gain_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["RX_Gain"])

    @callback(
        [
            Output("NR_RX_Gain_b", "options"),
            Output("NR_RX_Gain_scatt", "figure"),
            Output("NR_RX_Gain_histo", "figure"),
        ],
        [
            Input("NR_RX_Gain_r", "value"),
            Input("NR_RX_Gain_b", "value"),
            Input("sld_RX_Gain_scat", "value"),
            Input("sld_RX_Gain_hist", "value"),
        ],
    )
    def update_RX_Gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["RX_Gain"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["RX_Gain"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX RSRP Cal =================================
    @callback(Output("NR_RX_RSRP_b", "value"), Input("NR_RX_RSRP_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["RX_RSRP"])

    @callback(
        [
            Output("NR_RX_RSRP_b", "options"),
            Output("NR_RX_RSRP_scatt", "figure"),
            Output("NR_RX_RSRP_histo", "figure"),
        ],
        [
            Input("NR_RX_RSRP_r", "value"),
            Input("NR_RX_RSRP_b", "value"),
            Input("sld_RX_RSRP_scat", "value"),
            Input("sld_RX_RSRP_hist", "value"),
        ],
    )
    def update_RX_Gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["RX_RSRP"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["RX_RSRP"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Freq Cal =================================
    @callback(Output("NR_RX_Comp_b", "value"), Input("NR_RX_Comp_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["RX_Comp"])

    @callback(
        [
            Output("NR_RX_Comp_b", "options"),
            Output("NR_RX_Comp_scatt", "figure"),
            Output("NR_RX_Comp_histo", "figure"),
        ],
        [
            Input("NR_RX_Comp_r", "value"),
            Input("NR_RX_Comp_b", "value"),
            Input("sld_RX_Comp_scat", "value"),
            Input("sld_RX_Comp_hist", "value"),
        ],
    )
    def update_RX_Gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["RX_Comp"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["RX_Comp"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Mixer Cal =================================
    @callback(Output("NR_RX_Mix_b", "value"), Input("NR_RX_Mix_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["RX_Mix"])

    @callback(
        [
            Output("NR_RX_Mix_b", "options"),
            Output("NR_RX_Mix_scatt", "figure"),
            Output("NR_RX_Mix_histo", "figure"),
        ],
        [
            Input("NR_RX_Mix_r", "value"),
            Input("NR_RX_Mix_b", "value"),
            Input("sld_RX_Mix_scat", "value"),
            Input("sld_RX_Mix_hist", "value"),
        ],
    )
    def update_RX_Gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["RX_Mix"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["RX_Mix"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 FBRX Gain Cal =================================

    @callback(Output("NR_FBRX_GM_b", "value"), Input("NR_FBRX_GM_r", "value"))
    def FBRX_GM_NR(selected_r):
        return Initialize_band(selected_r, data_frame["FBRX_GM"])

    @callback(
        [
            Output("NR_FBRX_GM_b", "options"),
            Output("NR_FBRX_GM_grp_scatt", "figure"),
            Output("NR_FBRX_GM_grp_histo", "figure"),
            Output("NR_FBRX_GC_grp_scatt", "figure"),
            Output("NR_FBRX_GC_grp_histo", "figure"),
            Output("fbrx_gm_scc", "children"),
        ],
        [
            Input("NR_FBRX_GM_r", "value"),
            Input("NR_FBRX_GM_b", "value"),
            Input("sld_FBRX_GM_scat", "value"),
            Input("sld_FBRX_GM_hist", "value"),
            State("fbrx_gm_scc", "children"),
        ],
    )
    def update_FBRX_GM(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["FBRX_GM"], selected_r)
        filtered_df = data_frame["FBRX_GM"][data_frame["FBRX_GM"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2 = Drawing_pcc(
                selected_r, selected_b, filtered_df, scatt_range, histo_range, scatt_range, histo_range
            )
            # * _scc_scatt 포함된 layout 제거
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            # * _scc_scatt layout 생성
            children = Drawing_scc(
                selected_r,
                selected_b,
                filtered_df,
                "FBRX Gain Cal",
                children,
                scatt_range,
                histo_range,
                scatt_range,
                histo_range,
            )

            return band_opt, scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2, children
        else:
            scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2 = Drawing_pcc(
                selected_r, selected_b, filtered_df, scatt_range, histo_range, scatt_range, histo_range
            )
            # * _scc_scatt 포함된 layout 제거
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            # * PCC만 리턴
            return band_opt, scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2, children

    # ** ================================= Sub6 FBRX Freq Cal =================================
    @callback(Output("NR_FBRX_FM_b", "value"), Input("NR_FBRX_FM_r", "value"))
    def FBRX_FM_NR(selected_r):
        return Initialize_band(selected_r, data_frame["FBRX_FM"])

    @callback(
        [
            Output("NR_FBRX_FM_b", "options"),
            Output("NR_FBRX_FM_grp_scatt", "figure"),
            Output("NR_FBRX_FM_grp_histo", "figure"),
            Output("NR_FBRX_FC_grp_scatt", "figure"),
            Output("NR_FBRX_FC_grp_histo", "figure"),
            Output("fbrx_fm_scc", "children"),
        ],
        [
            Input("NR_FBRX_FM_r", "value"),
            Input("NR_FBRX_FM_b", "value"),
            Input("sld_FBRX_FM_scat", "value"),
            Input("sld_FBRX_FM_hist", "value"),
            State("fbrx_fm_scc", "children"),
        ],
    )
    def update_FBRXFreq(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["FBRX_FM"], selected_r)
        filtered_df = data_frame["FBRX_FM"][data_frame["FBRX_FM"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2 = Drawing_pcc(
                selected_r, selected_b, filtered_df, scatt_range, histo_range, scatt_range, histo_range
            )
            # * _scc_scatt 포함된 layout 제거
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            # * _scc_scatt layout 생성
            children = Drawing_scc(
                selected_r,
                selected_b,
                filtered_df,
                "FBRX Gain Cal",
                children,
                scatt_range,
                histo_range,
                scatt_range,
                histo_range,
            )

            return band_opt, scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2, children
        else:
            scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2 = Drawing_pcc(
                selected_r, selected_b, filtered_df, scatt_range, histo_range, scatt_range, histo_range
            )
            # * _scc_scatt 포함된 layout 제거
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            # * PCC만 리턴
            return band_opt, scatt_fig_pcc1, histo_fig_pcc1, scatt_fig_pcc2, histo_fig_pcc2, children

    # ** ================================= Sub6 APT Measuremnt =================================
    @callback(Output("NR_APT_Meas_b", "value"), Input("NR_APT_Meas_r", "value"))
    def APTMeas_NR(selected_r):
        return Initialize_band(selected_r, data_frame["APT_Meas"])

    @callback(
        [
            Output("NR_APT_Meas_b", "options"),
            Output("NR_APT_Meas_scatt", "figure"),
            Output("NR_APT_Meas_histo", "figure"),
            Output("apt_measure_scc", "children"),
        ],
        [
            Input("NR_APT_Meas_r", "value"),
            Input("NR_APT_Meas_b", "value"),
            Input("sld_APT_Meas_scat", "value"),
            Input("sld_APT_Meas_hist", "value"),
            State("apt_measure_scc", "children"),
        ],
    )
    def update_APTMeas(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["APT_Meas"], selected_r)
        filtered_df = data_frame["APT_Meas"][data_frame["APT_Meas"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            children = Drawing_scc(selected_r, selected_b, filtered_df, "ET-SAPT", children, scatt_range, histo_range)
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children
        else:
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children

    # ** ================================= Sub6 ET-SAPT Psat =================================
    @callback(Output("NR_ET_Psat_b", "value"), Input("NR_ET_Psat_r", "value"))
    def ET_Psat_NR(selected_r):
        return Initialize_band(selected_r, data_frame["ET_Psat"])

    @callback(
        [
            Output("NR_ET_Psat_b", "options"),
            Output("NR_ET_Psat_scatt", "figure"),
            Output("NR_ET_Psat_histo", "figure"),
            Output("et_psat_scc", "children"),
        ],
        [
            Input("NR_ET_Psat_r", "value"),
            Input("NR_ET_Psat_b", "value"),
            Input("sld_ET_Psat_scat", "value"),
            Input("sld_ET_Psat_hist", "value"),
            State("et_psat_scc", "children"),
        ],
    )
    def update_ET_Psat(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["ET_Psat"], selected_r)
        filtered_df = data_frame["ET_Psat"][data_frame["ET_Psat"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            children = Drawing_scc(selected_r, selected_b, filtered_df, "ET-SAPT", children, scatt_range, histo_range)
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children
        else:
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children

    # ** ================================= Sub6 ET-SAPT Pgain =================================
    @callback(Output("NR_ET_Pgain_b", "value"), Input("NR_ET_Pgain_r", "value"))
    def ET_Pgain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["ET_Pgain"])

    @callback(
        [
            Output("NR_ET_Pgain_b", "options"),
            Output("NR_ET_Pgain_scatt", "figure"),
            Output("NR_ET_Pgain_histo", "figure"),
            Output("et_pgain_scc", "children"),
        ],
        [
            Input("NR_ET_Pgain_r", "value"),
            Input("NR_ET_Pgain_b", "value"),
            Input("sld_ET_Pgain_scat", "value"),
            Input("sld_ET_Pgain_hist", "value"),
            State("et_pgain_scc", "children"),
        ],
    )
    def update_ET_Pgain(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["ET_Pgain"], selected_r)
        filtered_df = data_frame["ET_Pgain"][data_frame["ET_Pgain"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            children = Drawing_scc(selected_r, selected_b, filtered_df, "ET-SAPT", children, scatt_range, histo_range)
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children
        else:
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children

    # ** ================================= Sub6 ET-SAPT Power =================================
    @callback(Output("NR_ET_Power_b", "value"), Input("NR_ET_Power_r", "value"))
    def ET_Power_NR(selected_r):
        return Initialize_band(selected_r, data_frame["ET_Power"])

    @callback(
        [
            Output("NR_ET_Power_b", "options"),
            Output("NR_ET_Power_scatt", "figure"),
            Output("NR_ET_Power_histo", "figure"),
            Output("et_power_scc", "children"),
        ],
        [
            Input("NR_ET_Power_r", "value"),
            Input("NR_ET_Power_b", "value"),
            Input("sld_ET_Power_scat", "value"),
            Input("sld_ET_Power_hist", "value"),
            State("et_power_scc", "children"),
        ],
    )
    def update_ET_Power(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["ET_Power"], selected_r)
        filtered_df = data_frame["ET_Power"][data_frame["ET_Power"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            children = Drawing_scc(selected_r, selected_b, filtered_df, "ET-SAPT", children, scatt_range, histo_range)
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children
        else:
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children

    # ** ================================= Sub6 ET-SAPT Freq =================================
    @callback(Output("NR_ET_Freq_b", "value"), Input("NR_ET_Freq_r", "value"))
    def ET_Freq_NR(selected_r):
        return Initialize_band(selected_r, data_frame["ET_Freq"])

    @callback(
        [
            Output("NR_ET_Freq_b", "options"),
            Output("NR_ET_Freq_scatt", "figure"),
            Output("NR_ET_Freq_histo", "figure"),
            Output("et_freq_scc", "children"),
        ],
        [
            Input("NR_ET_Freq_r", "value"),
            Input("NR_ET_Freq_b", "value"),
            Input("sld_ET_Freq_scat", "value"),
            Input("sld_ET_Freq_hist", "value"),
            State("et_freq_scc", "children"),
        ],
    )
    def update_ET_Freq(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["ET_Freq"], selected_r)
        filtered_df = data_frame["ET_Freq"][data_frame["ET_Freq"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            children = Drawing_scc(selected_r, selected_b, filtered_df, "ET-SAPT", children, scatt_range, histo_range)
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children
        else:
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children

    dash.register_page(__name__, path="/NR_Sub6", name="NR_Sub6", title="NR_Sub6", layout=layout)

    return layout
