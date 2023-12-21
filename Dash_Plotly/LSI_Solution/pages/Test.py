import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, Output, Input, State, callback_context, ALL, MATCH
import plotly.graph_objects as go
import pandas as pd
import json


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
        return None, None


def Drawing_pcc(selected_rat, selected_band, dataframe, scatt_range):
    cols_to_drop = dataframe[dataframe["Path"].str.contains("Tx2")].index
    selected_df = dataframe.drop(cols_to_drop)
    scatter_fig, histogram_fig = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range)

    return scatter_fig, histogram_fig


def Drawing_scc(selected_rat, selected_band, dataframe, scatt_range, st1, children):
    selected_df = dataframe[dataframe["Path"].str.contains("Tx2")]
    item = selected_df.Item.iloc[0]
    scatter_fig, histogram_fig = Update_band_and_graph(selected_df, selected_rat, selected_band, scatt_range)

    layout = html.Div(
        [
            dbc.Row([dbc.Col(html.H2(f"NR {st1} {item} SCC", className="display-7"), width="auto")]),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_scatt'"}, figure=scatter_fig)),
                    dbc.Col(dcc.Graph(id={"type": "dynamic-output", "index": f"'{item}_scc_histo'"}, figure=histogram_fig)),
                ],
                align="center",
            ),
        ]
    )
    children.append(layout)
    return children


def tweet_callback(st1, st2, dataframe):
    return f"{st1} {st2} {dataframe.Item[0]} PCC"


app = Dash()

df_NR_ET_Psat = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_20\\CSV_ETSAPT_Sub6_Psat.csv")
df_NR_ET_Pgain = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_20\\CSV_ETSAPT_Sub6_Pgain.csv")
df_NR_ET_Power = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_20\\CSV_ETSAPT_Sub6_Power.csv")
df_NR_ET_Freq = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_20\\CSV_ETSAPT_Sub6_Freq.csv")

dict_nr = {
    "ET_Psat": df_NR_ET_Psat,
    "ET_Pgain": df_NR_ET_Pgain,
    "ET_Power": df_NR_ET_Power,
    "ET_Freq": df_NR_ET_Freq,
}

df_ET_Psat = dict_nr["ET_Psat"]
df_ET_Pgain = dict_nr["ET_Pgain"]

band_opt = [{"label": "", "value": ""}]

drop_ET_Psat_rat = Create_dropdown("nr_et_psat_rat", "n", [{"label": "NR", "value": "n"}])
drop_ET_Psat_band = Create_dropdown("nr_et_psat_band", "", band_opt)

drop_ET_Pgain_rat = Create_dropdown("nr_et_pgain_rat", "n", [{"label": "NR", "value": "n"}])
drop_ET_Pgain_band = Create_dropdown("nr_et_pgain_band", "", band_opt)

app.layout = html.Div(
    [
        # * ================================= Sub6 ET Psat =================================
        html.Div(
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(
                                children=tweet_callback("NR", "ET-SAPT", df_ET_Psat), id="head_et_psat", className="display-7"
                            ),
                            width="auto",
                        ),
                        dbc.Col(drop_ET_Psat_rat, width=1),
                        dbc.Col(drop_ET_Psat_band, width=1),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id="nr_et_psat_scatt"), width={"size": 6, "offset": 0}),
                        dbc.Col(dcc.Graph(id="nr_et_psat_histo"), width={"size": 6, "offset": 0}),
                    ],
                    align="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            Create_range_slider("sld_et_psat_pcc", df_ET_Psat, use_min_max=False),
                            width={"size": 6, "offset": 0},
                        )
                    ],
                    align="center",
                ),
            ]
        ),
        html.Div(id="et_psat_scc", children=[]),
        html.Hr(),
        # ** ================================= Sub6 ET Pgain =================================
        html.Div(
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2(children=tweet_callback("NR", "ET-SAPT", df_ET_Pgain), className="display-7"), width="auto"
                        ),
                        dbc.Col(drop_ET_Pgain_rat, width=1),
                        dbc.Col(drop_ET_Pgain_band, width=1),
                    ],
                    align="center",
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id="nr_et_pgain_scatt"), width={"size": 6, "offset": 0}),
                        dbc.Col(dcc.Graph(id="nr_et_pgain_histo"), width={"size": 6, "offset": 0}),
                    ],
                    align="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            Create_range_slider("sld_et_pgain_pcc", df_ET_Pgain, use_min_max=False),
                            width={"size": 6, "offset": 0},
                        )
                    ],
                    align="center",
                ),
            ]
        ),
        html.Div(id="et_pgain_scc", children=[]),
        html.Hr(),
    ]
)


