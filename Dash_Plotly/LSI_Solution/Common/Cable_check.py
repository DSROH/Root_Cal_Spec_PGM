import re
import math
import tkinter as tk
import numpy as np
import pandas as pd
import LSI_Solution.Common.Function as func


def Daseul_cable_ave(df_Meas, Save_data, text_area):
    df_CableCheck = df_Meas[df_Meas["Test Conditions"].str.contains("CableCheck").to_list()]
    if any(df_CableCheck["Test Conditions"].iloc[0:1].str.startswith("CableCheck")):
        df_CableCheck_Value = df_CableCheck.iloc[:, 1:].astype(float)
        df_CableCheck_Item = df_CableCheck["Test Conditions"].str.split(r"_| |\[MHz]|CH", expand=True)
        # 의미없는 컬럼 삭제
        df_CableCheck_Item.drop(columns=[0, 5, 6, 7, 8, 9], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_CableCheck_Item.columns = ["RAT", "Band", "Path", "CH_MHz"]
        df_CableCheck = pd.merge(df_CableCheck_Item, df_CableCheck_Value, left_index=True, right_index=True)
        df_CableCheck_Mean = round(df_CableCheck.groupby(["RAT", "Band", "Path", "CH_MHz"]).mean(), 1)
        Old_V = True
    else:
        df_CableCheck_Value = df_CableCheck.iloc[:, 1:].astype(float)
        df_CableCheck_Item = df_CableCheck["Test Conditions"].str.split(r"_|\[MHz]|CH", expand=True)
        # 의미없는 컬럼 삭제
        df_CableCheck_Item.drop(columns=[2, 4, 6], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_CableCheck_Item.columns = ["RAT", "Band", "CH_MHz", "Path"]
        df_CableCheck = pd.merge(df_CableCheck_Item, df_CableCheck_Value, left_index=True, right_index=True)
        df_CableCheck_Mean = round(df_CableCheck.groupby(["RAT", "Band", "Path", "CH_MHz"]).mean(), 1)
        Old_V = False

    df_CableCheck_Mean = pd.concat(
        [
            df_CableCheck_Mean,
            round(df_CableCheck_Mean.mean(axis=1), 1).rename("Average"),
        ],
        axis=1,
    )
    df_CableCheck_Mean = pd.concat([df_CableCheck_Mean, round(df_CableCheck_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_CableCheck_Mean = pd.concat([df_CableCheck_Mean, round(df_CableCheck_Mean.min(axis=1), 1).rename("Min")], axis=1)
    df_CableCheck_Mean = pd.concat(
        [
            df_CableCheck_Mean,
            round(
                (df_CableCheck_Mean["Max"] - df_CableCheck_Mean["Min"]).rename("Max-Min"),
                1,
            ),
        ],
        axis=1,
    )

    if Save_data:
        filename = "Excel_CableCheck.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_CableCheck_Mean.to_excel(writer, sheet_name="CableCheck")
        func.WB_Format(filename, 2, 3, 0, text_area)
        # df_CableCheck_Mean.to_csv("CSV_CableCheck.csv", encoding="utf-8-sig")

    return df_CableCheck_Mean, Old_V


def chng_cable_spec(Selected_spc, df_CableCheck, Cable_Spec_var, Old_Ver, text_area):
    CableCheck = df_CableCheck["Average"]
    Cable_Spec = int(Cable_Spec_var.get())
    target_word = "[INSERT_RF_CABLE_CHECK]"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            text_area.insert(tk.END, f"[INSERT_RF_CABLE_CHECK]\n")
            text_area.see(tk.END)
            new_text_content += line
        elif Check & line.startswith("Test Band"):
            New_String = Old_String = line
            Numofturn = re.split(f"Test Band|=|\n", line)[1]
            Test_Path = re.split(f"Test Band|=|\n", line)[2]

            if Old_Ver:
                if Test_Path == "SUB6_RX":
                    path = "RX"
                elif Test_Path == "SUB6_2TX":
                    path = "2TX"
                else:
                    path = "TX"
            else:
                if Test_Path == "SUB6_RX":
                    path = "RX"
                elif Test_Path == "SUB6_TX1CA1":
                    path = "TX1 CA1"
                else:
                    path = "TX1"

            Test_Band = re.split(f"Band Number{Numofturn}=|\n", data_lines[index + 1])
            Test_Band = ",".join([v for v in Test_Band if v])
            Test_Freq = re.split(f"Test TxFreq{Numofturn}=|\n", data_lines[index + 2])
            Test_Freq = ",".join([v for v in Test_Freq if v])
            new_text_content += line
            continue
        elif Check & line.startswith(f"LOWER_LIMIT"):
            New_String = Old_String = line
            New_String = str(New_String).strip().split("=")
            New_String = [v for v in New_String if v]
            text_area.insert(tk.END, f"n{Test_Band:<2} Path= {path:>3}\n")
            text_area.see(tk.END)
            text_area.insert(tk.END, f"LOWER_LIMIT {Numofturn:<18}| {float(New_String[1]):>5.1f}")
            text_area.see(tk.END)
            if Test_Freq:
                if int(Test_Freq) > 3000000:
                    arfcn = str(math.trunc(600000 + (int(Test_Freq) * 1000 - 3000000000) / 15000))
                    Average = round(CableCheck["NR", f"n{Test_Band}", path, arfcn])
                elif int(Test_Freq) <= 3000000:
                    arfcn = str(math.trunc((int(Test_Freq) * 1000) / 5000))
                    Average = round(CableCheck["NR", f"n{Test_Band}", path, arfcn])
            else:
                Average = round(CableCheck["NR", f"n{Test_Band}", path].iloc[0], 1)
            text_area.insert(tk.END, f"\t\u2192\t")
            New_String[1] = str(round(Average - Cable_Spec, 1))
            text_area.insert(tk.END, f"{float(New_String[1]):>5.1f}\n")
            text_area.see(tk.END)
            New_String = "=".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
            continue

        elif Check & line.startswith(f"UPPER_LIMIT"):
            New_String = Old_String = line
            New_String = str(New_String).strip().split("=")
            New_String = [v for v in New_String if v]
            text_area.insert(tk.END, f"UPPER_LIMIT {Numofturn:<18}| {float(New_String[1]):>5.1f}")
            text_area.insert(tk.END, f"\t\u2192\t")
            New_String[1] = str(round(Average + Cable_Spec, 1))
            text_area.insert(tk.END, f"{float(New_String[1]):>5.1f}\n\n")
            text_area.see(tk.END)
            New_String = "=".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
            continue

        elif line == "[RF_CAL_VERIFY]\n":
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_cable_spec_only(Selected_spc, Cable_Spec_var, text_area):
    Cable_Spec = int(Cable_Spec_var.get())
    target_word = "[INSERT_RF_CABLE_CHECK]"
    new_text_content = ""
    Cable = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        if target_word in line:
            text_area.insert(tk.END, f"\n[INSERT_RF_CABLE_CHECK]\n")
            Cable = True
            new_text_content += line
        elif Cable & line.startswith("Test Band"):
            New_String = Old_String = line
            String = re.split(f"Test Band|=|\n", line)
            Numofturn = String[1]
            Test_Path = String[2]
            path = "RX" if Test_Path == "SUB6_RX" else "TX"
            Test_Band = re.split(f"Band Number{Numofturn}=|\n", data_lines[index + 1])
            Test_Band = ",".join([v for v in Test_Band if v])
            Test_Freq = re.split(f"Test TxFreq{Numofturn}=|\n", data_lines[index + 2])
            Test_Freq = ",".join([v for v in Test_Freq if v])
            text_area.insert(tk.END, f"SUB6 n{Test_Band:<2} {path:<2}  {Test_Freq:<7}          | ")
            new_text_content += line
            continue

        elif Cable & line.startswith(f"LOWER_LIMIT"):
            New_String = Old_String = line
            New_String = re.split("=", New_String)
            New_String = [v for v in New_String if v]
            LOWER_LIMIT = New_String[1]
            UPPER_LIMIT = re.split(f"UPPER_LIMIT{Numofturn}=|\n", data_lines[index + 1])
            UPPER_LIMIT = ",".join([v for v in UPPER_LIMIT if v])
            Cable_Value = [float(LOWER_LIMIT), float(UPPER_LIMIT)]
            Cable_mean = np.mean(Cable_Value)
            New_String[1] = str(round(Cable_mean - Cable_Spec, 1))
            text_area.insert(tk.END, f"LOWER_LIMIT : {float(LOWER_LIMIT):>5} \u2192 {New_String[1]:>5}\n")
            New_String = "=".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
            continue

        elif Cable & line.startswith(f"UPPER_LIMIT"):
            New_String = Old_String = line
            New_String = re.split("=", New_String)
            New_String = [v for v in New_String if v]
            New_String[1] = str(round(Cable_mean + Cable_Spec, 1))
            text_area.insert(
                tk.END,
                f"                              | UPPER_LIMIT : {float(UPPER_LIMIT):>5} \u2192 {New_String[1]:>5}\n\n",
            )
            New_String = "=".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
            continue

        elif line == "[RF_CAL_VERIFY]\n":
            new_text_content += line
            Cable = False
        else:
            new_text_content += line

    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()
