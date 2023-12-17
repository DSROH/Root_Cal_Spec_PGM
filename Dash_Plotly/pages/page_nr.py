import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
from pages.page_CF import create_dropdown, create_range_slider, Initialize_band, update_band_and_graph


def initialize_nr(df_fbrxgm_NR, df_fbrxgc_NR, df_fbrxfm_NR, df_fbrxfc_NR):
    band_opt = [{"label": "", "value": ""}]

    drop_NRFBRXGain_rat = create_dropdown("NRFBRXGain_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_NRFBRXFreq_rat = create_dropdown("NRFBRXFreq_RAT", "n", [{"label": "NR", "value": "n"}])

    drop_NRFBRXGain_band = create_dropdown("NRFBRXGain_band", "", band_opt)
    drop_NRFBRXFreq_band = create_dropdown("NRFBRXFreq_band", "", band_opt)

    layout = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 FBRX Gain Cal", className="display-7")),
                    dbc.Col(drop_NRFBRXGain_rat),
                    dbc.Col(drop_NRFBRXGain_band),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NRFBRX_GM_grp_scatt")),
                    dbc.Col(dcc.Graph(id="NRFBRX_GM_grp_histo")),
                    dbc.Col(dcc.Graph(id="NRFBRX_GC_grp_scatt")),
                    dbc.Col(dcc.Graph(id="NRFBRX_GC_grp_histo")),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(create_range_slider("sld_NRFBRX_GM_scat", df_fbrxgm_NR, use_min_max=False)),
                    dbc.Col(create_range_slider("sld_NRFBRX_GC_scat", df_fbrxgc_NR, use_min_max=False)),
                ],
            ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(html.H2("Sub6 FBRX Freq Cal", className="display-7")),
                    dbc.Col(drop_NRFBRXFreq_rat),
                    dbc.Col(drop_NRFBRXFreq_band),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="NRFBRX_FM_grp_scatt")),
                    dbc.Col(dcc.Graph(id="NRFBRX_FM_grp_histo")),
                    dbc.Col(dcc.Graph(id="NRFBRX_FC_grp_scatt")),
                    dbc.Col(dcc.Graph(id="NRFBRX_FC_grp_histo")),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(create_range_slider("sld_NRFBRX_FM_scat", df_fbrxfm_NR, use_min_max=False)),
                    dbc.Col(create_range_slider("sld_NRFBRX_FC_scat", df_fbrxfc_NR, use_min_max=False)),
                ],
            ),
        ]
    )

    @callback(Output("NRFBRXGain_band", "value"), Input("NRFBRXGain_RAT", "value"))
    def FBRXGain_NR(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxgm_NR)

    @callback(
        [
            Output("NRFBRXGain_band", "options"),
            Output("NRFBRX_GM_grp_scatt", "figure"),
            Output("NRFBRX_GM_grp_histo", "figure"),
            Output("NRFBRX_GC_grp_scatt", "figure"),
            Output("NRFBRX_GC_grp_histo", "figure"),
        ],
        [
            Input("NRFBRXGain_RAT", "value"),
            Input("NRFBRXGain_band", "value"),
            Input("sld_NRFBRX_GM_scat", "value"),
            Input("sld_NRFBRX_FC_scat", "value"),
        ],
    )
    def update_FBRXGain(Sel_rat, Sel_band, scatt_range1, scatt_range2):
        band_opt, scatter_fig1, histogram_fig1 = update_band_and_graph(df_fbrxgm_NR, Sel_rat, Sel_band, scatt_range1)
        band_opt, scatter_fig2, histogram_fig2 = update_band_and_graph(df_fbrxgc_NR, Sel_rat, Sel_band, scatt_range2)
        return band_opt, scatter_fig1, histogram_fig1, scatter_fig2, histogram_fig2

    @callback(Output("NRFBRXFreq_band", "value"), Input("NRFBRXFreq_RAT", "value"))
    def FBRXFreq_NR_band(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxfm_NR)

    @callback(
        [
            Output("NRFBRXFreq_band", "options"),
            Output("NRFBRX_FM_grp_scatt", "figure"),
            Output("NRFBRX_FM_grp_histo", "figure"),
            Output("NRFBRX_FC_grp_scatt", "figure"),
            Output("NRFBRX_FC_grp_histo", "figure"),
        ],
        [
            Input("NRFBRXFreq_RAT", "value"),
            Input("NRFBRXFreq_band", "value"),
            Input("sld_NRFBRX_FM_scat", "value"),
            Input("sld_NRFBRX_FC_scat", "value"),
        ],
    )
    def update_NRFBRXFreq(Sel_rat, Sel_band, scatt_range1, scatt_range2):
        band_opt, scatt_fig1, histo_fig1 = update_band_and_graph(df_fbrxfm_NR, Sel_rat, Sel_band, scatt_range1)
        band_opt, scatt_fig2, histo_fig2 = update_band_and_graph(df_fbrxfc_NR, Sel_rat, Sel_band, scatt_range2)
        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    dash.register_page(
        __name__,
        path="/NR_Sub6",  # represents the url text
        name="NR Sub6",  # name of page, commonly used as name of link
        title="NR Sub6",  # epresents the title of browser's tab
        description="Description of Sub6 Page",
        layout=layout,  # 초기화한 레이아웃 등록
    )

    return layout  # 이 레이아웃을 반환하여 페이지를 초기화합니다.
