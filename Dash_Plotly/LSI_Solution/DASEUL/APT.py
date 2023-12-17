import re
import pandas as pd
import LSI_Solution.Common.Function as func


def chng_sub6_apt(Selected_spc, rat, band, APT_Spec_var, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min):
    APT_Spec = float(APT_Spec_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_APT_High_Gain_Index_"):
            New_String = Old_String = line
            New_String = sub6_apt(line, band, "High", APT_Spec, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_APT_Mid_Gain_Index_"):
            New_String = Old_String = line
            New_String = sub6_apt(line, band, "Mid", APT_Spec, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_APT_Low_Gain_Index_"):
            New_String = Old_String = line
            New_String = sub6_apt(line, band, "Low", APT_Spec, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_APT_High_Gain_Index_"):
            New_String = Old_String = line
            New_String = sub6_apt(line, band, "High", APT_Spec, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_APT_Mid_Gain_Index_"):
            New_String = Old_String = line
            New_String = sub6_apt(line, band, "Mid", APT_Spec, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX2_APT_Low_Gain_Index_"):
            New_String = Old_String = line
            New_String = sub6_apt(line, band, "Low", APT_Spec, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif Check & line.startswith("TX_APT_Cal_Diff"):
            New_String = Old_String = line
            New_String = sub6_apt_slim(line, APT_Spec)
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


def sub6_apt(line, band, Pa_stage, APT_Spec, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    if Word[0] == "TX":
        Path = "Tx"
    elif Word[0] == "TX2":
        Path = "Tx2"
    values = [
        APT_Meas_sub6_Ave[band, Path, Pa_stage, f"Index{Word[5]} "],
        APT_Meas_sub6_Max[band, Path, Pa_stage, f"Index{Word[5]} "],
        APT_Meas_sub6_Min[band, Path, Pa_stage, f"Index{Word[5]} "],
    ]
    if all(v == -10.0 for v in values):
        New_String[1] = -10
        New_String[2] = -10.1
        New_String[3] = -9.9
    else:
        New_String[1] = round(APT_Meas_sub6_Ave[band, Path, Pa_stage, f"Index{Word[5]} "])
        New_String[2] = New_String[1] - APT_Spec
        New_String[3] = New_String[1] + APT_Spec
    Word = "_".join(Word) + "\t" + "="
    New_String[0] = Word
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String


def sub6_apt_slim(line, APT_Spec):
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


def apt_average(df_Meas, Save_data, text_area):
    APT_Meas_3G_Ave = Apt_3g_meas_average(df_Meas, Save_data, text_area)
    APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min = Apt_sub6_meas_average(df_Meas, Save_data, text_area)

    return APT_Meas_3G_Ave, APT_Meas_sub6_Ave, APT_Meas_sub6_Max, APT_Meas_sub6_Min


def Apt_3g_meas_average(df_Meas, Save_data, text_area):
    df_APT_Meas_3G = df_Meas[df_Meas["Test Conditions"].str.contains("_APT_PA_").to_list()]
    df_APT_Meas_3G_Value = df_APT_Meas_3G.iloc[:, 1:].astype(float)
    df_APT_Meas_3G_Item = df_APT_Meas_3G["Test Conditions"].str.split("_|\\(|\\)", expand=True)
    # 의미없는 컬럼 삭제
    df_APT_Meas_3G_Item.drop(columns=[0, 2, 3, 4, 5, 7, 9, 10], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_APT_Meas_3G_Item.columns = ["Band", "PA Stage", "Index"]
    df_APT_Meas_3G = pd.merge(df_APT_Meas_3G_Item, df_APT_Meas_3G_Value, left_index=True, right_index=True)
    df_APT_Meas_3G_mean = round(df_APT_Meas_3G.groupby(["Band", "PA Stage", "Index"], sort=False).mean(), 2)
    df_APT_Meas_3G_mean = pd.concat([df_APT_Meas_3G_mean, round(df_APT_Meas_3G_mean.mean(axis=1), 2).rename("Average")], axis=1)
    df_APT_Meas_3G_mean = pd.concat([df_APT_Meas_3G_mean, round(df_APT_Meas_3G_mean.max(axis=1), 2).rename("Max")], axis=1)
    df_APT_Meas_3G_mean = pd.concat([df_APT_Meas_3G_mean, round(df_APT_Meas_3G_mean.min(axis=1), 2).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_APT_Meas_3G.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_APT_Meas_3G_mean.to_excel(writer, sheet_name="APT_Meas_3G_Mean")
        func.WB_Format(filename, 2, 4, 0, text_area)

    return df_APT_Meas_3G_mean["Average"]


def Apt_sub6_meas_average(df_Meas, Save_data, text_area):
    df_3G = df_Meas[df_Meas["Test Conditions"].str.contains("WCDMA")].index
    df_Meas.drop(df_3G, inplace=True)
    df_MCH = df_Meas[df_Meas["Test Conditions"].str.contains("_MCH_APT_")].index
    df_Meas.drop(df_MCH, inplace=True)
    df_APT_sub6 = df_Meas[df_Meas["Test Conditions"].str.contains("CH_APT_").to_list()]
    df_APT_sub6_Value = df_APT_sub6.iloc[:, 1:].astype(float)
    df_APT_sub6_Item = df_APT_sub6["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_APT_sub6_Item.drop(columns=[0, 3, 4, 5, 7], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_APT_sub6_Item.columns = ["Band", "Path", "PA Stage", "Index"]
    df_APT_sub6 = pd.merge(df_APT_sub6_Item, df_APT_sub6_Value, left_index=True, right_index=True)
    df_APT_sub6_Mean = round(df_APT_sub6.groupby(["Band", "Path", "PA Stage", "Index"], sort=False).mean(), 2)

    df_APT_sub6_Mean = pd.concat([df_APT_sub6_Mean, round(df_APT_sub6_Mean.mean(axis=1), 2).rename("Average")], axis=1)
    df_APT_sub6_Mean = pd.concat([df_APT_sub6_Mean, round(df_APT_sub6_Mean.max(axis=1), 2).rename("Max")], axis=1)
    df_APT_sub6_Mean = pd.concat([df_APT_sub6_Mean, round(df_APT_sub6_Mean.min(axis=1), 2).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_APT_Meas_Sub6.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_APT_sub6_Mean.to_excel(writer, sheet_name="APT_Meas_Sub6_Mean")
        func.WB_Format(filename, 2, 4, 0, text_area)

    return df_APT_sub6_Mean["Average"], df_APT_sub6_Mean["Max"], df_APT_sub6_Mean["Min"]


def chng_3g_apt(Selected_spc, rat, band, APT_Spec_var, APT_Meas_3G_Ave):
    APT_Spec = float(APT_Spec_var.get())  # 1dB = 100
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
        elif Check & line.startswith("TX_APT_PA_"):
            New_String = Old_String = line
            New_String = apt_3g(line, band, APT_Spec, APT_Meas_3G_Ave)
            new_string = line.replace(Old_String, New_String)
            new_text_content += new_string
        elif line.startswith("TxP_Channel_Comp_PA_MID_"):
            new_text_content += line
            Check = False
        else:
            new_text_content += line

    with open(Selected_spc, "w", encoding="utf-8") as f:
        f.writelines(new_text_content)
    f.close()


def apt_3g(line, band, APT_Spec, APT_Meas_NR_Ave):
    New_String = re.split("=|\t|\n", line)
    New_String = [v for v in New_String if v]
    Word = re.split("_", New_String[0])
    Word = [v for v in Word if v]
    Pa_stage = Word[3]
    Read_index = int(Word[5])
    Index_count = APT_Meas_NR_Ave.loc[(band, Pa_stage)].count()
    if Read_index < Index_count:
        New_String[1] = round(APT_Meas_NR_Ave[band, Pa_stage].iloc[Read_index])
        New_String[2] = round(APT_Meas_NR_Ave[band, Pa_stage].iloc[Read_index]) - APT_Spec
        New_String[3] = round(APT_Meas_NR_Ave[band, Pa_stage].iloc[Read_index]) + APT_Spec
    else:
        New_String[1] = -10
        New_String[2] = New_String[1] - 0.1
        New_String[3] = New_String[1] + 0.1
    Word = "_".join(Word) + "\t" + "="
    New_String[0] = Word
    New_String = [str(v) for v in New_String]
    New_String = "\t".join(New_String) + "\n"

    return New_String
