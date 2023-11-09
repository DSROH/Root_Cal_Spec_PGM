import tkinter.messagebox as msgbox
import LSI_cable as Lcable
import LSI_sub6_et as Lsub6et
import LSI_mtm as Lmtm
import LSI_apt as Lapt
import LSI_daseul as Ldaseul
import LSI_spec_only as Lspec
import LSI_fbrx as Lfbrx


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
                elif Check_Sub6 and line.startswith("Num_RxGain_Stage="):
                    RxgainStage = line.strip().split("=")
                    read_stage = int(RxgainStage[1])
                    Check_Sub6 = False
                elif Search_HSPA == line:
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
                    Check_HSPA = False
                elif Search_2G == line:
                    Check_2G = True
                elif Check_2G and line.startswith("Cal_Band="):
                    item_2G = line.strip().replace("=", "").split(",")
                    key = dict.fromkeys(["GSM"])
                    Test_List.update({"GSM": ["G085", "G09", "G18", "G19"]})
                    Check_2G = False
                    break
                else:
                    continue

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
                        Lfbrx.Chng_fbrx_meas_spec_only(Selected_spc, rat, band, FBRX_Meas_var, FBRX_3G_Spec_var, text_area)
                        Lapt.Chng_apt_cal_spec_only(Selected_spc, rat, band, APT_Spec_var, text_area)
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
                Selected_spc,
                data_lines,
                Test_List,
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

    except Exception as e:
        msgbox.showwarning("ERROR", e)

    msgbox.showwarning("Message", "작업 완료")
