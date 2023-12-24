import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
from LSI_Solution.pages.page_cf import (
    Initialize_dropdowns,
    Generate_section,
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
    layout = html.Div([Generate_section(key, rat, dropdowns, data_frame) for key in dropdown_keys])

    # ** ============================== 3G RX Gain Cal ==============================
    @callback(Output("3g_rx_gain_b", "value"), Input("3g_rx_gain_r", "value"))
    def rx_gain(selected_r):
        return Initialize_band(selected_r, data_frame["rx_gain"])

    @callback(
        [
            Output("3g_rx_gain_b", "options"),
            Output("3g_rx_gain_scatt", "figure"),
            Output("3g_rx_gain_histo", "figure"),
        ],
        [
            Input("3g_rx_gain_r", "value"),
            Input("3g_rx_gain_b", "value"),
            Input("sld_rx_gain_scat", "value"),
            Input("sld_rx_gain_hist", "value"),
        ],
    )
    def update_rx_gain(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["rx_gain"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["rx_gain"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G RX Channel components ==============================
    @callback(Output("3g_rx_comp_b", "value"), Input("3g_rx_comp_r", "value"))
    def rx_comp(selected_r):
        return Initialize_band(selected_r, data_frame["rx_comp"])

    @callback(
        [
            Output("3g_rx_comp_b", "options"),
            Output("3g_rx_comp_scatt", "figure"),
            Output("3g_rx_comp_histo", "figure"),
        ],
        [
            Input("3g_rx_comp_r", "value"),
            Input("3g_rx_comp_b", "value"),
            Input("sld_rx_comp_scat", "value"),
            Input("sld_rx_comp_hist", "value"),
        ],
    )
    def update_rx_comp(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["rx_comp"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["rx_comp"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    # ** ============================== 3G FBRX Gain Cal ==============================
    @callback(Output("3g_fbrx_gm_b", "value"), Input("3g_fbrx_gm_r", "value"))
    def fbrx_gain(selected_r):
        return Initialize_band(selected_r, data_frame["fbrx_gm"])

    @callback(
        [
            Output("3g_fbrx_gm_b", "options"),
            Output("3g_fbrx_gm_scatt", "figure"),
            Output("3g_fbrx_gm_histo", "figure"),
            Output("3g_fbrx_gc_scatt", "figure"),
            Output("3g_fbrx_gc_histo", "figure"),
        ],
        [
            Input("3g_fbrx_gm_r", "value"),
            Input("3g_fbrx_gm_b", "value"),
            Input("sld_fbrx_gm_scat", "value"),
            Input("sld_fbrx_gm_hist", "value"),
        ],
    )
    def update_fbrx_gain(selected_r, selected_b, scatt_range, histo_range):
        scatt_fig1, histo_fig1 = Update_band_and_graph(data_frame["fbrx_gm"], selected_r, selected_b, scatt_range)
        scatt_fig2, histo_fig2 = Update_band_and_graph(data_frame["fbrx_gc"], selected_r, selected_b, None, histo_range)
        band_opt = Band_list(data_frame["fbrx_gm"], selected_r)

        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    # ** ============================== 3G FBRX Freq Cal ==============================
    @callback(Output("3g_fbrx_fm_b", "value"), Input("3g_fbrx_fm_r", "value"))
    def fbrx_freq(selected_r):
        return Initialize_band(selected_r, data_frame["fbrx_fm"])

    @callback(
        [
            Output("3g_fbrx_fm_b", "options"),
            Output("3g_fbrx_fm_scatt", "figure"),
            Output("3g_fbrx_fm_histo", "figure"),
            Output("3g_fbrx_fc_scatt", "figure"),
            Output("3g_fbrx_fc_histo", "figure"),
        ],
        [
            Input("3g_fbrx_fm_r", "value"),
            Input("3g_fbrx_fm_b", "value"),
            Input("sld_fbrx_fm_scat", "value"),
            Input("sld_fbrx_fm_hist", "value"),
        ],
    )
    def update_fbrx_freq(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig1, histogram_fig1 = Update_band_and_graph(
            data_frame["fbrx_fm"], selected_r, selected_b, scatt_range, histo_range
        )
        scatter_fig2, histogram_fig2 = Update_band_and_graph(
            data_frame["fbrx_fc"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["fbrx_fc"], selected_r)

        return band_opt, scatter_fig1, histogram_fig1, scatter_fig2, histogram_fig2

    # ** ============================== 3G FBRX Freq Cal - Channel ==============================
    @callback(Output("3g_fbrx_freq_ch_b", "value"), Input("3g_fbrx_freq_ch_r", "value"))
    def fbrx_freq_Ch(selected_r):
        return Initialize_band(selected_r, data_frame["fbrx_freq_ch"])

    @callback(
        [
            Output("3g_fbrx_freq_ch_b", "options"),
            Output("3g_fbrx_fm_ch_scatt", "figure"),
            Output("3g_fbrx_fm_ch_histo", "figure"),
        ],
        [
            Input("3g_fbrx_freq_ch_r", "value"),
            Input("3g_fbrx_freq_ch_b", "value"),
            Input("sld_fbrx_freq_ch_scat", "value"),
            Input("sld_fbrx_freq_ch_hist", "value"),
        ],
    )
    def update_fbrx_freq_ch(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig1, scatter_fig2 = Update_band_and_graph(
            data_frame["fbrx_freq_ch"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["fbrx_freq_ch"])

        return band_opt, scatter_fig1, scatter_fig2

    # ** ============================== 3G APT Measuremnet ==============================
    @callback(Output("3g_apt_meas_b", "value"), Input("3g_apt_meas_r", "value"))
    def apt_meas(selected_r):
        return Initialize_band(selected_r, data_frame["apt_meas"])

    @callback(
        [
            Output("3g_apt_meas_b", "options"),
            Output("3g_apt_meas_scatt", "figure"),
            Output("3g_apt_meas_histo", "figure"),
        ],
        [
            Input("3g_apt_meas_r", "value"),
            Input("3g_apt_meas_b", "value"),
            Input("sld_apt_meas_scat", "value"),
            Input("sld_apt_meas_hist", "value"),
        ],
    )
    def update_apt_meas(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["apt_meas"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["apt_meas"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G TxP Channel Components ==============================
    @callback(Output("3g_txp_cc_b", "value"), Input("3g_txp_cc_r", "value"))
    def txp_cc(selected_r):
        return Initialize_band(selected_r, data_frame["txp_cc"])

    @callback(
        [
            Output("3g_txp_cc_b", "options"),
            Output("3g_txp_cc_scatt", "figure"),
            Output("3g_txp_cc_histo", "figure"),
        ],
        [
            Input("3g_txp_cc_r", "value"),
            Input("3g_txp_cc_b", "value"),
            Input("sld_txp_cc_scat", "value"),
            Input("sld_txp_cc_hist", "value"),
        ],
    )
    def update_txp_cc(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["txp_cc"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["txp_cc"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Psat ==============================
    @callback(Output("3g_et_psat_b", "value"), Input("3g_et_psat_r", "value"))
    def et_psat(selected_r):
        return Initialize_band(selected_r, data_frame["et_psat"])

    @callback(
        [
            Output("3g_et_psat_b", "options"),
            Output("3g_et_psat_scatt", "figure"),
            Output("3g_et_psat_histo", "figure"),
        ],
        [
            Input("3g_et_psat_r", "value"),
            Input("3g_et_psat_b", "value"),
            Input("sld_et_psat_scat", "value"),
            Input("sld_et_psat_hist", "value"),
        ],
    )
    def update_et_psat(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["et_psat"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["et_psat"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 3G ET Power ==============================
    @callback(Output("3g_et_power_b", "value"), Input("3g_et_power_r", "value"))
    def et_power(selected_r):
        return Initialize_band(selected_r, data_frame["et_power"])

    @callback(
        [
            Output("3g_et_power_b", "options"),
            Output("3g_et_power_scatt", "figure"),
            Output("3g_et_power_histo", "figure"),
        ],
        [
            Input("3g_et_power_r", "value"),
            Input("3g_et_power_b", "value"),
            Input("sld_et_power_scat", "value"),
            Input("sld_et_power_hist", "value"),
        ],
    )
    def update_et_power(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["et_power"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["et_power"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/WCDMA", name="WCDMA", title="WCDMA", layout=layout)

    return layout
