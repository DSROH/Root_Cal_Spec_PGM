import re
import tkinter as tk
import pandas as pd
import LSI_Solution.Common.Function as func


def chng_sub6_rfic_gain(Selected_spc, rat, band, RFIC_Spec_var, RFIC_gain, text_area):
    RFIC_gain_Spec = int(RFIC_Spec_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_RFIC_Index_"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Extract_String = [v for v in New_String[0].split("TX_") if v]
            gainindex = int(re.sub(r"[^0-9]", "", Extract_String[0]))
            Word = re.split("_", New_String[0])
            Word = [v for v in Word if v]
            if Word[0] == "TX":
                Path = "Tx"
            elif Word[0] == "TX2":
                Path = "Tx2"
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
            text_area.see(tk.END)

            if gainindex == 0:
                New_String[2] = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                New_String[3] = int(New_String[2]) - 0.1
                New_String[4] = int(New_String[2]) + 0.1
            elif gainindex <= 8:
                New_String[2] = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                New_String[3] = New_String[2] - RFIC_gain_Spec
                New_String[4] = New_String[2] + RFIC_gain_Spec
            elif gainindex <= 12:
                value = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                New_String[2] = value
                New_String[3] = New_String[2] - RFIC_gain_Spec - 5
                New_String[4] = New_String[2] + RFIC_gain_Spec + 5
            elif gainindex >= 13:
                if RFIC_gain["NR"][band][Path].get(f"Index{gainindex} ") is not None:
                    value = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                    New_String[2] = value
                    New_String[3] = New_String[2] - RFIC_gain_Spec - 5
                    New_String[4] = New_String[2] + RFIC_gain_Spec + 5
                else:
                    New_String[2] = value - 5
                    New_String[3] = New_String[2] - RFIC_gain_Spec - 5
                    New_String[4] = New_String[2] + RFIC_gain_Spec + 5

            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string

        elif Check & line.startswith("TX2_RFIC_Index_"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Extract_String = [v for v in New_String[0].split("TX2_") if v]
            gainindex = int(re.sub(r"[^0-9]", "", Extract_String[0]))
            Word = re.split("_", New_String[0])
            Word = [v for v in Word if v]
            if Word[0] == "TX":
                Path = "Tx"
            elif Word[0] == "TX2":
                Path = "Tx2"
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
            text_area.see(tk.END)

            if gainindex == 0:
                New_String[2] = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                New_String[3] = int(New_String[2]) - 0.1
                New_String[4] = int(New_String[2]) + 0.1
            elif gainindex <= 8:
                New_String[2] = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                New_String[3] = New_String[2] - RFIC_gain_Spec
                New_String[4] = New_String[2] + RFIC_gain_Spec
            elif gainindex <= 12:
                value = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                New_String[2] = value
                New_String[3] = New_String[2] - RFIC_gain_Spec - 5
                New_String[4] = New_String[2] + RFIC_gain_Spec + 5
            elif gainindex >= 13:
                if RFIC_gain["NR"][band][Path].get(f"Index{gainindex} ") is not None:
                    value = round(RFIC_gain["NR"][band][Path][f"Index{gainindex} "])
                    New_String[2] = value
                    New_String[3] = New_String[2] - RFIC_gain_Spec - 5
                    New_String[4] = New_String[2] + RFIC_gain_Spec + 5
                else:
                    New_String[2] = value - 5
                    New_String[3] = New_String[2] - RFIC_gain_Spec - 5
                    New_String[4] = New_String[2] + RFIC_gain_Spec + 5

            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string

        elif line.startswith("RX_Gain_main"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_sub6_thermistor_code(Selected_spc, rat, band, thermistor, text_area):
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
        elif Check & line.startswith("Thermistor_GPADC"):
            New_String = Old_String = line
            New_String = sub6_thermistor(line, band, 1500, thermistor, text_area)
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


def sub6_thermistor(line, band, Therm_Spec, df_Thermistor, text_area):
    New_String = re.split("\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    if Word[1] == "GPADC":
        Path = "1"
    elif Word[1] == "GPADC2":
        Path = "2"

    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")

    if df_Thermistor.get(band) is not None:
        if df_Thermistor[band].get(Path) is not None:
            New_String[2] = round(df_Thermistor[band, Path])
        else:
            New_String[2] = 0

    New_String[3] = New_String[2] - Therm_Spec
    New_String[4] = New_String[2] + Therm_Spec

    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)

    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def chng_sub6_bwcal(Selected_spc, rat, band, BW_Cal_Spec_var, BW_Cal, text_area):
    BWCal_Spec = float(BW_Cal_Spec_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_BW_Cal_Diff"):
            text_area.insert(tk.END, f"BW Power Calibration\n")
            text_area.see(tk.END)
            New_String = Old_String = line
            New_String = sub6_bwcal(line, band, BWCal_Spec, BW_Cal)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_BW_Cal_Diff"):
            New_String = Old_String = line
            New_String = sub6_bwcal(line, band, BWCal_Spec, BW_Cal)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("RX_Gain_main_"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_bwcal(line, band, BWCal_Spec, BW_Cal):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]

    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]

    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"

    New_String[1] = round(BW_Cal[band, Path])
    New_String[2] = round(0 - BWCal_Spec)
    New_String[3] = round(0 + BWCal_Spec)

    Word = "_".join(Word) + "\t" + "="
    New_String[0] = Word
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def sub6_bw_cal_average(df_Meas, Save_data, text_area):
    df_bwcal = df_Meas[df_Meas["Test Conditions"].str.contains("CH_BW_").to_list()]

    if df_bwcal.empty:
        return pd.DataFrame()
    else:
        df_bwcal_Value = df_bwcal.iloc[:, 1:].astype(float)
        df_bwcal_Item = df_bwcal["Test Conditions"].str.split("_", expand=True)
        # 의미없는 컬럼 삭제
        df_bwcal_Item.drop(columns=[0, 3, 4, 5], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_bwcal_Item.columns = ["Band", "Path"]
        df_bw_cal = pd.merge(df_bwcal_Item, df_bwcal_Value, left_index=True, right_index=True)
        df_bw_cal_mean = round(df_bw_cal.groupby(["Band", "Path"], sort=False).mean(), 1)
        # df_bw_cal_data = round(df_bw_cal.groupby(["Band", "Path"], sort=False).agg(["mean", "max", "min"]), 1)
        df_bw_cal_mean = pd.concat([df_bw_cal_mean, round(df_bw_cal_mean.mean(axis=1), 1).rename("Average")], axis=1)
        df_bw_cal_mean = pd.concat([df_bw_cal_mean, round(df_bw_cal_mean.max(axis=1), 1).rename("Max")], axis=1)
        df_bw_cal_mean = pd.concat([df_bw_cal_mean, round(df_bw_cal_mean.min(axis=1), 1).rename("Min")], axis=1)

        if Save_data:
            filename = "Excel_Sub6_BW_Cal.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_bw_cal_mean.to_excel(writer, sheet_name="Sub6_BW_Cal_Mean")
            func.WB_Format(filename, 2, 3, 0, text_area)

    return df_bw_cal_mean["Average"]


def therm_average(df_Code, Save_data, text_area):
    df_Therm = df_Code[df_Code["Test Conditions"].str.contains("Thermistor ADC").to_list()]

    if df_Therm.empty:
        return pd.DataFrame()
    else:
        df_Therm_Value = df_Therm.iloc[:, 1:].astype(float)
        df_Therm_Item = df_Therm["Test Conditions"].str.split("_", expand=True)
        if len(df_Therm_Item.columns) == 4:  # Thermistor ADC 2 있을 경우 (TX2 지원)
            df_Therm_Item.fillna("1", inplace=True)
            # 의미없는 컬럼 삭제
            df_Therm_Item.drop(columns=[0, 2], inplace=True)
            df_Therm_Item.columns = ["Band", "Therm_CH"]
            df_Therm_Item["Therm_CH"] = df_Therm_Item["Therm_CH"].str.replace(" ", "")
        else:
            df_Therm_Item.drop(columns=[0], inplace=True)
            df_Therm_Item.columns = ["Band", "Therm_CH"]
            df_Therm_Item["Therm_CH"] = df_Therm_Item["Therm_CH"].str.replace("Thermistor ADC", "1")
            df_Therm_Item["Therm_CH"] = df_Therm_Item["Therm_CH"].str.replace(" ", "")

        # groupby 실행을 위한 컬럼명 변경
        df_Therm = pd.merge(df_Therm_Item, df_Therm_Value, left_index=True, right_index=True)
        df_Therm_mean = round(df_Therm.groupby(["Band", "Therm_CH"], sort=False).mean())
        df_Therm_mean = pd.concat([df_Therm_mean, round(df_Therm_mean.mean(axis=1)).rename("Average")], axis=1)
        df_Therm_mean = pd.concat([df_Therm_mean, round(df_Therm_mean.max(axis=1)).rename("Max")], axis=1)
        df_Therm_mean = pd.concat([df_Therm_mean, round(df_Therm_mean.min(axis=1)).rename("Min")], axis=1)

        if Save_data:
            filename = "Excel_Thermistor.xlsx"
            with pd.ExcelWriter(filename) as writer:
                df_Therm_mean.to_excel(writer, sheet_name="Thermistor_GPADC")
            func.WB_Format(filename, 2, 2, 0, text_area)

    return df_Therm_mean["Average"]
