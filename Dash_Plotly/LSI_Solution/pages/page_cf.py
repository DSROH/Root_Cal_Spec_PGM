import dash
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input


def df_strip(dataframe):
    df_data = dataframe.apply(lambda x: x.map(lambda y: y.strip()) if x.dtype == "object" else x)
    return df_data


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


def Initialize_dropdowns(dict, rat, keys, band_opt=None):
    if band_opt is None:
        band_opt = [{"label": "", "value": ""}]

    dropdowns = {}
    dataframes = {}
    for key in keys:
        df = dict[key].apply(lambda x: x.map(lambda y: y.strip()) if x.dtype == "object" else x)
        dataframes[key] = df

        if rat == "2g":
            dropdowns[key + "_r"] = Create_dropdown(f"{rat}_{key}_r", "G", [{"label": "2G", "value": "G"}])
        elif rat == "3g":
            dropdowns[key + "_r"] = Create_dropdown(f"{rat}_{key}_r", "B", [{"label": "3G", "value": "B"}])
        elif rat == "nr":
            dropdowns[key + "_r"] = Create_dropdown(f"{rat}_{key}_r", "n", [{"label": "NR", "value": "n"}])

        dropdowns[key + "_b"] = Create_dropdown(f"{rat}_{key}_b", "", band_opt)

    return dropdowns, dataframes


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
    if "hist" in sld_id:
        x_min = 0
        x_max = 5
        x_step = 0.05

        return dcc.Slider(
            id=sld_id,
            marks={i: str(i) for i in range(0, x_max + 1, (x_max // 10) + 1)},
            min=x_min,
            max=x_max,
            step=x_step,
            value=2.5,
        )
    else:
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
            step=1,
            value=[x_min, x_max],
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


def Initialize_band(selected_r, df):
    filtered_df = df[df["Band"].str.contains(selected_r)].reset_index(drop=True)
    band_opt = filtered_df["Band"].unique()

    return band_opt[0] if len(band_opt) > 0 else ""


def Band_list(df, selected_r):
    filtered_df = df[df["Band"].str.contains(selected_r)].reset_index(drop=True)
    band_opt = filtered_df["Band"].unique()
    band_opt_out = [{"label": i, "value": i} for i in band_opt]

    return band_opt_out


def Update_band_and_graph(df, selected_r, selected_b, scatt_range=None, histo_range=None):
    filtered_df = df[df["Band"].str.contains(selected_r)].reset_index(drop=True)

    if not filtered_df.empty:
        filtered_df = df[df["Band"] == selected_b].reset_index(drop=True)
        scatt_fig = go.Figure()
        histo_fig = go.Figure()

        df_Transposed = Trans_dataframe(filtered_df).dropna()

        for i in df_Transposed.columns:
            scatt_fig.add_trace(
                go.Scatter(
                    x=list(range(len(df_Transposed.index))),
                    y=df_Transposed[f"{i}"],
                    mode="lines+markers",
                    showlegend=False,
                    opacity=0.75,
                    name=f"{i}",
                )
            )
            histo_fig.add_trace(
                go.Histogram(
                    x=df_Transposed[f"{i}"],
                    showlegend=False,
                    autobinx=False,
                    xbins=dict(size=histo_range),
                    opacity=0.75,
                    name=f"{i}",
                )
            )

        # histo_fig = ff.create_distplot(
        #     [df_Transposed[c] for c in df_Transposed.columns],
        #     df_Transposed.columns,
        #     # show_hist=False,
        #     show_curve=False,
        #     # curve_type="normal",
        #     show_rug=False,
        #     histnorm="",
        #     bin_size=1,
        # )

        scatt_fig.update_layout(
            title="Scatter Plot",
            xaxis=dict(
                tickmode="linear",
                tick0=0,
                dtick=(len(df_Transposed.index) // 10),
                # showticklabels=False,
            ),
        )

        histo_fig.update_layout(title="Histogram", barmode="overlay")
        value = df_Transposed.values

        if (value.mean() == value.min()) or (value.max() == value.mean()):
            lsl = round(value.mean() - (12 * value.std()))
            usl = round(value.mean() + (12 * value.std()))
        else:
            Cpk = min(((value.max() - value.mean()) / (3 * value.std())), ((value.mean() - value.min()) / (3 * value.std())))
            lsl = round(value.mean() - (12 * value.std() * Cpk))
            usl = round(value.mean() + (12 * value.std() * Cpk))

        Update_axes(scatt_fig, scatt_range, None)
        Update_axes(histo_fig, [lsl, usl], None)

        return scatt_fig, histo_fig
    else:
        return go.Figure(data=[]), go.Figure(data=[])


def Drawing_pcc(
    selected_r, selected_b, df1, df2=None, scatt_range1=None, histo_range1=None, scatt_range2=None, histo_range2=None
):
    cols_to_drop1 = df1[df1["Path"].str.contains("Tx2")].index
    selected_df1 = df1.drop(cols_to_drop1)

    if scatt_range2 is not None:
        cols_to_drop2 = df2[df2["Path"].str.contains("Tx2")].index
        selected_df2 = df2.drop(cols_to_drop2)
        scatt_fig1, histo_fig1 = Update_band_and_graph(selected_df1, selected_r, selected_b, scatt_range1, histo_range1)
        scatt_fig2, histo_fig2 = Update_band_and_graph(selected_df2, selected_r, selected_b, scatt_range2, histo_range2)
        return scatt_fig1, histo_fig1, scatt_fig2, histo_fig2
    else:
        scatt_fig, histo_fig = Update_band_and_graph(selected_df1, selected_r, selected_b, scatt_range1, histo_range1)
        return scatt_fig, histo_fig


def Drawing_scc(
    selected_r,
    selected_b,
    rat,
    st1,
    children,
    df1,
    df2=None,
    scatt_range1=None,
    histo_range1=None,
    scatt_range2=None,
    histo_range2=None,
):
    selected_df1 = df1[df1["Path"].str.contains("Tx2")]
    try:
        item = selected_df1.Item.iloc[0]
    except:
        item = ""

    if scatt_range2 is not None:
        selected_df2 = df2[df2["Path"].str.contains("Tx2")]
        scatt_fig1, histo_fig1 = Update_band_and_graph(selected_df1, selected_r, selected_b, scatt_range1, histo_range1)
        scatt_fig2, histo_fig2 = Update_band_and_graph(selected_df2, selected_r, selected_b, scatt_range2, histo_range2)
        layout = html.Div(
            [
                dbc.Row([dbc.Col(html.H2(f"{rat.upper()} {st1.upper()} {item} SCC", className="display-7"), width="auto")]),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_scatt_1'"}, figure=scatt_fig1),
                            width={"size": 3, "offset": 0},
                        ),
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_histo_1'"}, figure=histo_fig1),
                            width={"size": 3, "offset": 0},
                        ),
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_scatt_2'"}, figure=scatt_fig2),
                            width={"size": 3, "offset": 0},
                        ),
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_histo_2'"}, figure=histo_fig2),
                            width={"size": 3, "offset": 0},
                        ),
                    ],
                    align="center",
                ),
            ]
        )
        children.append(layout)
    else:
        scatt_fig1, histo_fig1 = Update_band_and_graph(selected_df1, selected_r, selected_b, scatt_range1, histo_range1)
        layout = html.Div(
            [
                dbc.Row([dbc.Col(html.H2(f"{rat.upper()} {st1.upper()} {item} SCC", className="display-7"), width="auto")]),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_scatt'"}, figure=scatt_fig1),
                            width={"size": 6, "offset": 0},
                        ),
                        dbc.Col(
                            dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_histo'"}, figure=histo_fig1),
                            width={"size": 6, "offset": 0},
                        ),
                    ],
                    align="center",
                ),
            ]
        )
        children.append(layout)

    return children


