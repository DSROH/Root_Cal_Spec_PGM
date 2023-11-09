import re
import tkinter as tk
import numpy as np
import pandas as pd
import Common_function as func


def GSM_Params(band, data_lines):
    target_word = f"[{band}_Calibration_Parameter]"
    Param = False
    MPM = LPM = ULPM = True
    for index, line in enumerate(data_lines):
        if target_word in line:
            Param = True
        elif Param & line.startswith("Tx_PAMAPTGainMode_GMSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            Gainmode = New_String[1:]
            if Gainmode[1] == "0":
                MPM = False
            if Gainmode[2] == "0":
                LPM = False
            if Gainmode[3] == "0":
                ULPM = False
        elif Param & line.startswith("Tx_APT_HPM_CalIndex_GMSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            HPM_Index = New_String[1:5]
        elif Param & line.startswith("Tx_APT_MPM_CalIndex_GMSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            MPM_Index = New_String[1:3]
        elif Param & line.startswith("Tx_APT_LPM_CalIndex_GMSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            LPM_Index = New_String[1:3]
        elif Param & line.startswith("Tx_APT_ULPM_CalIndex_GMSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            ULPM_Index = New_String[1:3]
        elif Param & line.startswith("Tx_PAMAPTGainMode_EPSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            Gainmode = New_String[1:]
            if Gainmode[1] == "0":
                EPSK_MPM = False
            if Gainmode[2] == "0":
                EPSK_LPM = False
            if Gainmode[3] == "0":
                EPSK_ULPM = False
        elif Param & line.startswith("Tx_APT_HPM_CalIndex_EPSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            EPSK_HPM_Index = New_String[1:5]
        elif Param & line.startswith("Tx_APT_MPM_CalIndex_EPSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            EPSK_MPM_Index = New_String[1:5]
        elif Param & line.startswith("Tx_APT_LPM_CalIndex_EPSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            EPSK_LPM_Index = New_String[1:5]
        elif Param & line.startswith("Tx_APT_ULPM_CalIndex_EPSK="):
            New_String = re.split("=|,| |//|\n", line)
            New_String = [v for v in New_String if v]
            EPSK_ULPM_Index = New_String[1:5]
        elif line.startswith("EPSK_FineTxCal="):
            Param = False

    return (
        HPM_Index,
        MPM_Index,
        LPM_Index,
        ULPM_Index,
        EPSK_HPM_Index,
        EPSK_MPM_Index,
        EPSK_LPM_Index,
        EPSK_ULPM_Index,
        MPM,
        LPM,
        ULPM,
        EPSK_MPM,
        EPSK_LPM,
        EPSK_ULPM,
    )


def chng_2g_index_GMSK(Selected_spc, band, GMSK_Code_Mean, text_area):
    target_word = f"[{band}_Calibration_Parameter]"
    new_text_content = ""
    Check = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()
    HCheck = MCheck = LCheck = ULCheck = False

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("Tx_PAMAPTGainMode_GMSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            Gainmode = [int(float(v)) for v in New_String[1:] if v]
            # HPM max level
            if band in ["G09", "G085"]:
                if Gainmode[0] == 19:
                    Gainmode[4] = 19
                    One_gainmode = True
                else:
                    One_gainmode = False
                Gainmode[0] = 5
                HCheck = True
            else:
                if Gainmode[0] == 15:
                    Gainmode[4] = 15
                    One_gainmode = True
                else:
                    One_gainmode = False
                Gainmode[0] = 0
                HCheck = True
            # Gain mode
            if Gainmode[1] != 0:
                MCheck = True
            if Gainmode[2] != 0:
                LCheck = True
            if Gainmode[3] != 0:
                ULCheck = True
            new_text_content += line
        elif Check & HCheck & line.startswith("Tx_APT_HPM_CalIndex_GMSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            HPM_index = [int(float(v)) for v in New_String[1:] if v]
            if One_gainmode:
                HPM_index[0] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[0]}"]) - 2
                HPM_index[1] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[4]}"])
                HPM_index[2] = HPM_index[1] + 1
                HPM_index[3] = HPM_index[2] + 1
            else:
                HPM_index[0] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[0]}"]) - 2
                HPM_index[1] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[4]}"])
            New_String1 = ",".join(map(str, HPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & MCheck & line.startswith("Tx_APT_MPM_CalIndex_GMSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            MPM_index = [int(float(v)) for v in New_String[1:] if v]
            MPM_index[0] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[1]}"])
            MPM_index[1] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[5]}"])
            New_String1 = ",".join(map(str, MPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & LCheck & line.startswith("Tx_APT_LPM_CalIndex_GMSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            LPM_index = [int(float(v)) for v in New_String[1:] if v]
            LPM_index[0] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[2]}"])
            LPM_index[1] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[6]}"])
            New_String1 = ",".join(map(str, LPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & ULCheck & line.startswith("Tx_APT_ULPM_CalIndex_GMSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            ULPM_index = [int(float(v)) for v in New_String[1:] if v]
            ULPM_index[0] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[3]}"])
            ULPM_index[1] = round(GMSK_Code_Mean[band, f"TxL{Gainmode[7]}"])
            New_String1 = ",".join(map(str, ULPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & ("_Calibration_Parameter]" in line):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    text_area.insert(tk.END, f"\n")
    text_area.see(tk.END)

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_2g_index_EPSK(Selected_spc, band, EPSK_Code_Mean, text_area):
    target_word = f"[{band}_Calibration_Parameter]"
    new_text_content = ""
    Check = False
    One_gainmode = False

    with open(Selected_spc, "r", encoding="utf-8") as f:
        data_lines = f.readlines()
    f.close()
    HCheck = MCheck = LCheck = ULCheck = False

    for index, line in enumerate(data_lines):
        if target_word in line:
            Check = True
            new_text_content += line
        elif Check & line.startswith("Tx_PAMAPTGainMode_EPSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            Gainmode = [int(float(v)) for v in New_String[1:] if v]
            # HPM max level
            if band in ["G09", "G085"]:
                if Gainmode[0] == 19:
                    Gainmode[4] = 19
                    One_gainmode = True
                else:
                    One_gainmode = False
                Gainmode[0] = 8
                HCheck = True
            else:
                if Gainmode[0] == 15:
                    Gainmode[4] = 15
                    One_gainmode = True
                else:
                    One_gainmode = False
                Gainmode[0] = 2
                HCheck = True
            # Gain mode
            if Gainmode[1] != 0:
                MCheck = True
            if Gainmode[2] != 0:
                LCheck = True
            if Gainmode[3] != 0:
                ULCheck = True
            new_text_content += line
        elif Check & HCheck & line.startswith("Tx_APT_HPM_CalIndex_EPSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            HPM_index = [int(float(v)) for v in New_String[1:] if v]
            if One_gainmode:
                HPM_index[0] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[0]}"]) - 2
                HPM_index[1] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[4]}"])
                HPM_index[2] = HPM_index[1] + 1
                HPM_index[3] = HPM_index[2] + 1
            else:
                HPM_index[0] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[0]}"]) - 2
                HPM_index[1] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[4]}"])
            New_String1 = ",".join(map(str, HPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & MCheck & line.startswith("Tx_APT_MPM_CalIndex_EPSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            MPM_index = [int(float(v)) for v in New_String[1:] if v]
            MPM_index[0] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[1]}"])
            MPM_index[1] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[5]}"])
            New_String1 = ",".join(map(str, MPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & LCheck & line.startswith("Tx_APT_LPM_CalIndex_EPSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            LPM_index = [int(float(v)) for v in New_String[1:] if v]
            LPM_index[0] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[2]}"])
            LPM_index[1] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[6]}"])
            New_String1 = ",".join(map(str, LPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & ULCheck & line.startswith("Tx_APT_ULPM_CalIndex_EPSK"):
            New_String = Old_String = line
            New_String = re.split("=|,| |//|\n", line)
            ULPM_index = [int(float(v)) for v in New_String[1:] if v]
            ULPM_index[0] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[3]}"])
            ULPM_index[1] = round(EPSK_Code_Mean[band, f"TxL{Gainmode[7]}"])
            New_String1 = ",".join(map(str, ULPM_index))
            New_String = New_String[0] + "=" + New_String1 + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & ("_Calibration_Parameter]" in line):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def chng_2g_tx_gmsk(
    Selected_spc,
    band,
    GMSK_Spec_var,
    GMSK_Mean,
    GTxL_Spec_var,
    GMSK_TXL_Mean,
    GCode_Spec_var,
    GMSK_Code_Mean,
    MPM,
    LPM,
    ULPM,
    HPM_Index,
    MPM_Index,
    LPM_Index,
    ULPM_Index,
    text_area,
):
    GMSK_Spec = int(GMSK_Spec_var.get())
    GTxL_Spec = int(GTxL_Spec_var.get())
    GCode_Spec = int(GCode_Spec_var.get())
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
        elif Check & line.startswith("GMSK_Ref_Power"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Word = re.split("Power", New_String[0])
            Word = [v for v in Word if v]
            Index_N = int(Word[1])
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            if Index_N in [0, 1, 2, 3]:
                gain = "HPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain][HPM_Index[Index_N]])
            elif Index_N in [4]:
                gain = "HPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain]["Index"])
            elif MPM & (Index_N in [5, 6]):
                gain = "MPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain][MPM_Index[Index_N - 5]])
            elif MPM & (Index_N in [7]):
                gain = "MPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain]["Index"])
            elif LPM & (Index_N in [8, 9]):
                gain = "LPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain][LPM_Index[Index_N - 8]])
            elif LPM & (Index_N in [10]):
                gain = "LPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain]["Index"])
            elif ULPM & (Index_N in [11, 12]):
                gain = "ULPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain][ULPM_Index[Index_N - 11]])
            elif ULPM & (Index_N in [13]):
                gain = "ULPM"
                New_String[2] = round(GMSK_Mean[band, "GMSK", gain]["Index"])
            else:
                New_String[2] = 0
            New_String[3] = New_String[2] - GMSK_Spec
            New_String[4] = New_String[2] + GMSK_Spec
            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            Word = "Power".join(Word)
            New_String[0] = Word
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("GMSK_TxL"):  # Code
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Word = re.split("_", New_String[0])
            Word = [v for v in Word if v]
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            New_String[2] = round(GMSK_Code_Mean[band, Word[1]])
            New_String[3] = New_String[2] - GCode_Spec
            New_String[4] = New_String[2] + GCode_Spec
            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("GMSK_Power_TxL"):  # TX Powerl level
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Word = re.split("_", New_String[0])
            Word = [v for v in Word if v]
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[2]:>5}\t{New_String[3]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            New_String[2] = str(round(GMSK_TXL_Mean[band, Word[2]]) - GTxL_Spec)
            New_String[3] = str(round(GMSK_TXL_Mean[band, Word[2]]) + GTxL_Spec)
            text_area.insert(tk.END, f"{New_String[2]:>5}\t{New_String[3]:>5}\n")
            text_area.see(tk.END)
            New_String = "\t".join(New_String) + "\n"
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


def chng_2g_tx_epsk(
    Selected_spc,
    band,
    EPSK_Spec_var,
    EPSK_Mean,
    ETxL_Spec_var,
    EPSK_TXL_Mean,
    ECode_Spec_var,
    EPSK_Code_Mean,
    EPSK_MPM,
    EPSK_LPM,
    EPSK_ULPM,
    EPSK_HPM_Index,
    EPSK_MPM_Index,
    EPSK_LPM_Index,
    EPSK_ULPM_Index,
    text_area,
):
    EPSK_Spec = int(EPSK_Spec_var.get())
    ETxL_Spec = int(ETxL_Spec_var.get())
    ECode_Spec = int(ECode_Spec_var.get())
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
        elif Check & line.startswith("EPSK_Ref_Power"):
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Word = re.split("Power", New_String[0])
            Word = [v for v in Word if v]
            Index_N = int(Word[1])
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            if Index_N in [0, 1, 2, 3]:
                gain = "HPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain][EPSK_HPM_Index[Index_N]])
            elif (EPSK_MPM == True or EPSK_LPM == True or EPSK_ULPM == True) & (Index_N in [4]):
                gain = "HPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain]["Index"])
            elif EPSK_MPM & (Index_N in [5, 6]):
                gain = "MPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain][EPSK_MPM_Index[Index_N - 5]])
            elif EPSK_MPM & (Index_N in [7]):
                gain = "MPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain]["Index"])
            elif EPSK_LPM & (Index_N in [8, 9]):
                gain = "LPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain][EPSK_LPM_Index[Index_N - 8]])
            elif EPSK_LPM & (Index_N in [10]):
                gain = "LPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain]["Index"])
            elif EPSK_ULPM & (Index_N in [11, 12]):
                gain = "ULPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain][EPSK_ULPM_Index[Index_N - 11]])
            elif EPSK_ULPM & (Index_N in [13]):
                gain = "ULPM"
                New_String[2] = round(EPSK_Mean[band, "EPSK", gain]["Index"])
            else:
                New_String[2] = 0
            New_String[3] = New_String[2] - EPSK_Spec
            New_String[4] = New_String[2] + EPSK_Spec
            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            Word = "Power".join(Word)
            New_String[0] = Word
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("EPSK_TxL"):  # Code
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Word = re.split("_", New_String[0])
            Word = [v for v in Word if v]
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            New_String[2] = round(EPSK_Code_Mean[band, Word[1]])
            New_String[3] = New_String[2] - ECode_Spec
            New_String[4] = New_String[2] + ECode_Spec
            text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
            text_area.see(tk.END)
            New_String = [str(v) for v in New_String]
            New_String = "\t".join(New_String) + "\n"
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("EPSK_Power_TxL"):  # TX Power level
            New_String = Old_String = line
            New_String = re.split("\t|\n", line)
            New_String = [v for v in New_String if v]
            Word = re.split("_", New_String[0])
            Word = [v for v in Word if v]
            text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[2]:>5}\t{New_String[3]:>5}\t\t\u2192\t")
            text_area.see(tk.END)
            New_String[2] = str(round(EPSK_TXL_Mean[band, Word[2]]) - ETxL_Spec)
            New_String[3] = str(round(EPSK_TXL_Mean[band, Word[2]]) + ETxL_Spec)
            text_area.insert(tk.END, f"{New_String[2]:>5}\t{New_String[3]:>5}\n")
            text_area.see(tk.END)
            New_String = "\t".join(New_String) + "\n"
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


def gsm_tx_gmsk_average(df_Meas, df_Code, Save_data_var, text_area):
    df_gmsk = df_Meas[df_Meas["Test Conditions"].str.contains("CH_GMSK_").to_list()]
    df_gmsk_Value = df_gmsk.iloc[:, 1:]
    df_gmsk_Item = df_gmsk["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_gmsk_Item.drop(columns=[1, 2, 5, 7, 8, 9, 10, 11], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_gmsk_Item.columns = ["Band", "Type", "Gain", "Index"]
    df_gmsk_Item = df_gmsk_Item.replace({"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}})
    df_gmsk = pd.merge(df_gmsk_Item, df_gmsk_Value, left_index=True, right_index=True)
    df_null = df_gmsk[df_gmsk["Index"].isnull()].index
    df_gmsk.drop(df_null, inplace=True)

    df_gmsk_Mean = round(df_gmsk.groupby(["Band", "Type", "Gain", "Index"], sort=False).mean(), 1)
    df_gmsk_Mean = pd.concat([df_gmsk_Mean, round(df_gmsk_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_gmsk_Mean = pd.concat([df_gmsk_Mean, round(df_gmsk_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_gmsk_Mean = pd.concat([df_gmsk_Mean, round(df_gmsk_Mean.min(axis=1), 1).rename("Min")], axis=1)

    df_gmsk_TxL = df_Meas[df_Meas["Test Conditions"].str.contains("CH_GMSK_TxL").to_list()]
    df_gmsk_TxL_Value = df_gmsk_TxL.iloc[:, 1:]
    df_gmsk_TxL_Item = df_gmsk_TxL["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_gmsk_TxL_Item.drop(columns=[1, 2, 3, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_gmsk_TxL_Item.columns = ["Band", "TXL"]
    df_gmsk_TxL_Item = df_gmsk_TxL_Item.replace(
        {"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}}
    )
    df_gmsk_TxL = pd.merge(df_gmsk_TxL_Item, df_gmsk_TxL_Value, left_index=True, right_index=True)
    df_gmsk_TxL_Mean = round(df_gmsk_TxL.groupby(["Band", "TXL"], sort=False).mean(), 1)
    df_gmsk_TxL_Mean = pd.concat([df_gmsk_TxL_Mean, round(df_gmsk_TxL_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_gmsk_TxL_Mean = pd.concat([df_gmsk_TxL_Mean, round(df_gmsk_TxL_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_gmsk_TxL_Mean = pd.concat([df_gmsk_TxL_Mean, round(df_gmsk_TxL_Mean.min(axis=1), 1).rename("Min")], axis=1)

    df_gmsk_Code = df_Code[df_Code["Test Conditions"].str.contains("CH_GMSK_TxL").to_list()]
    df_gmsk_Code_Value = df_gmsk_Code.iloc[:, 1:]
    df_gmsk_Code_Item = df_gmsk_Code["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_gmsk_Code_Item.drop(columns=[1, 2, 3, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_gmsk_Code_Item.columns = ["Band", "TXL"]
    df_gmsk_Code_Item = df_gmsk_Code_Item.replace(
        {"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}}
    )
    df_gmsk_Code = pd.merge(df_gmsk_Code_Item, df_gmsk_Code_Value, left_index=True, right_index=True)
    df_gmsk_Code_Mean = round(df_gmsk_Code.groupby(["Band", "TXL"], sort=False).mean(), 1)
    df_gmsk_Code_Mean = pd.concat([df_gmsk_Code_Mean, round(df_gmsk_Code_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_gmsk_Code_Mean = pd.concat([df_gmsk_Code_Mean, round(df_gmsk_Code_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_gmsk_Code_Mean = pd.concat([df_gmsk_Code_Mean, round(df_gmsk_Code_Mean.min(axis=1), 1).rename("Min")], axis=1)

    if Save_data_var.get():
        filename = "Excel_2G_GMSK.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_gmsk_Mean.to_excel(writer, sheet_name="GMSK_Mean")
            df_gmsk_TxL_Mean.to_excel(writer, sheet_name="GMSK_TXL_Mean")
            df_gmsk_Code_Mean.to_excel(writer, sheet_name="GMSK_Code_Mean")
        func.WB_Format(filename, 2, 5, 0, text_area)

    return df_gmsk_Mean["Average"], df_gmsk_TxL_Mean["Average"], df_gmsk_Code_Mean["Average"]


def gsm_tx_edge_average(df_Meas, df_Code, Save_data_var, text_area):
    df_edge = df_Meas[df_Meas["Test Conditions"].str.contains("CH_EPSK_").to_list()]
    df_edge_Value = df_edge.iloc[:, 1:]
    df_edge_Item = df_edge["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_edge_Item.drop(columns=[1, 2, 5, 7, 8, 9, 10], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_edge_Item.columns = ["Band", "Type", "Gain", "Index"]
    df_edge_Item = df_edge_Item.replace({"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}})
    df_edge = pd.merge(df_edge_Item, df_edge_Value, left_index=True, right_index=True)
    df_null = df_edge[df_edge["Index"].isnull()].index
    df_edge.drop(df_null, inplace=True)

    df_edge_Mean = round(df_edge.groupby(["Band", "Type", "Gain", "Index"], sort=False).mean(), 1)
    df_edge_Mean = pd.concat([df_edge_Mean, round(df_edge_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_edge_Mean = pd.concat([df_edge_Mean, round(df_edge_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_edge_Mean = pd.concat([df_edge_Mean, round(df_edge_Mean.min(axis=1), 1).rename("Min")], axis=1)

    df_edge_TxL = df_Meas[df_Meas["Test Conditions"].str.contains("CH_EPSK_TxL").to_list()]
    df_edge_TxL_Value = df_edge_TxL.iloc[:, 1:]
    df_edge_TxL_Item = df_edge_TxL["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_edge_TxL_Item.drop(columns=[1, 2, 3, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_edge_TxL_Item.columns = ["Band", "TXL"]
    df_edge_TxL_Item = df_edge_TxL_Item.replace(
        {"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}}
    )
    df_edge_TxL = pd.merge(df_edge_TxL_Item, df_edge_TxL_Value, left_index=True, right_index=True)
    df_edge_TxL_Mean = round(df_edge_TxL.groupby(["Band", "TXL"], sort=False).mean(), 1)
    df_edge_TxL_Mean = pd.concat([df_edge_TxL_Mean, round(df_edge_TxL_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_edge_TxL_Mean = pd.concat([df_edge_TxL_Mean, round(df_edge_TxL_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_edge_TxL_Mean = pd.concat([df_edge_TxL_Mean, round(df_edge_TxL_Mean.min(axis=1), 1).rename("Min")], axis=1)

    df_edge_Code = df_Code[df_Code["Test Conditions"].str.contains("CH_EPSK_TxL").to_list()]
    df_edge_Code_Value = df_edge_Code.iloc[:, 1:]
    df_edge_Code_Item = df_edge_Code["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_edge_Code_Item.drop(columns=[1, 2, 3, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_edge_Code_Item.columns = ["Band", "TXL"]
    df_edge_Code_Item = df_edge_Code_Item.replace(
        {"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}}
    )
    df_edge_Code = pd.merge(df_edge_Code_Item, df_edge_Code_Value, left_index=True, right_index=True)
    df_edge_Code_Mean = round(df_edge_Code.groupby(["Band", "TXL"], sort=False).mean(), 1)
    df_edge_Code_Mean = pd.concat([df_edge_Code_Mean, round(df_edge_Code_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_edge_Code_Mean = pd.concat([df_edge_Code_Mean, round(df_edge_Code_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_edge_Code_Mean = pd.concat([df_edge_Code_Mean, round(df_edge_Code_Mean.min(axis=1), 1).rename("Min")], axis=1)

    if Save_data_var.get():
        filename = "Excel_2G_EPSK.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_edge_Mean.to_excel(writer, sheet_name="EDGE_Mean")
            df_edge_TxL_Mean.to_excel(writer, sheet_name="EDGE_TXL_Mean")
            df_edge_Code_Mean.to_excel(writer, sheet_name="EDGE_Code_Mean")
        func.WB_Format(filename, 2, 5, 0, text_area)

    return df_edge_Mean["Average"], df_edge_TxL_Mean["Average"], df_edge_Code_Mean["Average"]
