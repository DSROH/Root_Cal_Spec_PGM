import pandas as pd
from dash_app import MultiPageApp
from pages.page_CF import initialize_cf
from pages.page_3G import initialize_3g
from pages.page_NR import initialize_nr

# from pages.page_2G import initialize_2g

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
    app.run()  # 데이터프레임은 여기서 사용하지 않습니다.

    # pg1.py 파일에 데이터프레임 전달
    layout_cf = initialize_cf(df_TXDC, df_IIP2, df_Cable)
    layout_3g = initialize_3g(df_3GTXCP, df_fbrxgm_3G, df_fbrxgc_3G, df_fbrxfm_3G)
    layout_nr = initialize_nr(df_fbrxgm_NR, df_fbrxgc_NR, df_fbrxfm_NR, df_fbrxfc_NR)
