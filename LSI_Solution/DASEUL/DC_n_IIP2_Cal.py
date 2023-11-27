import pandas as pd
import LSI_Solution.Common.Function as func


def daseul_dc_iip2(df_Code, Save_data, text_area):
    df_DC_Cal = df_Code[df_Code["Test Conditions"].str.contains("_DC_").to_list()]

    df_3G_DC_Cal = df_DC_Cal[df_DC_Cal["Test Conditions"].str.contains("WCDMA_").to_list()]
    df_3G_DC_Cal_Value = df_3G_DC_Cal.iloc[:, 1:].astype(float)
    df_3G_DC_Cal_Item = df_3G_DC_Cal["Test Conditions"].str.split("WCDMA_|_", expand=True)
    # 의미없는 컬럼 삭제
    df_3G_DC_Cal_Item.drop(columns=[0, 3], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_3G_DC_Cal_Item.columns = ["Band", "Path", "Plane", "Number"]
    df_3G_DC_Cal = pd.merge(df_3G_DC_Cal_Item, df_3G_DC_Cal_Value, left_index=True, right_index=True)

    df_2G_DC_Cal = df_DC_Cal[df_DC_Cal["Test Conditions"].str.contains("GSM_").to_list()]
    df_2G_DC_Cal_Value = df_2G_DC_Cal.iloc[:, 1:].astype(float)
    df_2G_DC_Cal_Item = df_2G_DC_Cal["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_2G_DC_Cal_Item.drop(columns=[2], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_2G_DC_Cal_Item.columns = ["Band", "Path", "Plane", "Number"]
    df_2G_DC_Cal = pd.merge(df_2G_DC_Cal_Item, df_2G_DC_Cal_Value, left_index=True, right_index=True)

    df_NR_DC_Cal = df_DC_Cal[df_DC_Cal["Test Conditions"].str.contains("NR_").to_list()]
    df_NR_DC_Cal_Value = df_NR_DC_Cal.iloc[:, 1:].astype(float)
    df_NR_DC_Cal_Item = df_NR_DC_Cal["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_NR_DC_Cal_Item.drop(columns=[0, 3], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_NR_DC_Cal_Item.columns = ["Band", "Path", "Plane", "Number"]
    df_NR_DC_Cal = pd.merge(df_NR_DC_Cal_Item, df_NR_DC_Cal_Value, left_index=True, right_index=True)

    df_DC_Cal = pd.concat([df_3G_DC_Cal, df_2G_DC_Cal, df_NR_DC_Cal], ignore_index=True)
    df_DC_Cal_Mean = round(df_DC_Cal.groupby(["Band", "Path", "Plane", "Number"], sort=False).mean(), 1)
    df_DC_Cal_Mean = pd.concat([df_DC_Cal_Mean, round(df_DC_Cal_Mean.mean(axis=1)).rename("Average")], axis=1)
    df_DC_Cal_Mean = pd.concat([df_DC_Cal_Mean, round(df_DC_Cal_Mean.max(axis=1)).rename("Max")], axis=1)
    df_DC_Cal_Mean = pd.concat([df_DC_Cal_Mean, round(df_DC_Cal_Mean.min(axis=1)).rename("Min")], axis=1)

    df_IIP2_Cal = df_Code[df_Code["Test Conditions"].str.contains("_IIP2_").to_list()]
    df_IIP2_Cal_Value = df_IIP2_Cal.iloc[:, 1:].astype(float)
    df_IIP2_Cal_Item = df_IIP2_Cal["Test Conditions"].str.split("_", expand=True)
    # 의미없는 컬럼 삭제
    df_IIP2_Cal_Item.drop(columns=[0, 3], inplace=True)
    # groupby 실행을 위한 컬럼명 변경
    df_IIP2_Cal_Item.columns = ["Band", "Path", "Plane", "Number"]
    df_IIP2_Cal = pd.merge(df_IIP2_Cal_Item, df_IIP2_Cal_Value, left_index=True, right_index=True)
    df_IIP2_Cal_mean = round(df_IIP2_Cal.groupby(["Band", "Path", "Plane", "Number"], sort=False).mean(), 1)
    df_IIP2_Cal_mean = pd.concat([df_IIP2_Cal_mean, round(df_IIP2_Cal_mean.mean(axis=1)).rename("Average")], axis=1)
    df_IIP2_Cal_mean = pd.concat([df_IIP2_Cal_mean, round(df_IIP2_Cal_mean.max(axis=1)).rename("Max")], axis=1)
    df_IIP2_Cal_mean = pd.concat([df_IIP2_Cal_mean, round(df_IIP2_Cal_mean.min(axis=1)).rename("Min")], axis=1)

    if Save_data:
        filename = "Excel_DC_IIP2_Cal.xlsx"
        with pd.ExcelWriter(filename) as writer:
            df_DC_Cal_Mean.to_excel(writer, sheet_name="DC_Cal")
            df_IIP2_Cal_mean.to_excel(writer, sheet_name="IIP2_Cal")
        func.WB_Format(filename, 2, 5, 0, text_area)

    return df_DC_Cal_Mean, df_IIP2_Cal_mean, df_3G_DC_Cal, df_2G_DC_Cal, df_NR_DC_Cal
