import re
import tkinter as tk


def chng_3g_rx_gain_default(flag, Selected_spc, rat, band, HSPA_RX_Gain_default, text_area):
    if flag == "daseul":
        target_word = f"[{rat}_BAND{band}_CAL_PARAM]"
        with open(Selected_spc, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()
    elif flag == "mtm":
        target_word = f"[{rat}_CALIBRATION_PARAM_BAND{band}]"
        with open(Selected_spc, "r", encoding="latin_1") as file:
            data_lines = file.readlines()
        file.close()

    text_area.insert(tk.END, f"\n{target_word}\n")
    text_area.insert(tk.END, "-" * 100)
    text_area.insert(tk.END, "\n")
    text_area.see(tk.END)

    new_text_content = ""
    Check = False
    enable_4RX = False

    for index, line in enumerate(data_lines):
        New_String = Old_String = line

        if line.startswith(target_word):
            new_text_content += line
            Check = True
        elif Check & line.startswith("4RX_Cal_Mode="):
            Diversity = re.split("=| |//", line)
            if Diversity[1] != "0":
                enable_4RX = True
            new_text_content += line
        # Gainstate를 for로 할 경우 너무 많은 반복 -> if 문으로 처리
        elif Check & line.startswith(f"RX_Gain_PRX_Default_LNAOn="):
            New_String = Rxgain_3g_cal(line, band, "Main", "PRX", "LNAON", 5, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"RX_Gain_PRX_Default_LNAOn2="):
            New_String = Rxgain_3g_cal(line, band, "Main", "PRX", "LNAON2", 5, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"RX_Gain_PRX_Default_BypassLNA="):
            New_String = Rxgain_3g_cal(line, band, "Main", "PRX", "LNABYP", 5, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"RX_Gain_DRX_Default_LNAOn="):
            New_String = Rxgain_3g_cal(line, band, "Main", "DRX", "LNAON", 5, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"RX_Gain_DRX_Default_LNAOn2="):
            New_String = Rxgain_3g_cal(line, band, "Main", "DRX", "LNAON2", 5, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"RX_Gain_DRX_Default_BypassLNA="):
            New_String = Rxgain_3g_cal(line, band, "Main", "DRX", "LNABYP", 5, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & enable_4RX & line.startswith(f"RX_Gain_4RX(PRX)Default="):
            New_String = Rxgain_3g_cal(line, band, "4RX", "PRX", "LNAON", 3, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & enable_4RX & line.startswith(f"RX_Gain_4RX(DRX)Default="):
            New_String = Rxgain_3g_cal(line, band, "4RX", "DRX", "LNAON", 3, HSPA_RX_Gain_default, text_area)
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
            enable_4RX = False
        elif Check & (line.startswith("ET_MODE")):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    # text_area.insert(tk.END, f"Tech= {rat}  \t| Band= {band:<7}\t| Ant= {Antenna}\t| Path= {Path}\n")
    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def Rxgain_3g_cal(line, band, ant, path, lna, Position, HSPA_RX_Gain_default, text_area):
    band = f"WB{band}"
    New_String = re.split(r"[_=,\n]", line)  # 띄어쓰기로 분리
    New_String = [v for v in New_String if v]

    if HSPA_RX_Gain_default[band][ant][path].get([lna]) is not None:
        text_area.insert(tk.END, f"{ant:<4} {path} {lna:<6}|   ")
        text_area.insert(tk.END, f"{New_String[Position]:>5}\n")

        New_String[Position] = int(round(HSPA_RX_Gain_default[band][ant][path][lna], 1) * 256)

        text_area.insert(tk.END, f"               | \u2192 ")
        text_area.insert(tk.END, f"{New_String[Position]:>5}\n\n")
        text_area.see(tk.END)

    New_String1 = "_".join(map(str, New_String[:Position]))
    New_String = New_String1 + "=" + str(New_String[Position]) + "\n"

    return New_String


def chng_3g_rx_freq_default(
    flag, Selected_spc, rat, band, HSPA_RX_Freq_default, Bluetick, blue_3grx_freq, blue_3gdrx_offset, text_area
):
    if flag == "daseul":
        target_word = f"[{rat}_BAND{band}_CAL_PARAM]"
        with open(Selected_spc, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()
    elif flag == "mtm":
        target_word = f"[{rat}_CALIBRATION_PARAM_BAND{band}]"
        with open(Selected_spc, "r", encoding="latin_1") as file:
            data_lines = file.readlines()
        file.close()

    new_text_content = ""
    Check = False
    Enable_4RX = False

    for index, line in enumerate(data_lines):
        New_String = Old_String = line

        if line.startswith(target_word):
            new_text_content += line
            Check = True
        elif Check & line.startswith("4RX_Cal_Mode="):
            Diversity = re.split("=| |//", line)
            if Diversity[1] != "0":
                Enable_4RX = True
            new_text_content += line
        elif Check & line.startswith("RX_Comp_Ch="):
            result = re.split(r"[ |\t|//]", line)  # 띄어쓰기로 // 분리
            Freq_List = re.split("[=,\n]", result[0])[1:]
            Freq_List = [v for v in Freq_List if v]
            new_text_content += line
        elif Check & line.startswith(f"RX_Comp_PRX_Default="):
            New_String = Rxfreq_3g_cal(
                Freq_List,
                line,
                band,
                "Main",
                "PRX",
                4,
                HSPA_RX_Freq_default,
                Bluetick,
                blue_3grx_freq,
                blue_3gdrx_offset,
                text_area,
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"RX_Comp_DRX_Default="):
            New_String = Rxfreq_3g_cal(
                Freq_List,
                line,
                band,
                "Main",
                "DRX",
                4,
                HSPA_RX_Freq_default,
                Bluetick,
                blue_3grx_freq,
                blue_3gdrx_offset,
                text_area,
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & Enable_4RX & line.startswith(f"RX_Comp_4RX(PRX)Default="):
            New_String = Rxfreq_3g_cal(
                Freq_List,
                line,
                band,
                "4RX",
                "PRX",
                3,
                HSPA_RX_Freq_default,
                Bluetick,
                blue_3grx_freq,
                blue_3gdrx_offset,
                text_area,
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & Enable_4RX & line.startswith(f"RX_Comp_4RX(DRX)Default="):
            New_String = Rxfreq_3g_cal(
                Freq_List,
                line,
                band,
                "4RX",
                "DRX",
                3,
                HSPA_RX_Freq_default,
                Bluetick,
                blue_3grx_freq,
                blue_3gdrx_offset,
                text_area,
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"ET_MODE"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def Rxfreq_3g_cal(
    Freq_List, line, band, ant, path, Position, HSPA_RX_Freq_default, Bluetick, blue_3grx_freq, blue_3gdrx_offset, text_area
):
    band = f"WB{band}"
    New_String = re.split("[_=,\n]", line)
    New_String = [v for v in New_String if v]
    text_area.insert(tk.END, f"{ant:<4} {path} FREQ  |   ")
    text_area.see(tk.END)

    for i in range(len(New_String[Position:])):
        if i == range(len(New_String[Position:]))[-1]:
            text_area.insert(tk.END, f"{New_String[Position+i]:>5}\n")
            text_area.see(tk.END)
        else:
            text_area.insert(tk.END, f"{New_String[Position+i]:>5}, ")
            text_area.see(tk.END)
    text_area.insert(tk.END, f"               | \u2192 ")

    del New_String[Position:]
    # Freq_List 길이만큼 0 으로 채워넣기 하고 값을 변경
    for i in range(len(Freq_List)):
        New_String.append(0)
        if Bluetick & (band == "WB5") & (path == "DRX"):
            if int(Freq_List[i]) == blue_3grx_freq:
                New_String[Position + i] = int(
                    (round(HSPA_RX_Freq_default[band][ant][path][Freq_List[i]], 1) - blue_3gdrx_offset) * 256
                )
            else:
                New_String[Position + i] = int(round(HSPA_RX_Freq_default[band][ant][path][Freq_List[i]], 1) * 256)
        else:
            New_String[Position + i] = int(round(HSPA_RX_Freq_default[band][ant][path][Freq_List[i]], 1) * 256)

    for i in range(len(Freq_List)):
        if i == range(len(Freq_List))[-1]:
            text_area.insert(tk.END, f"{New_String[Position+i]:>5}\n\n")
            text_area.see(tk.END)
        else:
            text_area.insert(tk.END, f"{New_String[Position+i]:>5}, ")
            text_area.see(tk.END)
    text_area.see(tk.END)

    New_String1 = "_".join(map(str, New_String[:Position]))
    New_String2 = ",".join(map(str, New_String[Position:]))
    New_String = New_String1 + "=" + New_String2 + "\n"

    return New_String
