import re
import tkinter as tk
import pandas as pd
import LSI_Solution.Common.Function as func


def Fbrx_ave(df_Meas, df_Code, Save_data, text_area):
    Gain_Meas_3G, Gain_Meas_NR = Fbrx_gain_meas_ave(df_Meas, Save_data, text_area)
    Gain_Code_3G, Gain_Code_NR = Fbrx_gain_code_ave(df_Code, Save_data, text_area)
    # FBRX Gain은 센터채널만 하기 때문에 편차가 적으나, FBRX Freq는 Min, Max 편차 발생함 -> Min, Max 구해서 스펙에 반영
    Freq_Meas_3G, Freq_Meas_3G_CH, Freq_Meas_NR = Fbrx_freq_meas_ave(df_Meas, Save_data, text_area)
    Freq_Code_NR = Fbrx_nr_freq_code_ave(df_Code, Save_data, text_area)

    return Gain_Meas_3G, Gain_Code_3G, Freq_Meas_3G, Freq_Meas_3G_CH, Gain_Meas_NR, Gain_Code_NR, Freq_Meas_NR, Freq_Code_NR


def Fbrx_gain_meas_ave(df_Meas, Save_data, text_area):
    df_3g_fbrx_gain = df_Meas[df_Meas["Test Conditions"].str.contains("_FBRX_Gain_").to_list()]
    df_3g_fbrx_gain_Value = df_3g_fbrx_gain.iloc[:, 1:].astype(float)
    df_3g_fbrx_gain_Item = df_3g_fbrx_gain["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_3g_fbrx_gain_Item.drop(columns=[3, 4, 5], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_3g_fbrx_gain_Item.columns = ["RAT", "Band", "Path", "Index"]
    df_3g_fbrx_gain = pd.merge(df_3g_fbrx_gain_Item, df_3g_fbrx_gain_Value, left_index=True, right_index=True)
    df_3g_fbrx_gain_Mean = round(df_3g_fbrx_gain.groupby(["RAT", "Band", "Path", "Index"], sort=False).mean(), 1)
    df_3g_fbrx_gain_Max = round(df_3g_fbrx_gain.groupby(["RAT", "Band", "Path", "Index"], sort=False).max(), 1)
    df_3g_fbrx_gain_Min = round(df_3g_fbrx_gain.groupby(["RAT", "Band", "Path", "Index"], sort=False).min(), 1)
    # df_3g_fbrx_gain_Data = round(df_3g_fbrx_gain.groupby(["RAT", "Band", "Index"]).agg(["mean", "max", "min"]), 2)
    df_3g_fbrx_gain_Mean = pd.concat(
        [df_3g_fbrx_gain_Mean, round(df_3g_fbrx_gain_Mean.mean(axis=1), 2).rename("Average")], axis=1
    )
    df_3g_fbrx_gain_Mean = pd.concat([df_3g_fbrx_gain_Mean, round(df_3g_fbrx_gain_Max.max(axis=1), 2).rename("Max")], axis=1)
    df_3g_fbrx_gain_Mean = pd.concat([df_3g_fbrx_gain_Mean, round(df_3g_fbrx_gain_Min.min(axis=1), 2).rename("Min")], axis=1)

    df_nr_fbrx_gain = df_Meas[df_Meas["Test Conditions"].str.contains("_FBRX_Index").to_list()]
    df_nr_fbrx_gain_Value = df_nr_fbrx_gain.iloc[:, 1:].astype(float)
    df_nr_fbrx_gain_Item = df_nr_fbrx_gain["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_nr_fbrx_gain_Item.drop(columns=[3, 4], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_nr_fbrx_gain_Item.columns = ["RAT", "Band", "Path", "Index"]
    df_nr_fbrx_gain = pd.merge(df_nr_fbrx_gain_Item, df_nr_fbrx_gain_Value, left_index=True, right_index=True)
    df_nr_fbrx_gain_Mean = round(df_nr_fbrx_gain.groupby(["RAT", "Band", "Path", "Index"], sort=False).mean(), 1)
    df_nr_fbrx_gain_Max = round(df_nr_fbrx_gain.groupby(["RAT", "Band", "Path", "Index"], sort=False).max(), 1)
    df_nr_fbrx_gain_Min = round(df_nr_fbrx_gain.groupby(["RAT", "Band", "Path", "Index"], sort=False).min(), 1)
    # df_nr_fbrx_gain_Data = round(df_nr_fbrx_gain.groupby(["RAT", "Band","Path", "Index"]).agg(["mean", "max", "min"]), 2)
    df_nr_fbrx_gain_Mean = pd.concat(
        [df_nr_fbrx_gain_Mean, round(df_nr_fbrx_gain_Mean.mean(axis=1), 2).rename("Average")], axis=1
    )
    df_nr_fbrx_gain_Mean = pd.concat([df_nr_fbrx_gain_Mean, round(df_nr_fbrx_gain_Max.max(axis=1), 2).rename("Max")], axis=1)
    df_nr_fbrx_gain_Mean = pd.concat([df_nr_fbrx_gain_Mean, round(df_nr_fbrx_gain_Min.min(axis=1), 2).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_FBRX_Gain_Meas.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_3g_fbrx_gain_Mean.to_excel(writer, sheet_name="Gain_Meas_3G_Mean")
            df_nr_fbrx_gain_Mean.to_excel(writer, sheet_name="Gain_Meas_NR_Mean")
        func.WB_Format(filename, 2, 5, 0, text_area)

        df_3g_fbrx_gain_Mean.to_csv("CSV_FBRX_Gain_Meas_3G.csv", encoding="utf-8-sig")
        df_nr_fbrx_gain_Mean.to_csv("CSV_FBRX_Gain_Meas_NR.csv", encoding="utf-8-sig")

    return df_3g_fbrx_gain_Mean, df_nr_fbrx_gain_Mean


def Fbrx_gain_code_ave(df_Code, Save_data, text_area):
    df_3g_fbrx_code = df_Code[df_Code["Test Conditions"].str.contains("_Modulation_FBRX_Result").to_list()]
    df_3g_fbrx_code_Value = df_3g_fbrx_code.iloc[:, 1:].astype(int)
    df_3g_fbrx_code_Item = df_3g_fbrx_code["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_3g_fbrx_code_Item.drop(columns=[4, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_3g_fbrx_code_Item.columns = ["RAT", "Band", "Path", "CH"]
    df_3g_fbrx_code = pd.merge(df_3g_fbrx_code_Item, df_3g_fbrx_code_Value, left_index=True, right_index=True)
    df_3g_fbrx_code_mean = round(df_3g_fbrx_code.groupby(["RAT", "Band", "Path", "CH"], sort=False).mean())
    df_3g_fbrx_code_max = round(df_3g_fbrx_code.groupby(["RAT", "Band", "Path", "CH"], sort=False).max())
    df_3g_fbrx_code_min = round(df_3g_fbrx_code.groupby(["RAT", "Band", "Path", "CH"], sort=False).min())
    # df_3g_fbrx_code_data = round(df_3g_fbrx_code.groupby(["RAT", "Band", "CH"]).agg(["mean", "max", "min"]))
    df_3g_fbrx_code_mean = pd.concat([df_3g_fbrx_code_mean, round(df_3g_fbrx_code_mean.mean(axis=1)).rename("Average")], axis=1)
    df_3g_fbrx_code_mean = pd.concat([df_3g_fbrx_code_mean, round(df_3g_fbrx_code_max.max(axis=1)).rename("Max")], axis=1)
    df_3g_fbrx_code_mean = pd.concat([df_3g_fbrx_code_mean, round(df_3g_fbrx_code_min.min(axis=1)).rename("Min")], axis=1)

    df_nr_fbrx_code = df_Code[df_Code["Test Conditions"].str.contains("_FBRX_Index").to_list()]
    df_nr_fbrx_code_Value = df_nr_fbrx_code.iloc[:, 1:].astype(int)
    df_nr_fbrx_code_Item = df_nr_fbrx_code["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_nr_fbrx_code_Item.drop(columns=[3, 4], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_nr_fbrx_code_Item.columns = ["RAT", "Band", "Path", "Index"]
    df_nr_fbrx_code = pd.merge(df_nr_fbrx_code_Item, df_nr_fbrx_code_Value, left_index=True, right_index=True)
    df_nr_fbrx_code_mean = round(df_nr_fbrx_code.groupby(["RAT", "Band", "Path", "Index"], sort=False).mean())
    df_nr_fbrx_code_max = round(df_nr_fbrx_code.groupby(["RAT", "Band", "Path", "Index"], sort=False).max())
    df_nr_fbrx_code_min = round(df_nr_fbrx_code.groupby(["RAT", "Band", "Path", "Index"], sort=False).min())
    # df_nr_fbrx_code_data = round(df_nr_fbrx_code.groupby(["RAT", "Path", "Band", "Index"]).agg(["mean", "max", "min"]))
    df_nr_fbrx_code_mean = pd.concat([df_nr_fbrx_code_mean, round(df_nr_fbrx_code_mean.mean(axis=1)).rename("Average")], axis=1)
    df_nr_fbrx_code_mean = pd.concat([df_nr_fbrx_code_mean, round(df_nr_fbrx_code_max.max(axis=1)).rename("Max")], axis=1)
    df_nr_fbrx_code_mean = pd.concat([df_nr_fbrx_code_mean, round(df_nr_fbrx_code_min.min(axis=1)).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_FBRX_Gain_Code.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_3g_fbrx_code_mean.to_excel(writer, sheet_name="Gain_Code_3G_Mean")
            df_nr_fbrx_code_mean.to_excel(writer, sheet_name="Gain_Code_NR_Mean")
        func.WB_Format(filename, 2, 5, 0, text_area)

        df_3g_fbrx_code_mean.to_csv("CSV_FBRX_Gain_Code_3G.csv", encoding="utf-8-sig")
        df_nr_fbrx_code_mean.to_csv("CSV_FBRX_Gain_Code_NR.csv", encoding="utf-8-sig")

    return df_3g_fbrx_code_mean, df_nr_fbrx_code_mean


def Fbrx_freq_meas_ave(df_Meas, Save_data, text_area):
    df_3g_drop = df_Meas[df_Meas["Test Conditions"].str.contains("_FBRX_Gain_Index")].index
    df_Meas.drop(df_3g_drop, inplace=True)
    df_3g = df_Meas[df_Meas["Test Conditions"].str.contains("WCDMA").to_list()]
    df_3g_fbrx_freq = df_3g[df_3g["Test Conditions"].str.contains("CH_FBRX_").to_list()]
    df_3g_fbrx_freq_Value = df_3g_fbrx_freq.iloc[:, 1:].astype(float)
    df_3g_fbrx_freq_Item = df_3g_fbrx_freq["Test Conditions"].str.split("_", expand=True)
    df_3g_fbrx_freq_chitem = df_3g_fbrx_freq_Item.copy()
    # 의미없는 컬럼 삭제
    df_3g_fbrx_freq_Item.drop(columns=[3, 5], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_3g_fbrx_freq_Item.columns = ["RAT", "Band", "Path", "FBRX"]
    df_3g_fbrx_freq = pd.merge(df_3g_fbrx_freq_Item, df_3g_fbrx_freq_Value, left_index=True, right_index=True)
    df_3g_fbrx_freq_mean = round(df_3g_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).mean())
    df_3g_fbrx_freq_max = round(df_3g_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).max())
    df_3g_fbrx_freq_min = round(df_3g_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).min())
    # df_3g_fbrx_freq_data = round(df_3g_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"]).agg(["mean", "max", "min"]))
    df_3g_fbrx_freq_mean = pd.concat(
        [df_3g_fbrx_freq_mean, round(df_3g_fbrx_freq_mean.mean(axis=1), 2).rename("Average")], axis=1
    )
    df_3g_fbrx_freq_mean = pd.concat([df_3g_fbrx_freq_mean, round(df_3g_fbrx_freq_max.max(axis=1), 2).rename("Max")], axis=1)
    df_3g_fbrx_freq_mean = pd.concat([df_3g_fbrx_freq_mean, round(df_3g_fbrx_freq_min.min(axis=1), 2).rename("Min")], axis=1)
    df_3g_fbrx_freq_max = pd.concat([df_3g_fbrx_freq_max, round(df_3g_fbrx_freq_max.max(axis=1), 2).rename("Max")], axis=1)
    df_3g_fbrx_freq_max = pd.concat([df_3g_fbrx_freq_max, round(df_3g_fbrx_freq_max.min(axis=1), 2).rename("Min")], axis=1)
    df_3g_fbrx_freq_min = pd.concat([df_3g_fbrx_freq_min, round(df_3g_fbrx_freq_min.max(axis=1), 2).rename("Max")], axis=1)
    df_3g_fbrx_freq_min = pd.concat([df_3g_fbrx_freq_min, round(df_3g_fbrx_freq_min.min(axis=1), 2).rename("Min")], axis=1)

    # ** ========================== FBRX Freq Dash graph 위한 Dataframe 생성 ==========================

    df_3g_fbrx_freq_chitem.drop(columns=[4, 5], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_3g_fbrx_freq_chitem.columns = ["RAT", "Band", "Path", "CH"]
    df_3g_fbrx_freq_ch = pd.merge(df_3g_fbrx_freq_chitem, df_3g_fbrx_freq_Value, left_index=True, right_index=True)
    df_3g_fbrx_freq_ch_mean = round(df_3g_fbrx_freq_ch.groupby(["RAT", "Band", "Path", "CH"], sort=False).mean(), 2)

    # df_3g_fbrx_freq_data = round(df_3g_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"]).agg(["mean", "max", "min"]))
    df_3g_fbrx_freq_ch_mean = pd.concat(
        [df_3g_fbrx_freq_ch_mean, round(df_3g_fbrx_freq_ch_mean.mean(axis=1), 2).rename("Average")], axis=1
    )

    # ** ========================== FBRX Freq Dash graph 위한 Dataframe 생성 ==========================

    df_nr_drop = df_Meas[df_Meas["Test Conditions"].str.contains("_FBRX_Index")].index
    df_Meas.drop(df_nr_drop, inplace=True)
    df_nr = df_Meas[df_Meas["Test Conditions"].str.contains("NR").to_list()]
    df_nr_fbrx_freq = df_nr[df_nr["Test Conditions"].str.contains("_FBRX_").to_list()]
    df_nr_fbrx_freq_Value = df_nr_fbrx_freq.iloc[:, 1:].astype(float)
    df_nr_fbrx_freq_Item = df_nr_fbrx_freq["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_nr_fbrx_freq_Item.drop(columns=[3, 5], inplace=True)
    # df_nr_fbrx_freq_Item.drop(columns=[3, 4, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_nr_fbrx_freq_Item.columns = ["RAT", "Band", "Path", "FBRX"]
    df_nr_fbrx_freq = pd.merge(df_nr_fbrx_freq_Item, df_nr_fbrx_freq_Value, left_index=True, right_index=True)
    df_nr_fbrx_freq_mean = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).mean())
    df_nr_fbrx_freq_max = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).max())
    df_nr_fbrx_freq_min = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).min())
    # df_nr_fbrx_freq_data = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"]).agg(["mean", "max", "min"]))
    df_nr_fbrx_freq_mean = pd.concat(
        [df_nr_fbrx_freq_mean, round(df_nr_fbrx_freq_mean.mean(axis=1), 1).rename("Average")], axis=1
    )
    df_nr_fbrx_freq_mean = pd.concat([df_nr_fbrx_freq_mean, round(df_nr_fbrx_freq_max.max(axis=1), 1).rename("Max")], axis=1)
    df_nr_fbrx_freq_mean = pd.concat([df_nr_fbrx_freq_mean, round(df_nr_fbrx_freq_min.min(axis=1), 1).rename("Min")], axis=1)
    df_nr_fbrx_freq_max = pd.concat([df_nr_fbrx_freq_max, round(df_nr_fbrx_freq_max.max(axis=1), 1).rename("Max")], axis=1)
    df_nr_fbrx_freq_max = pd.concat([df_nr_fbrx_freq_max, round(df_nr_fbrx_freq_max.min(axis=1), 1).rename("Min")], axis=1)
    df_nr_fbrx_freq_min = pd.concat([df_nr_fbrx_freq_min, round(df_nr_fbrx_freq_min.max(axis=1), 1).rename("Max")], axis=1)
    df_nr_fbrx_freq_min = pd.concat([df_nr_fbrx_freq_min, round(df_nr_fbrx_freq_min.min(axis=1), 1).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_FBRX_Freq_Meas.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_3g_fbrx_freq_mean.to_excel(writer, sheet_name="Freq_Meas_3G_Mean")
            df_3g_fbrx_freq_max.to_excel(writer, sheet_name="Freq_Meas_3G_Max")
            df_3g_fbrx_freq_min.to_excel(writer, sheet_name="Freq_Meas_3G_Min")
            df_nr_fbrx_freq_mean.to_excel(writer, sheet_name="Freq_Meas_NR_Mean")
            df_nr_fbrx_freq_max.to_excel(writer, sheet_name="Freq_Meas_NR_Max")
            df_nr_fbrx_freq_min.to_excel(writer, sheet_name="Freq_Meas_NR_Min")
        func.WB_Format(filename, 2, 5, 0, text_area)

        df_nr_fbrx_freq_mean.to_csv("CSV_FBRX_Freq_Meas_NR.csv", encoding="utf-8-sig")
        df_3g_fbrx_freq_mean.to_csv("CSV_FBRX_Freq_Meas_3G.csv", encoding="utf-8-sig")
        df_3g_fbrx_freq_ch_mean.to_csv("CSV_FBRX_Freq_Meas_CH_3G.csv", encoding="utf-8-sig")

    return df_3g_fbrx_freq_mean, df_3g_fbrx_freq_ch_mean, df_nr_fbrx_freq_mean


def Fbrx_nr_freq_code_ave(df_Code, Save_data, text_area):
    df_nr_drop = df_Code[df_Code["Test Conditions"].str.contains("_FBRX_Index")].index
    df_Code.drop(df_nr_drop, inplace=True)
    df_nr = df_Code[df_Code["Test Conditions"].str.contains("NR").to_list()]
    df_nr_fbrx_freq = df_nr[df_nr["Test Conditions"].str.contains("_FBRX_").to_list()]
    df_nr_fbrx_freq_Value = df_nr_fbrx_freq.iloc[:, 1:].astype(int)
    df_nr_fbrx_freq_Item = df_nr_fbrx_freq["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_nr_fbrx_freq_Item.drop(columns=[3, 5], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_nr_fbrx_freq_Item.columns = ["RAT", "Band", "Path", "FBRX"]
    df_nr_fbrx_freq = pd.merge(df_nr_fbrx_freq_Item, df_nr_fbrx_freq_Value, left_index=True, right_index=True)
    df_nr_fbrx_freq_mean = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).mean())
    df_nr_fbrx_freq_max = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).max())
    df_nr_fbrx_freq_min = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"], sort=False).min())
    # df_nr_fbrx_freq_data = round(df_nr_fbrx_freq.groupby(["RAT", "Band", "Path", "FBRX"]).agg(["mean", "max", "min"]))
    df_nr_fbrx_freq_mean = pd.concat(
        [df_nr_fbrx_freq_mean, round(df_nr_fbrx_freq_mean.mean(axis=1), 1).rename("Average")], axis=1
    )
    df_nr_fbrx_freq_mean = pd.concat([df_nr_fbrx_freq_mean, round(df_nr_fbrx_freq_max.max(axis=1)).rename("Max")], axis=1)
    df_nr_fbrx_freq_mean = pd.concat([df_nr_fbrx_freq_mean, round(df_nr_fbrx_freq_min.min(axis=1)).rename("Min")], axis=1)
    df_nr_fbrx_freq_max = pd.concat([df_nr_fbrx_freq_max, round(df_nr_fbrx_freq_max.max(axis=1)).rename("Max")], axis=1)
    df_nr_fbrx_freq_max = pd.concat([df_nr_fbrx_freq_max, round(df_nr_fbrx_freq_max.min(axis=1)).rename("Min")], axis=1)
    df_nr_fbrx_freq_min = pd.concat([df_nr_fbrx_freq_min, round(df_nr_fbrx_freq_min.max(axis=1)).rename("Max")], axis=1)
    df_nr_fbrx_freq_min = pd.concat([df_nr_fbrx_freq_min, round(df_nr_fbrx_freq_min.min(axis=1)).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_FBRX_Freq_Code.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_nr_fbrx_freq_mean.to_excel(writer, sheet_name="Freq_Code_NR_Mean")
            df_nr_fbrx_freq_max.to_excel(writer, sheet_name="Freq_Code_NR_Max")
            df_nr_fbrx_freq_min.to_excel(writer, sheet_name="Freq_Code_NR_Min")
        func.WB_Format(filename, 2, 4, 0, text_area)

        df_nr_fbrx_freq_mean.to_csv("CSV_FBRX_Freq_Code_NR.csv", encoding="utf-8-sig")

    return df_nr_fbrx_freq_mean


def chng_sub6_fbrx_gain_meas(Selected_spc, rat, band, FBRX_Meas_var, df_FBRX_Gain_Meas_sub6, text_area):
    FBRX_Gain_Meas_sub6 = df_FBRX_Gain_Meas_sub6["Average"]
    FBRX_Spec = int(FBRX_Meas_var.get())
    band = f"n{band}"
    target_word = f"[{rat}_{band}_Calibration_Spec]"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("TX_FBRX_Pow_Index_"):
            New_String = Old_String = line
            New_String = sub6_fbrx_gain_meas(line, band, FBRX_Spec, FBRX_Gain_Meas_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_FBRX_Pow_Index_"):
            New_String = Old_String = line
            New_String = sub6_fbrx_gain_meas(line, band, FBRX_Spec, FBRX_Gain_Meas_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("// TX FBRX FREQ"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_fbrx_gain_meas(line, band, FBRX_Spec, FBRX_Gain_Meas_sub6, text_area):
    New_String = re.split("\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"
    gainstage = int(Word[4])
    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
    New_String[2] = round(FBRX_Gain_Meas_sub6["NR", band, Path, f"Index{gainstage} "])
    New_String[3] = New_String[2] - FBRX_Spec
    New_String[4] = New_String[2] + FBRX_Spec
    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def chng_sub6_fbrx_gain_code(Selected_spc, rat, band, FBRX_Code_var, df_FBRX_Gain_Code_sub6, text_area):
    FBRX_Gain_Code_sub6 = df_FBRX_Gain_Code_sub6["Average"]
    FBRX_Spec = int(FBRX_Code_var.get())
    band = f"n{band}"
    target_word = f"[{rat}_{band}_Calibration_Spec]"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("TX_FBRX_Code_Index_"):
            New_String = Old_String = line
            New_String = sub6_fbrx_gain_code(line, band, FBRX_Spec, FBRX_Gain_Code_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_FBRX_Code_Index_"):
            New_String = Old_String = line
            New_String = sub6_fbrx_gain_code(line, band, FBRX_Spec, FBRX_Gain_Code_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("// TX FBRX FREQ"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_fbrx_gain_code(line, band, FBRX_Spec, FBRX_Gain_Code_sub6, text_area):
    New_String = re.split("\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"
    gainstage = int(Word[4])
    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
    New_String[2] = round(FBRX_Gain_Code_sub6["NR", band, Path, f"Index{gainstage} "])
    New_String[3] = New_String[2] - FBRX_Spec
    New_String[4] = New_String[2] + FBRX_Spec
    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def chng_sub6_fbrx_freq_meas(Selected_spc, rat, band, FBRX_Meas_var, df_FBRX_Freq_Meas_sub6, text_area):
    FBRX_Spec = int(FBRX_Meas_var.get())
    band = f"n{band}"
    target_word = f"[{rat}_{band}_Calibration_Spec]"
    new_text_content = ""
    Cable = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            Cable = True
            new_text_content += line
        elif Cable & line.startswith("TX_FBRX_Channel_Pow"):
            New_String = Old_String = line
            New_String = sub6_fbrx_freq_meas(line, band, FBRX_Spec, df_FBRX_Freq_Meas_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Cable & line.startswith("TX2_FBRX_Channel_Pow"):
            New_String = Old_String = line
            New_String = sub6_fbrx_freq_meas(line, band, FBRX_Spec, df_FBRX_Freq_Meas_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("// APT"):
            new_text_content += line
            Cable = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_fbrx_freq_meas(line, band, FBRX_Spec, df_FBRX_Freq_Meas_sub6, text_area):
    FBRX_Freq_Meas_sub6 = df_FBRX_Freq_Meas_sub6["Average"]
    FBRX_Freq_Meas_sub6_Max = df_FBRX_Freq_Meas_sub6["Max"]
    FBRX_Freq_Meas_sub6_Min = df_FBRX_Freq_Meas_sub6["Min"]

    New_String = re.split("\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"
    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
    New_String[2] = round(FBRX_Freq_Meas_sub6["NR", band, Path, "FBRX"])
    New_String[3] = round(FBRX_Freq_Meas_sub6_Min["NR", band, Path, "FBRX"]) - FBRX_Spec
    New_String[4] = round(FBRX_Freq_Meas_sub6_Max["NR", band, Path, "FBRX"]) + FBRX_Spec
    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def chng_sub6_fbrx_freq_code(Selected_spc, rat, band, FBRX_Code_var, df_FBRX_Freq_Code_sub6, text_area):
    FBRX_Spec = int(FBRX_Code_var.get())
    band = f"n{band}"
    target_word = f"[{rat}_{band}_Calibration_Spec]"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("TX_FBRX_Channel_Code"):
            New_String = Old_String = line
            New_String = sub6_fbrx_freq_code(line, band, FBRX_Spec, df_FBRX_Freq_Code_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_FBRX_Channel_Code"):
            New_String = Old_String = line
            New_String = sub6_fbrx_freq_code(line, band, FBRX_Spec, df_FBRX_Freq_Code_sub6, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("// APT"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_fbrx_freq_code(line, band, FBRX_Spec, df_FBRX_Freq_Code_sub6, text_area):
    FBRX_Freq_Code_sub6 = df_FBRX_Freq_Code_sub6["Average"]
    FBRX_Freq_Code_sub6_Max = df_FBRX_Freq_Code_sub6["Max"]
    FBRX_Freq_Code_sub6_Min = df_FBRX_Freq_Code_sub6["Min"]
    New_String = re.split("\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"
    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
    New_String[2] = round(FBRX_Freq_Code_sub6["NR", band, Path, "FBRX"])
    New_String[3] = round(FBRX_Freq_Code_sub6_Min["NR", band, Path, "FBRX"]) - FBRX_Spec
    New_String[4] = round(FBRX_Freq_Code_sub6_Max["NR", band, Path, "FBRX"]) + FBRX_Spec
    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String
