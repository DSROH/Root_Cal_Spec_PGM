import pandas as pd
from LSI_Solution.pages.dash_app import MultiPageApp

df_TXDC = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_IIP2 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_Cable = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_3GTXCP = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgm_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgc_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxfm_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxfm_3G_ch = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgm_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxgc_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxfm_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_fbrxfc_NR = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_PRX_Gain_2G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_Ripple_2G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXGain_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXComp_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXGain_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXRSRP_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXComp_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXMixer_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_APT_Meas_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_APT_Meas_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_3G_ET_Pst = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_3G_ET_Power = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_NR_ET_Psat = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_NR_ET_Pgain = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_NR_ET_Power = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_NR_ET_Freq = pd.read_csv("Excel_DC_IIP2_Cal.csv")

dict_cf = {
    "TXDC": df_TXDC,
    "IIP2": df_IIP2,
    "Cable": df_Cable,
}
dict_2g = {
    "RXGain": df_PRX_Gain_2G,
    "RXRipp": df_Ripple_2G,
}
dict_3g = {
    "TxP_CC": df_3GTXCP,
    "RX_Gain": df_RXGain_3G,
    "RX_Comp": df_RXComp_3G,
    "FBRX_GM": df_fbrxgm_3G,
    "FBRX_GC": df_fbrxgc_3G,
    "FBRX_FM": df_fbrxfm_3G,
    "FBRX_FM_Ch": df_fbrxfm_3G_ch,
    "APT_Meas": df_APT_Meas_3G,
    "ET_Psat": df_3G_ET_Pst,
    "ET_Pgain": df_3G_ET_Power,
}

dict_nr = {
    "RX_Gain": df_RXGain_sub6,
    "RX_RSRP": df_RXRSRP_sub6,
    "RX_Comp": df_RXComp_sub6,
    "RX_Mix": df_RXMixer_sub6,
    "FBRX_GM": df_fbrxgm_NR,
    "FBRX_GC": df_fbrxgc_NR,
    "FBRX_FM": df_fbrxfm_NR,
    "FBRX_FC": df_fbrxfc_NR,
    "APT_Meas": df_APT_Meas_sub6,
    "ET_Psat": df_NR_ET_Psat,
    "ET_Pgain": df_NR_ET_Pgain,
    "ET_Power": df_NR_ET_Power,
    "ET_Freq": df_NR_ET_Freq,
}

MultiPageApp(dict_cf, dict_2g, dict_3g, dict_nr)
