import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import (
    Initialize_dropdowns,
    Create_range_slider,
    Initialize_band,
    Band_list,
    Update_band_and_graph,
)

def Initialize_3g(dict_3g, rat):
    dropdown_keys = [
        "rx_gain",
        "rx_comp",
        "fbrx_gm",
        "fbrx_gc",
        "fbrx_fm",
        "fbrx_fm_ch",
        "apt_meas",
        "txp_cc",
        "et_psat",
        "et_power",
    ]

    dropdowns, data_frame = Initialize_dropdowns(dict_3g, rat, dropdown_keys)
    layout = html.Div(
        [
            # ** ============================== 3G RX Gain Cal ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G RX Gain Cal", className="display-7"), width="auto"),
                    dbc.Col(dropdowns["rx_gain_r"], width=1),
                    dbc.Col(dropdowns["rx_gain_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="rx_gain_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="rx_gain_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_rx_gain_scat", data_frame["rx_gain"], use_min_max=False),
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
                    dbc.Col(dropdowns["rx_comp_r"], width=1),
                    dbc.Col(dropdowns["rx_comp_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="rx_comp_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="rx_comp_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_rx_comp_scat", data_frame["rx_comp"], use_min_max=False),
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
                    dbc.Col(dropdowns["fbrx_gm_r"], width=1),
                    dbc.Col(dropdowns["fbrx_gm_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="fbrx_gm_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="fbrx_gm_grp_histo"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="fbrx_gc_grp_scatt"), width={"size": 3, "offset": 0}),
                    dbc.Col(dcc.Graph(id="fbrx_gc_grp_histo"), width={"size": 3, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_fbrx_gm_scat", data_frame["fbrx_gm"], use_min_max=False),
                        width={"size": 3, "offset": 0},
                    ),
                    dbc.Col(
                        Create_range_slider("sld_fbrx_gc_scat", data_frame["fbrx_gm"], use_min_max=False),
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
                    dbc.Col(dropdowns["fbrx_fm_r"], width=1),
                    dbc.Col(dropdowns["fbrx_fm_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="fbrx_fm_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="fbrx_fm_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_fbrx_fm_scat", data_frame["fbrx_fm"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G FBRX Freq Cal - Channel ==============================
            # dbc.Row(
            #     [
            #         dbc.Col(html.H2("3G FBRX Freq Cal", className="display-7"), width="auto"),
            #         dbc.Col(dropdowns["fbrx_fm_ch_r"], width=1),
            #         dbc.Col(dropdowns["fbrx_fm_ch_b"], width=1),
            #     ],
            #     align="center",
            # ),
            # html.Br(),
            # dbc.Row(
            #     [
            #         dbc.Col(dcc.Graph(id="fbrx_fm_ch_grp_scatt"), width={"size": 6, "offset": 0}),
            #         dbc.Col(dcc.Graph(id="fbrx_fm_ch_grp_histo"), width={"size": 6, "offset": 0}),
            #     ],
            #     align="center",
            # ),
            # dbc.Row(
            #     [
            #         dbc.Col(
            #             Create_range_slider("sld_fbrx_fm_ch_scat", data_frame["fbrx_fm_ch"], use_min_max=False),
            #             width={"size": 6, "offset": 0},
            #         )
            #     ],
            #     align="center",
            # ),
            # html.Hr(),
            # ** ============================== 3G APT Measurement ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G APT Measuremnet", className="display-7"), width="auto"),
                    dbc.Col(dropdowns["apt_meas_r"], width=1),
                    dbc.Col(dropdowns["apt_meas_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="apt_meas_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="apt_meas_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_apt_meas_scat", data_frame["apt_meas"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
            # ** ============================== 3G TX Channel Components ==============================
            dbc.Row(
                [
                    dbc.Col(html.H2("3G TxP Channel Components", className="display-7"), width="auto"),
                    dbc.Col(dropdowns["txp_cc_r"], width=1),
                    dbc.Col(dropdowns["txp_cc_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="txp_cc_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="txp_cc_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_txp_cc_scat", data_frame["txp_cc"], use_min_max=False),
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
                    dbc.Col(dropdowns["et_psat_r"], width=1),
                    dbc.Col(dropdowns["et_psat_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="et_psat_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="et_psat_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_et_psat_scat", data_frame["et_psat"], use_min_max=False),
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
                    dbc.Col(dropdowns["et_power_r"], width=1),
                    dbc.Col(dropdowns["et_power_b"], width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="et_power_grp_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="et_power_grp_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        Create_range_slider("sld_et_power_scat", data_frame["et_power"], use_min_max=False),
                        width={"size": 6, "offset": 0},
                    )
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ** ============================== 3G RX Gain Cal ==============================
    @callback(Output("3g_rx_gain_b", "value"), Input("3g_rx_gain_r", "value"))
    def RX_Gain(selected_r):
        return Initialize_band(selected_r, data_frame["rx_gain"])

    @callback(
        [
            Output("3g_rx_gain_b", "options"),
            Output("rx_gain_grp_scatt", "figure"),
            Output("rx_gain_grp_histo", "figure"),
        ],
        [Input("3g_rx_gain_r", "value"), Input("3g_rx_gain_b", "value"), Input("sld_rx_gain_scat", "value")],
    )
    def update_RX_Gain(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["rx_gain"], selected_r, selected_b, scatt_range)
        band_opt = Band_list(data_frame["rx_gain"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G RX Channel components ==============================
    @callback(Output("3g_rx_comp_b", "value"), Input("3g_rx_comp_r", "value"))
    def RX_Comp(selected_r):
        return Initialize_band(selected_r, data_frame["rx_comp"])

    @callback(
        [
            Output("3g_rx_comp_b", "options"),
            Output("rx_comp_grp_scatt", "figure"),
            Output("rx_comp_grp_histo", "figure"),
        ],
        [Input("3g_rx_comp_r", "value"), Input("3g_rx_comp_b", "value"), Input("sld_rx_comp_scat", "value")],
    )
    def update_RX_Comp(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["rx_comp"], selected_r, selected_b, scatt_range)
        band_opt = Band_list(data_frame["rx_comp"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    # ** ============================== 3G FBRX Gain Cal ==============================
    @callback(Output("3g_fbrx_gm_b", "value"), Input("3g_fbrx_gm_r", "value"))
    def FBRX_Gain(selected_r):
        return Initialize_band(selected_r, data_frame["fbrx_gm"])

    @callback(
        [
            Output("3g_fbrx_gm_b", "options"),
            Output("fbrx_gm_grp_scatt", "figure"),
            Output("fbrx_gm_grp_histo", "figure"),
            Output("fbrx_gc_grp_scatt", "figure"),
            Output("fbrx_gc_grp_histo", "figure"),
        ],
        [
            Input("3g_fbrx_gm_r", "value"),
            Input("3g_fbrx_gm_b", "value"),
            Input("sld_fbrx_gm_scat", "value"),
            Input("sld_fbrx_gc_scat", "value"),
        ],
    )
    def update_FBRX_Gain(selected_r, selected_b, scatt_range1, scatt_range2):
        scatt_fig1, histo_fig1 = Update_band_and_graph(data_frame["fbrx_gm"], selected_r, selected_b, scatt_range1)
        scatt_fig2, histo_fig2 = Update_band_and_graph(data_frame["fbrx_gc"], selected_r, selected_b, scatt_range2)
        band_opt = Band_list(data_frame["fbrx_gm"], selected_r)

        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ** ============================== 3G FBRX Freq Cal ==============================
    @callback(Output("3g_fbrx_fm_b", "value"), Input("3g_fbrx_fm_r", "value"))
    def FBRX_Freq(selected_r):
        return Initialize_band(selected_r, data_frame["fbrx_fm"])

    @callback(
        [
            Output("3g_fbrx_fm_b", "options"),
            Output("fbrx_fm_grp_scatt", "figure"),
            Output("fbrx_fm_grp_histo", "figure"),
        ],
        [Input("3g_fbrx_fm_r", "value"), Input("3g_fbrx_fm_b", "value"), Input("sld_fbrx_fm_scat", "value")],
    )
    def update_FBRX_Freq(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["fbrx_fm"], selected_r, selected_b, scatt_range)
        band_opt = Band_list(data_frame["fbrx_fm"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G FBRX Freq Cal - Channel ==============================
    # @callback(Output("fbrx_freq_ch_b", "value"), Input("fbrx_freq_ch_r", "value"))
    # def FBRX_Freq_Ch(selected_r):
    #     return Initialize_band(selected_r, data_frame["fbrx_freq_ch"])

    # @callback(
    #     [
    #         Output("fbrx_freq_ch_b", "options"),
    #         Output("fbrx_fm_CH_1", "figure"),
    #         Output("fbrx_fm_CH_2", "figure"),
    #     ],
    #     [Input("fbrx_freq_ch_r", "value"), Input("fbrx_freq_ch_b", "value")],
    # )
    # def update_FBRX_Freq_ch(selected_r, selected_b):
    #     scatter_fig1, scatter_fig2 = Update_band_and_graph(data_frame["fbrx_freq_ch"], selected_r, selected_b, None)
    #     band_opt = Band_list(data_frame["fbrx_freq_ch"])

    #     return band_opt, scatter_fig1, scatter_fig2

    # ** ============================== 3G APT Measuremnet ==============================
    @callback(Output("3g_apt_meas_b", "value"), Input("3g_apt_meas_r", "value"))
    def apt_meas(selected_r):
        return Initialize_band(selected_r, data_frame["apt_meas"])

    @callback(
        [
            Output("3g_apt_meas_b", "options"),
            Output("apt_meas_grp_scatt", "figure"),
            Output("apt_meas_grp_histo", "figure"),
        ],
        [Input("3g_apt_meas_r", "value"), Input("3g_apt_meas_b", "value"), Input("sld_apt_meas_scat", "value")],
    )
    def update_apt_meas(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["apt_meas"], selected_r, selected_b, scatt_range)
        band_opt = Band_list(data_frame["apt_meas"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G TxP Channel Components ==============================
    @callback(Output("3g_txp_cc_b", "value"), Input("3g_txp_cc_r", "value"))
    def txp_cc(selected_r):
        return Initialize_band(selected_r, data_frame["txp_cc"])

    @callback(
        [
            Output("3g_txp_cc_b", "options"),
            Output("txp_cc_grp_scatt", "figure"),
            Output("txp_cc_grp_histo", "figure"),
        ],
        [Input("3g_txp_cc_r", "value"), Input("3g_txp_cc_b", "value"), Input("sld_txp_cc_scat", "value")],
    )
    def update_txp_cc(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["txp_cc"], selected_r, selected_b, scatt_range)
        band_opt = Band_list(data_frame["txp_cc"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Psat ==============================
    @callback(Output("3g_et_psat_b", "value"), Input("3g_et_psat_r", "value"))
    def ET_Psat(selected_r):
        return Initialize_band(selected_r, data_frame["et_psat"])

    @callback(
        [
            Output("3g_et_psat_b", "options"),
            Output("et_psat_grp_scatt", "figure"),
            Output("et_psat_grp_histo", "figure"),
        ],
        [Input("3g_et_psat_r", "value"), Input("3g_et_psat_b", "value"), Input("sld_et_psat_scat", "value")],
    )
    def update_ET_Psat(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["et_psat"], selected_r, selected_b, scatt_range)
        band_opt = Band_list(data_frame["et_psat"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Power ==============================
    @callback(Output("3g_et_power_b", "value"), Input("3g_et_power_r", "value"))
    def ET_Power(selected_r):
        return Initialize_band(selected_r, data_frame["et_power"])

    @callback(
        [
            Output("3g_et_power_b", "options"),
            Output("et_power_grp_scatt", "figure"),
            Output("et_power_grp_histo", "figure"),
        ],
        [Input("3g_et_power_r", "value"), Input("3g_et_power_b", "value"), Input("sld_et_power_scat", "value")],
    )
    def update_ET_Power(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["et_power"], selected_r, selected_b, scatt_range)
        band_opt = Band_list(data_frame["et_power"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    return layout
