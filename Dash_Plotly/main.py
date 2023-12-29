import pandas as pd
from LSI_Solution.pages.dash_app import MultiPageApp

df_TXDC = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_DC_Cal.csv")
df_IIP2 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_IIP2_Cal.csv")
df_Cable = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_CableCheck.csv")
df_TxP_CC_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_TxP_CC_3G.csv")

df_RX_Gain_2G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_RX_Gain.csv")
df_Ripple_2G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_RX_Ripple.csv")
df_GMSK_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_GMSK.csv")
df_GMSK_TxL_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_GMSK_TxL.csv")
df_GMSK_Code_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_GMSK_Code.csv")
df_EPSK_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_EPSK.csv")
df_EPSK_TxL_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_EPSK_TxL.csv")
df_EPSK_Code_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_2G_EPSK_Code.csv")

df_RXGain_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_3G_RX_Gain.csv")
df_RXComp_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_3G_RX_Comp.csv")

df_FBRX_GM_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Gain_Meas_3G.csv")
df_FBRX_GC_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Gain_Code_3G.csv")
df_FBRX_FM_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Freq_Meas_3G.csv")
df_FBRX_FM_3G_ch = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Freq_Meas_CH_3G.csv")
df_APT_Meas_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_APT_Meas_3G.csv")

df_3G_ET_Pst = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_ETSAPT_3G_Psat.csv")
df_3G_ET_Power = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_ETSAPT_3G_Power.csv")

df_RXGain_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_NR_RX_Gain.csv")
df_RXRSRP_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_NR_RX_RSRP.csv")
df_RXComp_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_NR_RX_Freq.csv")
df_RXMixer_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_NR_RX_Mixer.csv")

df_FBRX_GM_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Gain_Meas_NR.csv")
df_FBRX_GC_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Gain_Code_NR.csv")
df_FBRX_FM_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Freq_Meas_NR.csv")
df_FBRX_FC_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_FBRX_Freq_Code_NR.csv")
df_APT_Meas_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_APT_Meas_Sub6.csv")
df_Therm = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_Thermistor.csv")

df_NR_ET_Psat = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_ETSAPT_Sub6_Psat.csv")
df_NR_ET_Pgain = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_ETSAPT_Sub6_Pgain.csv")
df_NR_ET_Power = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_ETSAPT_Sub6_Power.csv")
df_NR_ET_Freq = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_ETSAPT_Sub6_Freq.csv")
df_BW_Cal = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_29\\CSV_BW_Cal.csv")

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
    "therm": df_Therm,
    "bw_cal": df_BW_Cal,
    "et_psat": df_NR_ET_Psat,
    "et_pgain": df_NR_ET_Pgain,
    "et_power": df_NR_ET_Power,
    "et_freq": df_NR_ET_Freq,
}

MultiPageApp(dict_cf, dict_2g, dict_3g, dict_nr)