@callback(Output("nr_et_psat_band", "value"), Input("nr_et_psat_rat", "value"))
def ET_Psat_NR(selected_rat):
    return Initialize_band(selected_rat, df_ET_Psat)


@callback(
    [
        Output("nr_et_psat_band", "options"),
        Output("nr_et_psat_scatt", "figure"),
        Output("nr_et_psat_histo", "figure"),
        Output("et_psat_scc", "children"),
    ],
    [
        Input("nr_et_psat_rat", "value"),
        Input("nr_et_psat_band", "value"),
        Input("sld_et_psat_pcc", "value"),
        State("et_psat_scc", "children"),
    ],
    # prevent_initial_call=True,
)
def ET_Psat(selected_rat, selected_band, scatt_range, children):
    band_opt = Band_list(df_ET_Psat, selected_rat)
    filtered_df = df_ET_Psat[df_ET_Psat["Band"] == selected_band].reset_index(drop=True)
    if filtered_df["Path"].str.contains("Tx2").any():
        scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_rat, selected_band, filtered_df, scatt_range)
        children = [layout for layout in children if "scc_scatt" not in str(layout)]
        children = Drawing_scc(selected_rat, selected_band, filtered_df, scatt_range, "ET-SAPT", children)

        return band_opt, scatt_fig_pcc, histo_fig_pcc, children
    else:
        scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_rat, selected_band, filtered_df, scatt_range)
        children = [layout for layout in children if f"Psat_scc_scatt" not in str(layout)]

        return band_opt, scatt_fig_pcc, histo_fig_pcc, children


@callback(Output("nr_et_pgain_band", "value"), Input("nr_et_pgain_rat", "value"))
def ET_Pgain_NR(selected_rat):
    return Initialize_band(selected_rat, df_ET_Pgain)


@callback(
    [
        Output("nr_et_pgain_band", "options"),
        Output("nr_et_pgain_scatt", "figure"),
        Output("nr_et_pgain_histo", "figure"),
        Output("et_pgain_scc", "children"),
    ],
    [
        Input("nr_et_pgain_rat", "value"),
        Input("nr_et_pgain_band", "value"),
        Input("sld_et_pgain_pcc", "value"),
        State("et_pgain_scc", "children"),
    ],
    # prevent_initial_call=True,
)
def ET_Pgain(selected_rat, selected_band, scatt_range, children):
    band_opt = Band_list(df_ET_Pgain, selected_rat)
    filtered_df = df_ET_Pgain[df_ET_Pgain["Band"] == selected_band].reset_index(drop=True)
    if filtered_df["Path"].str.contains("Tx2").any():
        scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_rat, selected_band, filtered_df, scatt_range)
        children = [layout for layout in children if "scc_scatt" not in str(layout)]
        children = Drawing_scc(selected_rat, selected_band, filtered_df, scatt_range, "ET-SAPT", children)

        return band_opt, scatt_fig_pcc, histo_fig_pcc, children
    else:
        scatt_fig_pcc, histo_fig_pcc = Drawing_pcc(selected_rat, selected_band, filtered_df, scatt_range)
        children = [layout for layout in children if f"Pgain_scc_scatt" not in str(layout)]

        return band_opt, scatt_fig_pcc, histo_fig_pcc, children


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=8050)
