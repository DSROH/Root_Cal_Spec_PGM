import os
import re
import tkinter as tk
import tkinter.messagebox as msgbox
import Common_function as func
import LSI_get_data as Lget
import LSI_2g_tx as L2gtx
import LSI_2g_rx as L2grx
import LSI_3g as L3g
import LSI_cable as Lcable
import LSI_et as Lsub6et
import LSI_3g_et as L3get
import LSI_mtm as mtm
import LSI_sub6 as Lsub6
import LSI_sub6_rx as Lsub6rx
import LSI_fbrx as Lfbrx
import LSI_apt as Lapt


def start(
    list_file,
    Option_var,
    path_spc_file,
    mtm_folder,
    Select_op,
    debug_var,
    daseul_select,
    mtm_select,
    Cable_Spec_var,
    RX_Gain_Spec_var,
    FBRX_Meas_var,
    FBRX_Code_var,
    APT_Spec_var,
    ET_Psat_var,
    ET_Pgain_var,
    ET_Freq_var,
    ET_Power_var,
    BW_Cal_Spec_var,
    RFIC_Spec_var,
    RX_Gain_3G_Spec_var,
    FBRX_3G_Spec_var,
    RX_Gain_2G_Spec_var,
    GMSK_Spec_var,
    GTxL_Spec_var,
    GCode_Spec_var,
    EPSK_Spec_var,
    ETxL_Spec_var,
    ECode_Spec_var,
    Save_data_var,
    Bluetick_var,
    Blue_3g_ch,
    Blue_3g_offs,
    Blue_nr_ch,
    Blue_nr_offs,
    text_area,
):
    text_area.delete("1.0", "end")
    Selected_Option = Option_var.get()
    Selected_spc = path_spc_file.get()
    Bluetick = Bluetick_var.get()
    try:
        if Selected_Option != 1:
            if Select_op == "Daseul":
                if Selected_spc == "":
                    msgbox.showwarning("경고", "SPC 파일(*.dec)을 선택하세요")
                    return
                elif Selected_Option == 3:
                    msgbox.showwarning("경고", "Daseul Option을 선택하세요")
                    return
            elif Select_op == "MTM":
                if Selected_Option != 3:
                    msgbox.showwarning("경고", "MTM Default Cal Data 옵션을 선택하세요")
                    return

        if daseul_select.get():
            # Test_List 생성
            Check_Sub6 = False
            Check_HSPA = False
            Check_2G = False

            Test_List = {}
            Search_SUB6 = "[SUB6_CALIBRATION_COMMON]\n"
            Search_HSPA = "[HSPA_COMMON]\n"
            Search_2G = "[Common_Parameter]\n"

            with open(Selected_spc, "r", encoding="utf-8") as file:
                data_lines = file.readlines()
            file.close()

            for index, line in enumerate(data_lines):
                if Search_SUB6 == line:
                    Check_Sub6 = True
                elif Check_Sub6 and line.startswith("Cal_Band="):
                    item_SUB6 = line.strip().replace("=", ",").split(",")
                    key = dict.fromkeys(["SUB6"])
                    list_a = item_SUB6[1 : len(item_SUB6)]
                    list_a = [v for v in list_a if v]  # 리스트 값 공백 제거
                    Test_List.update({"SUB6": list_a})
                    break
                else:
                    continue

            for index, line in enumerate(data_lines):
                if Search_SUB6 == line:
                    Check_Sub6 = True
                elif Check_Sub6 and line.startswith("Num_RxGain_Stage="):
                    RxgainStage = line.strip().split("=")
                    read_stage = int(RxgainStage[1])
                    break
                else:
                    continue

            for index, line in enumerate(data_lines):
                if Search_HSPA == line:
                    Check_HSPA = True
                elif Check_HSPA and line.startswith("Cal_Band="):
                    item_HSPA = line.strip().replace("=", ",").split(",")
                    key = dict.fromkeys(["HSPA"])
                    list_a = item_HSPA[1 : len(item_HSPA)]
                    list_a = [v for v in list_a if v]  # 리스트 값 공백 제거
                    # 인덱스가 필요하기 때문에 int로 변환
                    list_a = map(int, list_a)
                    # 인덱스 값과 일치시키고 list_a를 list_b로 변환
                    list_b = ["1", "2", "5", "4", "8"]
                    ent = {i: k for i, k in enumerate(list_b)}
                    result = list(map(ent.get, list_a))
                    Test_List.update({"HSPA": result})
                    break
                else:
                    continue

            for index, line in enumerate(data_lines):
                if Search_2G == line:
                    Check_2G = True
                elif Check_2G and line.startswith("Cal_Band="):
                    item_2G = line.strip().replace("=", "").split(",")
                    key = dict.fromkeys(["GSM"])
                    Test_List.update({"GSM": ["G085", "G09", "G18", "G19"]})
                    break
                else:
                    continue

        if daseul_select.get() & (Selected_Option == 1):
            Lcable.chng_cable_spec_only(Selected_spc, Cable_Spec_var, text_area)

            for rat in Test_List:
                for band in Test_List[rat]:
                    if (rat == "NR") and (band in ["75"]):
                        Lsub6.Chng_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_Spec_var, text_area)
                    elif rat == "GSM":
                        L2grx.Chng_2G_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_2G_Spec_var, text_area)
                        L2gtx.Chng_2g_tx_spec_only(
                            Selected_spc,
                            band,
                            GMSK_Spec_var,
                            GTxL_Spec_var,
                            GCode_Spec_var,
                            EPSK_Spec_var,
                            ETxL_Spec_var,
                            ECode_Spec_var,
                            text_area,
                        )
                    else:
                        Lsub6.Chng_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_Spec_var, text_area)
                        Lsub6.Chng_fbrx_meas_spec_only(Selected_spc, rat, band, FBRX_Meas_var, FBRX_3G_Spec_var, text_area)
                        Lapt.Chng_apt_cal_spec_only(Selected_spc, rat, band, APT_Spec_var, text_area)
                        Lsub6et.chng_et_psat_pgain_spec_only(Selected_spc, rat, band, ET_Psat_var, ET_Pgain_var, text_area)
                        Lsub6et.chng_et_freq_spec_only(Selected_spc, rat, band, ET_Freq_var, text_area)
                        Lsub6et.chng_et_power_spec_only(Selected_spc, rat, band, ET_Power_var, text_area)
        # ! Daseul
        elif daseul_select.get() & (Selected_Option == 2):
            if list_file.size() == 0:
                msgbox.showwarning("경고", "Cal log 파일(*.csv)을 추가하세요")
                return

            df_Meas, df_Code, df_RFIC_gain, save_dir, Strt_dir = Lget.get_data(
                list_file.get(0, tk.END), Select_op, Save_data_var, debug_var, text_area
            )
            df_Meas.dropna(how="all", axis=1, inplace=True)
            df_Code.dropna(how="all", axis=1, inplace=True)
            os.chdir(save_dir)

            CableCheck = Lget.daseul_cable_average(df_Meas, Save_data_var, text_area)
            RFIC_gain = Lget.rfic_gain_average(df_RFIC_gain, Save_data_var, text_area)
            TxP_Channel_comp_ave = L3g.TxP_3g_channel_comp_pa_mid(df_Meas, Save_data_var, text_area)
            (
                FBRX_Gain_Meas_3G,
                FBRX_Gain_Meas_sub6,
                FBRX_Gain_Code_3G,
                FBRX_Gain_Code_sub6,
                FBRX_Freq_Meas_3G,
                FBRX_Freq_Meas_3G_Max,
                FBRX_Freq_Meas_3G_Min,
                FBRX_Freq_Meas_sub6,
                FBRX_Freq_Meas_sub6_Max,
                FBRX_Freq_Meas_sub6_Min,
                FBRX_Freq_Code_sub6,
                FBRX_Freq_Code_sub6_Max,
                FBRX_Freq_Code_sub6_Min,
            ) = Lfbrx.fbrx_average(df_Meas, df_Code, Save_data_var, text_area)
            PRX_Gain_2G, Ripple_2G, RXGain_3G, RXComp_3G, RXGain_sub6, RXRSRP_sub6, RXComp_sub6 = Lget.daseul_rx_average(
                df_Meas, Save_data_var, text_area
            )
            GMSK_Mean, GMSK_TXL_Mean, GMSK_Code_Mean = L2gtx.gsm_tx_gmsk_average(df_Meas, df_Code, Save_data_var, text_area)
            EPSK_Mean, EPSK_TXL_Mean, EPSK_Code_Mean = L2gtx.gsm_tx_edge_average(df_Meas, df_Code, Save_data_var, text_area)

            ETSAPT_3G_Psat_Ave, ETSAPT_3G_Power_Ave = L3get.Et_3g_average(df_Meas, Save_data_var, text_area)
            thermistor = Lget.therm_average(df_Code, Save_data_var, text_area)
            APT_3G_Ave, APT_Sub6_Ave, APT_Sub6_Max, APT_Sub6_Min = Lapt.apt_average(df_Meas, Save_data_var, text_area)

            (
                ETSAPT_sub6_Psat_Ave,
                ETSAPT_sub6_Freq_Ave,
                ETSAPT_sub6_Freq_Max,
                ETSAPT_sub6_Freq_Min,
                ETSAPT_sub6_Pgain_Ave,
                ETSAPT_sub6_Power_Ave,
                ETSAPT_sub6_Power_Max,
                ETSAPT_sub6_Power_Min,
            ) = Lget.sub6_et_average(df_Meas, Save_data_var, text_area)
            BW_Cal = Lget.sub6_bw_cal_average(df_Meas, Save_data_var, text_area)

            Lcable.chng_cable_spec(Selected_spc, CableCheck, Cable_Spec_var, text_area)

            for rat in Test_List:
                for band in Test_List[rat]:
                    text_area.insert(tk.END, "=" * 85)
                    text_area.insert(tk.END, "\n\n")
                    text_area.insert(tk.END, f"{rat}, BAND = {band}\n\n")
                    text_area.see(tk.END)
                    if (rat == "SUB6") and (band in ["75"]):
                        Lsub6.chng_sub6_rx_gain(
                            Selected_spc,
                            rat,
                            band,
                            read_stage,
                            RX_Gain_Spec_var,
                            RXGain_sub6,
                            RXRSRP_sub6,
                            RXComp_sub6,
                            text_area,
                        )
                    elif rat == "GSM":
                        L2grx.chng_2g_rx_gain(Selected_spc, band, RX_Gain_2G_Spec_var, PRX_Gain_2G, Ripple_2G, text_area)
                        (
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
                        ) = L2gtx.GSM_Params(band, data_lines)

                        L2gtx.chng_2g_tx_gmsk(
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
                        )
                        L2gtx.chng_2g_tx_epsk(
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
                        )
                        L2gtx.chng_2g_index_GMSK(Selected_spc, band, GMSK_Code_Mean, text_area)
                        L2gtx.chng_2g_index_EPSK(Selected_spc, band, EPSK_Code_Mean, text_area)
                    elif rat == "HSPA":
                        L3g.chng_3g_rfic_gain(Selected_spc, rat, band, RFIC_Spec_var, RFIC_gain, text_area)
                        L3g.chng_3g_rx_gain(Selected_spc, rat, band, RX_Gain_3G_Spec_var, RXGain_3G, RXComp_3G, text_area)
                        L3g.chng_3g_fbrx_gain_meas(Selected_spc, rat, band, FBRX_3G_Spec_var, FBRX_Gain_Meas_3G, text_area)
                        L3g.chng_3g_fbrx_gain_code(Selected_spc, rat, band, FBRX_3G_Spec_var, FBRX_Gain_Code_3G, text_area)
                        L3g.chng_3g_fbrx_freq_meas(
                            Selected_spc,
                            rat,
                            band,
                            FBRX_3G_Spec_var,
                            FBRX_Freq_Meas_3G,
                            FBRX_Freq_Meas_3G_Max,
                            FBRX_Freq_Meas_3G_Min,
                            text_area,
                        )
                        L3g.chng_3g_apt(Selected_spc, rat, band, APT_Spec_var, APT_3G_Ave)
                        L3g.chng_Txp_comp(Selected_spc, rat, band, 3, TxP_Channel_comp_ave)
                        L3get.chng_3g_et_psat_pgain(
                            Selected_spc,
                            rat,
                            band,
                            ET_Psat_var,
                            ETSAPT_3G_Psat_Ave,
                            ET_Pgain_var,
                            ETSAPT_3G_Power_Ave,
                            text_area,
                        )

                    else:  # NR
                        Lsub6.chng_sub6_rfic_gain(Selected_spc, rat, band, RFIC_Spec_var, RFIC_gain, text_area)
                        text_area.insert(tk.END, f"RX GAIN Calibration\n")
                        text_area.see(tk.END)
                        Lsub6.chng_sub6_rx_gain(
                            Selected_spc,
                            rat,
                            band,
                            read_stage,
                            RX_Gain_Spec_var,
                            RXGain_sub6,
                            RXRSRP_sub6,
                            RXComp_sub6,
                            text_area,
                        )

                        text_area.insert(tk.END, f"FBRX GAIN Calibration\n")
                        text_area.see(tk.END)
                        Lfbrx.chng_sub6_fbrx_gain_meas(Selected_spc, rat, band, FBRX_Meas_var, FBRX_Gain_Meas_sub6, text_area)
                        Lfbrx.chng_sub6_fbrx_gain_code(Selected_spc, rat, band, FBRX_Code_var, FBRX_Gain_Code_sub6, text_area)

                        text_area.insert(tk.END, f"FBRX FREQ Calibration\n")
                        text_area.see(tk.END)
                        Lfbrx.chng_sub6_fbrx_freq_meas(
                            Selected_spc,
                            rat,
                            band,
                            FBRX_Meas_var,
                            FBRX_Freq_Meas_sub6,
                            FBRX_Freq_Meas_sub6_Max,
                            FBRX_Freq_Meas_sub6_Min,
                            text_area,
                        )
                        Lfbrx.chng_sub6_fbrx_freq_code(
                            Selected_spc,
                            rat,
                            band,
                            FBRX_Code_var,
                            FBRX_Freq_Code_sub6,
                            FBRX_Freq_Code_sub6_Max,
                            FBRX_Freq_Code_sub6_Min,
                            text_area,
                        )

                        text_area.insert(tk.END, f"Thermistor Code\n")
                        text_area.see(tk.END)
                        Lsub6.chng_sub6_thermistor_code(Selected_spc, rat, band, thermistor, text_area)
                        Lapt.chng_sub6_apt(Selected_spc, rat, band, APT_Spec_var, APT_Sub6_Ave, APT_Sub6_Max, APT_Sub6_Min)
                        text_area.insert(tk.END, f"ET-SAPT Calibration\n")
                        text_area.see(tk.END)

                        Lsub6et.chng_sub6_et_psat_pgain(
                            Selected_spc,
                            rat,
                            band,
                            ET_Psat_var,
                            ETSAPT_sub6_Psat_Ave,
                            ET_Pgain_var,
                            ETSAPT_sub6_Pgain_Ave,
                            text_area,
                        )
                        Lsub6et.chng_sub6_et_freq(
                            Selected_spc,
                            rat,
                            band,
                            ET_Freq_var,
                            ETSAPT_sub6_Freq_Ave,
                            ETSAPT_sub6_Freq_Max,
                            ETSAPT_sub6_Freq_Min,
                            text_area,
                        )
                        Lsub6et.chng_sub6_et_power(
                            Selected_spc,
                            rat,
                            band,
                            ET_Power_var,
                            ETSAPT_sub6_Power_Ave,
                            ETSAPT_sub6_Power_Max,
                            ETSAPT_sub6_Power_Min,
                            text_area,
                        )

                        Lsub6.chng_sub6_bwcal(Selected_spc, rat, band, BW_Cal_Spec_var, BW_Cal, text_area)
            os.chdir(Strt_dir)
        # ! MTM Default Cal data
        elif Selected_Option == 3:
            if list_file.size() == 0:
                msgbox.showwarning("경고", "MTM log 파일(*.csv)을 추가하세요")
                return

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

            df_Meas, df_Code, df_RFIC_gain, save_dir, Strt_dir = Lget.get_data(
                list_file.get(0, tk.END), Select_op, Save_data_var, debug_var, text_area
            )
            os.chdir(save_dir)

            Test_List = mtm.get_mtm_bandlist(list_file.get(0, tk.END))
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
                                Lsub6.Read_sub6_default_cal_option(
                                    "daseul", Selected_spc, rat, band, daseul_dict_option, text_area
                                )
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
                                Lsub6.Read_sub6_default_cal_option("mtm", mtm_nr_param, rat, band, mtm_dict_option, text_area)
                            )

            for rat in Test_List:
                if rat == "HSPA":
                    HSPA_RX_Gain_default = mtm.HSPA_Rx_gain_average_mtm(df_Meas, Save_data_var, text_area)
                    HSPA_RX_Freq_default = mtm.HSPA_Rx_freq_average_mtm(df_Meas, Save_data_var, text_area)
                elif rat == "GSM":
                    GSM_RX_Gain_Default = mtm.Rx_2G_gain_average_mtm(df_Meas, Save_data_var, text_area)
                    # 2G DRX RSSI는 INT((측정값-(전계세팅값))*16)=237 으로 계산되지만, Gain index를 캘 로그로는 알 수 없어서 Default 계산은 불가능
                    # INT((-45.18-(-60))*16)=237
                else:
                    Sub6_RX_Gain_default, Sub6_RSRP_Offset_default = mtm.Sub6_Rx_gain_average_mtm(
                        df_Meas, Save_data_var, text_area
                    )
                    Sub6_RX_Freq_default = mtm.Sub6_Rx_freq_average_mtm(df_Meas, Save_data_var, text_area)
                    Sub6_RX_Mixer_default = mtm.Sub6_Rx_mixer_average_mtm(df_Meas, Save_data_var, text_area)

            if daseul_select.get():  # ! Daseul
                for rat in Test_List:
                    for band in Test_List[rat]:
                        if rat == "HSPA":
                            L3g.chng_3g_rx_gain_default("daseul", Selected_spc, rat, band, HSPA_RX_Gain_default, text_area)
                            L3g.chng_3g_rx_freq_default(
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
                            L3g.chng_3g_rx_gain_default("mtm", mtm_3g_param, rat, band, HSPA_RX_Gain_default, text_area)
                            L3g.chng_3g_rx_freq_default(
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
            os.chdir(Strt_dir)
        else:
            msgbox.showwarning("ERROR", "옵션을 선택하세요")
            return

    except FileExistsError as e:
        msgbox.showwarning("ERROR", e)

    msgbox.showwarning("Message", "작업 완료")
