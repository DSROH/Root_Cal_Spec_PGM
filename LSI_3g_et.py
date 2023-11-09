import re
import tkinter as tk
import pandas as pd
import numpy as np
import Common_function as func


def chng_3g_et_psat_pgain(
    Selected_spc,
    rat,
    band,
    ET_Psat_var,
    ETSAPT_3G_Psat_Ave,
    ETSAPT_3G_Psat_Max,
    ETSAPT_3G_Psat_Min,
    ET_Pgain_var,
    ETSAPT_3G_Power_Ave,
    ETSAPT_3G_Power_Max,
    ETSAPT_3G_Power_Min,
    text_area,
):
    ET_Psat = float(ET_Psat_var.get())  # 1dB = 100
    ET_Pgain = float(ET_Pgain_var.get())
    target_word = f"[{rat}_BAND{band}_Calibration_Spec]"
    band = f"B{band}"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("TX_ET_S-APT_Psat"):
            New_String = Old_String = line
            New_String = et_3g(line, band, ET_Psat, ETSAPT_3G_Psat_Ave, ETSAPT_3G_Psat_Max, ETSAPT_3G_Psat_Min, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_ET_S-APT_Power"):
            New_String = Old_String = line
            New_String = et_3g(line, band, ET_Pgain, ETSAPT_3G_Power_Ave, ETSAPT_3G_Power_Max, ETSAPT_3G_Power_Min, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("TX_DC_I"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def et_3g(line, band, spec, df1, df2, df3, text_area):
    New_String = re.split("\t|\n", line)
    New_String = [v for v in New_String if v]
    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
    text_area.see(tk.END)

    if df1.empty:
        New_String[2] = 0
        New_String[3] = round(New_String[2] - spec)
        New_String[4] = round(New_String[2] + spec)
    else:
        New_String[2] = round((np.array([df1[band, "R99"], df1[band, "HSUPA"]])).mean())
        V_min = round((np.array([df3[band, "R99"], df3[band, "HSUPA"]])).min())
        if (V_min - spec) > (New_String[2] - 3):
            New_String[3] = round(New_String[2] - 3, 1)
        else:
            New_String[3] = round(V_min - spec, 1)
        V_max = round((np.array([df2[band, "R99"], df2[band, "HSUPA"]])).max())
        if (V_max + spec) < (New_String[2] + 3):
            New_String[4] = round(New_String[2] + 3, 1)
        else:
            New_String[4] = round(V_max + spec, 1)
    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def Et_3g_average(df_Meas, Save_data_var, text_area):
    ETSAPT_3G_Psat_Ave, ETSAPT_3G_Psat_Max, ETSAPT_3G_Psat_Min = Et_3g_psat_ave(df_Meas, Save_data_var, text_area)
    ETSAPT_3G_Power_Ave, ETSAPT_3G_Power_Max, ETSAPT_3G_Power_Min = Et_3g_power_ave(df_Meas, Save_data_var, text_area)

    return (
        ETSAPT_3G_Psat_Ave,
        ETSAPT_3G_Psat_Max,
        ETSAPT_3G_Psat_Min,
        ETSAPT_3G_Power_Ave,
        ETSAPT_3G_Power_Max,
        ETSAPT_3G_Power_Min,
    )


def Et_3g_psat_ave(df_Meas, Save_data_var, text_area):
    df_hspa = df_Meas[df_Meas["Test Conditions"].str.contains("WCDMA_").to_list()]
    df_et_psat = df_hspa[df_hspa["Test Conditions"].str.contains("_ET_S-APT_PSat").to_list()]

    if df_et_psat.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    else:
        df_et_psat_Value = df_et_psat.iloc[:, 1:].astype(float)
        df_et_psat_Item = df_et_psat["Test Conditions"].str.split("_", expand=True)
        # 의미없는 컬럼 삭제
        df_et_psat_Item.drop(columns=[0, 2, 3, 5, 6, 7], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_et_psat_Item.columns = ["Band", "R99"]
        df_et_psat = pd.merge(df_et_psat_Item, df_et_psat_Value, left_index=True, right_index=True)
        df_et_psat_mean = round(df_et_psat.groupby(["Band", "R99"], sort=False).mean(), 2)
        df_et_psat_max = round(df_et_psat.groupby(["Band", "R99"], sort=False).max(), 2)
        df_et_psat_min = round(df_et_psat.groupby(["Band", "R99"], sort=False).min(), 2)

        df_et_psat_mean = pd.concat([df_et_psat_mean, round(df_et_psat_mean.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_psat_mean = pd.concat([df_et_psat_mean, round(df_et_psat_mean.max(axis=1), 1).rename("Max")], axis=1)
        df_et_psat_mean = pd.concat([df_et_psat_mean, round(df_et_psat_mean.min(axis=1), 1).rename("Min")], axis=1)
        df_et_psat_max = pd.concat([df_et_psat_max, round(df_et_psat_max.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_psat_max = pd.concat([df_et_psat_max, round(df_et_psat_max.max(axis=1), 1).rename("Max")], axis=1)
        df_et_psat_max = pd.concat([df_et_psat_max, round(df_et_psat_max.min(axis=1), 1).rename("Min")], axis=1)
        df_et_psat_min = pd.concat([df_et_psat_min, round(df_et_psat_min.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_psat_min = pd.concat([df_et_psat_min, round(df_et_psat_min.max(axis=1), 1).rename("Max")], axis=1)
        df_et_psat_min = pd.concat([df_et_psat_min, round(df_et_psat_min.min(axis=1), 1).rename("Min")], axis=1)

        if Save_data_var.get():
            filename = "Excel_ETSAPT_3G_Psat.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_et_psat_mean.to_excel(writer, sheet_name="ETSAPT_3G_Psat_Ave")
                df_et_psat_max.to_excel(writer, sheet_name="ETSAPT_3G_Psat_Max")
                df_et_psat_min.to_excel(writer, sheet_name="ETSAPT_3G_Psat_Min")
            func.WB_Format(filename, 2, 3, 0, text_area)

        return df_et_psat_mean["Average"], df_et_psat_max["Average"], df_et_psat_min["Average"]


def Et_3g_power_ave(df_Meas, Save_data_var, text_area):
    df_hspa = df_Meas[df_Meas["Test Conditions"].str.contains("WCDMA_").to_list()]
    df_et_power = df_hspa[df_hspa["Test Conditions"].str.contains("_ET_S-APT_Power").to_list()]

    if df_et_power.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    else:
        df_et_power_Value = df_et_power.iloc[:, 1:].astype(float)
        df_et_power_Item = df_et_power["Test Conditions"].str.split("_", expand=True)
        # 의미없는 컬럼 삭제
        df_et_power_Item.drop(columns=[0, 2, 3, 5, 6, 7], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_et_power_Item.columns = ["Band", "R99"]
        df_et_power = pd.merge(df_et_power_Item, df_et_power_Value, left_index=True, right_index=True)
        df_et_power_mean = round(df_et_power.groupby(["Band", "R99"], sort=False).mean(), 2)
        df_et_power_max = round(df_et_power.groupby(["Band", "R99"], sort=False).max(), 2)
        df_et_power_min = round(df_et_power.groupby(["Band", "R99"], sort=False).min(), 2)
        df_et_power_mean = pd.concat([df_et_power_mean, round(df_et_power_mean.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_power_mean = pd.concat([df_et_power_mean, round(df_et_power_mean.max(axis=1), 1).rename("Max")], axis=1)
        df_et_power_mean = pd.concat([df_et_power_mean, round(df_et_power_mean.min(axis=1), 1).rename("Min")], axis=1)
        df_et_power_max = pd.concat([df_et_power_max, round(df_et_power_max.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_power_max = pd.concat([df_et_power_max, round(df_et_power_max.max(axis=1), 1).rename("Max")], axis=1)
        df_et_power_max = pd.concat([df_et_power_max, round(df_et_power_max.min(axis=1), 1).rename("Min")], axis=1)
        df_et_power_min = pd.concat([df_et_power_min, round(df_et_power_min.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_power_min = pd.concat([df_et_power_min, round(df_et_power_min.max(axis=1), 1).rename("Max")], axis=1)
        df_et_power_min = pd.concat([df_et_power_min, round(df_et_power_min.min(axis=1), 1).rename("Min")], axis=1)

        if Save_data_var.get():
            filename = "Excel_ETSAPT_3G_Power.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_et_power_mean.to_excel(writer, sheet_name="ETSAPT_3G_Power_Ave")
                df_et_power_max.to_excel(writer, sheet_name="ETSAPT_3G_Power_Max")
                df_et_power_min.to_excel(writer, sheet_name="ETSAPT_3G_Power_Min")
            func.WB_Format(filename, 2, 3, 0, text_area)

        return df_et_power_mean["Average"], df_et_power_max["Average"], df_et_power_min["Average"]
