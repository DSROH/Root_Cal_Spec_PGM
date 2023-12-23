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


def Initialize_nr(dict_nr, rat):
    dropdown_keys = [
        "rx_gain",
        "rx_rsrp",
        "rx_comp",
        "rx_mix",
        "fbrx_gm",
        "fbrx_gc",
        "fbrx_fm",
        "fbrx_fc",
        "apt_meas",
        "et_psat",
        "et_pgain",
        "et_power",
        "et_freq",
    ]
    dropdowns, data_frame = Initialize_dropdowns(dict_nr, rat, dropdown_keys)

    layout = html.Div(
        [
            # ** ================================= Sub6 RX Gain Cal =================================
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children=tweet_callback("NR", "RX", "Gain Cal"), id="head_rx_gain", className="display-7"),
                        width="auto",
                    ),
                    dbc.Col(dropdowns["rx_gain_r"], width=1),
                    dbc.Col(dropdowns["rx_gain_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_rx_gain_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_rx_gain_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_rx_gain_scat", data_frame["rx_gain"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_rx_gain_hist", data_frame["rx_gain"], use_min_max=False),
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
                    dbc.Col(dropdowns["rx_rsrp_r"], width=1),
                    dbc.Col(dropdowns["rx_rsrp_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_rx_rsrp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_rx_rsrp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_rx_rsrp_scat", data_frame["rx_rsrp"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_rx_rsrp_hist", data_frame["rx_rsrp"], use_min_max=False),
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
                    dbc.Col(dropdowns["rx_comp_r"], width=1),
                    dbc.Col(dropdowns["rx_comp_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_rx_comp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_rx_comp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_rx_comp_scat", data_frame["rx_comp"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_rx_comp_hist", data_frame["rx_comp"], use_min_max=False),
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
                    dbc.Col(dropdowns["rx_mix_r"], width=1),
                    dbc.Col(dropdowns["rx_mix_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_rx_mix_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_rx_mix_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_rx_mix_scat", data_frame["rx_mix"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_rx_mix_hist", data_frame["rx_mix"], use_min_max=False),
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
                    dbc.Col(dropdowns["fbrx_gm_r"], width=1),
                    dbc.Col(dropdowns["fbrx_gm_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_fbrx_gm_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_fbrx_gm_grp_histo"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_fbrx_gc_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_fbrx_gc_grp_histo"), width={"size": 3, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_fbrx_gm_scat", data_frame["fbrx_gm"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_fbrx_gm_hist", data_frame["fbrx_gm"], use_min_max=False),
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
                    dbc.Col(dropdowns["fbrx_fm_r"], width=1),
                    dbc.Col(dropdowns["fbrx_fm_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_fbrx_fm_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_fbrx_fm_grp_histo"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_fbrx_fc_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_fbrx_fc_grp_histo"), width={"size": 3, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_fbrx_fm_scat", data_frame["fbrx_fm"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_fbrx_fm_hist", data_frame["fbrx_fm"], use_min_max=False),
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
                    dbc.Col(dropdowns["apt_meas_r"], width=1),
                    dbc.Col(dropdowns["apt_meas_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_apt_meas_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_apt_meas_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_apt_meas_scat", data_frame["apt_meas"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_apt_meas_hist", data_frame["apt_meas"], use_min_max=False),
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
                    dbc.Col(dropdowns["et_psat_r"], width=1),
                    dbc.Col(dropdowns["et_psat_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_et_psat_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_et_psat_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_et_psat_scat", data_frame["et_psat"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_et_psat_hist", data_frame["et_psat"], use_min_max=False),
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
                    dbc.Col(dropdowns["et_pgain_r"], width=1),
                    dbc.Col(dropdowns["et_pgain_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_et_pgain_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_et_pgain_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_et_pgain_scat", data_frame["et_pgain"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_et_pgain_hist", data_frame["et_pgain"], use_min_max=False),
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
                    dbc.Col(dropdowns["et_power_r"], width=1),
                    dbc.Col(dropdowns["et_power_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="nr_et_power_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="nr_et_power_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_et_power_scat", data_frame["et_power"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_et_power_hist", data_frame["et_power"], use_min_max=False),
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
                            dbc.Col(dropdowns["et_freq_r"], width=1),
                            dbc.Col(dropdowns["et_freq_b"], width=1),
                        ],
                        align="center",
                    ),
                    html.Br(),
                    dbc.Row(
                        [
                            dbc.Col(dcc.Graph(id="nr_et_freq_scatt"), width={"size": 6, "offset": 0}),
                            dbc.Col(dcc.Graph(id="nr_et_freq_histo"), width={"size": 6, "offset": 0}),
                        ],
                        align="center",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                Create_range_slider("sld_et_freq_scat", data_frame["et_freq"], use_min_max=False),
                                width={"size": 6, "offset": 0},
                            ),
                            dbc.Col(
                                Create_range_slider("sld_et_freq_hist", data_frame["et_freq"], use_min_max=False),
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

    @callback(Output("nr_rx_gain_b", "value"), Input("nr_rx_gain_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["rx_gain"])

    @callback(
        [
            Output("nr_rx_gain_b", "options"),
            Output("nr_rx_gain_scatt", "figure"),
            Output("nr_rx_gain_histo", "figure"),
        ],
        [
            Input("nr_rx_gain_r", "value"),
            Input("nr_rx_gain_b", "value"),
            Input("sld_rx_gain_scat", "value"),
            Input("sld_rx_gain_hist", "value"),
        ],
    )
    def update_rx_gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["rx_gain"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["rx_gain"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX RSRP Cal =================================
    @callback(Output("nr_rx_rsrp_b", "value"), Input("nr_rx_rsrp_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["rx_rsrp"])

    @callback(
        [
            Output("nr_rx_rsrp_b", "options"),
            Output("nr_rx_rsrp_scatt", "figure"),
            Output("nr_rx_rsrp_histo", "figure"),
        ],
        [
            Input("nr_rx_rsrp_r", "value"),
            Input("nr_rx_rsrp_b", "value"),
            Input("sld_rx_rsrp_scat", "value"),
            Input("sld_rx_rsrp_hist", "value"),
        ],
    )
    def update_rx_gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["rx_rsrp"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["rx_rsrp"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Freq Cal =================================
    @callback(Output("nr_rx_comp_b", "value"), Input("nr_rx_comp_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["rx_comp"])

    @callback(
        [
            Output("nr_rx_comp_b", "options"),
            Output("nr_rx_comp_scatt", "figure"),
            Output("nr_rx_comp_histo", "figure"),
        ],
        [
            Input("nr_rx_comp_r", "value"),
            Input("nr_rx_comp_b", "value"),
            Input("sld_rx_comp_scat", "value"),
            Input("sld_rx_comp_hist", "value"),
        ],
    )
    def update_rx_gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["rx_comp"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["rx_comp"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Mixer Cal =================================
    @callback(Output("nr_rx_mix_b", "value"), Input("nr_rx_mix_r", "value"))
    def RXGain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["rx_mix"])

    @callback(
        [
            Output("nr_rx_mix_b", "options"),
            Output("nr_rx_mix_scatt", "figure"),
            Output("nr_rx_mix_histo", "figure"),
        ],
        [
            Input("nr_rx_mix_r", "value"),
            Input("nr_rx_mix_b", "value"),
            Input("sld_rx_mix_scat", "value"),
            Input("sld_rx_mix_hist", "value"),
        ],
    )
    def update_rx_gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig, histo_fig = Update_band_and_graph(data_frame["rx_mix"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["rx_mix"], selected_r)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 FBRX Gain Cal =================================

    @callback(Output("nr_fbrx_gm_b", "value"), Input("nr_fbrx_gm_r", "value"))
    def fbrx_gm_NR(selected_r):
        return Initialize_band(selected_r, data_frame["fbrx_gm"])

    @callback(
        [
            Output("nr_fbrx_gm_b", "options"),
            Output("nr_fbrx_gm_grp_scatt", "figure"),
            Output("nr_fbrx_gm_grp_histo", "figure"),
            Output("nr_fbrx_gc_grp_scatt", "figure"),
            Output("nr_fbrx_gc_grp_histo", "figure"),
            Output("fbrx_gm_scc", "children"),
        ],
        [
            Input("nr_fbrx_gm_r", "value"),
            Input("nr_fbrx_gm_b", "value"),
            Input("sld_fbrx_gm_scat", "value"),
            Input("sld_fbrx_gm_hist", "value"),
            State("fbrx_gm_scc", "children"),
        ],
    )
    def update_fbrx_gm(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["fbrx_gm"], selected_r)
        filtered_df = data_frame["fbrx_gm"][data_frame["fbrx_gm"]["Band"] == selected_b].reset_index(drop=True)
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
    @callback(Output("nr_fbrx_fm_b", "value"), Input("nr_fbrx_fm_r", "value"))
    def fbrx_fm_NR(selected_r):
        return Initialize_band(selected_r, data_frame["fbrx_fm"])

    @callback(
        [
            Output("nr_fbrx_fm_b", "options"),
            Output("nr_fbrx_fm_grp_scatt", "figure"),
            Output("nr_fbrx_fm_grp_histo", "figure"),
            Output("nr_fbrx_fc_grp_scatt", "figure"),
            Output("nr_fbrx_fc_grp_histo", "figure"),
            Output("fbrx_fm_scc", "children"),
        ],
        [
            Input("nr_fbrx_fm_r", "value"),
            Input("nr_fbrx_fm_b", "value"),
            Input("sld_fbrx_fm_scat", "value"),
            Input("sld_fbrx_fm_hist", "value"),
            State("fbrx_fm_scc", "children"),
        ],
    )
    def update_FBRXFreq(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["fbrx_fm"], selected_r)
        filtered_df = data_frame["fbrx_fm"][data_frame["fbrx_fm"]["Band"] == selected_b].reset_index(drop=True)
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
    @callback(Output("nr_apt_meas_b", "value"), Input("nr_apt_meas_r", "value"))
    def APTMeas_NR(selected_r):
        return Initialize_band(selected_r, data_frame["apt_meas"])

    @callback(
        [
            Output("nr_apt_meas_b", "options"),
            Output("nr_apt_meas_scatt", "figure"),
            Output("nr_apt_meas_histo", "figure"),
            Output("apt_measure_scc", "children"),
        ],
        [
            Input("nr_apt_meas_r", "value"),
            Input("nr_apt_meas_b", "value"),
            Input("sld_apt_meas_scat", "value"),
            Input("sld_apt_meas_hist", "value"),
            State("apt_measure_scc", "children"),
        ],
    )
    def update_APTMeas(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["apt_meas"], selected_r)
        filtered_df = data_frame["apt_meas"][data_frame["apt_meas"]["Band"] == selected_b].reset_index(drop=True)
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
    @callback(Output("nr_et_psat_b", "value"), Input("nr_et_psat_r", "value"))
    def et_psat_NR(selected_r):
        return Initialize_band(selected_r, data_frame["et_psat"])

    @callback(
        [
            Output("nr_et_psat_b", "options"),
            Output("nr_et_psat_scatt", "figure"),
            Output("nr_et_psat_histo", "figure"),
            Output("et_psat_scc", "children"),
        ],
        [
            Input("nr_et_psat_r", "value"),
            Input("nr_et_psat_b", "value"),
            Input("sld_et_psat_scat", "value"),
            Input("sld_et_psat_hist", "value"),
            State("et_psat_scc", "children"),
        ],
    )
    def update_et_psat(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["et_psat"], selected_r)
        filtered_df = data_frame["et_psat"][data_frame["et_psat"]["Band"] == selected_b].reset_index(drop=True)
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
    @callback(Output("nr_et_pgain_b", "value"), Input("nr_et_pgain_r", "value"))
    def et_pgain_NR(selected_r):
        return Initialize_band(selected_r, data_frame["et_pgain"])

    @callback(
        [
            Output("nr_et_pgain_b", "options"),
            Output("nr_et_pgain_scatt", "figure"),
            Output("nr_et_pgain_histo", "figure"),
            Output("et_pgain_scc", "children"),
        ],
        [
            Input("nr_et_pgain_r", "value"),
            Input("nr_et_pgain_b", "value"),
            Input("sld_et_pgain_scat", "value"),
            Input("sld_et_pgain_hist", "value"),
            State("et_pgain_scc", "children"),
        ],
    )
    def update_et_pgain(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["et_pgain"], selected_r)
        filtered_df = data_frame["et_pgain"][data_frame["et_pgain"]["Band"] == selected_b].reset_index(drop=True)
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
    @callback(Output("nr_et_power_b", "value"), Input("nr_et_power_r", "value"))
    def et_power_NR(selected_r):
        return Initialize_band(selected_r, data_frame["et_power"])

    @callback(
        [
            Output("nr_et_power_b", "options"),
            Output("nr_et_power_scatt", "figure"),
            Output("nr_et_power_histo", "figure"),
            Output("et_power_scc", "children"),
        ],
        [
            Input("nr_et_power_r", "value"),
            Input("nr_et_power_b", "value"),
            Input("sld_et_power_scat", "value"),
            Input("sld_et_power_hist", "value"),
            State("et_power_scc", "children"),
        ],
    )
    def update_et_power(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["et_power"], selected_r)
        filtered_df = data_frame["et_power"][data_frame["et_power"]["Band"] == selected_b].reset_index(drop=True)
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
    @callback(Output("nr_et_freq_b", "value"), Input("nr_et_freq_r", "value"))
    def et_freq_NR(selected_r):
        return Initialize_band(selected_r, data_frame["et_freq"])

    @callback(
        [
            Output("nr_et_freq_b", "options"),
            Output("nr_et_freq_scatt", "figure"),
            Output("nr_et_freq_histo", "figure"),
            Output("et_freq_scc", "children"),
        ],
        [
            Input("nr_et_freq_r", "value"),
            Input("nr_et_freq_b", "value"),
            Input("sld_et_freq_scat", "value"),
            Input("sld_et_freq_hist", "value"),
            State("et_freq_scc", "children"),
        ],
    )
    def update_et_freq(selected_r, selected_b, scatt_range, histo_range, children):
        band_opt = Band_list(data_frame["et_freq"], selected_r)
        filtered_df = data_frame["et_freq"][data_frame["et_freq"]["Band"] == selected_b].reset_index(drop=True)
        if filtered_df["Path"].str.contains("Tx2").any():
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            children = Drawing_scc(selected_r, selected_b, filtered_df, "ET-SAPT", children, scatt_range, histo_range)
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children
        else:
            scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_r, selected_b, filtered_df, scatt_range, histo_range)
            children = [layout for layout in children if f"_scc_scatt" not in str(layout)]
            return band_opt, scatt_fig_pcc, histo_fig_pcc, children

    dash.register_page(__name__, path="/NR_SUB6", name="NR_SUB6", title="NR_SUB6", layout=layout)

    return layout
