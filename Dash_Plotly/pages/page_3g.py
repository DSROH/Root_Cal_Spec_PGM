import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
from pages.page_CF import create_dropdown, create_range_slider, Initialize_band, update_band_and_graph


def initialize_3g(df_3GTXCP, df_fbrxgm_3G, df_fbrxgc_3G, df_fbrxfm_3G):
    band_opt = [{"label": "", "value": ""}]

    drop_3GTXCP_rat = create_dropdown("3GTXCP_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_3GFBRXGain_rat = create_dropdown("3GFBRXGain_RAT", "B", [{"label": "3G", "value": "B"}])
    drop_3GFBRXFreq_rat = create_dropdown("3GFBRXFreq_RAT", "B", [{"label": "3G", "value": "B"}])

    drop_3GTXCP_band = create_dropdown("3GTXCP_band", "", band_opt)
    drop_3GFBRXGain_band = create_dropdown("3GFBRXGain_band", "", band_opt)
    drop_3GFBRXFreq_band = create_dropdown("3GFBRXFreq_band", "", band_opt)

    layout = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.H2("3G TX Channel Components", className="display-7")),
                    dbc.Col(drop_3GTXCP_rat, width=4),
                    dbc.Col(drop_3GTXCP_band, width=4),
                ],
            ),
            html.Br(),
            dbc.Row([dbc.Col(dcc.Graph(id="3GTXCP_grp_scatt")), dbc.Col(dcc.Graph(id="3GTXCP_grp_histo"))]),
            dbc.Row([dbc.Col(create_range_slider("sld_3GTXCP_scat", df_3GTXCP, use_min_max=False))]),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(html.H2("3G FBRX Gain Cal", className="display-7")),
                    dbc.Col(drop_3GFBRXGain_rat, width=4),
                    dbc.Col(drop_3GFBRXGain_band, width=4),
                ],
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="3GFBRX_GM_grp_scatt")),
                    dbc.Col(dcc.Graph(id="3GFBRX_GM_grp_histo")),
                    dbc.Col(dcc.Graph(id="3GFBRX_GC_grp_scatt")),
                    dbc.Col(dcc.Graph(id="3GFBRX_GC_grp_histo")),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(create_range_slider("sld_3GFBRX_GM_scat", df_fbrxgm_3G, use_min_max=False)),
                    dbc.Col(create_range_slider("sld_3GFBRX_GC_scat", df_fbrxgc_3G, use_min_max=False)),
                ],
            ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(html.H2("3G FBRX Gain Cal", className="display-7")),
                    dbc.Col(drop_3GFBRXFreq_rat, width=4),
                    dbc.Col(drop_3GFBRXFreq_band, width=4),
                ],
            ),
            html.Br(),
            dbc.Row([dbc.Col(dcc.Graph(id="3GFBRX_FM_grp_scatt")), dbc.Col(dcc.Graph(id="3GFBRX_FM_grp_histo"))]),
            dbc.Row([dbc.Col(create_range_slider("sld_3GFBRX_FM_scat", df_fbrxfm_3G, use_min_max=False))]),
            html.Hr(),
        ]
    )

    @callback(Output("3GTXCP_band", "value"), Input("3GTXCP_RAT", "value"))
    def TXCP_3G(Sel_rat):
        return Initialize_band(Sel_rat, df_3GTXCP)

    @callback(
        [
            Output("3GTXCP_band", "options"),
            Output("3GTXCP_grp_scatt", "figure"),
            Output("3GTXCP_grp_histo", "figure"),
        ],
        [Input("3GTXCP_RAT", "value"), Input("3GTXCP_band", "value"), Input("sld_3GTXCP_scat", "value")],
    )
    def update_3GTXCP(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_3GTXCP, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    @callback(Output("3GFBRXGain_band", "value"), Input("3GFBRXGain_RAT", "value"))
    def FBRXGain_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxgm_3G)

    @callback(
        [
            Output("3GFBRXGain_band", "options"),
            Output("3GFBRX_GM_grp_scatt", "figure"),
            Output("3GFBRX_GM_grp_histo", "figure"),
            Output("3GFBRX_GC_grp_scatt", "figure"),
            Output("3GFBRX_GC_grp_histo", "figure"),
        ],
        [
            Input("3GFBRXGain_RAT", "value"),
            Input("3GFBRXGain_band", "value"),
            Input("sld_3GFBRX_GM_scat", "value"),
            Input("sld_3GFBRX_GC_scat", "value"),
        ],
    )
    def update_3GFBRXGain(Sel_rat, Sel_band, scatt_range1, scatt_range2):
        band_opt, scatt_fig1, histo_fig1 = update_band_and_graph(df_fbrxgm_3G, Sel_rat, Sel_band, scatt_range1)
        band_opt, scatt_fig2, histo_fig2 = update_band_and_graph(df_fbrxgc_3G, Sel_rat, Sel_band, scatt_range2)
        return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    @callback(Output("3GFBRXFreq_band", "value"), Input("3GFBRXFreq_RAT", "value"))
    def FBRXFreq_3G_band(Sel_rat):
        return Initialize_band(Sel_rat, df_fbrxgm_3G)

    @callback(
        [
            Output("3GFBRXFreq_band", "options"),
            Output("3GFBRX_FM_grp_scatt", "figure"),
            Output("3GFBRX_FM_grp_histo", "figure"),
        ],
        [Input("3GFBRXFreq_RAT", "value"), Input("3GFBRXFreq_band", "value"), Input("sld_3GFBRX_FM_scat", "value")],
    )
    def update_3GFBRXFreq(Sel_rat, Sel_band, scatt_range):
        band_opt, scatter_fig, histogram_fig = update_band_and_graph(df_fbrxfm_3G, Sel_rat, Sel_band, scatt_range)
        return band_opt, scatter_fig, histogram_fig

    dash.register_page(
        __name__,
        path="/WCDMA",  # represents the url text
        name="WCDMA",  # name of page, commonly used as name of link
        title="WCDMA",  # epresents the title of browser's tab
        description="Description of 3G Page",
        layout=layout,  # 초기화한 레이아웃 등록
    )

    return layout  # 이 레이아웃을 반환하여 페이지를 초기화합니다.
