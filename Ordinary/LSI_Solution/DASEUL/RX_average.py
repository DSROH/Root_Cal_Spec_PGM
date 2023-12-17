import pandas as pd
import LSI_Solution.Common.Function as func


def daseul_rx_average(df_Meas, Save_data, text_area):
    PRX_Gain_2G, Ripple_2G = daseul_2g_rx_average(df_Meas, Save_data, text_area)
    PRX_Gain_3G, PRX_Comp_3G = daseul_3G_rx_average(df_Meas, Save_data, text_area)
    RXGain_sub6, RXRSRP_sub6, RXComp_sub6 = daseul_sub6_rx_average(df_Meas, Save_data, text_area)

    return PRX_Gain_2G, Ripple_2G, PRX_Gain_3G, PRX_Comp_3G, RXGain_sub6, RXRSRP_sub6, RXComp_sub6


def daseul_2g_rx_average(df_Meas, Save_data, text_area):
    df_2g_gain = df_Meas[df_Meas["Test Conditions"].str.contains("CH_RxCalPower -60.00Bm").to_list()]
    df_2g_gain_Value = df_2g_gain.iloc[:, 1:].astype(float)
    df_2g_gain_Item = df_2g_gain["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_2g_gain_Item.drop(columns=[1, 2, 3, 4], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_2g_gain_Item.columns = ["Band"]
    df_2g_gain_Item = df_2g_gain_Item.replace({"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}})
    df_2g_gain = pd.merge(df_2g_gain_Item, df_2g_gain_Value, left_index=True, right_index=True)
    df_2g_gain_Mean = round(df_2g_gain.groupby(["Band"]).mean(), 1)
    df_2g_gain_Mean = pd.concat([df_2g_gain_Mean, round(df_2g_gain_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_2g_gain_Mean = pd.concat([df_2g_gain_Mean, round(df_2g_gain_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_2g_gain_Mean = pd.concat([df_2g_gain_Mean, round(df_2g_gain_Mean.min(axis=1), 1).rename("Min")], axis=1)

    df_2g_ripple = df_Meas[df_Meas["Test Conditions"].str.contains("_RX_Ripple").to_list()]
    df_2g_ripple_Value = df_2g_ripple.iloc[:, 1:].astype(float)
    df_2g_ripple_Item = df_2g_ripple["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_2g_ripple_Item.drop(columns=[1, 2, 3], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_2g_ripple_Item.columns = ["Band"]
    df_2g_ripple_Item = df_2g_ripple_Item.replace(
        {"Band": {"GSM850": "G085", "GSM900": "G09", "DCS1800": "G18", "PCS1900": "G19"}}
    )
    df_2g_ripple = pd.merge(df_2g_ripple_Item, df_2g_ripple_Value, left_index=True, right_index=True)
    df_2g_ripple_Mean = round(df_2g_ripple.groupby(["Band"]).mean(), 1)
    df_2g_ripple_Mean = pd.concat([df_2g_ripple_Mean, round(df_2g_ripple_Mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_2g_ripple_Mean = pd.concat([df_2g_ripple_Mean, round(df_2g_ripple_Mean.max(axis=1), 1).rename("Max")], axis=1)
    df_2g_ripple_Mean = pd.concat([df_2g_ripple_Mean, round(df_2g_ripple_Mean.min(axis=1), 1).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_RXCal_2G.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_2g_gain_Mean.to_excel(writer, sheet_name="2G_PRX_Gain_Mean")
            df_2g_ripple_Mean.to_excel(writer, sheet_name="2G_RX_Ripple_Mean")
        func.WB_Format(filename, 2, 2, 0, text_area)

    return df_2g_gain_Mean["Average"], df_2g_ripple_Mean["Average"]


def daseul_3G_rx_average(df_Meas, Save_data, text_area):
    df_PRX_Gain_3G = df_Meas[df_Meas["Test Conditions"].str.contains("_Main_PRX").to_list()]
    df_PRX_Gain_3G_Value = df_PRX_Gain_3G.iloc[:, 1:].astype(float)
    df_PRX_Gain_3G_Item = df_PRX_Gain_3G["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_PRX_Gain_3G_Item.drop(columns=[0, 2, 3, 4, 5], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_PRX_Gain_3G_Item.columns = ["Band"]
    df_PRX_Gain_3G = pd.merge(df_PRX_Gain_3G_Item, df_PRX_Gain_3G_Value, left_index=True, right_index=True)
    df_PRX_Gain_3G_mean = round(df_PRX_Gain_3G.groupby(["Band"]).mean(), 1)
    df_PRX_Gain_3G_mean = pd.concat([df_PRX_Gain_3G_mean, round(df_PRX_Gain_3G_mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_PRX_Gain_3G_mean = pd.concat([df_PRX_Gain_3G_mean, round(df_PRX_Gain_3G_mean.max(axis=1), 1).rename("Max")], axis=1)
    df_PRX_Gain_3G_mean = pd.concat([df_PRX_Gain_3G_mean, round(df_PRX_Gain_3G_mean.min(axis=1), 1).rename("Min")], axis=1)

    df_PRX_Comp_3G = df_Meas[df_Meas["Test Conditions"].str.contains("_MAIN_PRX_Comp").to_list()]
    df_PRX_Comp_3G_Value = df_PRX_Comp_3G.iloc[:, 1:].astype(float)
    df_PRX_Comp_3G_Item = df_PRX_Comp_3G["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_PRX_Comp_3G_Item.drop(columns=[0, 2, 4, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_PRX_Comp_3G_Item.columns = ["Band", "CH"]
    df_PRX_Comp_3G = pd.merge(df_PRX_Comp_3G_Item, df_PRX_Comp_3G_Value, left_index=True, right_index=True)
    df_PRX_Comp_3G_mean = round(df_PRX_Comp_3G.groupby(["Band", "CH"]).mean(), 1)
    # df_PRX_Comp_3G_data = round(df_PRX_Comp_3G.groupby(["Band", "CH"]).agg(["mean", "max", "min"]), 1)
    df_PRX_Comp_3G_mean = pd.concat([df_PRX_Comp_3G_mean, round(df_PRX_Comp_3G_mean.mean(axis=1), 1).rename("Average")], axis=1)
    df_PRX_Comp_3G_mean = pd.concat([df_PRX_Comp_3G_mean, round(df_PRX_Comp_3G_mean.max(axis=1), 1).rename("Max")], axis=1)
    df_PRX_Comp_3G_mean = pd.concat([df_PRX_Comp_3G_mean, round(df_PRX_Comp_3G_mean.min(axis=1), 1).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_RXCal_3G.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_PRX_Gain_3G_mean.to_excel(writer, sheet_name="3G_PRX_Gain_Mean")
            df_PRX_Comp_3G_mean.to_excel(writer, sheet_name="3G_PRX_Comp_Mean")
        func.WB_Format(filename, 2, 2, 0, text_area)

    return df_PRX_Gain_3G_mean["Average"], df_PRX_Comp_3G_mean["Average"]


def daseul_sub6_rx_average(df_Meas, Save_data, text_area):
    df_PRX_Gain_sub6 = df_Meas[df_Meas["Test Conditions"].str.contains("_MAIN_PRX_GAIN_STAGE").to_list()]
    df_PRX_Gain_sub6_Value = df_PRX_Gain_sub6.iloc[:, 1:].astype(float)
    df_PRX_Gain_sub6_Item = df_PRX_Gain_sub6["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_PRX_Gain_sub6_Item.drop(columns=[0, 2, 3, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_PRX_Gain_sub6_Item.columns = ["Band", "Path", "Stage"]
    df_PRX_Gain_sub6 = pd.merge(df_PRX_Gain_sub6_Item, df_PRX_Gain_sub6_Value, left_index=True, right_index=True)
    df_PRX_Gain_sub6_mean = round(df_PRX_Gain_sub6.groupby(["Band", "Path", "Stage"]).mean(), 1)
    # df_PRX_Gain_sub6_data = round(df_PRX_Gain_sub6.groupby(["Band", "Stage"]).agg(["mean", "max", "min"]), 1)
    df_PRX_Gain_sub6_mean = pd.concat(
        [df_PRX_Gain_sub6_mean, round(df_PRX_Gain_sub6_mean.mean(axis=1), 1).rename("Average")], axis=1
    )
    df_PRX_Gain_sub6_mean = pd.concat([df_PRX_Gain_sub6_mean, round(df_PRX_Gain_sub6_mean.max(axis=1), 1).rename("Max")], axis=1)
    df_PRX_Gain_sub6_mean = pd.concat([df_PRX_Gain_sub6_mean, round(df_PRX_Gain_sub6_mean.min(axis=1), 1).rename("Min")], axis=1)

    df_PRX_RSRP_sub6 = df_Meas[df_Meas["Test Conditions"].str.contains("_RSRP_OFFSET_MAIN_").to_list()]
    df_PRX_RSRP_sub6_Value = df_PRX_RSRP_sub6.iloc[:, 1:].astype(float)
    df_PRX_RSRP_sub6_Item = df_PRX_RSRP_sub6["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_PRX_RSRP_sub6_Item.drop(columns=[0, 2, 3, 4, 5], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_PRX_RSRP_sub6_Item.columns = ["Band", "Path1", "Path2"]
    df_PRX_RSRP_sub6 = pd.merge(df_PRX_RSRP_sub6_Item, df_PRX_RSRP_sub6_Value, left_index=True, right_index=True)
    df_PRX_RSRP_sub6_mean = round(df_PRX_RSRP_sub6.groupby(["Band", "Path1", "Path2"]).mean(), 1)
    # df_PRX_RSRP_sub6_data = round(df_PRX_RSRP_sub6.groupby(["Band"]).agg(["mean", "max", "min"]), 1)
    df_PRX_RSRP_sub6_mean = pd.concat(
        [df_PRX_RSRP_sub6_mean, round(df_PRX_RSRP_sub6_mean.mean(axis=1), 1).rename("Average")], axis=1
    )
    df_PRX_RSRP_sub6_mean = pd.concat([df_PRX_RSRP_sub6_mean, round(df_PRX_RSRP_sub6_mean.max(axis=1), 1).rename("Max")], axis=1)
    df_PRX_RSRP_sub6_mean = pd.concat([df_PRX_RSRP_sub6_mean, round(df_PRX_RSRP_sub6_mean.min(axis=1), 1).rename("Min")], axis=1)

    df_PRX_Comp_sub6_CA = df_Meas[df_Meas["Test Conditions"].str.contains("CH_Freq_CA")]
    df_Meas.drop(df_PRX_Comp_sub6_CA.index, inplace=True)
    df_PRX_Comp_sub6 = df_Meas[df_Meas["Test Conditions"].str.contains("CH_Freq_")]
    df_PRX_Comp_sub6.reset_index(drop=True, inplace=True)
    df_PRX_Comp_sub6_CA.reset_index(drop=True, inplace=True)

    df_PRX_Comp_sub6_Value = df_PRX_Comp_sub6.iloc[:, 1:].astype(float)
    df_PRX_Comp_sub6_Item = df_PRX_Comp_sub6["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_PRX_Comp_sub6_Item.drop(columns=[0, 2, 3, 4, 7], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_PRX_Comp_sub6_Item.columns = ["Band", "Ant", "path"]
    df_PRX_Comp_sub6 = pd.merge(df_PRX_Comp_sub6_Item, df_PRX_Comp_sub6_Value, left_index=True, right_index=True)
    df_PRX_Comp_sub6_mean = round(df_PRX_Comp_sub6.groupby(["Band", "Ant", "path"]).mean(), 1)
    # df_PRX_Comp_sub6_data = round(df_PRX_Comp_sub6.groupby(["Band", "Ant", "path"]).agg(["mean", "max", "min"]), 1)
    df_PRX_Comp_sub6_mean = pd.concat(
        [df_PRX_Comp_sub6_mean, round(df_PRX_Comp_sub6_mean.mean(axis=1), 1).rename("Average")], axis=1
    )
    df_PRX_Comp_sub6_mean = pd.concat([df_PRX_Comp_sub6_mean, round(df_PRX_Comp_sub6_mean.max(axis=1), 1).rename("Max")], axis=1)
    df_PRX_Comp_sub6_mean = pd.concat([df_PRX_Comp_sub6_mean, round(df_PRX_Comp_sub6_mean.min(axis=1), 1).rename("Min")], axis=1)

    if df_PRX_Comp_sub6_CA.empty:
        pass
    else:
        df_PRX_Comp_sub6_CA_Value = df_PRX_Comp_sub6_CA.iloc[:, 1:].astype(float)
        df_PRX_Comp_sub6_CA_Item = df_PRX_Comp_sub6_CA["Test Conditions"].str.split("_", expand=True)
        # 의미없는 컬럼 삭제
        df_PRX_Comp_sub6_CA_Item.drop(columns=[0, 2, 3, 4, 5, 9], inplace=True)
        # groupby 실행을 위한 컬럼명 변경
        df_PRX_Comp_sub6_CA_Item.columns = ["Band", "CA", "Ant", "path"]
        df_PRX_Comp_sub6_CA = pd.merge(df_PRX_Comp_sub6_CA_Item, df_PRX_Comp_sub6_CA_Value, left_index=True, right_index=True)
        df_PRX_Comp_sub6_CA_mean = round(df_PRX_Comp_sub6_CA.groupby(["Band", "CA", "Ant", "path"]).mean(), 1)
        # df_PRX_Comp_sub6_data = round(df_PRX_Comp_sub6.groupby(["Band","CA","Ant","path"]).agg(["mean", "max", "min"]), 1)
        df_PRX_Comp_sub6_CA_mean = pd.concat(
            [df_PRX_Comp_sub6_CA_mean, round(df_PRX_Comp_sub6_CA_mean.mean(axis=1), 1).rename("Average")], axis=1
        )
        df_PRX_Comp_sub6_CA_mean = pd.concat(
            [df_PRX_Comp_sub6_CA_mean, round(df_PRX_Comp_sub6_CA_mean.max(axis=1), 1).rename("Max")], axis=1
        )
        df_PRX_Comp_sub6_CA_mean = pd.concat(
            [df_PRX_Comp_sub6_CA_mean, round(df_PRX_Comp_sub6_CA_mean.min(axis=1), 1).rename("Min")], axis=1
        )

    df_Mixer_sub6 = df_Meas[df_Meas["Test Conditions"].str.contains("CH_Mixer").to_list()]
    df_Mixer_sub6_Value = df_Mixer_sub6.iloc[:, 1:].astype(float)
    df_Mixer_sub6_Item = df_Mixer_sub6["Test Conditions"].str.split("_| ", expand=True)
    # 의미없는 컬럼 삭제
    df_Mixer_sub6_Item.drop(columns=[0, 2, 4, 5, 6], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_Mixer_sub6_Item.columns = ["Band", "Mixer"]
    df_Mixer_sub6 = pd.merge(df_Mixer_sub6_Item, df_Mixer_sub6_Value, left_index=True, right_index=True)
    df_Mixer_sub6_mean = round(df_Mixer_sub6.groupby(["Band", "Mixer"], sort=False).mean(), 2)
    # df_PRX_Comp_sub6_data = round(df_PRX_Comp_sub6.groupby(["Band", "Mixer"]).agg(["mean", "max", "min"]), 1)
    df_Mixer_sub6_mean = pd.concat([df_Mixer_sub6_mean, round(df_Mixer_sub6_mean.mean(axis=1), 2).rename("Average")], axis=1)
    df_Mixer_sub6_mean = pd.concat([df_Mixer_sub6_mean, round(df_Mixer_sub6_mean.max(axis=1), 2).rename("Max")], axis=1)
    df_Mixer_sub6_mean = pd.concat([df_Mixer_sub6_mean, round(df_Mixer_sub6_mean.min(axis=1), 2).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_RXCal_Sub6.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_PRX_Gain_sub6_mean.to_excel(writer, sheet_name="Sub6_PRX_Gain_Mean")
            df_PRX_RSRP_sub6_mean.to_excel(writer, sheet_name="Sub6_PRX_RSRP_Mean")
            df_PRX_Comp_sub6_mean.to_excel(writer, sheet_name="Sub6_PRX_Comp_Mean")
            if df_PRX_Comp_sub6_CA.empty:
                pass
            else:
                df_PRX_Comp_sub6_CA_mean.to_excel(writer, sheet_name="Sub6_PRX_Comp_CA_Mean")
        func.WB_Format(filename, 2, 4, 0, text_area)

        filename = "Excel_RXMixer.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_Mixer_sub6_mean.to_excel(writer, sheet_name="Sub6_Mixer_Mean")
        func.WB_Format(filename, 2, 2, 0, text_area)

    return df_PRX_Gain_sub6_mean["Average"], df_PRX_RSRP_sub6_mean["Average"], df_PRX_Comp_sub6_mean["Average"]
