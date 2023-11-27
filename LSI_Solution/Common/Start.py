import tkinter.messagebox as msgbox
import LSI_Solution.Common.Spec_only as Lspec
import LSI_Solution.Common.Cable_check as Lcable
import LSI_Solution.Common.Test_list as Ltestlist
import LSI_Solution.DASEUL.DASEUL as Ldaseul
import LSI_Solution.DASEUL.ET_Sub6 as Lsub6et
import LSI_Solution.MTM.MTM as Lmtm
import traceback as tb


def start(
    list_file,
    Option_var,
    path_spc_file,
    mtm_folder,
    Select_op,
    debug_var,
    raw_data_var,
    get_data_var,
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
            Test_List, read_stage, data_lines = Ltestlist.get_test_list(Selected_spc)

        # ! Spec only
        if daseul_select.get() & (Selected_Option == 1):
            Lcable.chng_cable_spec_only(Selected_spc, Cable_Spec_var, text_area)

            for rat in Test_List:
                for band in Test_List[rat]:
                    if (rat == "NR") and (band in ["75"]):
                        Lspec.Chng_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_Spec_var, text_area)
                    elif rat == "GSM":
                        Lspec.Chng_2G_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_2G_Spec_var, text_area)
                        Lspec.Chng_2g_tx_spec_only(
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
                        Lspec.Chng_rx_gain_spec_only(Selected_spc, rat, band, RX_Gain_Spec_var, text_area)
                        Lspec.Chng_fbrx_meas_spec_only(Selected_spc, rat, band, FBRX_Meas_var, FBRX_3G_Spec_var, text_area)
                        Lspec.Chng_apt_cal_spec_only(Selected_spc, rat, band, APT_Spec_var, text_area)
                        Lsub6et.chng_et_psat_pgain_spec_only(Selected_spc, rat, band, ET_Psat_var, ET_Pgain_var, text_area)
                        Lsub6et.chng_sub6_et_freq_spec_only(Selected_spc, rat, band, ET_Freq_var, text_area)
                        Lsub6et.chng_sub6_et_power_spec_only(Selected_spc, rat, band, ET_Power_var, text_area)
        # ! Daseul
        elif daseul_select.get() & (Selected_Option == 2):
            if list_file.size() == 0:
                msgbox.showwarning("경고", "Cal log 파일(*.csv)을 추가하세요")
                return
            Ldaseul.daseul(
                list_file,
                Select_op,
                Save_data_var,
                debug_var,
                raw_data_var,
                get_data_var,
                Selected_spc,
                data_lines,
                read_stage,
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
                text_area,
            )
        # ! MTM Default Cal data
        elif Selected_Option == 3:
            if list_file.size() == 0:
                msgbox.showwarning("경고", "MTM log 파일(*.csv)을 추가하세요")
                return
            Lmtm.mtm(
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
            )
        else:
            msgbox.showwarning("ERROR", "옵션을 선택하세요")
            return

        msgbox.showwarning("Message", "작업 완료")

    except Exception:
        msgbox.showwarning("ERROR", tb.format_exc())
