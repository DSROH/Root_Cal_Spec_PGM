import dash
from dash import html, callback, Output, Input
from LSI_Solution.pages.page_cf import Initialize_dropdowns, Generate_layout, Initialize_band, Band_list, Update_band_and_graph


def Initialize_2g(dict_2g, rat):
    dropdown_keys = [
        "rx_gain",
        "rx_ripp",
        "gmsk",
        "gmsk_txl",
        "gmsk_code",
        "epsk",
        "epsk_txl",
        "epsk_code",
    ]
    dropdowns, data_frame = Initialize_dropdowns(dict_2g, rat, dropdown_keys)
    layout = html.Div([Generate_layout(key, rat, dropdowns, data_frame) for key in dropdown_keys])

    # ** ============================== 2G RX Cain cal ==============================
    @callback(Output("2g_rx_gain_b", "value"), Input("2g_rx_gain_r", "value"))
    def rx_gain(selected_r):
        return Initialize_band(selected_r, data_frame["rx_gain"])

    @callback(
        [
            Output("2g_rx_gain_b", "options"),
            Output("2g_rx_gain_scatt", "figure"),
            Output("2g_rx_gain_histo", "figure"),
        ],
        [
            Input("2g_rx_gain_r", "value"),
            Input("2g_rx_gain_b", "value"),
            Input("sld_rx_gain_scat", "value"),
            Input("sld_rx_gain_hist", "value"),
        ],
    )
    def update_rx_gain_2g(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["rx_gain"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["rx_gain"], selected_r)
        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G RX Ripple cal ==============================
    @callback(Output("2g_rx_ripp_b", "value"), Input("2g_rx_ripp_r", "value"))
    def rx_ripp_2g(selected_r):
        return Initialize_band(selected_r, data_frame["rx_ripp"])

    @callback(
        [
            Output("2g_rx_ripp_b", "options"),
            Output("2g_rx_ripp_scatt", "figure"),
            Output("2g_rx_ripp_histo", "figure"),
        ],
        [
            Input("2g_rx_ripp_r", "value"),
            Input("2g_rx_ripp_b", "value"),
            Input("sld_rx_ripp_scat", "value"),
            Input("sld_rx_ripp_hist", "value"),
        ],
    )
    def update_rx_ripp_2g(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["rx_ripp"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["rx_ripp"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX GMSK Index ==============================
    @callback(Output("2g_gmsk_b", "value"), Input("2g_gmsk_r", "value"))
    def gmsk(selected_r):
        return Initialize_band(selected_r, data_frame["gmsk"])

    @callback(
        [
            Output("2g_gmsk_b", "options"),
            Output("2g_gmsk_scatt", "figure"),
            Output("2g_gmsk_histo", "figure"),
        ],
        [
            Input("2g_gmsk_r", "value"),
            Input("2g_gmsk_b", "value"),
            Input("sld_gmsk_scat", "value"),
            Input("sld_gmsk_hist", "value"),
        ],
    )
    def update_gmsk(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["gmsk"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["gmsk"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX GMSK TxL ==============================
    @callback(Output("2g_gmsk_txl_b", "value"), Input("2g_gmsk_txl_r", "value"))
    def gmsk_txl(selected_r):
        return Initialize_band(selected_r, data_frame["gmsk_txl"])

    @callback(
        [
            Output("2g_gmsk_txl_b", "options"),
            Output("2g_gmsk_txl_scatt", "figure"),
            Output("2g_gmsk_txl_histo", "figure"),
        ],
        [
            Input("2g_gmsk_txl_r", "value"),
            Input("2g_gmsk_txl_b", "value"),
            Input("sld_gmsk_txl_scat", "value"),
            Input("sld_gmsk_txl_hist", "value"),
        ],
    )
    def update_gmsk_txl(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["gmsk_txl"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["gmsk_txl"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX GMSK Code ==============================
    @callback(Output("2g_gmsk_code_b", "value"), Input("2g_gmsk_code_r", "value"))
    def gmsk_code(selected_r):
        return Initialize_band(selected_r, data_frame["gmsk_code"])

    @callback(
        [
            Output("2g_gmsk_code_b", "options"),
            Output("2g_gmsk_code_scatt", "figure"),
            Output("2g_gmsk_code_histo", "figure"),
        ],
        [
            Input("2g_gmsk_code_r", "value"),
            Input("2g_gmsk_code_b", "value"),
            Input("sld_gmsk_code_scat", "value"),
            Input("sld_gmsk_code_hist", "value"),
        ],
    )
    def update_gmsk_code(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["gmsk_code"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["gmsk_code"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX EPSK Index ==============================
    @callback(Output("2g_epsk_b", "value"), Input("2g_epsk_r", "value"))
    def epsk(selected_r):
        return Initialize_band(selected_r, data_frame["epsk"])

    @callback(
        [
            Output("2g_epsk_b", "options"),
            Output("2g_epsk_scatt", "figure"),
            Output("2g_epsk_histo", "figure"),
        ],
        [
            Input("2g_epsk_r", "value"),
            Input("2g_epsk_b", "value"),
            Input("sld_epsk_scat", "value"),
            Input("sld_epsk_hist", "value"),
        ],
    )
    def update_epsk(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(data_frame["epsk"], selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(data_frame["epsk"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX EPSK TxL ==============================
    @callback(Output("2g_epsk_txl_b", "value"), Input("2g_epsk_txl_r", "value"))
    def epsk_txl(selected_r):
        return Initialize_band(selected_r, data_frame["epsk_txl"])

    @callback(
        [
            Output("2g_epsk_txl_b", "options"),
            Output("2g_epsk_txl_scatt", "figure"),
            Output("2g_epsk_txl_histo", "figure"),
        ],
        [
            Input("2g_epsk_txl_r", "value"),
            Input("2g_epsk_txl_b", "value"),
            Input("sld_epsk_txl_scat", "value"),
            Input("sld_epsk_txl_hist", "value"),
        ],
    )
    def update_epsk_txl(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["epsk_txl"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["epsk_txl"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ============================== 2G TX epsk Code ==============================
    @callback(Output("2g_epsk_code_b", "value"), Input("2g_epsk_code_r", "value"))
    def epsk_code(selected_r):
        return Initialize_band(selected_r, data_frame["epsk_code"])

    @callback(
        [
            Output("2g_epsk_code_b", "options"),
            Output("2g_epsk_code_scatt", "figure"),
            Output("2g_epsk_code_histo", "figure"),
        ],
        [
            Input("2g_epsk_code_r", "value"),
            Input("2g_epsk_code_b", "value"),
            Input("sld_epsk_code_scat", "value"),
            Input("sld_epsk_code_hist", "value"),
        ],
    )
    def update_epsk_code(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(
            data_frame["epsk_code"], selected_r, selected_b, scatt_range, histo_range
        )
        band_opt = Band_list(data_frame["epsk_code"], selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/GSM", name="GSM", title="GSM", layout=layout)

    return layout
