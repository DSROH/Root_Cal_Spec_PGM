import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# import pandas as pd
# import plotly.figure_factory as ff


class DataFrameDashApp:
    def __init__(
        self,
        df_TXDC=None,
        df_IIP2=None,
        df_Cable=None,
        df_3GTXCP=None,
        df_fbrxgm_3G=None,
        df_fbrxgc_3G=None,
        df_fbrxgm_NR=None,
        df_fbrxgc_NR=None,
        df_fbrxfm_3G=None,
        df_fbrxfm_NR=None,
        df_fbrxfc_NR=None,
    ):
        self.df_TXDC = df_TXDC.reset_index()
        self.df_IIP2 = df_IIP2.reset_index()
        self.df_Cable = df_Cable.reset_index()
        self.df_3GTXCP = df_3GTXCP.reset_index()
        self.df_fbrxgm_3G = df_fbrxgm_3G.reset_index()
        self.df_fbrxgc_3G = df_fbrxgc_3G.reset_index()
        self.df_fbrxgm_NR = df_fbrxgm_NR.reset_index()
        self.df_fbrxgc_NR = df_fbrxgc_NR.reset_index()
        self.df_fbrxfm_3G = df_fbrxfm_3G.reset_index()
        self.df_fbrxfm_NR = df_fbrxfm_NR.reset_index()
        self.df_fbrxfc_NR = df_fbrxfc_NR.reset_index()
        self.app = dash.Dash(__name__)
        self.set_up_dropdowns()
        self.set_up_layout()
        self.register_callbacks()

    def create_dropdown(self, drop_id, default_value, options):
        return dcc.Dropdown(
            id=drop_id,
            options=options,
            value=default_value,
            style={
                "width": "100px",
                "verticalAlign": "middle",
                "font-size": "12px",
                "marginRight": "10px",
                "display": "inline-block",
            },
            optionHeight=30,
            maxHeight=300,
        )

    def set_up_dropdowns(self):
        rat_options = [{"label": "3G", "value": "B"}, {"label": "2G", "value": "GSM"}, {"label": "NR", "value": "n"}]

        band_opt = [{"label": "", "value": ""}]

        self.drop_TXDC_rat = self.create_dropdown("TXDC_RAT", "B", rat_options)
        self.drop_IIP2_rat = self.create_dropdown("IIP2_RAT", "n", [{"label": "NR", "value": "n"}])
        self.drop_Cable_rat = self.create_dropdown("Cable_RAT", "n", [{"label": "NR", "value": "n"}])
        self.drop_3GTXCP_rat = self.create_dropdown("3GTXCP_RAT", "B", [{"label": "3G", "value": "B"}])
        self.drop_3GFBRXGain_rat = self.create_dropdown("3GFBRXGain_RAT", "B", [{"label": "3G", "value": "B"}])
        self.drop_NRFBRXGain_rat = self.create_dropdown("NRFBRXGain_RAT", "n", [{"label": "NR", "value": "n"}])
        self.drop_3GFBRXFreq_rat = self.create_dropdown("3GFBRXFreq_RAT", "B", [{"label": "3G", "value": "B"}])
        self.drop_NRFBRXFreq_rat = self.create_dropdown("NRFBRXFreq_RAT", "n", [{"label": "NR", "value": "n"}])

        self.drop_TXDC_band = self.create_dropdown("TXDC_band", "", band_opt)
        self.drop_IIP2_band = self.create_dropdown("IIP2_band", "", band_opt)
        self.drop_Cable_band = self.create_dropdown("Cable_band", "", band_opt)
        self.drop_3GTXCP_band = self.create_dropdown("3GTXCP_band", "", band_opt)
        self.drop_3GFBRXGain_band = self.create_dropdown("3GFBRXGain_band", "", band_opt)
        self.drop_NRFBRXGain_band = self.create_dropdown("NRFBRXGain_band", "", band_opt)
        self.drop_3GFBRXFreq_band = self.create_dropdown("3GFBRXFreq_band", "", band_opt)
        self.drop_NRFBRXFreq_band = self.create_dropdown("NRFBRXFreq_band", "", band_opt)

    def Trans_dataframe(self, df):
        col_name = list(df[df.columns[:4]].apply(lambda row: "_".join(row.values.astype(str)), axis=1))
        col_name = [c.strip() for c in col_name]

        Copied_df = df.copy()  # Original dataframe 변경 방지
        for i in Copied_df.columns:
            if i in [
                "RAT",
                "Band",
                "Path",
                "Plane",
                "Number",
                "CH_MHz",
                "CH",
                "Index",
                "FBRX",
                "BW",
                "Item",
                "Ant",
                "CellPower",
                "Target",
                "Stage",
                "Mixer",
                "Average",
                "Max",
                "Min",
                "Max-Min",
                "Min-Max",
            ]:
                Copied_df.drop(columns=[i], inplace=True)

        df_Transposed = Copied_df.T
        df_Transposed.columns = col_name

        return df_Transposed

    def create_range_slider(self, sld_id, df, use_min_max=True):
        df_Transposed = self.Trans_dataframe(df)

        if use_min_max:
            x_min = df_Transposed.min()
            x_max = df_Transposed.max()
        else:
            x_min, x_max = 0, len(df_Transposed.index) - 1

        return dcc.RangeSlider(
            id=sld_id,
            marks={i: str(i) for i in range(1, len(df_Transposed.index) + 1, len(df_Transposed.index) // 10)},
            min=x_min,
            max=x_max,
            value=[x_min, x_max],
            step=1,
        )

    def set_up_layout(self):
        self.grp_TXDC_scatt = dcc.Graph(id="TXDC_grp_Scatt")
        self.grp_TXDC_histo = dcc.Graph(id="TXDC_grp_Histo")
        self.grp_IIP2_scatt = dcc.Graph(id="IIP2_grp_Scatt")
        self.grp_IIP2_histo = dcc.Graph(id="IIP2_grp_Histo")
        self.grp_Cable_scatt = dcc.Graph(id="Cable_grp_Scatt")
        self.grp_Cable_histo = dcc.Graph(id="Cable_grp_Histo")
        self.grp_3GTXCP_scatt = dcc.Graph(id="3GTXCP_grp_scatt")
        self.grp_3GTXCP_histo = dcc.Graph(id="3GTXCP_grp_histo")
        self.grp_3GFBRX_GM_scatt = dcc.Graph(id="3GFBRX_GM_grp_scatt")
        self.grp_3GFBRX_GM_histo = dcc.Graph(id="3GFBRX_GM_grp_histo")
        self.grp_NRFBRX_GM_scatt = dcc.Graph(id="NRFBRX_GM_grp_scatt")
        self.grp_NRFBRX_GM_histo = dcc.Graph(id="NRFBRX_GM_grp_histo")
        self.grp_3GFBRX_GC_scatt = dcc.Graph(id="3GFBRX_GC_grp_scatt")
        self.grp_3GFBRX_GC_histo = dcc.Graph(id="3GFBRX_GC_grp_histo")
        self.grp_NRFBRX_GC_scatt = dcc.Graph(id="NRFBRX_GC_grp_scatt")
        self.grp_NRFBRX_GC_histo = dcc.Graph(id="NRFBRX_GC_grp_histo")
        self.grp_3GFBRX_FM_scatt = dcc.Graph(id="3GFBRX_FM_grp_scatt")
        self.grp_3GFBRX_FM_histo = dcc.Graph(id="3GFBRX_FM_grp_histo")
        self.grp_NRFBRX_FM_scatt = dcc.Graph(id="NRFBRX_FM_grp_scatt")
        self.grp_NRFBRX_FM_histo = dcc.Graph(id="NRFBRX_FM_grp_histo")
        self.grp_NRFBRX_FC_scatt = dcc.Graph(id="NRFBRX_FC_grp_scatt")
        self.grp_NRFBRX_FC_histo = dcc.Graph(id="NRFBRX_FC_grp_histo")

        self.sld_TXDC_scatt = self.create_range_slider("sld_TXDC_scat", self.df_TXDC, use_min_max=False)
        self.sld_IIP2_scatt = self.create_range_slider("sld_IIP2_scat", self.df_IIP2, use_min_max=False)
        self.sld_Cable_scatt = self.create_range_slider("sld_Cable_scat", self.df_Cable, use_min_max=False)
        self.sld_3GTXCP_scatt = self.create_range_slider("sld_3GTXCP_scat", self.df_3GTXCP, use_min_max=False)
        self.sld_3GFBRX_GM_scatt = self.create_range_slider("sld_3GFBRX_GM_scat", self.df_fbrxgm_3G, use_min_max=False)
        self.sld_NRFBRX_GM_scatt = self.create_range_slider("sld_NRFBRX_GM_scat", self.df_fbrxgm_NR, use_min_max=False)
        self.sld_3GFBRX_GC_scatt = self.create_range_slider("sld_3GFBRX_GC_scat", self.df_fbrxgc_3G, use_min_max=False)
        self.sld_NRFBRX_GC_scatt = self.create_range_slider("sld_NRFBRX_GC_scat", self.df_fbrxgc_NR, use_min_max=False)
        self.sld_3GFBRX_FM_scatt = self.create_range_slider("sld_3GFBRX_FM_scat", self.df_fbrxfm_3G, use_min_max=False)
        self.sld_NRFBRX_FM_scatt = self.create_range_slider("sld_NRFBRX_FM_scat", self.df_fbrxfm_NR, use_min_max=False)
        self.sld_NRFBRX_FC_scatt = self.create_range_slider("sld_NRFBRX_FC_scat", self.df_fbrxfc_NR, use_min_max=False)

        self.app.layout = html.Div(
            children=[
                html.Div(
                    children=[
                        html.H1("TX_DC_Cal", style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"}),
                        html.Div(
                            [self.drop_TXDC_rat, self.drop_TXDC_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [self.grp_TXDC_scatt, self.sld_TXDC_scatt],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    self.grp_TXDC_histo,
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    children=[
                        html.H1("RX_IIP2_Cal", style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"}),
                        html.Div(
                            [self.drop_IIP2_rat, self.drop_IIP2_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [self.grp_IIP2_scatt, self.sld_IIP2_scatt],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    self.grp_IIP2_histo,
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    children=[
                        html.H1("RF_Cable_Check", style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"}),
                        html.Div(
                            [self.drop_Cable_rat, self.drop_Cable_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [self.grp_Cable_scatt, self.sld_Cable_scatt],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    self.grp_Cable_histo,
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    children=[
                        html.H1(
                            "3G TX Channel Component",
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            [self.drop_3GTXCP_rat, self.drop_3GTXCP_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [self.grp_3GTXCP_scatt, self.sld_3GTXCP_scatt],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    self.grp_3GTXCP_histo,
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    children=[
                        html.H1(
                            "3G TX FBRX Gain Calibration",
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            [self.drop_3GFBRXGain_rat, self.drop_3GFBRXGain_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [
                                        html.Div(
                                            self.grp_3GFBRX_GM_scatt,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        html.Div(
                                            self.grp_3GFBRX_GM_histo,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        self.sld_3GFBRX_GM_scatt,
                                    ],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            self.grp_3GFBRX_GC_scatt,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        html.Div(
                                            self.grp_3GFBRX_GC_histo,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        self.sld_3GFBRX_GC_scatt,
                                    ],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    children=[
                        html.H1(
                            "NR TX FBRX Gain Calibration",
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            [self.drop_NRFBRXGain_rat, self.drop_NRFBRXGain_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [
                                        html.Div(
                                            self.grp_NRFBRX_GM_scatt,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        html.Div(
                                            self.grp_NRFBRX_GM_histo,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        self.sld_NRFBRX_GM_scatt,
                                    ],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            self.grp_NRFBRX_GC_scatt,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        html.Div(
                                            self.grp_NRFBRX_GC_histo,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        self.sld_NRFBRX_GC_scatt,
                                    ],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    children=[
                        html.H1(
                            "3G TX FBRX Freq Calibration",
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            [self.drop_3GFBRXFreq_rat, self.drop_3GFBRXFreq_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [self.grp_3GFBRX_FM_scatt, self.sld_3GFBRX_FM_scatt],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    self.grp_3GFBRX_FM_histo,
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    children=[
                        html.H1(
                            "NR TX FBRX Freq Calibration",
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            [self.drop_NRFBRXFreq_rat, self.drop_NRFBRXFreq_band],
                            style={"verticalAlign": "middle", "padding": 10, "display": "inline-block"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    [
                                        html.Div(
                                            self.grp_NRFBRX_FM_scatt,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        html.Div(
                                            self.grp_NRFBRX_FM_histo,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        self.sld_NRFBRX_FM_scatt,
                                    ],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            self.grp_NRFBRX_FC_scatt,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        html.Div(
                                            self.grp_NRFBRX_FC_histo,
                                            style={"width": "50%", "display": "inline-block", "verticalAlign": "top"},
                                        ),
                                        self.sld_NRFBRX_FC_scatt,
                                    ],
                                    style={"width": "49%", "display": "inline-block", "verticalAlign": "top"},
                                ),
                            ],
                        ),
                    ],
                ),
            ]
        )

    def update_axes(self, fig, x_range=None, y_range=None):
        if x_range is not None:
            fig.update_xaxes(range=[x_range[0] - 1, x_range[1] + 1])
        if y_range is not None:
            fig.update_yaxes(range=[y_range[0] - 1, y_range[1] + 1])

        fig.update_xaxes(
            ticks="outside", showline=True, linewidth=1.5, mirror=True, linecolor="black", gridcolor="lightgrey", showgrid=True
        )
        fig.update_yaxes(
            ticks="outside", showline=True, linewidth=1.5, mirror=True, linecolor="black", gridcolor="lightgrey", showgrid=True
        )
        fig.update_layout(
            font_family="Cascadia Code",
            title_font_family="Arial",
            hovermode="x unified",
            legend_traceorder="normal",
            hoverlabel=dict(namelength=-1),
            template="plotly_white",
            margin=dict(l=30, r=25, t=25, b=25),
        )

    def Initialize(self, Sel_rat, df):
        filtered_df = df[df["Band"].str.contains(Sel_rat)].reset_index(drop=True)
        band_opt = filtered_df["Band"].unique()

        return band_opt[0] if len(band_opt) > 0 else ""

    def update_band_and_graph(self, df, Sel_rat, Sel_band, scatt_range):
        filtered_df = df[df["Band"].str.contains(Sel_rat)].reset_index(drop=True)
        band_opt = filtered_df["Band"].unique()
        band_opt_out = [{"label": i, "value": i} for i in band_opt]

        if not filtered_df.empty:
            filtered_df = df[df["Band"] == Sel_band].reset_index(drop=True)
            scatter_fig = go.Figure()
            histogram_fig = go.Figure()

            df_Transposed = self.Trans_dataframe(filtered_df)

            for i in df_Transposed.columns:
                scatter_fig.add_trace(
                    go.Scatter(
                        x=df_Transposed.index,  # list(range(len(df_Transposed.index))),
                        y=df_Transposed[f"{i}"],
                        mode="lines+markers",
                        showlegend=False,
                        opacity=0.75,
                        name=f"{i}",
                    )
                )
                histogram_fig.add_trace(
                    go.Histogram(
                        x=df_Transposed[f"{i}"],
                        showlegend=False,
                        xbins=dict(size=len(df_Transposed.index) // 100),
                        opacity=0.75,
                        name=f"{i}",
                    )
                )

            # histogram_fig = ff.create_distplot(
            #     [df_Transposed[c] for c in df_Transposed.columns],
            #     df_Transposed.columns,
            #     # show_hist=False,
            #     show_curve=False,
            #     # curve_type="normal",
            #     show_rug=False,
            #     histnorm="",
            #     bin_size=1,
            # )

            scatter_fig.update_layout(
                title="Scatter Plot",
                xaxis=dict(
                    tickmode="linear",
                    tick0=0,
                    dtick=(len(df_Transposed.index) // 10),
                    # showticklabels=False,
                ),
            )
            histogram_fig.update_layout(title="Histogram", barmode="overlay")
            value = df_Transposed.values
            Cpk = min(((value.max() - value.mean()) / (3 * value.std())), ((value.mean() - value.min()) / (3 * value.std())))
            lsl = round(value.mean() - (12 * value.std() * Cpk))
            usl = round(value.mean() + (12 * value.std() * Cpk))

            self.update_axes(scatter_fig, scatt_range, None)
            self.update_axes(histogram_fig, [lsl, usl], None)

            return band_opt_out, scatter_fig, histogram_fig
        else:
            return band_opt_out, go.Figure(data=[]), go.Figure(data=[])

    def register_callbacks(self):
        @self.app.callback(Output("TXDC_band", "value"), Input("TXDC_RAT", "value"))
        def TXDC_band(Sel_rat):
            return self.Initialize(Sel_rat, self.df_TXDC)

        @self.app.callback(
            [Output("TXDC_band", "options"), Output("TXDC_grp_Scatt", "figure"), Output("TXDC_grp_Histo", "figure")],
            [Input("TXDC_RAT", "value"), Input("TXDC_band", "value"), Input("sld_TXDC_scat", "value")],
        )
        def update_TXDC(Sel_rat, Sel_band, scatt_range):
            band_opt, scatter_fig, histogram_fig = self.update_band_and_graph(self.df_TXDC, Sel_rat, Sel_band, scatt_range)
            return band_opt, scatter_fig, histogram_fig

        @self.app.callback(Output("IIP2_band", "value"), Input("IIP2_RAT", "value"))
        def IIP2_band(Sel_rat):
            return self.Initialize(Sel_rat, self.df_IIP2)

        @self.app.callback(
            [Output("IIP2_band", "options"), Output("IIP2_grp_Scatt", "figure"), Output("IIP2_grp_Histo", "figure")],
            [Input("IIP2_RAT", "value"), Input("IIP2_band", "value"), Input("sld_IIP2_scat", "value")],
        )
        def update_IIP2_cal(Sel_rat, Sel_band, scatt_range):
            band_opt, scatter_fig, histogram_fig = self.update_band_and_graph(self.df_IIP2, Sel_rat, Sel_band, scatt_range)
            return band_opt, scatter_fig, histogram_fig

        @self.app.callback(Output("Cable_band", "value"), Input("Cable_RAT", "value"))
        def Cable_band(Sel_rat):
            return self.Initialize(Sel_rat, self.df_Cable)

        @self.app.callback(
            [Output("Cable_band", "options"), Output("Cable_grp_Scatt", "figure"), Output("Cable_grp_Histo", "figure")],
            [Input("Cable_RAT", "value"), Input("Cable_band", "value"), Input("sld_Cable_scat", "value")],
        )
        def update_Cable_Check(Sel_rat, Sel_band, scatt_range):
            band_opt, scatter_fig, histogram_fig = self.update_band_and_graph(self.df_Cable, Sel_rat, Sel_band, scatt_range)
            return band_opt, scatter_fig, histogram_fig

        @self.app.callback(Output("3GTXCP_band", "value"), Input("3GTXCP_RAT", "value"))
        def TXCP_3G(Sel_rat):
            return self.Initialize(Sel_rat, self.df_3GTXCP)

        @self.app.callback(
            [Output("3GTXCP_band", "options"), Output("3GTXCP_grp_scatt", "figure"), Output("3GTXCP_grp_histo", "figure")],
            [Input("3GTXCP_RAT", "value"), Input("3GTXCP_band", "value"), Input("sld_3GTXCP_scat", "value")],
        )
        def update_3GTXCP(Sel_rat, Sel_band, scatt_range):
            band_opt, scatter_fig, histogram_fig = self.update_band_and_graph(self.df_3GTXCP, Sel_rat, Sel_band, scatt_range)
            return band_opt, scatter_fig, histogram_fig

        @self.app.callback(Output("3GFBRXGain_band", "value"), Input("3GFBRXGain_RAT", "value"))
        def FBRXGain_3G_band(Sel_rat):
            return self.Initialize(Sel_rat, self.df_fbrxgm_3G)

        @self.app.callback(
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
            band_opt, scatt_fig1, histo_fig1 = self.update_band_and_graph(self.df_fbrxgm_3G, Sel_rat, Sel_band, scatt_range1)
            band_opt, scatt_fig2, histo_fig2 = self.update_band_and_graph(self.df_fbrxgc_3G, Sel_rat, Sel_band, scatt_range2)
            return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

        @self.app.callback(Output("NRFBRXGain_band", "value"), Input("NRFBRXGain_RAT", "value"))
        def FBRXGain_NR_band(Sel_rat):
            return self.Initialize(Sel_rat, self.df_fbrxgm_NR)

        @self.app.callback(
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
                Input("sld_NRFBRX_GC_scat", "value"),
            ],
        )
        def update_NRFBRXGain(Sel_rat, Sel_band, scatt_range1, scatt_range2):
            band_opt, scatt_fig1, histo_fig1 = self.update_band_and_graph(self.df_fbrxgm_NR, Sel_rat, Sel_band, scatt_range1)
            band_opt, scatt_fig2, histo_fig2 = self.update_band_and_graph(self.df_fbrxgc_NR, Sel_rat, Sel_band, scatt_range2)
            return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

        @self.app.callback(Output("3GFBRXFreq_band", "value"), Input("3GFBRXFreq_RAT", "value"))
        def FBRXFreq_3G_band(Sel_rat):
            return self.Initialize(Sel_rat, self.df_fbrxgm_3G)

        @self.app.callback(
            [
                Output("3GFBRXFreq_band", "options"),
                Output("3GFBRX_FM_grp_scatt", "figure"),
                Output("3GFBRX_FM_grp_histo", "figure"),
            ],
            [Input("3GFBRXFreq_RAT", "value"), Input("3GFBRXFreq_band", "value"), Input("sld_3GFBRX_FM_scat", "value")],
        )
        def update_3GFBRXFreq(Sel_rat, Sel_band, scatt_range):
            band_opt, scatter_fig, histogram_fig = self.update_band_and_graph(self.df_fbrxfm_3G, Sel_rat, Sel_band, scatt_range)
            return band_opt, scatter_fig, histogram_fig

        @self.app.callback(Output("NRFBRXFreq_band", "value"), Input("NRFBRXFreq_RAT", "value"))
        def FBRXFreq_NR_band(Sel_rat):
            return self.Initialize(Sel_rat, self.df_fbrxgm_NR)

        @self.app.callback(
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
            band_opt, scatt_fig1, histo_fig1 = self.update_band_and_graph(self.df_fbrxfm_NR, Sel_rat, Sel_band, scatt_range1)
            band_opt, scatt_fig2, histo_fig2 = self.update_band_and_graph(self.df_fbrxfc_NR, Sel_rat, Sel_band, scatt_range2)
            return band_opt, scatt_fig1, histo_fig1, scatt_fig2, histo_fig2

    def run(self):
        self.app.run_server(debug=True, port=8050)
