import dash
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input


def Trans_dataframe(df):
    df = df.reset_index(drop=True).dropna(axis=1)

    col_name = [f"{a}_{b}_{c}_{d}" for a, b, c, d in df.iloc[:, :4].astype(str).values]
    col_name = [c.strip() for c in col_name]

    cols_to_keep = [
        c
        for c in df.columns
        if c
        not in [
            "RAT",
            "Band",
            "Path",
            "Plane",
            "Number",
            "CH_MHz",
            "CH",
            "Index",
            "index",
            "PA Stage",
            "Gain",
            "Type",
            "FBRX",
            "TxL",
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
        ]
    ]

    Copied_df = df.loc[:, cols_to_keep]
    df_Transposed = Copied_df.T
    df_Transposed.columns = col_name

    return df_Transposed


def Create_dropdown(drop_id, default_value, options):
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
        # optionHeight=30,
        # maxHeight=300,
    )


def Create_range_slider(sld_id, df, use_min_max=True):
    df_Transposed = Trans_dataframe(df)

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


def Update_axes(fig, x_range=None, y_range=None):
    if x_range is not None:
        fig.update_xaxes(range=[x_range[0] - 1, x_range[1] + 1])
    if y_range is not None:
        fig.update_yaxes(range=[y_range[0] - 1, y_range[1] + 1])

    fig.update_xaxes(
        ticks="outside",
        showline=True,
        linewidth=1.5,
        mirror=True,
        linecolor="black",
        gridcolor="lightgrey",
        showgrid=True,
    )
    fig.update_yaxes(
        ticks="outside",
        showline=True,
        linewidth=1.5,
        mirror=True,
        linecolor="black",
        gridcolor="lightgrey",
        showgrid=True,
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


def Initialize_band(selected_rat, df):
    filtered_df = df[df["Band"].str.contains(selected_rat)].reset_index(drop=True)
    band_opt = filtered_df["Band"].unique()

    return band_opt[0] if len(band_opt) > 0 else ""


def Band_list(df, selected_rat):
    filtered_df = df[df["Band"].str.contains(selected_rat)].reset_index(drop=True)
    band_opt = filtered_df["Band"].unique()
    band_opt_out = [{"label": i, "value": i} for i in band_opt]

    return band_opt_out


def Update_band_and_graph(df, selected_rat, selected_band, scatt_range):
    filtered_df = df[df["Band"].str.contains(selected_rat)].reset_index(drop=True)

    if not filtered_df.empty:
        filtered_df = df[df["Band"] == selected_band].reset_index(drop=True)
        scatter_fig = go.Figure()
        histogram_fig = go.Figure()

        df_Transposed = Trans_dataframe(filtered_df).dropna()

        for i in df_Transposed.columns:
            scatter_fig.add_trace(
                go.Scatter(
                    x=list(range(len(df_Transposed.index))),
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

        if (value.mean() == value.min()) or (value.max() == value.mean()):
            lsl = round(value.mean() - (12 * value.std()))
            usl = round(value.mean() + (12 * value.std()))
        else:
            Cpk = min(((value.max() - value.mean()) / (3 * value.std())), ((value.mean() - value.min()) / (3 * value.std())))
            lsl = round(value.mean() - (12 * value.std() * Cpk))
            usl = round(value.mean() + (12 * value.std() * Cpk))

        Update_axes(scatter_fig, scatt_range, None)
        Update_axes(histogram_fig, [lsl, usl], None)

        return scatter_fig, histogram_fig
    else:
        return go.Figure(data=[]), go.Figure(data=[])


def Drawing_pcc(selected_rat, selected_band, dataframe, scatt_range1=None, scatt_range2=None):
    cols_to_drop = dataframe[dataframe["Path"].str.contains("Tx2")].index
    selected_df = dataframe.drop(cols_to_drop)
    if scatt_range2 is not None:
        scatter_fig1, histogram_fig1 = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range1)
        scatter_fig2, histogram_fig2 = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range2)

        return scatter_fig1, histogram_fig1, scatter_fig2, histogram_fig2
    else:
        scatter_fig1, histogram_fig1 = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range1)

        return scatter_fig1, histogram_fig1


def Drawing_scc(selected_rat, selected_band, dataframe, st1, children, scatt_range1=None, scatt_range2=None):
    selected_df = dataframe[dataframe["Path"].str.contains("Tx2")]
    item = selected_df.Item.iloc[0]
    if scatt_range2 is not None:
        scatter_fig1, histogram_fig1 = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range1)
        scatter_fig2, histogram_fig2 = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range2)

        layout = html.Div(
            [
                dbc.Row([dbc.Col(html.H2(f"NR {st1} {item} SCC", className="display-7"), width="auto")]),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_scatt1'"}, figure=scatter_fig1)),
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_histo1'"}, figure=histogram_fig1)
                        ),
                        dbc.Col(dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_scatt2'"}, figure=scatter_fig2)),
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_histo2'"}, figure=histogram_fig2)
                        ),
                    ],
                    align="center",
                ),
            ]
        )
        children.append(layout)

    else:
        scatter_fig1, histogram_fig1 = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range1)

        layout = html.Div(
            [
                dbc.Row([dbc.Col(html.H2(f"NR {st1} {item} SCC", className="display-7"), width="auto")]),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_scatt'"}, figure=scatter_fig1)),
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_histo'"}, figure=histogram_fig1)
                        ),
                    ],
                    align="center",
                ),
            ]
        )
        children.append(layout)

    return children


