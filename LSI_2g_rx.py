import re
import tkinter as tk
import numpy as np
import pandas as pd
import Common_function as func


def rx_gain(PRX_Gain_2G, RX_Gain_2G_Spec, band, spec_only, String, text_area):
    text_area.insert(tk.END, f"{String[0]:<30}| {String[3]:>5}\t{String[4]:>5}\t\t\u2192\t")
    text_area.see(tk.END)

    if spec_only == "Spec_Only":
        RX_agcoffset = [float(String[3]), float(String[4])]
        RX_agc_mean = np.mean(RX_agcoffset)
        String[2] = round(int(RX_agc_mean))
        String[3] = round(int(RX_agc_mean) - RX_Gain_2G_Spec)
        String[4] = round(int(RX_agc_mean) + RX_Gain_2G_Spec)
    else:
        String[2] = round(PRX_Gain_2G[band])
        String[3] = round(int(String[2]) - RX_Gain_2G_Spec)
        String[4] = round(int(String[2]) + RX_Gain_2G_Spec)

    text_area.insert(tk.END, f"{String[3]:>5}\t{String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = "\t".join(map(str, String)) + "\n"

    return New_String


def chng_2g_rx_gain(Selected_spc, band, RX_Gain_2G_Spec_var, PRX_Gain_2G, Ripple_2G, text_area):
    RX_Gain_2G_Spec = int(RX_Gain_2G_Spec_var.get())  # 1dB = 100
    target_word = f"[{band}_Calibration_Spec]"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("Rx_AGCOffset_0"):
            String = Old_String = line
            String = re.split("\t|\n", line)
            String = [v for v in String if v]
            New_String = rx_gain(PRX_Gain_2G, RX_Gain_2G_Spec, band, "daseul", String, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("Rx_Ripple"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", New_String)
            New_String = [v for v in New_String if v]
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[2]:>5}\t{New_String[3]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            New_String[3] = round(Ripple_2G[band]) + 2
            text_area.insert(tk.END, f"{New_String[2]:>5}\t{New_String[3]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("GMSK_Ref_Power0"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def daseul_2g_rx_average(df_Meas, Save_data_var, text_area):
    df_2g_gain = df_Meas[df_Meas["Test Conditions"].str.contains("CH_RxCalPower -60.00Bm").to_list()]
    df_2g_gain_Value = df_2g_gain.iloc[:, 1:].astype(float)
    df_2g_gain_Item = df_2g_gain["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_2g_gain_Item.drop(columns=[1, 2, 3, 4], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_2g_gain_Item.columns = ["Band"]
    df_2g_gain_Item = df_2g_gain_Item.replace({"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}})
    df_2g_gain = pd.merge(df_2g_gain_Item, df_2g_gain_Value, left_index=True, right_index=True)
    df_2g_gain_Mean = round(df_2g_gain.groupby(["Band"]).mean(), 1)
    df_2g_gain_Mean = pd.concat([df_2g_gain_Mean, round(df_2g_gain_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_2g_gain_Mean = pd.concat([df_2g_gain_Mean, round(df_2g_gain_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_2g_gain_Mean = pd.concat([df_2g_gain_Mean, round(df_2g_gain_Mean.min(axis=1), 1).rename("Min")], axis=1)

    df_2g_ripple = df_Meas[df_Meas["Test Conditions"].str.contains("_RX_Ripple").to_list()]
    df_2g_ripple_Value = df_2g_ripple.iloc[:, 1:].astype(float)
    df_2g_ripple_Item = df_2g_ripple["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_2g_ripple_Item.drop(columns=[1, 2, 3], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_2g_ripple_Item.columns = ["Band"]
    df_2g_ripple_Item = df_2g_ripple_Item.replace(
        {"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}}
    )
    df_2g_ripple = pd.merge(df_2g_ripple_Item, df_2g_ripple_Value, left_index=True, right_index=True)
    df_2g_ripple_Mean = round(df_2g_ripple.groupby(["Band"]).mean(), 1)
    df_2g_ripple_Mean = pd.concat([df_2g_ripple_Mean, round(df_2g_ripple_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_2g_ripple_Mean = pd.concat([df_2g_ripple_Mean, round(df_2g_ripple_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_2g_ripple_Mean = pd.concat([df_2g_ripple_Mean, round(df_2g_ripple_Mean.min(axis=1), 1).rename("Min")], axis=1)

    if Save_data_var.get():
        filename = "Excel_RXCal_2G.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_2g_gain_Mean.to_excel(writer, sheet_name="2G_PRX_Gain_Mean")
            df_2g_ripple_Mean.to_excel(writer, sheet_name="2G_RX_Ripple_Mean")
        func.WB_Format(filename, 2, 2, 0, text_area)

    return df_2g_gain_Mean["Average"], df_2g_ripple_Mean["Average"]