def tweet_callback(st1, st2, st3=None):
    if st3 is not None:
        return f"{st1.upper()} {st2.upper()} {st3} PCC"
    else:
        return f"{st1.upper()} {st2.upper()} PCC"


def Generate_layout(key, rat, dropdowns, data_frame):
    # ** gc, fc는 스킵하고 gm, fm에서 code까지 다 생성한다.
    if key in ["fbrx_gc", "fbrx_fc"]:
        return
    elif (key in ["fbrx_gm"]) or ((rat == "nr") & (key in ["fbrx_fm"])):
        layout = html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(
                                children=tweet_callback(rat, key),
                                id=f"head_{key}",
                                className="display-7",
                            ),
                            width="auto",
                        ),
                        dbc.Col(dropdowns[f"{key}_r"], width=1),
                        dbc.Col(dropdowns[f"{key}_b"], width=1),
                    ],
                    align="center",
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id=f"{rat}_{key[:-1]}m_scatt"), width={"size": 3, "offset": 0}),
                        dbc.Col(dcc.Graph(id=f"{rat}_{key[:-1]}m_histo"), width={"size": 3, "offset": 0}),
                        dbc.Col(dcc.Graph(id=f"{rat}_{key[:-1]}c_scatt"), width={"size": 3, "offset": 0}),
                        dbc.Col(dcc.Graph(id=f"{rat}_{key[:-1]}c_histo"), width={"size": 3, "offset": 0}),
                    ],
                    align="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            Create_range_slider(f"sld_{key}_scat", data_frame[key], use_min_max=False),
                            width={"size": 6, "offset": 0},
                        ),
                        dbc.Col(
                            Create_range_slider(f"sld_{key}_hist", data_frame[key], use_min_max=False),
                            width={"size": 6, "offset": 0},
                        ),
                    ],
                    align="center",
                ),
                html.Div(id=f"{key}_scc", children=[]),
                html.Hr(),
            ]
        )
    else:
        layout = html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(children=tweet_callback(rat, key), id=f"head_{key}", className="display-7"),
                            width="auto",
                        ),
                        dbc.Col(dropdowns[f"{key}_r"], width=1),
                        dbc.Col(dropdowns[f"{key}_b"], width=1),
                    ],
                    align="center",
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id=f"{rat}_{key}_scatt"), width={"size": 6, "offset": 0}),
                        dbc.Col(dcc.Graph(id=f"{rat}_{key}_histo"), width={"size": 6, "offset": 0}),
                    ],
                    align="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            Create_range_slider(f"sld_{key}_scat", data_frame[key], use_min_max=False),
                            width={"size": 6, "offset": 0},
                        ),
                        dbc.Col(
                            Create_range_slider(f"sld_{key}_hist", data_frame[key], use_min_max=False),
                            width={"size": 6, "offset": 0},
                        ),
                    ],
                    align="center",
                ),
                html.Div(id=f"{key}_scc", children=[]),
                html.Hr(),
            ]
        )
    return layout