def tweet_callback(st1, st2, st3):
    return f"{st1} {st2} {st3} PCC"


def Initialize_cf(dict_cf):
    df_TXDC = dict_cf["TXDC"]
    df_IIP2 = dict_cf["IIP2"]
    df_Cable = dict_cf["Cable"]

    rat_options = [{"label": "3G", "value": "B"}, {"label": "2G", "value": "GSM"}, {"label": "NR", "value": "n"}]
    band_opt = [{"label": "", "value": ""}]

    # Create_dropdown 메서드를 사용하여 드롭다운 생성
    drop_TXDC_rat = Create_dropdown("TXDC_RAT", "B", rat_options)
    drop_IIP2_rat = Create_dropdown("IIP2_RAT", "n", [{"label": "NR", "value": "n"}])
    drop_Cable_rat = Create_dropdown("Cable_RAT", "n", [{"label": "NR", "value": "n"}])

    drop_TXDC_band = Create_dropdown("TXDC_band", "", band_opt)
    drop_IIP2_band = Create_dropdown("IIP2_band", "", band_opt)
    drop_Cable_band = Create_dropdown("Cable_band", "", band_opt)

    # 페이지 레이아웃을 초기화합니다.
    layout = html.Div(
        [
            # ! TXDC Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("TXDC Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_TXDC_rat, width=1),
                    dbc.Col(drop_TXDC_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="TXDC_grp_Scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="TXDC_grp_Histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [dbc.Col(Create_range_slider("sld_TXDC_scat", df_TXDC, use_min_max=False), width={"size": 6, "offset": 0})],
                align="center",
            ),
            html.Hr(),
            # ! IIP2 Cal
            dbc.Row(
                [
                    dbc.Col(html.H2("IIP2 Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_IIP2_rat, width=1),
                    dbc.Col(drop_IIP2_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="IIP2_grp_Scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="IIP2_grp_Histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [dbc.Col(Create_range_slider("sld_IIP2_scat", df_IIP2, use_min_max=False), width={"size": 6, "offset": 0})],
                align="center",
            ),
            html.Hr(),
            # ! Cable Check
            dbc.Row(
                [
                    dbc.Col(html.H2("RF Cable Check", className="display-7"), width="auto"),
                    dbc.Col(drop_Cable_rat, width=1),
                    dbc.Col(drop_Cable_band, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="Cable_grp_Scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="Cable_grp_Histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [dbc.Col(Create_range_slider("sld_IIP2_scat", df_Cable, use_min_max=False), width={"size": 6, "offset": 0})],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ! TXDC Cal
    @callback(Output("TXDC_band", "value"), Input("TXDC_RAT", "value"))
    def TXDC_CF(selected_rat):
        return Initialize_band(selected_rat, df_TXDC)

    @callback(
        [Output("TXDC_band", "options"), Output("TXDC_grp_Scatt", "figure"), Output("TXDC_grp_Histo", "figure")],
        [Input("TXDC_RAT", "value"), Input("TXDC_band", "value"), Input("sld_TXDC_scat", "value")],
    )
    def update_TXDC(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_TXDC, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_TXDC, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # ! TXDC Cal
    @callback(Output("IIP2_band", "value"), Input("IIP2_RAT", "value"))
    def IIP2_CF(selected_rat):
        return Initialize_band(selected_rat, df_IIP2)

    @callback(
        [Output("IIP2_band", "options"), Output("IIP2_grp_Scatt", "figure"), Output("IIP2_grp_Histo", "figure")],
        [Input("IIP2_RAT", "value"), Input("IIP2_band", "value"), Input("sld_IIP2_scat", "value")],
    )
    def update_IIP2_cal(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_IIP2, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_IIP2, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # ! RF Cable Check
    @callback(Output("Cable_band", "value"), Input("Cable_RAT", "value"))
    def Cable_CF(selected_rat):
        return Initialize_band(selected_rat, df_Cable)

    @callback(
        [Output("Cable_band", "options"), Output("Cable_grp_Scatt", "figure"), Output("Cable_grp_Histo", "figure")],
        [Input("Cable_RAT", "value"), Input("Cable_band", "value"), Input("sld_IIP2_scat", "value")],
    )
    def update_Cable(selected_rat, selected_band, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_Cable, selected_rat, selected_band, scatt_range)
        band_opt = Band_list(df_Cable, selected_rat)

        return band_opt, scatter_fig, histogram_fig

    # 페이지 등록
    dash.register_page(__name__, path="/", name="Common Func", title="Common Func", layout=layout)

    return layout
