import tkinter as tk
import LSI_Solution.Common.get_data as Lget
import LSI_Solution.Common.Cable_check as Lcable
import LSI_Solution.Common.Test_list as Ltestlist
import LSI_Solution.DASEUL.TX_2g as L2gtx
import LSI_Solution.DASEUL.RX_2g as L2grx
import LSI_Solution.DASEUL.TX_3g as L3gtx
import LSI_Solution.DASEUL.RX_3g as L3grx
import LSI_Solution.DASEUL.TX_sub6 as Lsub6tx
import LSI_Solution.DASEUL.RX_sub6 as Lsub6rx
import LSI_Solution.DASEUL.ET_3g as L3get
import LSI_Solution.DASEUL.ET_Sub6 as Lsub6et
import LSI_Solution.DASEUL.FBRX as Lfbrx
import LSI_Solution.DASEUL.APT as Lapt


def daseul(
    list_file,
    Select_op,
    Save_data_var,
    debug_var,
    raw_data_var,
    get_data_var,
    Selected_spc,
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
):
    Test_List, read_stage, data_lines = Ltestlist.get_test_list(Selected_spc)

    (
        CableCheck,
        RFIC_gain,
        TxP_Channel_comp_ave,
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
        PRX_Gain_2G,
        Ripple_2G,
        RXGain_3G,
        RXComp_3G,
        RXGain_sub6,
        RXRSRP_sub6,
        RXComp_sub6,
        GMSK_Mean,
        GMSK_TXL_Mean,
        GMSK_Code_Mean,
        EPSK_Mean,
        EPSK_TXL_Mean,
        EPSK_Code_Mean,
        ETSAPT_3G_Psat_Ave,
        ETSAPT_3G_Psat_Max,
        ETSAPT_3G_Psat_Min,
        ETSAPT_3G_Power_Ave,
        ETSAPT_3G_Power_Max,
        ETSAPT_3G_Power_Min,
        thermistor,
        APT_3G_Ave,
        APT_Sub6_Ave,
        APT_Sub6_Max,
        APT_Sub6_Min,
        ETSAPT_sub6_Psat_Ave,
        ETSAPT_sub6_Psat_Max,
        ETSAPT_sub6_Psat_Min,
        ETSAPT_sub6_Freq_Ave,
        ETSAPT_sub6_Freq_Max,
        ETSAPT_sub6_Freq_Min,
        ETSAPT_sub6_Pgain_Ave,
        ETSAPT_sub6_Pgain_Max,
        ETSAPT_sub6_Pgain_Min,
        ETSAPT_sub6_Power_Ave,
        ETSAPT_sub6_Power_Max,
        ETSAPT_sub6_Power_Min,
        BW_Cal,
    ) = Lget.get_data(list_file, Select_op, Save_data_var, debug_var, raw_data_var, get_data_var, text_area)

    # Average data save 전에 chdir 실행

    # ! Change spec
    Lcable.chng_cable_spec(Selected_spc, CableCheck, Cable_Spec_var, text_area)

    for rat in Test_List:
        for band in Test_List[rat]:
            text_area.insert(tk.END, "=" * 85)
            text_area.insert(tk.END, "\n\n")
            text_area.insert(tk.END, f"{rat}, BAND = {band}\n\n")
            text_area.see(tk.END)
            if (rat == "SUB6") and (band in ["75"]):
                Lsub6rx.chng_sub6_rx_gain(
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
                ) = L2gtx.GSM_Params(Selected_spc, band)

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
                L3gtx.chng_3g_rfic_gain(Selected_spc, rat, band, RFIC_Spec_var, RFIC_gain, text_area)
                L3grx.chng_3g_rx_gain(Selected_spc, rat, band, RX_Gain_3G_Spec_var, RXGain_3G, RXComp_3G, text_area)
                L3gtx.chng_3g_fbrx_gain_meas(Selected_spc, rat, band, FBRX_3G_Spec_var, FBRX_Gain_Meas_3G, text_area)
                L3gtx.chng_3g_fbrx_gain_code(Selected_spc, rat, band, FBRX_3G_Spec_var, FBRX_Gain_Code_3G, text_area)
                L3gtx.chng_3g_fbrx_freq_meas(
                    Selected_spc,
                    rat,
                    band,
                    FBRX_3G_Spec_var,
                    FBRX_Freq_Meas_3G,
                    FBRX_Freq_Meas_3G_Max,
                    FBRX_Freq_Meas_3G_Min,
                    text_area,
                )
                Lapt.chng_3g_apt(Selected_spc, rat, band, APT_Spec_var, APT_3G_Ave)
                L3gtx.chng_Txp_comp(Selected_spc, rat, band, 3, TxP_Channel_comp_ave)
                L3get.chng_3g_et_psat_pgain(
                    Selected_spc,
                    rat,
                    band,
                    ET_Psat_var,
                    ETSAPT_3G_Psat_Ave,
                    ETSAPT_3G_Psat_Max,
                    ETSAPT_3G_Psat_Min,
                    ET_Pgain_var,
                    ETSAPT_3G_Power_Ave,
                    ETSAPT_3G_Power_Max,
                    ETSAPT_3G_Power_Min,
                    text_area,
                )

            else:  # NR
                Lsub6tx.chng_sub6_rfic_gain(Selected_spc, rat, band, RFIC_Spec_var, RFIC_gain, text_area)
                text_area.insert(tk.END, f"RX GAIN Calibration\n")
                text_area.see(tk.END)
                Lsub6rx.chng_sub6_rx_gain(
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
                Lsub6tx.chng_sub6_thermistor_code(Selected_spc, rat, band, thermistor, text_area)
                Lapt.chng_sub6_apt(Selected_spc, rat, band, APT_Spec_var, APT_Sub6_Ave, APT_Sub6_Max, APT_Sub6_Min)
                text_area.insert(tk.END, f"ET-SAPT Calibration\n")
                text_area.see(tk.END)

                Lsub6et.chng_sub6_et_psat_pgain(
                    Selected_spc,
                    rat,
                    band,
                    ET_Psat_var,
                    ETSAPT_sub6_Psat_Ave,
                    ETSAPT_sub6_Psat_Max,
                    ETSAPT_sub6_Psat_Min,
                    ET_Pgain_var,
                    ETSAPT_sub6_Pgain_Ave,
                    ETSAPT_sub6_Pgain_Max,
                    ETSAPT_sub6_Pgain_Min,
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

                Lsub6tx.chng_sub6_bwcal(Selected_spc, rat, band, BW_Cal_Spec_var, BW_Cal, text_area)
