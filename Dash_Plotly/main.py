import pandas as pd
from LSI_Solution.pages.dash_app import MultiPageApp


df_TXDC = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_DC_Cal.csv")
df_IIP2 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_IIP2_Cal.csv")
df_Cable = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_CableCheck.csv")
df_TxP_CC_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_TxP_CC_3G.csv")

df_FBRX_GM_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Gain_Meas_3G.csv")
df_FBRX_GC_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Gain_Code_3G.csv")
df_FBRX_FM_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Freq_Meas_3G.csv")
df_FBRX_FM_3G_ch = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Freq_Meas_CH_3G.csv")
df_FBRX_GM_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Gain_Meas_NR.csv")
df_FBRX_GC_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Gain_Code_NR.csv")
df_FBRX_FM_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Freq_Meas_NR.csv")
df_FBRX_FC_NR = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_FBRX_Freq_Code_NR.csv")

df_RX_Gain_2G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_RX_Gain.csv")
df_Ripple_2G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_RX_Ripple.csv")
df_GMSK_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_GMSK.csv")
df_GMSK_TxL_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_GMSK_TxL.csv")
df_GMSK_Code_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_GMSK_Code.csv")
df_EPSK_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_EPSK.csv")
df_EPSK_TxL_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_EPSK_TxL.csv")
df_EPSK_Code_Mean = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_2G_EPSK_Code.csv")

df_RXGain_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_3G_RX_Gain.csv")
df_RXComp_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_3G_RX_Comp.csv")

df_RXGain_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_NR_RX_Gain.csv")
df_RXRSRP_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_NR_RX_RSRP.csv")
df_RXComp_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_NR_RX_Freq.csv")
df_RXMixer_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_NR_RX_Mixer.csv")

df_APT_Meas_3G = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_APT_Meas_3G.csv")
df_APT_Meas_sub6 = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_APT_Meas_Sub6.csv")

df_3G_ET_Pst = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_ETSAPT_3G_Psat.csv")
df_3G_ET_Power = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_ETSAPT_3G_Power.csv")

df_NR_ET_Psat = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_ETSAPT_Sub6_Psat.csv")
df_NR_ET_Pgain = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_ETSAPT_Sub6_Pgain.csv")
df_NR_ET_Power = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_ETSAPT_Sub6_Power.csv")
df_NR_ET_Freq = pd.read_csv("D:\\DATA\\바탕화면\\Exported_Data\\2023_12_19\\CSV_ETSAPT_Sub6_Freq.csv")


dict_cf = {
    "TXDC": df_TXDC,
    "IIP2": df_IIP2,
    "Cable": df_Cable,
}
dict_2g = {
    "RXGain": df_RX_Gain_2G,
    "RXRipp": df_Ripple_2G,
    "GMSK": df_GMSK_Mean,
    "GMSK_TxL": df_GMSK_TxL_Mean,
    "GMSK_Code": df_GMSK_Code_Mean,
    "EPSK": df_EPSK_Mean,
    "EPSK_TxL": df_EPSK_TxL_Mean,
    "EPSK_Code": df_EPSK_Code_Mean,
}
dict_3g = {
    "TxP_CC": df_TxP_CC_3G,
    "RX_Gain": df_RXGain_3G,
    "RX_Comp": df_RXComp_3G,
    "FBRX_GM": df_FBRX_GM_3G,
    "FBRX_GC": df_FBRX_GC_3G,
    "FBRX_FM": df_FBRX_FM_3G,
    "FBRX_FM_Ch": df_FBRX_FM_3G_ch,
    "APT_Meas": df_APT_Meas_3G,
    "ET_Psat": df_3G_ET_Pst,
    "ET_Pgain": df_3G_ET_Power,
}

dict_nr = {
    "RX_Gain": df_RXGain_sub6,
    "RX_RSRP": df_RXRSRP_sub6,
    "RX_Comp": df_RXComp_sub6,
    "RX_Mix": df_RXMixer_sub6,
    "FBRX_GM": df_FBRX_GM_NR,
    "FBRX_GC": df_FBRX_GC_NR,
    "FBRX_FM": df_FBRX_FM_NR,
    "FBRX_FC": df_FBRX_FC_NR,
    "APT_Meas": df_APT_Meas_sub6,
    "ET_Psat": df_NR_ET_Psat,
    "ET_Pgain": df_NR_ET_Pgain,
    "ET_Power": df_NR_ET_Power,
    "ET_Freq": df_NR_ET_Freq,
}

MultiPageApp(dict_cf, dict_2g, dict_3g, dict_nr)
