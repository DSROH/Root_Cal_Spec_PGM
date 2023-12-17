import re
import tkinter as tk
import numpy as np


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
