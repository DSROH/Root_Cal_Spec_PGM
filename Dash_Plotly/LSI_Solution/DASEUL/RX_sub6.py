import re
import tkinter as tk


def chng_sub6_rx_gain(Selected_spc, rat, band, read_stage, RX_Gain_Spec_var, RXGain_sub6, RXRSRP_sub6, RXComp_sub6, text_area):
    RX_Gain_Spec = int(RX_Gain_Spec_var.get())
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
        elif Check & line.startswith("RX_Gain_main_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "MAIN", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_Gain_4rx_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "4RX", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_Gain_6rx_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "6RX", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_Gain_8rx_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "8RX", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_Gain_10rx_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "10RX", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_Gain_12rx_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "12RX", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_Gain_14rx_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "14RX", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_Gain_16rx_"):
            new_text_content = Sub6_RX_Gain(
                new_text_content, line, read_stage, band, "16RX", RXGain_sub6, RX_Gain_Spec, text_area
            )
        elif Check & line.startswith("RX_RsrpOffset_main_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "MAIN", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_RsrpOffset_4rx_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "4RX", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_RsrpOffset_6rx_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "6RX", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_RsrpOffset_8rx_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "8RX", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_RsrpOffset_10rx_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "10RX", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_RsrpOffset_12rx_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "12RX", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_RsrpOffset_14rx_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "14RX", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_RsrpOffset_16rx_"):
            new_text_content = Sub6_RX_RSRP_offset(new_text_content, line, band, "16RX", RXRSRP_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_FreqOffset_prx_"):
            new_text_content = Sub6_RX_FREQ_offset(new_text_content, line, band, "PRX", RXComp_sub6, RX_Gain_Spec, text_area)
        elif Check & line.startswith("RX_FreqOffset_drx_"):
            new_text_content = Sub6_RX_FREQ_offset(new_text_content, line, band, "DRX", RXComp_sub6, RX_Gain_Spec, text_area)
        elif line == "// TX FBRX\n":
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def Sub6_RX_Gain(new_text_content, line, read_stage, band, path, RXGain_sub6, RX_Gain_Spec, text_area):
    New_String = Old_String = line
    New_String = re.split("\t|\n", New_String)
    New_String = [v for v in New_String if v]
    gainstage = int(re.sub(r"[^0-9]", "", re.split("_", New_String[0])[3]))

    if gainstage > read_stage:
        new_text_content += line
    elif read_stage == 7:
        text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
        if RXGain_sub6[band].get(path) is not None:
            New_String[2] = round(RXGain_sub6[band, path, f"STAGE{gainstage-1}(-50.00dBm) "])
        else:
            New_String[2] = 0

        New_String[3] = New_String[2] - RX_Gain_Spec
        New_String[4] = New_String[2] + RX_Gain_Spec
        text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
        text_area.see(tk.END)
        New_String = [str(v) for v in New_String]
        New_String = "\t".join(New_String) + "\n"
        new_string = line.replace(Old_String, New_String)
        new_text_content += new_string
    else:
        text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
        if RXGain_sub6[band].get(path) is not None:
            New_String[2] = round(RXGain_sub6[band, path, f"STAGE{gainstage}(-50.00dBm) "])
        else:
            New_String[2] = 0

        New_String[3] = New_String[2] - RX_Gain_Spec
        New_String[4] = New_String[2] + RX_Gain_Spec
        text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
        text_area.see(tk.END)
        New_String = [str(v) for v in New_String]
        New_String = "\t".join(New_String) + "\n"
        new_string = line.replace(Old_String, New_String)
        new_text_content += new_string

    return new_text_content


def Sub6_RX_RSRP_offset(new_text_content, line, band, path1, RXRSRP_sub6, RX_Gain_Spec, text_area):
    New_String = Old_String = line
    New_String = re.split("\t|\n", New_String)
    New_String = [v for v in New_String if v]
    gainstage = int(re.sub(r"[^0-9]", "", re.split("_", New_String[0])[3]))

    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
    if RXRSRP_sub6[band].get(path1) is not None:
        if gainstage == 0:
            New_String[2] = round(RXRSRP_sub6[band, path1, f"PRX(-50.00dBm) "])
        else:
            if RXRSRP_sub6[band, path1].get(f"DRX(-50.00dBm) ") is not None:
                New_String[2] = round(RXRSRP_sub6[band, path1, f"DRX(-50.00dBm) "])
            else:
                New_String[2] = 0
    else:
        New_String[2] = 0

    New_String[3] = New_String[2] - RX_Gain_Spec
    New_String[4] = New_String[2] + RX_Gain_Spec
    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"
    new_string = line.replace(Old_String, New_String)
    new_text_content += new_string

    return new_text_content


def Sub6_RX_FREQ_offset(new_text_content, line, band, path, RXComp_sub6, RX_Gain_Spec, text_area):
    New_String = Old_String = line
    New_String = re.split("\t|\n", New_String)
    New_String = [v for v in New_String if v]
    list_a = map(int, [v for v in re.sub(r"[^0-9]", "", New_String[0]) if v])
    list_b = ["MAIN", "4RX", "6RX", "8RX", "10RX"]
    ent = {i: k for i, k in enumerate(list_b)}
    ant = list(map(ent.get, list_a))[0]
    text_area.insert(tk.END, f"{New_String[0]:<30}| {New_String[3]:>5}\t{New_String[4]:>5}\t\t\u2192\t")
    if RXComp_sub6[band].get(ant) is not None:
        if RXComp_sub6[band, ant].get(path) is not None:
            New_String[2] = round(RXComp_sub6[band, ant, path])
        else:
            New_String[2] = 0
    else:
        New_String[2] = 0

    New_String[3] = New_String[2] - RX_Gain_Spec
    New_String[4] = New_String[2] + RX_Gain_Spec
    text_area.insert(tk.END, f"{New_String[3]:>5}\t{New_String[4]:>5}\n")
    text_area.see(tk.END)
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"
    new_string = line.replace(Old_String, New_String)
    new_text_content += new_string

    return new_text_content
