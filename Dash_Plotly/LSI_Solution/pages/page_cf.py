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
                    autobinx=False,
                    xbins=dict(size=histo_range),
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


def Drawing_pcc(selected_r, selected_b, df, scatt_range1=None, histo_range1=None, scatt_range2=None, histo_range2=None):
    cols_to_drop = df[df["Path"].str.contains("Tx2")].index
    selected_df = df.drop(cols_to_drop)
    if scatt_range2 is not None:
        scatter_fig1, histogram_fig1 = Update_band_and_graph(selected_df, selected_r, selected_b, scatt_range1, histo_range1)
        scatter_fig2, histogram_fig2 = Update_band_and_graph(selected_df, selected_r, selected_b, scatt_range2, histo_range2)
        return scatter_fig1, histogram_fig1, scatter_fig2, histogram_fig2
    else:
        scatter_fig, histogram_fig = Update_band_and_graph(selected_df, selected_r, selected_b, scatt_range1, histo_range1)
        return scatter_fig, histogram_fig


def Drawing_scc(
    selected_r, selected_b, df, st1, children, scatt_range1=None, histo_range1=None, scatt_range2=None, histo_range2=None
):
    selected_df = df[df["Path"].str.contains("Tx2")]
    item = selected_df.Item.iloc[0]

    if scatt_range2 is not None:
        scatter_fig1, histogram_fig1 = Update_band_and_graph(selected_df, selected_r, selected_b, scatt_range1, histo_range1)
        scatter_fig2, histogram_fig2 = Update_band_and_graph(selected_df, selected_r, selected_b, scatt_range2, histo_range2)
        layout = html.Div(
            [
                dbc.Row([dbc.Col(html.H2(f"NR {st1} {item} SCC", className="display-7"), width="auto")]),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_scatt_1'"}, figure=scatter_fig1)),
                        dbc.Col(dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_histo_1'"}, figure=histogram_fig1)),
                        dbc.Col(dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_scatt_2'"}, figure=scatter_fig2)),
                        dbc.Col(dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_histo_2'"}, figure=histogram_fig2)),
                    ],
                    align="center",
                ),
            ]
        )
        children.append(layout)
    else:
        scatter_fig1, histogram_fig1 = Update_band_and_graph(selected_df, selected_r, selected_b, scatt_range1, histo_range1)
        layout = html.Div(
            [
                dbc.Row([dbc.Col(html.H2(f"NR {st1} {item} SCC", className="display-7"), width="auto")]),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_scatt'"}, figure=scatter_fig1)),
                        dbc.Col(dcc.Graph(id={"type": "dynamic-grp", "index": f"'{item}_scc_histo'"}, figure=histogram_fig1)),
                    ],
                    align="center",
                ),
            ]
        )
        children.append(layout)

    return children


def tweet_callback(st1, st2, st3):
    return f"{st1} {st2} {st3} PCC"


def Initialize_cf(dict_cf, rat):
    df_TXDC = dict_cf["TXDC"]
    df_IIP2 = dict_cf["IIP2"]
    df_Cable = dict_cf["Cable"]

    rat_options = [{"label": "3G", "value": "B"}, {"label": "2G", "value": "GSM"}, {"label": "NR", "value": "n"}]
    band_opt = [{"label": "", "value": ""}]

    # Create_dropdown 메서드를 사용하여 드롭다운 생성
    drop_TXDC_r = Create_dropdown("TXDC_r", "B", rat_options)
    drop_IIP2_r = Create_dropdown("IIP2_r", "n", [{"label": "NR", "value": "n"}])
    drop_Cable_r = Create_dropdown("Cable_r", "n", [{"label": "NR", "value": "n"}])

    drop_TXDC_b = Create_dropdown("TXDC_b", "", band_opt)
    drop_IIP2_b = Create_dropdown("IIP2_b", "", band_opt)
    drop_Cable_b = Create_dropdown("Cable_b", "", band_opt)

    # 페이지 레이아웃을 초기화합니다.
    layout = html.Div(
        [
            # ** ================================= TXDC Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("TXDC Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_TXDC_r, width=1),
                    dbc.Col(drop_TXDC_b, width=1),
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
            # ** ================================= IIP2 Cal =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("IIP2 Cal", className="display-7"), width="auto"),
                    dbc.Col(drop_IIP2_r, width=1),
                    dbc.Col(drop_IIP2_b, width=1),
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
            # ** ================================= Cable Check =================================
            dbc.Row(
                [
                    dbc.Col(html.H2("RF Cable Check", className="display-7"), width="auto"),
                    dbc.Col(drop_Cable_r, width=1),
                    dbc.Col(drop_Cable_b, width=1),
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

    # ** ================================= TXDC Cal =================================
    @callback(Output("TXDC_b", "value"), Input("TXDC_r", "value"))
    def TXDC_CF(selected_r):
        return Initialize_band(selected_r, df_TXDC)

    @callback(
        [Output("TXDC_b", "options"), Output("TXDC_grp_Scatt", "figure"), Output("TXDC_grp_Histo", "figure")],
        [Input("TXDC_r", "value"), Input("TXDC_b", "value"), Input("sld_TXDC_scat", "value")],
    )
    def update_TXDC(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_TXDC, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_TXDC, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ================================= TXDC Cal =================================
    @callback(Output("IIP2_b", "value"), Input("IIP2_r", "value"))
    def IIP2_CF(selected_r):
        return Initialize_band(selected_r, df_IIP2)

    @callback(
        [Output("IIP2_b", "options"), Output("IIP2_grp_Scatt", "figure"), Output("IIP2_grp_Histo", "figure")],
        [Input("IIP2_r", "value"), Input("IIP2_b", "value"), Input("sld_IIP2_scat", "value")],
    )
    def update_IIP2_cal(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_IIP2, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_IIP2, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # ** ================================= RF Cable Check =================================
    @callback(Output("Cable_b", "value"), Input("Cable_r", "value"))
    def Cable_CF(selected_r):
        return Initialize_band(selected_r, df_Cable)

    @callback(
        [Output("Cable_b", "options"), Output("Cable_grp_Scatt", "figure"), Output("Cable_grp_Histo", "figure")],
        [Input("Cable_r", "value"), Input("Cable_b", "value"), Input("sld_IIP2_scat", "value")],
    )
    def update_Cable(selected_r, selected_b, scatt_range):
        scatter_fig, histogram_fig = Update_band_and_graph(df_Cable, selected_r, selected_b, scatt_range)
        band_opt = Band_list(df_Cable, selected_r)

        return band_opt, scatter_fig, histogram_fig

    # 페이지 등록
    dash.register_page(__name__, path="/", name="Common Func", title="Common Func", layout=layout)

    return layout
