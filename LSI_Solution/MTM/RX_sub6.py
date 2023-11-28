import re
import tkinter as tk


def chng_sub6_rx_gain_default(flag, Selected_spc, rat, band, dict_option, rxgainstage, Sub6_RX_Gain_default, text_area):
    if flag == "daseul":
        target_word = f"[{rat}_n{band}_CAL_PARAM]"
        with open(Selected_spc, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()
    else:
        target_word = f"[{rat}_CAL_PARAM_BAND{band}]"
        with open(Selected_spc, "r", encoding="latin_1") as file:
            data_lines = file.readlines()
        file.close()

    band = f"n{band}"
    text_area.insert(tk.END, "\n")
    text_area.insert(tk.END, f"{target_word}\n")
    text_area.insert(tk.END, "-" * 100)
    text_area.insert(tk.END, "\n")
    text_area.see(tk.END)

    new_text_content = ""
    Check = False

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(target_word):
            new_text_content += line
            Check = True
        # Gainstate를 for로 할 경우 너무 많은 반복 -> if 문으로 처리
        elif Check & line.startswith(f"PRX_RxGAIN_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rxgain_cal(
                line, band, path[2], path[0], dict_option[band]["GDeP"], rxgainstage, Sub6_RX_Gain_default, text_area
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"DRX_RxGAIN_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rxgain_cal(
                line, band, path[2], path[0], dict_option[band]["GDeD"], rxgainstage, Sub6_RX_Gain_default, text_area
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & (line.startswith("// TX Cal Parameters")):
            new_text_content += line
            Check = False
        else:
            new_text_content += line
    text_area.see(tk.END)
    # text_area.insert(tk.END, f"Tech= {rat}  \t| Band= {band:<7}\t| Ant= {Antenna}\t| Path= {Path}\n")
    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_rxgain_cal(line, band, ant, path, dict_option, rxgainstage, Sub6_RX_Gain_default, text_area):
    check = False
    if (ant == "MAIN") & (path == "PRX" or path == "DRX"):
        check = dict_option[10]
    elif (ant == "4RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[9]
    elif (ant == "6RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[8]
    elif (ant == "8RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[7]
    elif (ant == "10RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[6]
    elif (ant == "12RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[5]
    elif (ant == "14RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[4]
    elif (ant == "16RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[3]
    elif (ant == "CA1") & (path == "PRX" or path == "DRX"):
        check = dict_option[2]
    elif (ant == "CA2") & (path == "PRX" or path == "DRX"):
        check = dict_option[1]
    elif (ant == "CA3") & (path == "PRX" or path == "DRX"):
        check = dict_option[0]

    if check:
        New_String = re.split("[_=,\n]", line)
        New_String = [v for v in New_String if v]
        if ant == "CA1" or ant == "CA2" or ant == "CA3":
            ca = ant
            ant = "MAIN"
            text_area.insert(tk.END, f"{ca:<4} {path} GAIN  |   ")
        else:
            ca = "NonCA"
            text_area.insert(tk.END, f"{ant:<4} {path} GAIN  |   ")

        for i in range(rxgainstage):
            if i == (rxgainstage - 1):
                try:
                    text_area.insert(tk.END, f"{New_String[5+i]:>5}\n")
                except:
                    New_String.append(0)
                    text_area.insert(tk.END, f"{New_String[5+i]:>5}\n")
            else:
                try:
                    text_area.insert(tk.END, f"{New_String[5+i]:>5}, ")
                except:
                    New_String.append(0)
                    text_area.insert(tk.END, f"{New_String[5+i]:>5}, ")

        for i in range(rxgainstage):
            New_String[5 + i] = round(Sub6_RX_Gain_default[band][ant][path][f"Stage{i}"] * 100)

        text_area.insert(tk.END, f"               | \u2192 ")

        for i in range(rxgainstage):
            if i == (rxgainstage - 1):
                text_area.insert(tk.END, f"{New_String[5+i]:>5}\n\n")
            else:
                text_area.insert(tk.END, f"{New_String[5+i]:>5}, ")

        text_area.see(tk.END)
    else:
        New_String = re.split("[_=,\n]", line)
        New_String = [v for v in New_String if v]
        del New_String[5:]

        for i in range(rxgainstage):
            New_String.append(0)

    New_String1 = "_".join(map(str, New_String[:5]))
    New_String2 = ",".join(map(str, New_String[5:]))
    New_String = New_String1 + "=" + New_String2 + "\n"

    return New_String


def chng_sub6_rsrp_offset_default(flag, Selected_spc, rat, band, dict_option, Sub6_RSRP_Offset_default, text_area):
    if flag == "daseul":
        target_word = f"[{rat}_n{band}_CAL_PARAM]"
        with open(Selected_spc, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()
    else:
        target_word = f"[{rat}_CAL_PARAM_BAND{band}]"
        with open(Selected_spc, "r", encoding="latin_1") as file:
            data_lines = file.readlines()
        file.close()
    band = f"n{band}"
    new_text_content = ""
    Check = False

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(target_word):
            new_text_content += line
            Check = True
        # Gainstate를 for로 할 경우 너무 많은 반복 -> if 문으로 처리
        elif Check & line.startswith(f"PRX_RSRP_Offset_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rsrp_offset(
                index, line, rat, band, path[3], path[0], dict_option[band]["GDeP"], Sub6_RSRP_Offset_default, text_area
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"DRX_RSRP_Offset_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rsrp_offset(
                index, line, rat, band, path[3], path[0], dict_option[band]["GDeD"], Sub6_RSRP_Offset_default, text_area
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & (line.startswith("// TX Cal Parameters")):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_rsrp_offset(index, line, rat, band, ant, path, dict_option, Sub6_RSRP_Offset_default, text_area):
    check = False
    if (ant == "MAIN") & (path == "PRX" or path == "DRX"):
        check = dict_option[10]
    elif (ant == "4RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[9]
    elif (ant == "6RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[8]
    elif (ant == "8RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[7]
    elif (ant == "10RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[6]
    elif (ant == "12RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[5]
    elif (ant == "14RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[4]
    elif (ant == "16RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[3]
    elif (ant == "CA1") & (path == "PRX" or path == "DRX"):
        check = dict_option[2]
    elif (ant == "CA2") & (path == "PRX" or path == "DRX"):
        check = dict_option[1]
    elif (ant == "CA3") & (path == "PRX" or path == "DRX"):
        check = dict_option[0]

    New_String = re.split("[_=,\n]", line)
    New_String = [v for v in New_String if v]
    if check:
        if ant == "CA1" or ant == "CA2" or ant == "CA3":
            ca = ant
            ant = "MAIN"
            text_area.insert(tk.END, f"{ca:<4} {path} RSRP  |   ")
        else:
            ca = "NonCA"
            text_area.insert(tk.END, f"{ant:<4} {path} RSRP  |   ")

        text_area.insert(tk.END, f"{New_String[6]:>5}\n")
        New_String[6] = round(Sub6_RSRP_Offset_default[band][ant][path] * 100)
        text_area.insert(tk.END, f"               | \u2192 {New_String[6]:>5}\n\n")
        text_area.see(tk.END)
    else:
        New_String[6] = 0

    New_String1 = "_".join(map(str, New_String[:6]))
    New_String2 = ",".join(map(str, New_String[6:]))
    New_String = New_String1 + "=" + New_String2 + "\n"

    return New_String


def chng_sub6_rx_freq_default(
    flag,
    Selected_spc,
    rat,
    band,
    dict_option,
    Sub6_RX_Freq_default,
    Bluetick,
    blue_nrrx_freq,
    blue_nrdrx_offset,
    text_area,
):
    if flag == "daseul":
        target_word = f"[{rat}_n{band}_CAL_PARAM]"
        with open(Selected_spc, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()
    else:
        target_word = f"[{rat}_CAL_PARAM_BAND{band}]"
        with open(Selected_spc, "r", encoding="latin_1") as file:
            data_lines = file.readlines()
        file.close()

    band = f"n{band}"
    new_text_content = ""
    Check = False

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(target_word):
            new_text_content += line
            Check = True
        elif Check & line.startswith(f"PRX_RXFREQ_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rxfreq_cal(
                dict_option[band]["Freq"],
                index,
                line,
                rat,
                band,
                path[2],
                path[0],
                dict_option[band]["FreP"],
                Sub6_RX_Freq_default,
                Bluetick,
                blue_nrrx_freq,
                blue_nrdrx_offset,
                text_area,
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"DRX_RXFREQ_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rxfreq_cal(
                dict_option[band]["Freq"],
                index,
                line,
                rat,
                band,
                path[2],
                path[0],
                dict_option[band]["FreD"],
                Sub6_RX_Freq_default,
                Bluetick,
                blue_nrrx_freq,
                blue_nrdrx_offset,
                text_area,
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"// TX Cal Parameters"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_rxfreq_cal(
    Freq_List,
    index,
    line,
    rat,
    band,
    ant,
    path,
    dict_option,
    Sub6_RX_Freq_default,
    Bluetick,
    blue_nrrx_freq,
    blue_nrdrx_offset,
    text_area,
):
    check = False
    if (ant == "MAIN") & (path == "PRX" or path == "DRX"):
        check = dict_option[10]
    elif (ant == "4RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[9]
    elif (ant == "6RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[8]
    elif (ant == "8RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[7]
    elif (ant == "10RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[6]
    elif (ant == "12RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[5]
    elif (ant == "14RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[4]
    elif (ant == "16RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[3]
    elif (ant == "CA1") & (path == "PRX" or path == "DRX"):
        check = dict_option[2]
    elif (ant == "CA2") & (path == "PRX" or path == "DRX"):
        check = dict_option[1]
    elif (ant == "CA3") & (path == "PRX" or path == "DRX"):
        check = dict_option[0]

    if check:
        New_String = re.split("[_=,\n]", line)
        New_String = [v for v in New_String if v]
        if ant == "CA1" or ant == "CA2" or ant == "CA3":
            ca = ant
            ant = "MAIN"
            text_area.insert(tk.END, f"{ca:<4} {path} FREQ  |   ")
        else:
            ca = "NonCA"
            text_area.insert(tk.END, f"{ant:<4} {path} FREQ  |   ")

        for i in range(len(New_String[4:])):
            if i == range(len(New_String[4:]))[-1]:
                text_area.insert(tk.END, f"{New_String[4+i]:>5}\n")
            else:
                text_area.insert(tk.END, f"{New_String[4+i]:>5}, ")
        text_area.insert(tk.END, f"               | \u2192 ")
        # New_String의 Freq list를 모두 지우고, Freq_List 길이만큼 0 으로 채워넣기 후 값을 변경
        del New_String[4:]

        for i in range(len(Freq_List)):
            New_String.append(0)
            try:
                value = Sub6_RX_Freq_default[band][ca][ant][path][Freq_List[i]]
                if Bluetick & (band == "n28") & (path == "DRX"):
                    if int(Freq_List[i]) == blue_nrrx_freq:
                        New_String[4 + i] = round(value * 100) + (blue_nrdrx_offset * 100)
                    elif int(Freq_List[i]) in [blue_nrrx_freq - 1000, blue_nrrx_freq + 1000]:
                        New_String[4 + i] = round(value * 100) + 100
                    else:
                        New_String[4 + i] = round(value * 100)
                else:
                    New_String[4 + i] = round(value * 100)
            except:
                pass

        for i in range(len(Freq_List)):
            if i == range(len(Freq_List))[-1]:
                text_area.insert(tk.END, f"{New_String[4+i]:>5}\n\n")
            else:
                text_area.insert(tk.END, f"{New_String[4+i]:>5}, ")
        text_area.see(tk.END)

    else:
        New_String = re.split("[_=,\n]", line)
        New_String = [v for v in New_String if v]
        del New_String[4:]

        for i in range(len(Freq_List)):
            New_String.append(0)

    New_String1 = "_".join(map(str, New_String[:4]))
    New_String2 = ",".join(map(str, New_String[4:]))
    New_String = New_String1 + "=" + New_String2 + "\n"

    return New_String


def chng_sub6_rx_mixer_default(flag, Selected_spc, rat, band, dict_option, Sub6_RX_Mixer_default, text_area):
    if flag == "daseul":
        target_word = f"[{rat}_n{band}_CAL_PARAM]"
        with open(Selected_spc, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()
    else:
        target_word = f"[{rat}_CAL_PARAM_BAND{band}]"
        with open(Selected_spc, "r", encoding="latin_1") as file:
            data_lines = file.readlines()
        file.close()
    band = f"n{band}"
    new_text_content = ""
    Check = False

    # band별 Mixer 갯수 구하기
    # Mixer = Sub6_RX_Mixer_default.reset_index().groupby("Band")['Mixer'].nunique().loc[band]
    Mixer_list = Sub6_RX_Mixer_default[band].index.get_level_values("Mixer").tolist()
    Mixer = list(dict.fromkeys(Mixer_list))  # list 중복 제거

    for index, line in enumerate(data_lines):
        New_String = Old_String = line
        if line.startswith(target_word):
            new_text_content += line
            Check = True
        elif Check & line.startswith(f"PRX_MIXER_RSRP_Offset_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rx_mixer_cal(
                index, line, rat, band, Mixer, path[4], path[0], dict_option[band]["MixP"], Sub6_RX_Mixer_default, text_area
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif Check & line.startswith(f"DRX_MIXER_RSRP_Offset_"):
            path = re.split("_|=|,|\n", line)
            New_String = sub6_rx_mixer_cal(
                index, line, rat, band, Mixer, path[4], path[0], dict_option[band]["MixD"], Sub6_RX_Mixer_default, text_area
            )
            Change_Str = line.replace(Old_String, New_String)
            new_text_content += Change_Str
        elif line.startswith(f"// TX Cal Parameters"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def sub6_rx_mixer_cal(index, line, rat, band, Mixer, ant, path, dict_option, Sub6_RX_Mixer_default, text_area):
    check = False
    if (ant == "MAIN") & (path == "PRX" or path == "DRX"):
        check = dict_option[10]
    elif (ant == "4RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[9]
    elif (ant == "6RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[8]
    elif (ant == "8RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[7]
    elif (ant == "10RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[6]
    elif (ant == "12RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[5]
    elif (ant == "14RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[4]
    elif (ant == "16RX") & (path == "PRX" or path == "DRX"):
        check = dict_option[3]
    elif (ant == "CA1") & (path == "PRX" or path == "DRX"):
        check = dict_option[2]
    elif (ant == "CA2") & (path == "PRX" or path == "DRX"):
        check = dict_option[1]
    elif (ant == "CA3") & (path == "PRX" or path == "DRX"):
        check = dict_option[0]

    New_String = re.split("[_=,\n]", line)
    New_String = [v for v in New_String if v]
    if check:
        Mixer_no = []
        Old_Mixer_no = New_String[7::2]
        Old_Value = New_String[8::2]

        if ant == "CA1" or ant == "CA2" or ant == "CA3":
            ca = ant
            ant = "MAIN"
            text_area.insert(tk.END, f"{ca:<4} {path} MIXER |   ")
            if ant == "MAIN":
                for i in Mixer:
                    if len(i) == 2:
                        Mixer_no.append(i)
            elif ant == "4RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 1.0):
                        Mixer_no.append(i)
            elif ant == "6RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 2.0):
                        Mixer_no.append(i)
            elif ant == "8RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 3.0):
                        Mixer_no.append(i)
            elif ant == "10RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 4.0):
                        Mixer_no.append(i)
            elif ant == "12RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 5.0):
                        Mixer_no.append(i)
            elif ant == "14RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 6.0):
                        Mixer_no.append(i)
            elif ant == "16RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 7.0):
                        Mixer_no.append(i)
        else:
            ca = "NonCA"
            text_area.insert(tk.END, f"{ant:<4} {path} MIXER |   ")
            if ant == "MAIN":
                for i in Mixer:
                    if len(i) == 2:
                        Mixer_no.append(i)
            elif ant == "4RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 1.0):
                        Mixer_no.append(i)
            elif ant == "6RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 2.0):
                        Mixer_no.append(i)
            elif ant == "8RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 3.0):
                        Mixer_no.append(i)
            elif ant == "10RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 4.0):
                        Mixer_no.append(i)
            elif ant == "12RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 5.0):
                        Mixer_no.append(i)
            elif ant == "14RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 6.0):
                        Mixer_no.append(i)
            elif ant == "16RX":
                for i in Mixer:
                    if (len(i) == 3) & (int(i) // 100 == 7.0):
                        Mixer_no.append(i)
        count = 0
        # spc 파일의 default cal mixer 갯수와 실제 캘된 mixer 갯수가 다를 수 있기 때문에 mixer 데이터를 삭제하고
        del New_String[7:]
        # Main ant의 mixer 넘버를 Mixer_no에 저장하고
        # Mixer_no의 길이만큼 0 으로 채워넣기 한다.
        for i in range(len(Mixer_no)):
            New_String.append(0)
            New_String.append(0)

        New_Mixer_no = New_String[7::2]
        New_Value = New_String[8::2]

        for i in Mixer_no:
            if count >= (len(Old_Mixer_no) - 1):
                Old_Mixer_no.append(0)
                Old_Value.append(0)
            text_area.insert(tk.END, f"{Old_Mixer_no[count]:>3}  {Old_Value[count]:>4}\n")
            text_area.insert(tk.END, f"               | \u2192 ")
            New_Mixer_no[count] = str(i)
            New_Value[count] = str(round(Sub6_RX_Mixer_default[band, i, path] * 100))
            text_area.insert(tk.END, f"{New_Mixer_no[count]:>3}  {New_Value[count]:>4}\n")
            if i == Mixer_no[-1]:
                pass
            else:
                text_area.insert(tk.END, f"               |   ")
            count += 1
        text_area.insert(tk.END, f"\n")
        text_area.see(tk.END)
        New_String[7::2] = New_Mixer_no
        New_String[8::2] = New_Value

    else:
        del New_String[7:]
        New_String.append(0)

    New_String1 = "_".join(map(str, New_String[:7]))
    New_String2 = ",".join(map(str, New_String[7:]))
    New_String = New_String1 + "=" + New_String2 + "\n"

    return New_String
