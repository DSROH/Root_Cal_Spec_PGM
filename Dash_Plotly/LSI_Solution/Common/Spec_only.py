import re
import tkinter as tk
import LSI_Solution.DASEUL.RX_2g as L2grx
import numpy as np


def Chng_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_Spec_var, text_area):
    RX_Gain_Spec = float(RX_Gain_Spec_var.get())
    new_text_content = ""
    Check = False

    if rat == "HSPA":
        Search_WD = f"[{rat}_BAND{band}_Calibration_Spec]"
        End_WD = f"// APT"
    elif rat == "SUB6":
        Search_WD = f"[{rat}_n{band}_Calibration_Spec]"
        End_WD = "// TX FBRX"

    with open(Selected_spc, "r", encoding="utf-8") as file:
        data_lines = file.readlines()
    file.close()

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(Search_WD):
            new_text_content += line
            Check = True
            text_area.insert(tk.END, f"\n\n{Search_WD}\n\n")
        # Gainstate를 for로 할 경우 너무 많은 반복 -> if 문으로 처리
        elif Check and line.startswith("RX_Gain_main_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_Gain_4rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_Gain_6rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_Gain_8rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_Gain_10rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_Gain_12rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_Gain_14rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_Gain_16rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_main_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_4rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_6rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_8rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_10rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_12rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_14rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("RX_RsrpOffset_16rx_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("AGC_Rx1_LNAON_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("AGC_Rx1_4RX_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("AGC_Rx1_LNAON2_"):
            New_String = change_rx_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("AGC_Rx1_Ch_"):
            New_String = change_rx_ch_spec(line, RX_Gain_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith(End_WD):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def change_rx_spec(line, RX_Gain_Spec, text_area):
    String = re.split("[_=,\t\n]", line)
    String = [v for v in String if v]
    if String[1] == "RsrpOffset":
        text_area.insert(
            tk.END, f"{String[0]:^4} RSRP   {String[2]:<6} {String[3]:<1}          | {String[5]:>5}\t{String[6]:>5}\t  \u2192  "
        )
    else:
        text_area.insert(
            tk.END,
            f"{String[0]:^4}{String[1]:^6}  {String[2]:<6} {String[3]:<1}          | {String[5]:>5}\t{String[6]:>5}\t  \u2192  ",
        )
    RX_Gain_Value = [float(String[5]), float(String[6])]
    RX_Gain_mean = np.mean(RX_Gain_Value)

    String[4] = round(RX_Gain_mean)
    String[5] = round(RX_Gain_mean - RX_Gain_Spec)
    String[6] = round(RX_Gain_mean + RX_Gain_Spec)

    text_area.insert(tk.END, f"\t{String[5]:>5}\t{String[6]:>5}\n")
    text_area.see(tk.END)
    New_String1 = "_".join(map(str, String[:4]))
    New_String2 = "\t".join(map(str, String[4:]))
    New_String = New_String1 + "\t=\t" + New_String2 + "\n"

    return New_String


def change_rx_ch_spec(line, RX_ch_Spec, text_area):
    String = re.split("[_=,\t\n]", line)
    String = [v for v in String if v]
    text_area.insert(
        tk.END,
        f"{String[0]:^4} {String[1]:<3} {String[2]:<2} {String[3]:<5}  {String[4]:<1}          | {String[6]:>5}\t{String[7]:>5}\t  \u2192  ",
    )
    RX_Gain_Value = [float(String[6]), float(String[7])]
    RX_Gain_mean = np.mean(RX_Gain_Value)

    String[5] = round(RX_Gain_mean)
    String[6] = round(RX_Gain_mean - RX_ch_Spec)
    String[7] = round(RX_Gain_mean + RX_ch_Spec)

    text_area.insert(tk.END, f"\t{String[6]:>5}\t{String[7]:>5}\n")
    text_area.see(tk.END)
    New_String1 = "_".join(map(str, String[:5]))
    New_String2 = "\t".join(map(str, String[5:]))
    New_String = New_String1 + "\t=\t" + New_String2 + "\n"

    return New_String


def Chng_2G_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_2G_Spec_var, text_area):
    RX_Gain_2G_Spec = float(RX_Gain_2G_Spec_var.get())
    target_word = f"[{band}_Calibration_Spec]"
    new_text_content = ""
    Check = False
    PRX_Gain_2G = []  # Spec only에서는 빈 리스트만 전달에서 오류 방지
    with open(Selected_spc, "r", encoding="utf-8") as file:
        data_lines = file.readlines()
    file.close()

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(target_word):
            new_text_content += line
            Check = True
            text_area.insert(tk.END, f"\n\n{target_word}\n\n")
        # Gainstate를 for로 할 경우 너무 많은 반복 -> if 문으로 처리
        elif Check & line.startswith("Rx_AGCOffset_0"):
            String = Old_String = line
            String = re.split("\t|\n", line)
            String = [v for v in String if v]
            New_String = L2grx.rx_gain(PRX_Gain_2G, RX_Gain_2G_Spec, band, "Spec_Only", String, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("Rx_AGCOffset_1"):
            String = Old_String = line
            String = re.split("\t|\n", line)
            String = [v for v in String if v]
            New_String = L2grx.rx_gain(PRX_Gain_2G, RX_Gain_2G_Spec, band, "Spec_Only", String, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("Rx_AGCOffset_2"):
            String = Old_String = line
            String = re.split("\t|\n", line)
            String = [v for v in String if v]
            New_String = L2grx.rx_gain(PRX_Gain_2G, RX_Gain_2G_Spec, band, "Spec_Only", String, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("Rx_AGCOffset_3"):
            String = Old_String = line
            String = re.split("\t|\n", line)
            String = [v for v in String if v]
            New_String = L2grx.rx_gain(PRX_Gain_2G, RX_Gain_2G_Spec, band, "Spec_Only", String, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("GMSK_Ref_Power"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def Chng_2g_tx_spec_only(
    Selected_spc, band, GMSK_Spec_var, GTxL_Spec_var, GCode_Spec_var, EPSK_Spec_var, ETxL_Spec_var, ECode_Spec_var, text_area
):
    # 2G TX FBRX Spec
    GMSK_2G_Spec = float(GMSK_Spec_var.get())
    GTxL_2G_Spec = float(GTxL_Spec_var.get())
    GCode_2G_Spec = float(GCode_Spec_var.get())
    EPSK_2G_Spec = float(EPSK_Spec_var.get())
    ETxL_2G_Spec = float(ETxL_Spec_var.get())
    ECode_2G_Spec = float(ECode_Spec_var.get())
    target_word = f"[{band}_Calibration_Spec]"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as file:
        data_lines = file.readlines()
    file.close()

    for index, line in enumerate(data_lines):
        if line.startswith(target_word):
            new_text_content += line
            Check = True
        # Gainstate를 for로 할 경우 너무 많은 반복 -> if 문으로 처리
        elif Check & line.startswith("GMSK_Ref_Power"):
            New_String = tx_power(GMSK_2G_Spec, band, "Ref", line, text_area)
            Change_Str = line.replace(line, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("GMSK_TxL"):
            New_String = tx_power(GCode_2G_Spec, band, "TxL", line, text_area)
            Change_Str = line.replace(line, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("GMSK_Power_TxL"):
            New_String = tx_power(GTxL_2G_Spec, band, "Power_TxL", line, text_area)
            Change_Str = line.replace(line, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("EPSK_Ref_Power"):
            New_String = tx_power(EPSK_2G_Spec, band, "Ref", line, text_area)
            Change_Str = line.replace(line, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("EPSK_TxL"):
            New_String = tx_power(ECode_2G_Spec, band, "TxL", line, text_area)
            Change_Str = line.replace(line, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("EPSK_Power_TxL"):
            New_String = tx_power(ETxL_2G_Spec, band, "Power_TxL", line, text_area)
            Change_Str = line.replace(line, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith("Channel_Comp_GMSK"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def tx_power(Spec_var, band, option, line, text_area):
    String = line.strip().split("\t")
    if option == "Power_TxL":
        text_area.insert(tk.END, f"{String[0]:<30}| {String[2]:>5}\t{String[3]:>5}\t\t\u2192\t")
        TxLevel = int(re.split("TxL|=|\t|\n", line)[1])
        if band == "G085" or band == "G09":
            TxP = (19 - TxLevel) * 2 + 5
        else:
            TxP = (15 - TxLevel) * 2
        String[2] = round(int(TxP) - Spec_var)
        String[3] = round(int(TxP) + Spec_var)
        text_area.insert(tk.END, f"{String[2]:>5}\t{String[3]:>5}\n")
    else:
        text_area.insert(tk.END, f"{String[0]:<30}| {String[3]:>5}\t{String[4]:>5}\t\t\u2192\t")
        text_area.see(tk.END)
        Tx_value = [float(String[3]), float(String[4])]
        Tx_mean = np.mean(Tx_value)
        String[2] = round(int(Tx_mean))
        String[3] = round(int(Tx_mean) - Spec_var)
        String[4] = round(int(Tx_mean) + Spec_var)
        text_area.insert(tk.END, f"{String[3]:>5}\t{String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = "\t".join(map(str, String)) + "\n"

    return New_String


def Chng_fbrx_meas_spec_only(Selected_spc, rat, band, FBRX_Meas_var, FBRX_3G_Spec_var, text_area):
    new_text_content = ""
    Check = False
    if rat == "SUB6":
        target_word = f"[{rat}_n{band}_Calibration_Spec]"
        FBRX_Spec = float(FBRX_Meas_var.get())
        End_word = f"// APT"
    else:
        target_word = f"[{rat}_BAND{band}_Calibration_Spec]"
        FBRX_Spec = float(FBRX_3G_Spec_var.get())
        End_word = f"// Rx Level"

    with open(Selected_spc, "r", encoding="utf-8") as file:
        data_lines = file.readlines()
    file.close()

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(target_word):
            new_text_content += line
            Check = True
        # Gainstate를 for로 할 경우 너무 많은 반복 -> if 문으로 처리
        elif Check and line.startswith("TX_FBRX_GAIN_Index_"):
            New_String = fbrx_spec(line, "hspa", FBRX_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX_Modulation_FBRX_Result"):
            New_String = fbrx_spec(line, "hspa", FBRX_Spec * 100, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX_FBRX_FREQ"):
            New_String = fbrxfreq_spec(line, "hspa", FBRX_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX_FBRX_Pow_Index_"):
            New_String = fbrx_spec(line, "nr", FBRX_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX_FBRX_Code_Index_"):
            New_String = fbrx_spec(line, "nr", FBRX_Spec * 100, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX_FBRX_Channel_Pow"):
            New_String = fbrxfreq_spec(line, "nr", FBRX_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX_FBRX_Channel_Code"):
            New_String = fbrxfreq_spec(line, "nr", FBRX_Spec * 100, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX2_FBRX_Pow_Index_"):
            New_String = fbrx_spec(line, "nr", FBRX_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX2_FBRX_Code_Index_"):
            New_String = fbrx_spec(line, "nr", FBRX_Spec * 100, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX2_FBRX_Channel_Pow"):
            New_String = fbrxfreq_spec(line, "nr", FBRX_Spec, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith("TX2_FBRX_Channel_Code"):
            New_String = fbrxfreq_spec(line, "nr", FBRX_Spec * 100, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check and line.startswith(End_word):
            new_text_content += line
            Check = False

        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def fbrx_spec(line, rat, FBRX_Spec, text_area):
    String = re.split("[_=,\t\n]", line)
    String = [v for v in String if v]
    if rat == "hspa":
        if String[3] == "Index":
            text_area.insert(
                tk.END,
                f"{String[0]:<3}  {String[1]:<6} {String[2]:<4}   {String[3]:<5}   {String[4]:<1}  | {String[6]:>5}\t{String[7]:>5}\t  \u2192  ",
            )
            FBRX_Value = [float(String[6]), float(String[7])]
            FBRX_mean = np.mean(FBRX_Value)
            String[5] = round(FBRX_mean)
            String[6] = round(String[5] - FBRX_Spec)
            String[7] = round(String[5] + FBRX_Spec)
            text_area.insert(tk.END, f"\t{String[6]:>5}\t{String[7]:>5}\n")
            text_area.see(tk.END)
            New_String1 = "_".join(map(str, String[:5]))
            New_String2 = "\t".join(map(str, String[5:]))
        elif line.startswith("TX_Modulation_FBRX_Result"):
            text_area.insert(
                tk.END,
                f"{String[0]:<3}  {String[1]:<10} {String[2]:<4}  {String[3]:<5}  | {String[5]:>5}\t{String[6]:>5}\t  \u2192  ",
            )
            FBRX_Value = [float(String[5]), float(String[6])]
            FBRX_mean = np.mean(FBRX_Value)
            String[4] = round(FBRX_mean)
            String[5] = round(String[4] - FBRX_Spec)
            String[6] = round(String[4] + FBRX_Spec)
            text_area.insert(tk.END, f"\t{String[5]:>5}\t{String[6]:>5}\n")
            text_area.see(tk.END)
            New_String1 = "_".join(map(str, String[:4]))
            New_String2 = "\t".join(map(str, String[4:]))
    elif rat == "nr":
        text_area.insert(
            tk.END,
            f" {String[0]:<3}{String[1]:^6}  {String[2]:<4}   {String[3]:<5}   {String[4]:<1}  | {String[6]:>5}\t{String[7]:>5}\t  \u2192  ",
        )
        FBRX_Value = [float(String[6]), float(String[7])]
        FBRX_mean = np.mean(FBRX_Value)
        String[5] = round(FBRX_mean)
        String[6] = round(String[5] - FBRX_Spec)
        String[7] = round(String[5] + FBRX_Spec)
        text_area.insert(tk.END, f"\t{String[6]:>5}\t{String[7]:>5}\n")
        text_area.see(tk.END)
        New_String1 = "_".join(map(str, String[:5]))
        New_String2 = "\t".join(map(str, String[5:]))

    New_String = New_String1 + "\t=\t" + New_String2 + "\n"

    return New_String


def fbrxfreq_spec(line, rat, FBRX_Spec, text_area):
    String = re.split("[_=,\t\n]", line)
    String = [v for v in String if v]
    if rat == "hspa":
        if String[3] == "RIPPLE":
            text_area.insert(
                tk.END,
                f"{String[0]:<3}  {String[1]:<4}   {String[2]:>4}   {String[3]:>6}     | {String[5]:>5}\t{String[6]:>5}\t  \u2192  ",
            )
            FBRX_Value = [float(String[5]), float(String[6])]
            FBRX_mean = np.mean(FBRX_Value)
            String[4] = round(FBRX_mean)
            String[5] = round(String[4] - FBRX_Spec)
            String[6] = round(String[4] + FBRX_Spec)
            text_area.insert(tk.END, f"\t{String[5]:>5}\t{String[6]:>5}\n")
            text_area.see(tk.END)
            New_String1 = "_".join(map(str, String[:4]))
            New_String2 = "\t".join(map(str, String[4:]))
        else:
            text_area.insert(
                tk.END,
                f"{String[0]:<3}  {String[1]:<4}   {String[2]:>4}              | {String[4]:>5}\t{String[5]:>5}\t  \u2192  ",
            )
            FBRX_Value = [float(String[4]), float(String[5])]
            FBRX_mean = np.mean(FBRX_Value)
            String[3] = round(FBRX_mean)
            String[4] = round(String[3] - FBRX_Spec)
            String[5] = round(String[3] + FBRX_Spec)
            text_area.insert(tk.END, f"\t{String[4]:>5}\t{String[5]:>5}\n")
            text_area.see(tk.END)
            New_String1 = "_".join(map(str, String[:3]))
            New_String2 = "\t".join(map(str, String[3:]))
    elif rat == "nr":
        text_area.insert(
            tk.END,
            f" {String[0]:<3}{String[1]:^6}  {String[2]:<6}{String[3]:<4}       | {String[5]:>5}\t{String[6]:>5}\t  \u2192  ",
        )
        FBRX_Value = [float(String[5]), float(String[6])]
        FBRX_mean = np.mean(FBRX_Value)
        String[4] = round(FBRX_mean)
        String[5] = round(String[4] - FBRX_Spec)
        String[6] = round(String[4] + FBRX_Spec)
        text_area.insert(tk.END, f"\t{String[5]:>5}\t{String[6]:>5}\n")
        text_area.see(tk.END)
        New_String1 = "_".join(map(str, String[:4]))
        New_String2 = "\t".join(map(str, String[4:]))

    New_String = New_String1 + "\t=\t" + New_String2 + "\n"

    return New_String


def Chng_apt_cal_spec_only(Selected_spc, rat, band, APT_Spec_var, text_area):
    APT_Spec = float(APT_Spec_var.get())
    new_text_content = ""
    Check = False

    if rat == "HSPA":
        Search_WD = f"[{rat}_BAND{band}_Calibration_Spec]"
        End_WD = f"TX_DC_I"
    elif rat == "SUB6":
        Search_WD = f"[{rat}_n{band}_Calibration_Spec]"
        End_WD = f"ET_Channel_Comp_0_0"

    with open(Selected_spc, "r", encoding="utf-8") as file:
        data_lines = file.readlines()
    file.close()

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(Search_WD):
            new_text_content += line
            Check = True
        elif Check & line.startswith("TX_APT_PA_"):  # !HSPA
            New_String = apt_spec_only(line, APT_Spec)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_APT_High_Gain_Index_"):  # !NR
            New_String = apt_spec_only(line, APT_Spec)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_APT_Mid_Gain_Index_"):
            New_String = apt_spec_only(line, APT_Spec)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_APT_Low_Gain_Index_"):
            New_String = apt_spec_only(line, APT_Spec)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_APT_High_Gain_Index_"):  # !NR TX2
            New_String = apt_spec_only(line, APT_Spec)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_APT_Mid_Gain_Index_"):
            New_String = apt_spec_only(line, APT_Spec)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_APT_Low_Gain_Index_"):
            New_String = apt_spec_only(line, APT_Spec)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_APT_Cal_Diff"):  # !APT Splim
            New_String = sub6_apt_slim_spec_only(line, APT_Spec)
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


def apt_spec_only(line, APT_Spec):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]

    if (New_String[1] == "-10") & (New_String[2] == "-10.1") & (New_String[3] == "-9.9"):
        pass
    else:
        New_String[2] = int(New_String[1]) - float(APT_Spec)
        New_String[3] = int(New_String[1]) + float(APT_Spec)

    New_String[0] = "_".join(Word) + "\t" + "="
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def sub6_apt_slim_spec_only(line, APT_Spec):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    New_String[1] = 0
    New_String[2] = int(New_String[1]) - float(APT_Spec)
    New_String[3] = int(New_String[1]) + float(APT_Spec)
    New_String[0] = "_".join(Word) + "\t" + "="
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String
