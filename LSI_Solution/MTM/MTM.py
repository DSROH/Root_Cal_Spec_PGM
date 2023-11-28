import os
import re
import tkinter as tk
import LSI_Solution.Common.Function as func
import LSI_Solution.Common.get_data as Lget
import LSI_Solution.MTM.RX_sub6 as Lsub6rx
import LSI_Solution.MTM.RX_3g as L3grx
import LSI_Solution.MTM.MTM_function as Lmtmfunc
import LSI_Solution.MTM.Sub6_default_cal_option as Caloption


def mtm(
    list_file,
    Selected_spc,
    mtm_folder,
    Select_op,
    debug_var,
    get_data_var,
    daseul_select,
    mtm_select,
    Save_data_var,
    Bluetick,
    Blue_3g_ch,
    Blue_3g_offs,
    Blue_nr_ch,
    Blue_nr_offs,
    text_area,
):
    if mtm_select:
        mtm_folder = mtm_folder.get()
        files = os.listdir(mtm_folder)
        for file in files:
            if file == "hspa_calibration_param.txt":
                mtm_3g_param = os.path.join(mtm_folder, file)
            elif file == "sub6_calibration_paramV2.txt":
                mtm_nr_param = os.path.join(mtm_folder, file)
            else:
                pass

    df_Meas = Lget.get_data(list_file, Select_op, Save_data_var, debug_var, Save_data_var, get_data_var, text_area)

    Test_List = Lmtmfunc.get_mtm_bandlist(list_file.get(0, tk.END))
    blue_3grx_freq = int(Blue_3g_ch.get())
    blue_3gdrx_offset = int(Blue_3g_offs.get())

    blue_nrrx_freq, blue_nrtx_freq = func.LTE_channel_converter(28, int(Blue_nr_ch.get()))
    blue_nrdrx_offset = int(Blue_nr_offs.get())

    daseul_dict_option = {}
    mtm_dict_option = {}

    if daseul_select.get():
        with open(Selected_spc, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()

        for line in data_lines:
            if line.startswith("Num_RxGain_Stage="):
                Daseul_rxgainstage = int(re.split("[=,//,\n]", line)[1])
                break

        for rat in Test_List:
            for band in Test_List[rat]:
                if rat == "SUB6":
                    daseul_dict_option.update(
                        Caloption.Read_sub6_default_cal_option("daseul", Selected_spc, rat, band, daseul_dict_option, text_area)
                    )

    if mtm_select.get():
        with open(mtm_nr_param, "r", encoding="utf-8") as file:
            data_lines = file.readlines()
        file.close()

        for line in data_lines:
            if line.startswith("Num_RxGain_Stage="):
                Mtm_rxgainstage = int(re.split("[=,//,\n]", line)[1])
                break

        for rat in Test_List:
            for band in Test_List[rat]:
                if rat == "SUB6":
                    mtm_dict_option.update(
                        Caloption.Read_sub6_default_cal_option("mtm", mtm_nr_param, rat, band, mtm_dict_option, text_area)
                    )

    for rat in Test_List:
        if rat == "HSPA":
            HSPA_RX_Gain_default = Lmtmfunc.HSPA_Rx_gain_average_mtm(df_Meas, Save_data_var, get_data_var, text_area)
            HSPA_RX_Freq_default = Lmtmfunc.HSPA_Rx_freq_average_mtm(df_Meas, Save_data_var, get_data_var, text_area)
        elif rat == "GSM":
            GSM_RX_Gain_Default = Lmtmfunc.Rx_2G_gain_average_mtm(df_Meas, Save_data_var, get_data_var, text_area)
            # 2G DRX RSSI는 INT((측정값-(전계세팅값))*16)=237 으로 계산되지만, Gain index를 캘 로그로는 알 수 없어서 Default 계산은 불가능
            # INT((-45.18-(-60))*16)=237
        else:
            Sub6_RX_Gain_default, Sub6_RSRP_Offset_default = Lmtmfunc.Sub6_Rx_gain_average_mtm(
                df_Meas, Save_data_var, get_data_var, text_area
            )
            Sub6_RX_Freq_default = Lmtmfunc.Sub6_Rx_freq_average_mtm(df_Meas, Save_data_var, get_data_var, text_area)
            Sub6_RX_Mixer_default = Lmtmfunc.Sub6_Rx_mixer_average_mtm(df_Meas, Save_data_var, get_data_var, text_area)

    if daseul_select.get():  # ! Daseul
        for rat in Test_List:
            for band in Test_List[rat]:
                if rat == "HSPA":
                    L3grx.chng_3g_rx_gain_default("daseul", Selected_spc, rat, band, HSPA_RX_Gain_default, text_area)
                    L3grx.chng_3g_rx_freq_default(
                        "daseul",
                        Selected_spc,
                        rat,
                        band,
                        HSPA_RX_Freq_default,
                        Bluetick,
                        blue_3grx_freq,
                        blue_3gdrx_offset,
                        text_area,
                    )
                else:
                    Lsub6rx.chng_sub6_rx_gain_default(
                        "daseul",
                        Selected_spc,
                        rat,
                        band,
                        daseul_dict_option,
                        Daseul_rxgainstage,
                        Sub6_RX_Gain_default,
                        text_area,
                    )
                    Lsub6rx.chng_sub6_rsrp_offset_default(
                        "daseul", Selected_spc, rat, band, daseul_dict_option, Sub6_RSRP_Offset_default, text_area
                    )
                    Lsub6rx.chng_sub6_rx_freq_default(
                        "daseul",
                        Selected_spc,
                        rat,
                        band,
                        daseul_dict_option,
                        Sub6_RX_Freq_default,
                        Bluetick,
                        blue_nrrx_freq,
                        blue_nrdrx_offset,
                        text_area,
                    )
                    Lsub6rx.chng_sub6_rx_mixer_default(
                        "daseul", Selected_spc, rat, band, daseul_dict_option, Sub6_RX_Mixer_default, text_area
                    )

    if mtm_select.get():  # ! MTM
        for rat in Test_List:
            for band in Test_List[rat]:
                if rat == "HSPA":
                    L3grx.chng_3g_rx_gain_default("mtm", mtm_3g_param, rat, band, HSPA_RX_Gain_default, text_area)
                    L3grx.chng_3g_rx_freq_default(
                        "mtm",
                        mtm_3g_param,
                        rat,
                        band,
                        HSPA_RX_Freq_default,
                        Bluetick,
                        blue_3grx_freq,
                        blue_3gdrx_offset,
                        text_area,
                    )
                else:
                    Lsub6rx.chng_sub6_rx_gain_default(
                        "mtm", mtm_nr_param, rat, band, mtm_dict_option, Mtm_rxgainstage, Sub6_RX_Gain_default, text_area
                    )
                    Lsub6rx.chng_sub6_rsrp_offset_default(
                        "mtm", mtm_nr_param, rat, band, mtm_dict_option, Sub6_RSRP_Offset_default, text_area
                    )
                    Lsub6rx.chng_sub6_rx_freq_default(
                        "mtm",
                        mtm_nr_param,
                        rat,
                        band,
                        mtm_dict_option,
                        Sub6_RX_Freq_default,
                        Bluetick,
                        blue_nrrx_freq,
                        blue_nrdrx_offset,
                        text_area,
                    )
                    Lsub6rx.chng_sub6_rx_mixer_default(
                        "mtm", mtm_nr_param, rat, band, mtm_dict_option, Sub6_RX_Mixer_default, text_area
                    )
