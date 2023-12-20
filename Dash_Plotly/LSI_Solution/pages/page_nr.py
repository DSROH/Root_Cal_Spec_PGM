import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import create_dropdown, create_range_slider, Initialize_band, Band_list, update_band_and_graph


def initialize_nr(dict_nr):
    df_RXGain = dict_nr["RX_Gain"]
    df_RXRSRP = dict_nr["RX_RSRP"]
    df_RXComp = dict_nr["RX_Comp"]
    df_RXMixer = dict_nr["RX_Mix"]
    df_fbrxgm = dict_nr["FBRX_GM"]
    df_fbrxgc = dict_nr["FBRX_GC"]
    df_fbrxfm = dict_nr["FBRX_FM"]
    df_fbrxfc = dict_nr["FBRX_FC"]
    df_APT_Meas = dict_nr["APT_Meas"]
    df_ET_Psat = dict_nr["ET_Psat"]
    df_ET_Pgain = dict_nr["ET_Pgain"]
    df_ET_Power = dict_nr["ET_Power"]
    df_ET_Freq = dict_nr["ET_Freq"]

    band_opt = [{"label": "", "value": ""}]

    drop_FBRXGain_rat = create_dropdown("NR_FBRXGain_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_FBRXFreq_rat = create_dropdown("NR_FBRXFreq_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_RXGain_rat = create_dropdown("NR_RXGain_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_RXRSRP_rat = create_dropdown("NR_RXRSRP_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_RXComp_rat = create_dropdown("NR_RXComp_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_RXMixer_rat = create_dropdown("NR_RXMixer_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_APTMeas_rat = create_dropdown("NR_APTMeas_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Psat_rat = create_dropdown("NR_ETPsat_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Pgain_rat = create_dropdown("NR_ETPgain_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Power_rat = create_dropdown("NR_ETPower_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ET_Freq_rat = create_dropdown("NR_ETFreq_RAT", "n", [{"label": "NR", "value": "n"}])

    drop_FBRXGain_band = create_dropdown("NR_FBRXGain_band", "", band_opt)
    drop_FBRXFreq_band = create_dropdown("NR_FBRXFreq_band", "", band_opt)
    drop_RXGain_band = create_dropdown("NR_RXGain_band", "", band_opt)
    drop_RXRSRP_band = create_dropdown("NR_RXRSRP_band", "", band_opt)
    drop_RXComp_band = create_dropdown("NR_RXComp_band", "", band_opt)
    drop_RXMixer_band = create_dropdown("NR_RXMixer_band", "", band_opt)
    drop_APTMeas_band = create_dropdown("NR_APTMeas_band", "", band_opt)
    drop_ET_Psat_band = create_dropdown("NR_ETPSat_band", "", band_opt)
    drop_ET_Pgain_band = create_dropdown("NR_ETPgain_band", "", band_opt)
    drop_ET_Power_band = create_dropdown("NR_ETPower_band", "", band_opt)
    drop_ET_Freq_band = create_dropdown("NR_ETFreq_band", "", band_opt)

    layout = html.Div(
        [
            # ** ================================= Sub6 FBRX Gain Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 FBRX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_FBRXGain_rat, width=1),
                    dbc.Col(drop_FBRXGain_band, width=1),
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
                        create_range_slider("sld_FBRX_GM_scat", df_fbrxgm, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        create_range_slider("sld_FBRX_GC_scat", df_fbrxgc, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 FBRX Freq Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 FBRX Freq Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_FBRXFreq_rat, width=1),
                    dbc.Col(drop_FBRXFreq_band, width=1),
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
                        create_range_slider("sld_FBRX_FM_scat", df_fbrxfm, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        create_range_slider("sld_FBRX_FC_scat", df_fbrxfc, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 RX Gain Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RXGain_rat, width=1),
                    dbc.Col(drop_RXGain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RXGain_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RXGain_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_RXGain_scat", df_RXGain, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 RX RSRP Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX RSRP Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RXRSRP_rat, width=1),
                    dbc.Col(drop_RXRSRP_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RXRSRP_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RXRSRP_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_RXRSRP_scat", df_RXRSRP, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 RX Freq Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX Freq Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RXComp_rat, width=1),
                    dbc.Col(drop_RXComp_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RXComp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RXComp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_RXComp_scat", df_RXComp, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 RX Mixer Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX Mixer Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_RXMixer_rat, width=1),
                    dbc.Col(drop_RXMixer_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_RXMixer_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_RXMixer_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_RXMixer_scat", df_RXComp, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 APT Measuremnt =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 APT Measurement", className="display-7"), width="auto"),
                    dbc.Col(drop_APTMeas_rat, width=1),
                    dbc.Col(drop_APTMeas_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_APTMeas_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_APTMeas_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_APTMeas_scat", df_APT_Meas, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 ET Psat =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Psat", className="display-7"), width="auto"),
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
                        create_range_slider("sld_ET_Psat_scat", df_ET_Psat, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 ET Pgain =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Pgain", className="display-7"), width="auto"),
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
                        create_range_slider("sld_ET_Pgain_scat", df_ET_Pgain, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 ET Power =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Power", className="display-7"), width="auto"),
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
                        create_range_slider("sld_ET_Power_scat", df_ET_Power, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= Sub6 ET Freq =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Freq", className="display-7"), width="auto"),
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
                        create_range_slider("sld_ET_Freq_scat", df_ET_Freq, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ** ================================= Sub6 FBRX Gain Cal =================================
    @callback(Output("NR_FBRXGain_band", "value"), Input("NR_FBRXGain_RAT", "value"))
    def FBRXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_fbrxgm)

    @callback(
        [
            Output("NR_FBRXGain_band", "options"),
            Output("NR_FBRX_GM_grp_scatt", "figure"),
            Output("NR_FBRX_GM_grp_histo", "figure"),
            Output("NR_FBRX_GC_grp_scatt", "figure"),
            Output("NR_FBRX_GC_grp_histo", "figure"),
        ],
        [
            Input("NR_FBRXGain_RAT", "value"),
            Input("NR_FBRXGain_band", "value"),
            Input("sld_FBRX_GM_scat", "value"),
            Input("sld_FBRX_FC_scat", "value"),
        ],
    )
    def update_FBRXGain(selected_rat, selected_band, scatt_range1, scatt_range2):
        scatter_fig1, histogram_fig1 = update_band_and_graph(df_fbrxgm, selected_rat, selected_band, scatt_range1)
        scatter_fig2, histogram_fig2 = update_band_and_graph(df_fbrxgc, selected_rat, selected_band, scatt_range2)
        band_opt = Band_list(df_fbrxgm, selected_rat)

        return band_opt, scatter_fig1, histogram_fig1, scatter_fig2, histogram_fig2

    # ** ================================= Sub6 FBRX Freq Cal =================================
    @callback(Output("NR_FBRXFreq_band", "value"), Input("NR_FBRXFreq_RAT", "value"))
    def FBRXFreq_NR(selected_rat):
        return Initialize_band(selected_rat, df_fbrxfm)

    @callback(
        [
            Output("NR_FBRXFreq_band", "options"),
            Output("NR_FBRX_FM_grp_scatt", "figure"),
            Output("NR_FBRX_FM_grp_histo", "figure"),
            Output("NR_FBRX_FC_grp_scatt", "figure"),
            Output("NR_FBRX_FC_grp_histo", "figure"),
        ],
        [
            Input("NR_FBRXFreq_RAT", "value"),
            Input("NR_FBRXFreq_band", "value"),
            Input("sld_FBRX_FM_scat", "value"),
            Input("sld_FBRX_FC_scat", "value"),
        ],
    )
    def update_FBRXFreq(selected_rat, selected_band, scatt_range1, scatt_range2):
        scatt_fig1, histo_fig1 = update_band_and_graph(df_fbrxfm, selected_rat, selected_band, scatt_range1)
        scatt_fig2, histo_fig2 = update_band_and_graph(df_fbrxfc, selected_rat, selected_band, scatt_range2)
        band_opt = Band_list(df_fbrxfm, selected_rat)

        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ** ================================= Sub6 RX Gain Cal =================================
    @callback(Output("NR_RXGain_band", "value"), Input("NR_RXGain_RAT", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RXGain)

    @callback(
        [
            Output("NR_RXGain_band", "options"),
            Output("NR_RXGain_scatt", "figure"),
            Output("NR_RXGain_histo", "figure"),
        ],
        [
            Input("NR_RXGain_RAT", "value"),
            Input("NR_RXGain_band", "value"),
            Input("sld_RXGain_scat", "value"),
        ],
    )
    def update_RXGain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_RXGain, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RXGain, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX RSRP Cal =================================
    @callback(Output("NR_RXRSRP_band", "value"), Input("NR_RXRSRP_RAT", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RXRSRP)

    @callback(
        [
            Output("NR_RXRSRP_band", "options"),
            Output("NR_RXRSRP_scatt", "figure"),
            Output("NR_RXRSRP_histo", "figure"),
        ],
        [
            Input("NR_RXRSRP_RAT", "value"),
            Input("NR_RXRSRP_band", "value"),
            Input("sld_RXRSRP_scat", "value"),
        ],
    )
    def update_RXGain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_RXRSRP, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RXRSRP, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Freq Cal =================================
    @callback(Output("NR_RXComp_band", "value"), Input("NR_RXComp_RAT", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RXComp)

    @callback(
        [
            Output("NR_RXComp_band", "options"),
            Output("NR_RXComp_scatt", "figure"),
            Output("NR_RXComp_histo", "figure"),
        ],
        [
            Input("NR_RXComp_RAT", "value"),
            Input("NR_RXComp_band", "value"),
            Input("sld_RXComp_scat", "value"),
        ],
    )
    def update_RXGain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_RXComp, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RXComp, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 RX Mixer Cal =================================
    @callback(Output("NR_RXMixer_band", "value"), Input("NR_RXMixer_RAT", "value"))
    def RXGain_NR(selected_rat):
        return Initialize_band(selected_rat, df_RXMixer)

    @callback(
        [
            Output("NR_RXMixer_band", "options"),
            Output("NR_RXMixer_scatt", "figure"),
            Output("NR_RXMixer_histo", "figure"),
        ],
        [
            Input("NR_RXMixer_RAT", "value"),
            Input("NR_RXMixer_band", "value"),
            Input("sld_RXMixer_scat", "value"),
        ],
    )
    def update_RXGain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_RXMixer, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_RXMixer, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 APT Measuremnt =================================
    @callback(Output("NR_APTMeas_band", "value"), Input("NR_APTMeas_RAT", "value"))
    def APTMeas_NR(selected_rat):
        return Initialize_band(selected_rat, df_APT_Meas)

    @callback(
        [
            Output("NR_APTMeas_band", "options"),
            Output("NR_APTMeas_scatt", "figure"),
            Output("NR_APTMeas_histo", "figure"),
        ],
        [
            Input("NR_APTMeas_RAT", "value"),
            Input("NR_APTMeas_band", "value"),
            Input("sld_APTMeas_scat", "value"),
        ],
    )
    def update_APTMeas(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_APT_Meas, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_APT_Meas, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Psat =================================
    @callback(Output("NR_ETPSat_band", "value"), Input("NR_ETPsat_RAT", "value"))
    def ET_Psat_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Psat)

    @callback(
        [
            Output("NR_ETPSat_band", "options"),
            Output("NR_ET_Psat_scatt", "figure"),
            Output("NR_ET_Psat_histo", "figure"),
        ],
        [
            Input("NR_ETPsat_RAT", "value"),
            Input("NR_ETPSat_band", "value"),
            Input("sld_ET_Psat_scat", "value"),
        ],
    )
    def update_ET_Psat(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_ET_Psat, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Psat, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Pgain =================================
    @callback(Output("NR_ETPgain_band", "value"), Input("NR_ETPgain_RAT", "value"))
    def ET_Pgain_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Pgain)

    @callback(
        [
            Output("NR_ETPgain_band", "options"),
            Output("NR_ET_Pgain_scatt", "figure"),
            Output("NR_ET_Pgain_histo", "figure"),
        ],
        [
            Input("NR_ETPgain_RAT", "value"),
            Input("NR_ETPgain_band", "value"),
            Input("sld_ET_Pgain_scat", "value"),
        ],
    )
    def update_ET_Pgain(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_ET_Pgain, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Pgain, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Power =================================
    @callback(Output("NR_ETPower_band", "value"), Input("NR_ETPower_RAT", "value"))
    def ET_Power_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Power)

    @callback(
        [
            Output("NR_ETPower_band", "options"),
            Output("NR_ET_Power_scatt", "figure"),
            Output("NR_ET_Power_histo", "figure"),
        ],
        [
            Input("NR_ETPower_RAT", "value"),
            Input("NR_ETPower_band", "value"),
            Input("sld_ET_Power_scat", "value"),
        ],
    )
    def update_ET_Power(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_ET_Power, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Power, selected_rat)

        return band_opt, scatt_fig, histo_fig

    # ** ================================= Sub6 ET-SAPT Freq =================================
    @callback(Output("NR_ETFreq_band", "value"), Input("NR_ETFreq_RAT", "value"))
    def ET_Freq_NR(selected_rat):
        return Initialize_band(selected_rat, df_ET_Freq)

    @callback(
        [
            Output("NR_ETFreq_band", "options"),
            Output("NR_ET_Freq_scatt", "figure"),
            Output("NR_ET_Freq_histo", "figure"),
        ],
        [
            Input("NR_ETFreq_RAT", "value"),
            Input("NR_ETFreq_band", "value"),
            Input("sld_ET_Freq_scat", "value"),
        ],
    )
    def update_ET_Freq(selected_rat, selected_band, scatt_range):
        scatt_fig, histo_fig = update_band_and_graph(df_ET_Freq, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_ET_Freq, selected_rat)

        return band_opt, scatt_fig, histo_fig

    dash.register_page(__name__, path="/NR", name="NR_ Sub6", title="NR_ Sub6", layout=layout)

    return layout
