import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import create_dropdown, create_range_slider, Initialize_band, update_band_and_graph


def initialize_nr(dict_nr):
    df_RXGain_sub6 = dict_nr["RX_Gain"]
    df_RXRSRP_sub6 = dict_nr["RX_RSRP"]
    df_RXComp_sub6 = dict_nr["RX_Comp"]
    df_RXMixer_sub6 = dict_nr["RX_Mix"]
    df_fbrxgm_NR = dict_nr["FBRX_GM"]
    df_fbrxgc_NR = dict_nr["FBRX_GC"]
    df_fbrxfm_NR = dict_nr["FBRX_FM"]
    df_fbrxfc_NR = dict_nr["FBRX_FC"]
    df_APT_Meas_sub6 = dict_nr["APT_Meas"]
    df_ETSAPT_Psat = dict_nr["ET_Psat"]
    df_ETSAPT_Pgain = dict_nr["ET_Pgain"]
    df_ETSAPT_Power = dict_nr["ET_Power"]
    df_ETSAPT_Freq = dict_nr["ET_Freq"]

    band_opt = [{"label": "", "value": ""}]

    drop_NRFBRXGain_rat = create_dropdown("NR_FBRXGain_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_NRFBRXFreq_rat = create_dropdown("NR_FBRXFreq_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_NRRXGain_rat = create_dropdown("NR_RXGain_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_NRRXRSRP_rat = create_dropdown("NR_RXRSRP_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_NRRXComp_rat = create_dropdown("NR_RXComp_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_NRRXMixer_rat = create_dropdown("NR_RXMixer_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_NRAPTMeas_rat = create_dropdown("NR_APTMeas_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ETSAPT_Psat_rat = create_dropdown("NR_ETPsat_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ETSAPT_Pgain_rat = create_dropdown("NR_ETPgain_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ETSAPT_Power_rat = create_dropdown("NR_ETPower_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_ETSAPT_Freq_rat = create_dropdown("NR_ETFreq_RAT", "n", [{"label": "NR", "value": "n"}])

    drop_NRFBRXGain_band = create_dropdown("NR_FBRXGain_band", "", band_opt)
    drop_NRFBRXFreq_band = create_dropdown("NR_FBRXFreq_band", "", band_opt)
    drop_NRRXGain_band = create_dropdown("NR_RXGain_band", "", band_opt)
    drop_NRRXRSRP_band = create_dropdown("NR_RXRSRP_band", "", band_opt)
    drop_NRRXComp_band = create_dropdown("NR_RXComp_band", "", band_opt)
    drop_NRRXMixer_band = create_dropdown("NR_RXMixer_band", "", band_opt)
    drop_NRAPTMeas_band = create_dropdown("NR_APTMeas_band", "", band_opt)
    drop_ETSAPT_Psat_band = create_dropdown("NR_ETPSat_band", "", band_opt)
    drop_ETSAPT_Pgain_band = create_dropdown("NR_ETPgain_band", "", band_opt)
    drop_ETSAPT_Power_band = create_dropdown("NR_ETPower_band", "", band_opt)
    drop_ETSAPT_Freq_band = create_dropdown("NR_ETFreq_band", "", band_opt)

    layout = html.Div(
        [
            # ! Sub6 FBRX Gain Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 FBRX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_NRFBRXGain_rat, width=1),
                    dbc.Col(drop_NRFBRXGain_band, width=1),
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
                        create_range_slider("sld_NRFBRX_GM_scat", df_fbrxgm_NR, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        create_range_slider("sld_NRFBRX_GC_scat", df_fbrxgc_NR, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 FBRX Freq Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 FBRX Freq Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_NRFBRXFreq_rat, width=1),
                    dbc.Col(drop_NRFBRXFreq_band, width=1),
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
                        create_range_slider("sld_NRFBRX_FM_scat", df_fbrxfm_NR, use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        create_range_slider("sld_NRFBRX_FC_scat", df_fbrxfc_NR, use_min_max=False),
                        width={"size": 3, "offset": 3},
                    ),
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 RX Gain Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_NRRXGain_rat, width=1),
                    dbc.Col(drop_NRRXGain_band, width=1),
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
                        create_range_slider("sld_NRRXGain_scat", df_RXGain_sub6, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 RX RSRP Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX RSRP Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_NRRXRSRP_rat, width=1),
                    dbc.Col(drop_NRRXRSRP_band, width=1),
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
                        create_range_slider("sld_NRRXRSRP_scat", df_RXRSRP_sub6, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 RX Freq Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX Freq Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_NRRXComp_rat, width=1),
                    dbc.Col(drop_NRRXComp_band, width=1),
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
                        create_range_slider("sld_NRRXComp_scat", df_RXComp_sub6, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 RX Mixer Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 RX Mixer Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_NRRXMixer_rat, width=1),
                    dbc.Col(drop_NRRXMixer_band, width=1),
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
                        create_range_slider("sld_NRRXMixer_scat", df_RXComp_sub6, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 APT Measuremnt
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 APT Measurement", className="display-7"), width="auto"),
                    dbc.Col(drop_NRAPTMeas_rat, width=1),
                    dbc.Col(drop_NRAPTMeas_band, width=1),
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
                        create_range_slider("sld_APTMeas_scat", df_APT_Meas_sub6, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 ETSAPT Psat
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Psat", className="display-7"), width="auto"),
                    dbc.Col(drop_ETSAPT_Psat_rat, width=1),
                    dbc.Col(drop_ETSAPT_Psat_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Psat_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Psat_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_ETSAPT_Psat_scat", df_ETSAPT_Psat, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 ETSAPT Pgain
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Pgain", className="display-7"), width="auto"),
                    dbc.Col(drop_ETSAPT_Pgain_rat, width=1),
                    dbc.Col(drop_ETSAPT_Pgain_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Pgain_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Pgain_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_ETSAPT_Pgain_scat", df_ETSAPT_Pgain, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 ETSAPT Power
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Power", className="display-7"), width="auto"),
                    dbc.Col(drop_ETSAPT_Power_rat, width=1),
                    dbc.Col(drop_ETSAPT_Power_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Power_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Power_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_ETSAPT_Power_scat", df_ETSAPT_Power, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ! Sub6 ETSAPT Freq
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 ET-SAPT Freq", className="display-7"), width="auto"),
                    dbc.Col(drop_ETSAPT_Freq_rat, width=1),
                    dbc.Col(drop_ETSAPT_Freq_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Freq_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="NR_ETSAPT_Freq_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        create_range_slider("sld_ETSAPT_Freq_scat", df_ETSAPT_Freq, use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ! Sub6 FBRX Gain Cal
    @callback(Output("NR_FBRXGain_band", "value"), Input("NR_FBRXGain_RAT", "value"))
    def FBRXGain_NR(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxgm_NR)

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
            Input("sld_NRFBRX_GM_scat", "value"),
            Input("sld_NRFBRX_FC_scat", "value"),
        ],
    )
    def update_FBRXGain(Sel_rat, Sel_band, scatt_range1, scatt_range2):
        band_opt, scatter_fig1, histogram_fig1 = update_band_and_graph(df_fbrxgm_NR, Sel_rat, Sel_band, scatt_range1)
        band_opt, scatter_fig2, histogram_fig2 = update_band_and_graph(df_fbrxgc_NR, Sel_rat, Sel_band, scatt_range2)
        return band_opt, scatter_fig1, histogram_fig1, scatter_fig2, histogram_fig2

    # ! Sub6 FBRX Freq Cal
    @callback(Output("NR_FBRXFreq_band", "value"), Input("NR_FBRXFreq_RAT", "value"))
    def FBRXFreq_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxfm_NR)

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
            Input("sld_NRFBRX_FM_scat", "value"),
            Input("sld_NRFBRX_FC_scat", "value"),
        ],
    )
    def update_NRFBRXFreq(Sel_rat, Sel_band, scatt_range1, scatt_range2):
        band_opt, scatt_fig1, histo_fig1 = update_band_and_graph(df_fbrxfm_NR, Sel_rat, Sel_band, scatt_range1)
        band_opt, scatt_fig2, histo_fig2 = update_band_and_graph(df_fbrxfc_NR, Sel_rat, Sel_band, scatt_range2)
        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ! Sub6 RX Gain Cal
    @callback(Output("NR_RXGain_band", "value"), Input("NR_RXGain_RAT", "value"))
    def RXGain_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_RXGain_sub6)

    @callback(
        [
            Output("NR_RXGain_band", "options"),
            Output("NR_RXGain_scatt", "figure"),
            Output("NR_RXGain_histo", "figure"),
        ],
        [
            Input("NR_RXGain_RAT", "value"),
            Input("NR_RXGain_band", "value"),
            Input("sld_NRRXGain_scat", "value"),
        ],
    )
    def update_NRRXGain(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_RXGain_sub6, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 RX RSRP Cal
    @callback(Output("NR_RXRSRP_band", "value"), Input("NR_RXRSRP_RAT", "value"))
    def RXGain_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_RXRSRP_sub6)

    @callback(
        [
            Output("NR_RXRSRP_band", "options"),
            Output("NR_RXRSRP_scatt", "figure"),
            Output("NR_RXRSRP_histo", "figure"),
        ],
        [
            Input("NR_RXRSRP_RAT", "value"),
            Input("NR_RXRSRP_band", "value"),
            Input("sld_NRRXRSRP_scat", "value"),
        ],
    )
    def update_NRRXGain(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_RXRSRP_sub6, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 RX Freq Cal
    @callback(Output("NR_RXComp_band", "value"), Input("NR_RXComp_RAT", "value"))
    def RXGain_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_RXComp_sub6)

    @callback(
        [
            Output("NR_RXComp_band", "options"),
            Output("NR_RXComp_scatt", "figure"),
            Output("NR_RXComp_histo", "figure"),
        ],
        [
            Input("NR_RXComp_RAT", "value"),
            Input("NR_RXComp_band", "value"),
            Input("sld_NRRXComp_scat", "value"),
        ],
    )
    def update_NRRXGain(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_RXComp_sub6, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 RX Mixer Cal
    @callback(Output("NR_RXMixer_band", "value"), Input("NR_RXMixer_RAT", "value"))
    def RXGain_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_RXMixer_sub6)

    @callback(
        [
            Output("NR_RXMixer_band", "options"),
            Output("NR_RXMixer_scatt", "figure"),
            Output("NR_RXMixer_histo", "figure"),
        ],
        [
            Input("NR_RXMixer_RAT", "value"),
            Input("NR_RXMixer_band", "value"),
            Input("sld_NRRXMixer_scat", "value"),
        ],
    )
    def update_NRRXGain(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_RXMixer_sub6, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 APT Measuremnt
    @callback(Output("NR_APTMeas_band", "value"), Input("NR_APTMeas_RAT", "value"))
    def APTMeas_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_APT_Meas_sub6)

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
    def update_NRAPTMeas(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_APT_Meas_sub6, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 ET-SAPT Psat
    @callback(Output("NR_ETPSat_band", "value"), Input("NR_ETPsat_RAT", "value"))
    def ETSAPT_Psat_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_ETSAPT_Psat)

    @callback(
        [
            Output("NR_ETPSat_band", "options"),
            Output("NR_ETSAPT_Psat_scatt", "figure"),
            Output("NR_ETSAPT_Psat_histo", "figure"),
        ],
        [
            Input("NR_ETPsat_RAT", "value"),
            Input("NR_ETPSat_band", "value"),
            Input("sld_ETSAPT_Psat_scat", "value"),
        ],
    )
    def update_NRETSAPT_Psat(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_ETSAPT_Psat, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 ET-SAPT Pgain
    @callback(Output("NR_ETPgain_band", "value"), Input("NR_ETPgain_RAT", "value"))
    def ETSAPT_Pgain_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_ETSAPT_Pgain)

    @callback(
        [
            Output("NR_ETPgain_band", "options"),
            Output("NR_ETSAPT_Pgain_scatt", "figure"),
            Output("NR_ETSAPT_Pgain_histo", "figure"),
        ],
        [
            Input("NR_ETPgain_RAT", "value"),
            Input("NR_ETPgain_band", "value"),
            Input("sld_ETSAPT_Pgain_scat", "value"),
        ],
    )
    def update_NRETSAPT_Pgain(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_ETSAPT_Pgain, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 ET-SAPT Power
    @callback(Output("NR_ETPower_band", "value"), Input("NR_ETPower_RAT", "value"))
    def ETSAPT_Power_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_ETSAPT_Power)

    @callback(
        [
            Output("NR_ETPower_RAT", "options"),
            Output("NR_ETSAPT_Power_scatt", "figure"),
            Output("NR_ETSAPT_Power_histo", "figure"),
        ],
        [
            Input("NR_ETPower_RAT", "value"),
            Input("NR_ETPower_band", "value"),
            Input("sld_ETSAPT_Power_scat", "value"),
        ],
    )
    def update_NRETSAPT_Power(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_ETSAPT_Power, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    # ! Sub6 ET-SAPT Freq
    @callback(Output("NR_ETFreq_band", "value"), Input("NR_ETFreq_RAT", "value"))
    def ETSAPT_Freq_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_ETSAPT_Freq)

    @callback(
        [
            Output("NR_ETFreq_band", "options"),
            Output("NR_ETSAPT_Freq_scatt", "figure"),
            Output("NR_ETSAPT_Freq_histo", "figure"),
        ],
        [
            Input("NR_ETFreq_RAT", "value"),
            Input("NR_ETFreq_band", "value"),
            Input("sld_ETSAPT_Freq_scat", "value"),
        ],
    )
    def update_NRETSAPT_Freq(Sel_rat, Sel_band, scatt_range):
        band_opt, scatt_fig, histo_fig = update_band_and_graph(df_ETSAPT_Freq, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatt_fig, histo_fig

    dash.register_page(__name__, path="/NR_Sub6", name="NR_ Sub6", title="NR_ Sub6", layout=layout)

    return layout
