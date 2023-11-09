import re
import tkinter as tk
import pandas as pd
import Common_function as func


def chng_3g_rfic_gain(Selected_spc, rat, band, RFIC_Spec_var, RFIC_gain, text_area):
    RFIC_gain_Spec = int(RFIC_Spec_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_RFIC_GAIN_Index_"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            gainindex = int(re.sub(r"[^0-9]", "", New_String[0]))
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            if gainindex == 0:
                New_String[3] = int(New_String[2]) - 0.1
                New_String[4] = int(New_String[2]) + 0.1
            elif gainindex <= 8:
                New_String[2] = round(RFIC_gain["WCDMA"][band]["Tx"][f"Index{gainindex} "])
                New_String[3] = New_String[2] - RFIC_gain_Spec
                New_String[4] = New_String[2] + RFIC_gain_Spec
            elif gainindex <= 12:
                value = round(RFIC_gain["WCDMA"][band]["Tx"][f"Index{gainindex} "])
                New_String[2] = value
                New_String[3] = New_String[2] - RFIC_gain_Spec - 5
                New_String[4] = New_String[2] + RFIC_gain_Spec + 5
            elif gainindex >= 13:
                if RFIC_gain["WCDMA"][band]["Tx"].get(f"Index{gainindex} ") is not None:
                    value = round(RFIC_gain["WCDMA"][band]["Tx"][f"Index{gainindex} "])
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
        elif line.startswith("TX_FBRX_GAIN_Index_0"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_3g_fbrx_gain_meas(Selected_spc, rat, band, FBRX_3G_Spec_var, FBRX_Gain_Meas_3G, text_area):
    FBRX_Spec = int(FBRX_3G_Spec_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_FBRX_GAIN_Index_"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", New_String)
            New_String = [v for v in New_String if v]
            Word = re.split("_", New_String[0])
            Word = [v for v in Word if v]
            Read_index = int(Word[4])
            Index_count = FBRX_Gain_Meas_3G.loc[("WCDMA", band)].count()
            text_area.insert(
                tk.END,
                f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t",
            )
            text_area.see(tk.END)
            if Read_index < Index_count:
                New_String[2] = round(FBRX_Gain_Meas_3G["WCDMA", band][Read_index])
                New_String[3] = New_String[2] - FBRX_Spec
                New_String[4] = New_String[2] + FBRX_Spec
            else:
                New_String[2] = 0
                New_String[3] = New_String[2] - FBRX_Spec
                New_String[4] = New_String[2] + FBRX_Spec
            text_area.insert(tk.END, f"{New_String[2]:>5}\t{New_String[3]:>5}\n")
            text_area.see(tk.END)
            Word = "_".join(Word)
            New_String[0] = Word
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("AGC_Rx1_LNAON_0"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_3g_fbrx_gain_code(Selected_spc, rat, band, FBRX_3G_Spec_var, FBRX_Gain_Code_3G, text_area):
    FBRX_Spec = int(FBRX_3G_Spec_var.get()) * 100  # 1dB = 100
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
        elif Check & line.startswith("TX_Modulation_FBRX_Result"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", New_String)
            New_String = [v for v in New_String if v]
            text_area.insert(
                tk.END,
                f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t",
            )
            text_area.see(tk.END)
            New_String[2] = round(FBRX_Gain_Code_3G["WCDMA", band][0])
            New_String[3] = New_String[2] - FBRX_Spec - 200
            New_String[4] = New_String[2] + FBRX_Spec + 200
            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("AGC_Rx1_LNAON_0"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_3g_fbrx_freq_meas(
    Selected_spc,
    rat,
    band,
    FBRX_3G_Spec_var,
    FBRX_Freq_Meas_3G,
    FBRX_Freq_Meas_3G_Max,
    FBRX_Freq_Meas_3G_Min,
    text_area,
):
    FBRX_Spec = int(FBRX_3G_Spec_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_FBRX_FREQ	="):
            New_String = Old_String = line
            New_String = re.split("\t|\n", New_String)
            New_String = [v for v in New_String if v]
            text_area.insert(
                tk.END,
                f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t",
            )
            New_String[2] = round(FBRX_Freq_Meas_3G["WCDMA", band])
            New_String[3] = New_String[2] - FBRX_Spec
            New_String[4] = New_String[2] + FBRX_Spec
            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_FBRX_FREQ_RIPPLE	="):
            New_String = Old_String = line
            New_String = re.split("\t|\n", New_String)
            New_String = [v for v in New_String if v]
            text_area.insert(
                tk.END,
                f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t",
            )
            New_String[2] = round(FBRX_Freq_Meas_3G_Max["WCDMA", band]) - round(FBRX_Freq_Meas_3G_Min["WCDMA", band])
            New_String[3] = 0
            New_String[4] = New_String[2] + 3
            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("AGC_Rx1_LNAON_0"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_Txp_comp(Selected_spc, rat, band, TxP_Channel_comp_Spec_var, TxP_Channel_comp_ave):
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
        elif Check & line.startswith("TxP_Channel_Comp_PA_MID_"):
            New_String = Old_String = line
            New_String = Txp_channel_comp(line, band, TxP_Channel_comp_Spec_var, TxP_Channel_comp_ave)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("TX_DC_I"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def Txp_channel_comp(line, band, TxP_Channel_comp_Spec_var, TxP_Channel_comp_ave):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    Read_index = int(Word[5])
    Index_count = TxP_Channel_comp_ave.loc[(band)].count()

    if Read_index < Index_count:
        New_String[1] = round(TxP_Channel_comp_ave[band][Read_index])
        New_String[2] = round(TxP_Channel_comp_ave[band][Read_index]) - TxP_Channel_comp_Spec_var
        New_String[3] = round(TxP_Channel_comp_ave[band][Read_index]) + TxP_Channel_comp_Spec_var
    else:
        New_String[1] = 0
        New_String[2] = New_String[1] - TxP_Channel_comp_Spec_var
        New_String[3] = New_String[1] + TxP_Channel_comp_Spec_var
    Word = "_".join(Word) + "\t" + "="
    New_String[0] = Word
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def TxP_3g_channel_comp_pa_mid(df_Meas, Save_data_var, text_area):
    df_TxP_Channel_comp = df_Meas[df_Meas["Test Conditions"].str.contains("_PA_MID_Comp ").to_list()]
    df_TxP_Channel_comp_Value = df_TxP_Channel_comp.iloc[:, 1:].astype(float)
    df_TxP_Channel_comp_Item = df_TxP_Channel_comp["Test Conditions"].str.split("_|\\(|\\)", expand=True)
    # 의미없는 컬럼 삭제
    df_TxP_Channel_comp_Item.drop(columns=[0, 2, 4, 5, 6, 7, 8], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_TxP_Channel_comp_Item.columns = ["Band", "Channel"]
    df_TxP_Channel_comp = pd.merge(df_TxP_Channel_comp_Item, df_TxP_Channel_comp_Value, left_index=True, right_index=True)
    df_TxP_Channel_comp_mean = round(df_TxP_Channel_comp.groupby(["Band", "Channel"], sort=False).mean(), 2)

    df_TxP_Channel_comp_mean = pd.concat(
        [df_TxP_Channel_comp_mean, round(df_TxP_Channel_comp_mean.mean(axis=1), 2).rename("Average")], axis=1
    )
    df_TxP_Channel_comp_mean = pd.concat(
        [df_TxP_Channel_comp_mean, round(df_TxP_Channel_comp_mean.max(axis=1), 2).rename("Max")], axis=1
    )
    df_TxP_Channel_comp_mean = pd.concat(
        [df_TxP_Channel_comp_mean, round(df_TxP_Channel_comp_mean.min(axis=1), 2).rename("Min")], axis=1
    )

    if Save_data_var.get():
        filename = "Excel_3G_TxP_Channel_Comp.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_TxP_Channel_comp_mean.to_excel(writer, sheet_name="3G_TxP_Channel_Comp_Mean")
        func.WB_Format(filename, 2, 2, 0, text_area)

    return df_TxP_Channel_comp_mean["Average"]
