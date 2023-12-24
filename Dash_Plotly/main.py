import pandas as pd
from LSI_Solution.pages.dash_app import MultiPageApp

df_TXDC = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_IIP2 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_Cable = pd.read_csv("Excel_DC_IIP2_Cal.csv")

df_RX_Gain_2G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_Ripple_2G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_GMSK_Mean = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_GMSK_TxL_Mean = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_GMSK_Code_Mean = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_EPSK_Mean = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_EPSK_TxL_Mean = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_EPSK_Code_Mean = pd.read_csv("Excel_DC_IIP2_Cal.csv")

df_TxP_CC_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXGain_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXComp_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_FBRX_GM_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_FBRX_GC_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_FBRX_FM_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_FBRX_FM_3G_ch = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_APT_Meas_3G = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_3G_ET_Pst = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_3G_ET_Power = pd.read_csv("Excel_DC_IIP2_Cal.csv")

df_RXGain_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXRSRP_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXComp_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_RXMixer_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_FBRX_GM_NR = pd.read_csv("Excel_FBRX_Gain_Cal.csv")
df_FBRX_GC_NR = pd.read_csv("Excel_FBRX_Gain_Cal.csv")
df_FBRX_FM_NR = pd.read_csv("Excel_FBRX_Freq_Cal.csv")
df_FBRX_FC_NR = pd.read_csv("Excel_FBRX_Freq_Cal.csv")
df_APT_Meas_sub6 = pd.read_csv("Excel_DC_IIP2_Cal.csv")
df_NR_ET_Psat = pd.read_csv("Excel_ET_SAPT_Psat.csv")
df_NR_ET_Pgain = pd.read_csv("Excel_ET_SAPT_Psat.csv")
df_NR_ET_Power = pd.read_csv("Excel_ET_SAPT_Psat.csv")
df_NR_ET_Freq = pd.read_csv("Excel_ET_SAPT_Freq.csv")

dict_cf = {"txdc": df_TXDC, "iip2": df_IIP2, "cable": df_Cable}
dict_2g = {
    "rx_gain": df_RX_Gain_2G,
    "rx_ripp": df_Ripple_2G,
    "gmsk": df_GMSK_Mean,
    "gmsk_txl": df_GMSK_TxL_Mean,
    "gmsk_code": df_GMSK_Code_Mean,
    "epsk": df_EPSK_Mean,
    "epsk_txl": df_EPSK_TxL_Mean,
    "epsk_code": df_EPSK_Code_Mean,
}
dict_3g = {
    "rx_gain": df_RXGain_3G,
    "rx_comp": df_RXComp_3G,
    "fbrx_gm": df_FBRX_GM_3G,
    "fbrx_gc": df_FBRX_GC_3G,
    "fbrx_fm": df_FBRX_FM_3G,
    "fbrx_fm_ch": df_FBRX_FM_3G_ch,
    "apt_meas": df_APT_Meas_3G,
    "txp_cc": df_TxP_CC_3G,
    "et_psat": df_3G_ET_Pst,
    "et_power": df_3G_ET_Power,
}

dict_nr = {
    "rx_gain": df_RXGain_sub6,
    "rx_rsrp": df_RXRSRP_sub6,
    "rx_comp": df_RXComp_sub6,
    "rx_mix": df_RXMixer_sub6,
    "fbrx_gm": df_FBRX_GM_NR,
    "fbrx_gc": df_FBRX_GC_NR,
    "fbrx_fm": df_FBRX_FM_NR,
    "fbrx_fc": df_FBRX_FC_NR,
    "apt_meas": df_APT_Meas_sub6,
    "et_psat": df_NR_ET_Psat,
    "et_pgain": df_NR_ET_Pgain,
    "et_power": df_NR_ET_Power,
    "et_freq": df_NR_ET_Freq,
}

MultiPageApp(dict_cf, dict_2g, dict_3g, dict_nr)
