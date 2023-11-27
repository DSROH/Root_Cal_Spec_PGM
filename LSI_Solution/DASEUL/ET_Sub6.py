import re
import tkinter as tk
import pandas as pd
import numpy as np
import LSI_Solution.Common.Function as func


def chng_sub6_et_psat_pgain(
    Selected_spc,
    rat,
    band,
    ET_Psat_var,
    ETSAPT_Psat_Ave,
    ETSAPT_Psat_Max,
    ETSAPT_Psat_Min,
    ET_Pgain_var,
    ETSAPT_Pgain_Ave,
    ETSAPT_Pgain_Max,
    ETSAPT_Pgain_Min,
    text_area,
):
    ET_Psat_spec = float(ET_Psat_var.get())  # 1dB = 100
    ET_Pgain_sepc = float(ET_Pgain_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_ET_S-APT_Psat"):
            New_String = Old_String = line
            New_String = sub6_et_psat_pgain(
                line, band, ET_Psat_spec, ETSAPT_Psat_Ave, ETSAPT_Psat_Max, ETSAPT_Psat_Min, text_area
            )
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_ET_S-APT_Pgain"):
            New_String = Old_String = line
            New_String = sub6_et_psat_pgain(
                line, band, ET_Pgain_sepc, ETSAPT_Pgain_Ave, ETSAPT_Pgain_Max, ETSAPT_Pgain_Min, text_area
            )
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_ET_S-APT_Psat"):
            New_String = Old_String = line
            New_String = sub6_et_psat_pgain(
                line, band, ET_Psat_spec, ETSAPT_Psat_Ave, ETSAPT_Psat_Max, ETSAPT_Psat_Min, text_area
            )
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_ET_S-APT_Pgain"):
            New_String = Old_String = line
            New_String = sub6_et_psat_pgain(
                line, band, ET_Pgain_sepc, ETSAPT_Pgain_Ave, ETSAPT_Pgain_Max, ETSAPT_Pgain_Min, text_area
            )
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("TX_DC_I	="):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_et_psat_pgain(line, band, Spec, df1, df2, df3, text_area):
    New_String = re.split("\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"
    text_area.insert(
        tk.END,
        f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t",
    )
    text_area.see(tk.END)

    if df1.get(band) is not None:
        if df1[band].get(Path) is not None:
            New_String[2] = round(df1[band, Path])
            if (round(df3[band, Path]) - Spec) > (New_String[2] - 3):
                New_String[3] = round(New_String[2] - 3)  # Average - 3
            else:
                New_String[3] = round(df3[band, Path]) - Spec  # ETSAT Min - Spec

            if (round(df2[band, Path]) + Spec) < (New_String[2] + 3):
                New_String[4] = round(New_String[2] + 3)  # Average + 3
            else:
                New_String[4] = round(df2[band, Path]) + Spec  # ETSAT Max + Spec
        else:
            New_String[2] = 0
            New_String[3] = New_String[2] - Spec
            New_String[4] = New_String[2] + Spec
    else:
        New_String[2] = 0
        New_String[3] = New_String[2] - Spec
        New_String[4] = New_String[2] + Spec

    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def chng_sub6_et_freq(Selected_spc, rat, band, ET_Freq_var, ETSAPT_Freq_Ave, ETSAPT_Freq_Max, ETSAPT_Freq_Min, text_area):
    ET_Freq = int(ET_Freq_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_ET_S-APT_Freq_Pow_Index_"):
            New_String = Old_String = line
            New_String = sub6_et_freq(line, band, ET_Freq, ETSAPT_Freq_Ave, ETSAPT_Freq_Max, ETSAPT_Freq_Min, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_ET_S-APT_Freq_Pow_Index_"):
            New_String = Old_String = line
            New_String = sub6_et_freq(line, band, ET_Freq, ETSAPT_Freq_Ave, ETSAPT_Freq_Max, ETSAPT_Freq_Min, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("TX_DC_I	="):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_et_freq(line, band, ET_Freq, ETSAPT_Freq_Ave, ETSAPT_Freq_Max, ETSAPT_Freq_Min, text_area):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    Read_index = int(Word[6])
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"

    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[2]:>5}\t{New_String[3]:>5}\t\t\u2192\t")
    text_area.see(tk.END)

    if ETSAPT_Freq_Ave.get(band) is not None:
        if ETSAPT_Freq_Ave[band].get(Path) is not None:
            Index_count = ETSAPT_Freq_Ave.loc[(band, Path)].count()
            if Read_index < Index_count:
                New_String[1] = round(ETSAPT_Freq_Ave[band, Path].iloc[Read_index])
                New_String[2] = round(ETSAPT_Freq_Min[band, Path].iloc[Read_index]) - ET_Freq
                New_String[3] = round(ETSAPT_Freq_Max[band, Path].iloc[Read_index]) + ET_Freq
            else:
                New_String[1] = 0
                New_String[2] = New_String[1] - ET_Freq
                New_String[3] = New_String[1] + ET_Freq
        else:
            New_String[1] = 0
            New_String[2] = New_String[1] - ET_Freq
            New_String[3] = New_String[1] + ET_Freq
    else:
        New_String[1] = 0
        New_String[2] = New_String[1] - ET_Freq
        New_String[3] = New_String[1] + ET_Freq

    text_area.insert(tk.END, f"{New_String[2]:>5}\t{New_String[3]:>5}\n")
    text_area.see(tk.END)
    Word = "_".join(Word) + "\t" + "="
    New_String[0] = Word
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def chng_sub6_et_power(Selected_spc, rat, band, ET_Power_var, ETSAPT_Power_Ave, ETSAPT_Power_Max, ETSAPT_Power_Min, text_area):
    ET_Power = int(ET_Power_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_ET_S-APT_Pow_Index_"):
            New_String = Old_String = line
            New_String = sub6_et_power(line, band, ET_Power, ETSAPT_Power_Ave, ETSAPT_Power_Max, ETSAPT_Power_Min, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_ET_S-APT_Pow_Index_"):
            New_String = Old_String = line
            New_String = sub6_et_power(line, band, ET_Power, ETSAPT_Power_Ave, ETSAPT_Power_Max, ETSAPT_Power_Min, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("TX_DC_I	="):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_et_power(line, band, ET_Power, ETSAPT_Power_Ave, ETSAPT_Power_Max, ETSAPT_Power_Min, text_area):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    Read_index = int(Word[5])
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"

    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[2]:>5}\t{New_String[3]:>5}\t\t\u2192\t")
    text_area.see(tk.END)

    if ETSAPT_Power_Ave.get(band) is not None:
        if ETSAPT_Power_Ave[band].get(Path) is not None:
            Index_count = ETSAPT_Power_Ave.loc[(band, Path)].count()
            if Read_index < Index_count:
                New_String[1] = round(ETSAPT_Power_Ave[band, Path].iloc[Read_index])
                New_String[2] = round(ETSAPT_Power_Min[band, Path].iloc[Read_index]) - ET_Power
                New_String[3] = round(ETSAPT_Power_Max[band, Path].iloc[Read_index]) + ET_Power
            else:
                New_String[1] = 0
                New_String[2] = New_String[1] - ET_Power
                New_String[3] = New_String[1] + ET_Power
        else:
            New_String[1] = 0
            New_String[2] = New_String[1] - ET_Power
            New_String[3] = New_String[1] + ET_Power
    else:
        New_String[1] = 0
        New_String[2] = New_String[1] - ET_Power
        New_String[3] = New_String[1] + ET_Power

    text_area.insert(tk.END, f"{New_String[2]:>5}\t{New_String[3]:>5}\n")
    text_area.see(tk.END)
    Word = "_".join(Word) + "\t" + "="
    New_String[0] = Word
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def chng_et_psat_pgain_spec_only(Selected_spc, rat, band, ET_Psat_var, ET_Pgain_var, text_area):
    ET_Psat = float(ET_Psat_var.get())  # 1dB = 100
    ET_Pgain = float(ET_Pgain_var.get())  # 1dB = 100

    if rat == "HSPA":
        Search_WD = f"[{rat}_BAND{band}_Calibration_Spec]"
    elif rat == "SUB6":
        Search_WD = f"[{rat}_n{band}_Calibration_Spec]"

    End_WD = f"TX_DC_I"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if Search_WD in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("TX_ET_S-APT_Psat"):  # !HSPA & Sub6 Both
            New_String = et_psat_pgain_spec_only(line, rat, ET_Psat, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_ET_S-APT_Power"):  # !HSPA
            New_String = et_psat_pgain_spec_only(line, rat, ET_Psat, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_ET_S-APT_Pgain"):  # !Sub6 Only
            New_String = et_psat_pgain_spec_only(line, rat, ET_Pgain, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_ET_S-APT_Psat"):  # !Sub6 Only
            New_String = et_psat_pgain_spec_only(line, rat, ET_Psat, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_ET_S-APT_Pgain"):  # !Sub6 Only
            New_String = et_psat_pgain_spec_only(line, rat, ET_Pgain, text_area)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith(End_WD):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def et_psat_pgain_spec_only(line, rat, Spec, text_area):
    New_String = re.split("[_=,\t\n]", line)
    New_String = [v for v in New_String if v]
    text_area.insert(
        tk.END,
        f" {New_String[0]:<3} {New_String[1]:<2} {New_String[2]:<4} {New_String[3]:<5}           | {New_String[5]:>5}\t{New_String[6]:>5}\t  \u2192  ",
    )
    text_area.see(tk.END)

    ET_Value = [float(New_String[5]), float(New_String[6])]
    ET_mean = np.mean(ET_Value)
    New_String[4] = round(ET_mean)
    New_String[5] = float(New_String[5]) - Spec
    New_String[6] = float(New_String[6]) + Spec

    text_area.insert(tk.END, f"{New_String[5]:>5}\t{New_String[6]:>5}\n")
    text_area.see(tk.END)

    New_String1 = "_".join(map(str, New_String[:4]))
    New_String2 = "\t".join(map(str, New_String[4:]))

    New_String = New_String1 + "\t=\t" + New_String2 + "\n"

    return New_String


def chng_sub6_et_freq_spec_only(Selected_spc, rat, band, ET_Freq_var, text_area):
    if rat == "SUB6":
        ET_Freq = int(ET_Freq_var.get())  # 1dB = 100
        band = f"n{band}"
        target_word = f"[{rat}_{band}_Calibration_Spec]"
        new_text_content = ""
        Check = False

        with open(Selected_spc, "r", encoding="utf-8") as f:
            data_lines = f.readlines()
        f.close()

        for index, line in enumerate(data_lines):
            New_String = Old_String = line
            if target_word in line:
                Check = True
                new_text_content += line
            elif Check & line.startswith("TX_ET_S-APT_Freq_Pow_Index_"):
                New_String = et_freq_spec_only(line, ET_Freq, text_area)
                new_string = line.replace(Old_String, New_String)
                new_text_content += new_string
            elif Check & line.startswith("TX2_ET_S-APT_Freq_Pow_Index_"):
                New_String = et_freq_spec_only(line, ET_Freq, text_area)
                new_string = line.replace(Old_String, New_String)
                new_text_content += new_string
            elif line.startswith("TX_DC_I	="):
                new_text_content += line
                Check = False
            else:
                new_text_content += line

        text_area.see(tk.END)

        with open(Selected_spc, "w", encoding="utf-8") as f:
            f.writelines(new_text_content)
        f.close()

    else:
        pass


def et_freq_spec_only(line, ET_Freq, text_area):
    New_String = re.split("_|=|\t|\n", line)
    New_String = [v for v in New_String if v]

    text_area.insert(
        tk.END,
        f" {New_String[0]:<3} {New_String[1]:<2}_{New_String[2]:<4} {New_String[3]:<4}_{New_String[4]:<3}_Ind {New_String[6]:<1}  | {New_String[8]:>5}\t{New_String[9]:>5}\t  \u2192  ",
    )
    text_area.see(tk.END)

    ETfreq_Value = [float(New_String[8]), float(New_String[9])]
    ETfreq_mean = np.mean(ETfreq_Value)
    New_String[7] = round(ETfreq_mean)
    New_String[8] = round(New_String[7] - ET_Freq)
    New_String[9] = round(New_String[7] + ET_Freq)

    text_area.insert(tk.END, f"{New_String[8]:>5}\t{New_String[9]:>5}\n")
    text_area.see(tk.END)

    New_String1 = "_".join(map(str, New_String[:7]))
    New_String2 = "\t".join(map(str, New_String[7:]))

    New_String = New_String1 + "\t=\t" + New_String2 + "\n"

    return New_String


def chng_sub6_et_power_spec_only(Selected_spc, rat, band, ET_Power_var, text_area):
    if rat == "SUB6":
        ET_Power = int(ET_Power_var.get())  # 1dB = 100
        band = f"n{band}"
        target_word = f"[{rat}_{band}_Calibration_Spec]"
        new_text_content = ""
        Check = False

        with open(Selected_spc, "r", encoding="utf-8") as f:
            data_lines = f.readlines()
        f.close()

        for index, line in enumerate(data_lines):
            New_String = Old_String = line
            if target_word in line:
                Check = True
                new_text_content += line
            elif Check & line.startswith("TX_ET_S-APT_Pow_Index_"):
                New_String = et_power_spec_only(line, ET_Power, text_area)
                new_string = line.replace(Old_String, New_String)
                new_text_content += new_string
            elif Check & line.startswith("TX2_ET_S-APT_Pow_Index_"):
                New_String = et_power_spec_only(line, ET_Power, text_area)
                new_string = line.replace(Old_String, New_String)
                new_text_content += new_string
            elif line.startswith("TX_DC_I	="):
                new_text_content += line
                Check = False
            else:
                new_text_content += line

        text_area.see(tk.END)

        with open(Selected_spc, "w", encoding="utf-8") as f:
            f.writelines(new_text_content)
        f.close()
    else:
        pass


def et_power_spec_only(line, ET_Power, text_area):
    New_String = re.split("_|=|\t|\n", line)
    New_String = [v for v in New_String if v]

    text_area.insert(
        tk.END,
        f" {New_String[0]:<3} {New_String[1]:<2}_{New_String[2]:<4} (BW) {New_String[3]:<3}_Ind {New_String[5]:<2} | {New_String[7]:>5}\t{New_String[8]:>5}\t  \u2192  ",
    )
    text_area.see(tk.END)

    ET_Power_Value = [float(New_String[7]), float(New_String[8])]
    ET_Power_mean = np.mean(ET_Power_Value)
    New_String[6] = round(ET_Power_mean)
    New_String[7] = round(New_String[6] - ET_Power)
    New_String[8] = round(New_String[6] + ET_Power)

    text_area.insert(tk.END, f"{New_String[7]:>5}\t{New_String[8]:>5}\n")
    text_area.see(tk.END)

    New_String1 = "_".join(map(str, New_String[:6]))
    New_String2 = "\t".join(map(str, New_String[6:]))

    New_String = New_String1 + "\t=\t" + New_String2 + "\n"

    return New_String


def sub6_et_average(df_Meas, Save_data, text_area):
    ETSAPT_sub6_Psat_Ave, ETSAPT_sub6_Psat_Max, ETSAPT_sub6_Psat_Min = sub6_et_psat_ave(df_Meas, Save_data, text_area)
    ETSAPT_sub6_Pgain_Ave, ETSAPT_sub6_Pgain_Max, ETSAPT_sub6_Pgain_Min = sub6_et_pgain_ave(df_Meas, Save_data, text_area)
    ETSAPT_sub6_Freq_Ave, ETSAPT_sub6_Freq_Max, ETSAPT_sub6_Freq_Min = sub6_et_freq_ave(df_Meas, Save_data, text_area)
    ETSAPT_sub6_Power_Ave, ETSAPT_sub6_Power_Max, ETSAPT_sub6_Power_Min = sub6_et_power_ave(df_Meas, Save_data, text_area)

    return (
        ETSAPT_sub6_Psat_Ave,
        ETSAPT_sub6_Psat_Max,
        ETSAPT_sub6_Psat_Min,
        ETSAPT_sub6_Freq_Ave,
        ETSAPT_sub6_Freq_Max,
        ETSAPT_sub6_Freq_Min,
        ETSAPT_sub6_Pgain_Ave,
        ETSAPT_sub6_Pgain_Max,
        ETSAPT_sub6_Pgain_Min,
        ETSAPT_sub6_Power_Ave,
        ETSAPT_sub6_Power_Max,
        ETSAPT_sub6_Power_Min,
    )


def sub6_et_psat_ave(df_Meas, Save_data, text_area):
    df_et_psat = df_Meas[df_Meas["Test Conditions"].str.contains("_ET_S-APT_Psat").to_list()]

    if df_et_psat.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    else:
        df_et_psat_Value = df_et_psat.iloc[:, 1:].astype(float)
        df_et_psat_Item = df_et_psat["Test Conditions"].str.split("_| ", expand=True)
        # 의미없는 컬럼 삭제
        df_et_psat_Item.drop(columns=[0, 3, 4, 5, 6, 7, 8], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_et_psat_Item.columns = ["Band", "Path"]
        df_et_psat = pd.merge(df_et_psat_Item, df_et_psat_Value, left_index=True, right_index=True)
        df_et_psat_mean = round(df_et_psat.groupby(["Band", "Path"], sort=False).mean(), 1)
        df_et_psat_max = round(df_et_psat.groupby(["Band", "Path"], sort=False).max(), 1)
        df_et_psat_min = round(df_et_psat.groupby(["Band", "Path"], sort=False).min(), 1)
        # df_et_psat_data = round(df_et_psat.groupby(["Band", "Path"], sort=False).agg(["mean", "max", "min"]), 1)
        df_et_psat_mean = pd.concat([df_et_psat_mean, round(df_et_psat_mean.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_psat_mean = pd.concat([df_et_psat_mean, round(df_et_psat_mean.max(axis=1), 1).rename("Max")], axis=1)
        df_et_psat_mean = pd.concat([df_et_psat_mean, round(df_et_psat_mean.min(axis=1), 1).rename("Min")], axis=1)
        df_et_psat_max = pd.concat([df_et_psat_max, round(df_et_psat_max.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_psat_max = pd.concat([df_et_psat_max, round(df_et_psat_max.max(axis=1), 1).rename("Max")], axis=1)
        df_et_psat_max = pd.concat([df_et_psat_max, round(df_et_psat_max.min(axis=1), 1).rename("Min")], axis=1)
        df_et_psat_min = pd.concat([df_et_psat_min, round(df_et_psat_min.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_psat_min = pd.concat([df_et_psat_min, round(df_et_psat_min.max(axis=1), 1).rename("Max")], axis=1)
        df_et_psat_min = pd.concat([df_et_psat_min, round(df_et_psat_min.min(axis=1), 1).rename("Min")], axis=1)

        if Save_data:
            filename = "Excel_ETSAPT_Sub6_Psat.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_et_psat_mean.to_excel(writer, sheet_name="ETSAPT_sub6_Psat_Mean")
                df_et_psat_max.to_excel(writer, sheet_name="ETSAPT_sub6_Psat_Max")
                df_et_psat_min.to_excel(writer, sheet_name="ETSAPT_sub6_Psat_Min")
            func.WB_Format(filename, 2, 3, 0, text_area)

        return df_et_psat_mean["Average"], df_et_psat_max["Average"], df_et_psat_min["Average"]


def sub6_et_pgain_ave(df_Meas, Save_data, text_area):
    df_et_pgain = df_Meas[df_Meas["Test Conditions"].str.contains("_ET_S-APT_Pgain").to_list()]

    if df_et_pgain.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    else:
        df_et_pgain_Value = df_et_pgain.iloc[:, 1:].astype(float)
        df_et_pgain_Item = df_et_pgain["Test Conditions"].str.split("_| ", expand=True)
        # 의미없는 컬럼 삭제
        df_et_pgain_Item.drop(columns=[0, 3, 4, 5, 6, 7, 8], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_et_pgain_Item.columns = ["Band", "Path"]
        df_et_pgain = pd.merge(df_et_pgain_Item, df_et_pgain_Value, left_index=True, right_index=True)
        df_et_pgain_mean = round(df_et_pgain.groupby(["Band", "Path"], sort=False).mean(), 1)
        df_et_pgain_max = round(df_et_pgain.groupby(["Band", "Path"], sort=False).max(), 1)
        df_et_pgain_min = round(df_et_pgain.groupby(["Band", "Path"], sort=False).min(), 1)
        # df_et_pgain_data = round(df_et_pgain.groupby(["Band", "Path"], sort=False).agg(["mean", "max", "min"]), 1)
        df_et_pgain_mean = pd.concat([df_et_pgain_mean, round(df_et_pgain_mean.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_pgain_mean = pd.concat([df_et_pgain_mean, round(df_et_pgain_mean.max(axis=1), 1).rename("Max")], axis=1)
        df_et_pgain_mean = pd.concat([df_et_pgain_mean, round(df_et_pgain_mean.min(axis=1), 1).rename("Min")], axis=1)
        df_et_pgain_max = pd.concat([df_et_pgain_max, round(df_et_pgain_max.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_pgain_max = pd.concat([df_et_pgain_max, round(df_et_pgain_max.max(axis=1), 1).rename("Max")], axis=1)
        df_et_pgain_max = pd.concat([df_et_pgain_max, round(df_et_pgain_max.min(axis=1), 1).rename("Min")], axis=1)
        df_et_pgain_min = pd.concat([df_et_pgain_min, round(df_et_pgain_min.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_pgain_min = pd.concat([df_et_pgain_min, round(df_et_pgain_min.max(axis=1), 1).rename("Max")], axis=1)
        df_et_pgain_min = pd.concat([df_et_pgain_min, round(df_et_pgain_min.min(axis=1), 1).rename("Min")], axis=1)

        if Save_data:
            filename = "Excel_ETSAPT_Sub6_Pgain.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_et_pgain_mean.to_excel(writer, sheet_name="ETSAPT_sub6_Pgain_Mean")
                df_et_pgain_max.to_excel(writer, sheet_name="ETSAPT_sub6_Pgain_Max")
                df_et_pgain_min.to_excel(writer, sheet_name="ETSAPT_sub6_Pgain_Min")
            func.WB_Format(filename, 2, 3, 0, text_area)

        return df_et_pgain_mean["Average"], df_et_pgain_max["Average"], df_et_pgain_min["Average"]


def sub6_et_freq_ave(df_Meas, Save_data, text_area):
    df_et_freqp = df_Meas[df_Meas["Test Conditions"].str.contains("_ET_S-APT_Freq_Power").to_list()]

    if df_et_freqp.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    else:
        df_et_freqp_Value = df_et_freqp.iloc[:, 1:].astype(float)
        df_et_freqp_Item = df_et_freqp["Test Conditions"].str.split("_", expand=True)
        # 의미없는 컬럼 삭제
        df_et_freqp_Item.drop(columns=[0, 3, 4, 5, 6, 7, 8, 10], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_et_freqp_Item.columns = ["Band", "Path", "BW"]
        df_et_freqp = pd.merge(df_et_freqp_Item, df_et_freqp_Value, left_index=True, right_index=True)
        df_et_freqp_mean = round(df_et_freqp.groupby(["Band", "Path", "BW"], sort=False).mean(), 1)
        # df_et_freqp_data = round(df_et_freqp.groupby(["Band", "Path", "BW"], sort=False).agg(["mean", "max", "min"]), 1)
        df_et_freqp_mean = pd.concat([df_et_freqp_mean, round(df_et_freqp_mean.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_freqp_mean = pd.concat([df_et_freqp_mean, round(df_et_freqp_mean.max(axis=1), 1).rename("Max")], axis=1)
        df_et_freqp_mean = pd.concat([df_et_freqp_mean, round(df_et_freqp_mean.min(axis=1), 1).rename("Min")], axis=1)

        if Save_data:
            filename = "Excel_ETSAPT_Sub6_Freq.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_et_freqp_mean.to_excel(writer, sheet_name="ETSAPT_sub6_Freq_Mean")
            func.WB_Format(filename, 2, 3, 0, text_area)

        return df_et_freqp_mean["Average"], df_et_freqp_mean["Max"], df_et_freqp_mean["Min"]


def sub6_et_power_ave(df_Meas, Save_data, text_area):
    df_et_power = df_Meas[df_Meas["Test Conditions"].str.contains("_ET_S-APT_Power_VBand").to_list()]

    if df_et_power.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    else:
        df_et_power_Value = df_et_power.iloc[:, 1:].astype(float)
        df_et_power_Item = df_et_power["Test Conditions"].str.split("_", expand=True)
        # 의미없는 컬럼 삭제
        df_et_power_Item.drop(columns=[0, 3, 4, 5, 6, 7, 8], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_et_power_Item.columns = ["Band", "Path", "Target"]
        df_et_power = pd.merge(df_et_power_Item, df_et_power_Value, left_index=True, right_index=True)
        df_et_power_mean = round(df_et_power.groupby(["Band", "Path", "Target"], sort=False).mean(), 2)
        # df_et_power_data = round(df_et_power.groupby(["Band", "Path", "Target"], sort=False).agg(["mean", "max", "min"]), 2)
        df_et_power_mean = pd.concat([df_et_power_mean, round(df_et_power_mean.mean(axis=1), 1).rename("Average")], axis=1)
        df_et_power_mean = pd.concat([df_et_power_mean, round(df_et_power_mean.max(axis=1), 1).rename("Max")], axis=1)
        df_et_power_mean = pd.concat([df_et_power_mean, round(df_et_power_mean.min(axis=1), 1).rename("Min")], axis=1)

        if Save_data:
            filename = "Excel_ETSAPT_Sub6_Power.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_et_power_mean.to_excel(writer, sheet_name="ETSAPT_sub6_Power_Mean")
            func.WB_Format(filename, 2, 3, 0, text_area)

        return df_et_power_mean["Average"], df_et_power_mean["Max"], df_et_power_mean["Min"]
