import re

def Read_sub6_default_cal_option(flag, Selected_spc, rat, band, dict_option, text_area):
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

    Check = False
    Check_4rx = False
    Check_6rx = False
    Check_8rx = False
    Check_10rx = False
    Check_12rx = False
    Check_14rx = False
    Check_16rx = False
    Check_Freq = False
    Check_Freq_ca1 = False
    Check_Freq_ca2 = False
    Check_Freq_ca3 = False
    Check_mixer = False

    Rxpath_bit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Mixer_bit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Band_number = "n" + str(band)

    dict_option = {
        Band_number: {
            # CA3, CA2, CA1, 16RX_EN, 14RX_EN, 12RX_EN, 10RX_EN, 8RX_EN, 6RX_EN, 4RX_EN, Main
            "GDeP": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "GDeD": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "FreP": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "FreD": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "MixP": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "MixD": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "Freq": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        }
    }

    with open(Selected_spc, "r", encoding="utf-8") as file:
        data_lines = file.readlines()
    file.close()

    for index, line in enumerate(data_lines):
        if line.startswith(target_word):
            Check = True
        # ? RX Gain cal default option
        elif Check & line.startswith("Rx_4RX_CAL_EN=1"):
            Check_4rx = True
        elif Check & line.startswith("Rx_6RX_CAL_EN=1"):
            Check_6rx = True
        elif Check & line.startswith("Rx_8RX_CAL_EN=1"):
            Check_8rx = True
        elif Check & line.startswith("Rx_10RX_CAL_EN=1"):
            Check_10rx = True
        elif Check & line.startswith("Rx_12RX_CAL_EN=1"):
            Check_12rx = True
        elif Check & line.startswith("Rx_14RX_CAL_EN=1"):
            Check_14rx = True
        elif Check & line.startswith("Rx_16RX_CAL_EN=1"):
            Check_16rx = True
        elif Check & line.startswith("Use_PRX_MAIN_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][10] = 1
        elif Check & line.startswith("Use_DRX_MAIN_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][10] = 1
        elif (Check & Check_4rx) & line.startswith("Use_PRX_4RX_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][9] = 1
        elif (Check & Check_4rx) & line.startswith("Use_DRX_4RX_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][9] = 1
        elif (Check & Check_6rx) & line.startswith("Use_PRX_6RX_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][8] = 1
        elif (Check & Check_6rx) & line.startswith("Use_DRX_6RX_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][8] = 1
        elif (Check & Check_8rx) & line.startswith("Use_PRX_8RX_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][7] = 1
        elif (Check & Check_8rx) & line.startswith("Use_DRX_8RX_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][7] = 1
        elif (Check & Check_10rx) & line.startswith("Use_PRX_10RX_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][6] = 1
        elif (Check & Check_10rx) & line.startswith("Use_DRX_10RX_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][6] = 1
        elif (Check & Check_12rx) & line.startswith("Use_PRX_12RX_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][5] = 1
        elif (Check & Check_12rx) & line.startswith("Use_DRX_12RX_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][5] = 1
        elif (Check & Check_14rx) & line.startswith("Use_PRX_14RX_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][4] = 1
        elif (Check & Check_14rx) & line.startswith("Use_DRX_14RX_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][4] = 1
        elif (Check & Check_16rx) & line.startswith("Use_PRX_16RX_DEFAULT=1"):
            dict_option[Band_number]["GDeP"][3] = 1
        elif (Check & Check_16rx) & line.startswith("Use_DRX_16RX_DEFAULT=1"):
            dict_option[Band_number]["GDeD"][3] = 1

        # ? Freq. cal default option
        elif Check & line.startswith("RX_FREQ_CAL_EN=1"):
            Check_Freq = True
        elif (Check & Check_Freq) & line.startswith("RX_FREQv2_MAIN_EN"):
            bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            Rxpath_bit = [*f"{bit:0>8}"]
        elif (Check & Check_Freq) & line.startswith("RX_FREQv2_CA1_EN"):
            Freq_ca1_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            if Freq_ca1_bit == "1":
                Check_Freq_ca1 = True
        elif (Check & Check_Freq) & line.startswith("RX_FREQv2_CA2_EN"):
            Freq_ca2_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            if Freq_ca2_bit == "1":
                Check_Freq_ca2 = True
        elif (Check & Check_Freq) & line.startswith("RX_FREQv2_CA3_EN"):
            Freq_ca3_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            if Freq_ca3_bit == "1":
                Check_Freq_ca3 = True
        elif (Check & Check_Freq) & ((Rxpath_bit[7] == "1") & line.startswith("RX_FREQv2_MAIN_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][10] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][10] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & ((Rxpath_bit[6] == "1") & line.startswith("RX_FREQv2_4RX_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][9] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][9] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & ((Rxpath_bit[5] == "1") & line.startswith("RX_FREQv2_6RX_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][8] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][8] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & ((Rxpath_bit[4] == "1") & line.startswith("RX_FREQv2_8RX_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][7] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][7] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & ((Rxpath_bit[3] == "1") & line.startswith("RX_FREQv2_10RX_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][6] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][6] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & ((Rxpath_bit[2] == "1") & line.startswith("RX_FREQv2_12RX_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][5] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][5] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & ((Rxpath_bit[1] == "1") & line.startswith("RX_FREQv2_14RX_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][4] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][4] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & ((Rxpath_bit[0] == "1") & line.startswith("RX_FREQv2_16RX_USE_DEFAULT")):
            f_bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][3] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][3] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & (Check_Freq_ca1 & line.startswith("RX_FREQv2_CA1_USE_DEFAULT")):
            freqca = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{freqca:0>2}"]
            dict_option[Band_number]["FreP"][2] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][2] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & (Check_Freq_ca2 & line.startswith("RX_FREQv2_CA2_USE_DEFAULT")):
            freqca = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][1] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][1] = int(freqbit[0])  # DRX
        elif (Check & Check_Freq) & (Check_Freq_ca3 & line.startswith("RX_FREQv2_CA3_USE_DEFAULT")):
            freqca = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            freqbit = [*f"{f_bit:0>2}"]
            dict_option[Band_number]["FreP"][0] = int(freqbit[1])  # PRX
            dict_option[Band_number]["FreD"][0] = int(freqbit[0])  # DRX

        elif Check & line.startswith("RX_CAL_FREQ"):
            result = re.split("[\t|//]", line)  # Tab, // 분리
            Freq_List = re.split("[=,\n]", result[0])[1:]
            Freq_List = [v for v in Freq_List if v]
            dict_option[Band_number]["Freq"] = [v for v in Freq_List if v]

        # ? Mixer Cal default option
        elif Check & line.startswith("RX_Mixer_Cal_mode"):
            bit = bin(int(re.split("[=,//,\n]", line)[1]))[2:]
            Mixer_bit = [*f"{bit:0>8}"]
            Check_mixer = True
        elif (Check & Check_mixer) & ((Mixer_bit[7] == "1") & line.startswith("Use_PRX_MAIN_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][10] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[7] == "1") & line.startswith("Use_DRX_MAIN_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][10] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[6] == "1") & line.startswith("Use_PRX_4RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][9] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[6] == "1") & line.startswith("Use_DRX_4RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][9] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[5] == "1") & line.startswith("Use_PRX_6RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][8] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[5] == "1") & line.startswith("Use_DRX_6RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][8] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[4] == "1") & line.startswith("Use_PRX_8RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][7] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[4] == "1") & line.startswith("Use_DRX_8RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][7] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[3] == "1") & line.startswith("Use_PRX_10RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][6] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[3] == "1") & line.startswith("Use_DRX_10RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][6] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[2] == "1") & line.startswith("Use_PRX_12RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][5] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[2] == "1") & line.startswith("Use_DRX_12RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][5] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[1] == "1") & line.startswith("Use_PRX_14RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][4] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[1] == "1") & line.startswith("Use_DRX_14RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][4] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[0] == "1") & line.startswith("Use_PRX_16RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixP"][3] = 1
        elif (Check & Check_mixer) & ((Mixer_bit[0] == "1") & line.startswith("Use_DRX_16RX_Offset_DEFAULT=1")):
            dict_option[Band_number]["MixD"][3] = 1
        elif Check & line.startswith("// TX Cal Parameters"):
            break

    return dict_option