def Initialize_cf(dict_cf, rat):
    df_txdc = dict_cf["txdc"]
    df_iip2 = dict_cf["iip2"]
    df_cable = dict_cf["cable"]

    rat_options = [{"label": "3G", "value": "B"}, {"label": "2G", "value": "GSM"}, {"label": "NR", "value": "n"}]
    band_opt = [{"label": "", "value": ""}]

    # Create_dropdown 메서드를 사용하여 드롭다운 생성
    drop_txdc_r = Create_dropdown("txdc_r", "B", rat_options)
    drop_iip2_r = Create_dropdown("iip2_r", "n", [{"label": "NR", "value": "n"}])
    drop_cable_r = Create_dropdown("cable_r", "n", [{"label": "NR", "value": "n"}])

    drop_txdc_b = Create_dropdown("txdc_b", "", band_opt)
    drop_iip2_b = Create_dropdown("iip2_b", "", band_opt)
    drop_cable_b = Create_dropdown("cable_b", "", band_opt)

    # 페이지 레이아웃을 초기화합니다.
    layout = html.Div(
        [
            # ** ================================= txdc Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("TXCD Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_txdc_r, width=1),
                    dbc.Col(drop_txdc_b, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="txdc_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="txdc_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(Create_range_slider("sld_txdc_scat", df_txdc, use_min_max=False), width={"size": 6, "offset": 0}),
                    dbc.Col(Create_range_slider("sld_txdc_hist", df_txdc, use_min_max=False), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= iip2 Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("IIP2 Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_iip2_r, width=1),
                    dbc.Col(drop_iip2_b, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="iip2_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="iip2_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(Create_range_slider("sld_iip2_scat", df_iip2, use_min_max=False), width={"size": 6, "offset": 0}),
                    dbc.Col(Create_range_slider("sld_iip2_hist", df_iip2, use_min_max=False), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            html.Hr(),
            # ** ================================= cable Check =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("RF Cable Check", className="display-7"), width="auto"),
                    dbc.Col(drop_cable_r, width=1),
                    dbc.Col(drop_cable_b, width=1),
                ],
                align="center",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="cable_scatt"), width={"size": 6, "offset": 0}),
                    dbc.Col(dcc.Graph(id="cable_histo"), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(Create_range_slider("sld_cable_scat", df_cable, use_min_max=False), width={"size": 6, "offset": 0}),
                    dbc.Col(Create_range_slider("sld_cable_hist", df_cable, use_min_max=False), width={"size": 6, "offset": 0}),
                ],
                align="center",
            ),
            html.Hr(),
        ]
    )

    # ** ================================= txdc Cal =================================
    @callback(Output("txdc_b", "value"), Input("txdc_r", "value"))
    def txdc(selected_r):
        return Initialize_band(selected_r, df_txdc)

    @callback(
        [
            Output("txdc_b", "options"),
            Output("txdc_scatt", "figure"),
            Output("txdc_histo", "figure"),
        ],
        [
            Input("txdc_r", "value"),
            Input("txdc_b", "value"),
            Input("sld_txdc_scat", "value"),
            Input("sld_txdc_hist", "value"),
        ],
    )
    def update_txdc(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_txdc, selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(df_txdc, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ================================= txdc Cal =================================
    @callback(Output("iip2_b", "value"), Input("iip2_r", "value"))
    def iip2(selected_r):
        return Initialize_band(selected_r, df_iip2)

    @callback(
        [
            Output("iip2_b", "options"),
            Output("iip2_scatt", "figure"),
            Output("iip2_histo", "figure"),
        ],
        [
            Input("iip2_r", "value"),
            Input("iip2_b", "value"),
            Input("sld_iip2_scat", "value"),
            Input("sld_iip2_hist", "value"),
        ],
    )
    def update_iip2(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_iip2, selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(df_iip2, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ================================= RF cable Check =================================
    @callback(Output("cable_b", "value"), Input("cable_r", "value"))
    def cable(selected_r):
        return Initialize_band(selected_r, df_cable)

    @callback(
        [
            Output("cable_b", "options"),
            Output("cable_scatt", "figure"),
            Output("cable_histo", "figure"),
        ],
        [
            Input("cable_r", "value"),
            Input("cable_b", "value"),
            Input("sld_cable_scat", "value"),
            Input("sld_cable_hist", "value"),
        ],
    )
    def update_cable(selected_r, selected_b, scatt_range, histo_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_cable, selected_r, selected_b, scatt_range, histo_range)
        band_opt = Band_list(df_cable, selected_r)

        return band_opt, scatter_fig, histogram_fig

    dash.register_page(__name__, path="/", name="Common Func", title="Common Func", layout=layout)

    return layout
