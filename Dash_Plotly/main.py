import pandas as pd
from Dash_Plotly.pages.dash_app import MultiPageApp


df_TXDC = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_IIP2 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_Cable = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_3GTXCP = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgm_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgc_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxfm_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgm_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgc_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxfm_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxfc_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")

if __name__ == "__main__":
    app = MultiPageApp(
        df_TXDC,
        df_IIP2,
        df_Cable,
        df_3GTXCP,
        df_fbrxgm_3G,
        df_fbrxgc_3G,
        df_fbrxfm_3G,
        df_fbrxgm_NR,
        df_fbrxgc_NR,
        df_fbrxfm_NR,
        df_fbrxfc_NR,
    )
    app.run()
