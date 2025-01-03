import glob
import threading
import tkinter as tk
import tkinter.scrolledtext as st
import ttkbootstrap as ttkbst
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from openpyxl.styles import Font

import LSI_Solution.Common.Function as func
import LSI_Solution.Common.get_data as Lget
import LSI_Solution.Common.Start as Lstart

# %%
class Win_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cal_Spec_PGM_S25_LSI_Solomon_Dash_V1.0.0_241227")
        self.root.attributes("-topmost", True)
        self.root.geometry("1425x600")  # py : 1407x560 ipynb : 1635x670
        self.root.resizable(False, False)
        # self.root.option_add("*Font", "Consolas 10")
        self.theme_options = self.root.style.theme_names()
        self.font_style = Font(
            name="Calibri",
            size=10,
            bold=False,
            italic=False,
            vertAlign=None,  # 첨자
            underline="none",  # 밑줄
            strike=False,  # 취소선
            color="00000000",  # 블랙, # 00FF0000 Red, # 000000FF Blue
        )
        self.list_lna_setting = []
        self.selected_tool = "Daseul"
        self.option_var = ttkbst.IntVar()
        self.debug_var = ttkbst.BooleanVar(value=False)
        self.mtm_select = ttkbst.BooleanVar(value=False)
        self.das_select = ttkbst.BooleanVar(value=False)
        self.bluetick_var = ttkbst.BooleanVar(value=True)
        self.get_data_var = ttkbst.BooleanVar(value=False)
        self.raw_data_var = ttkbst.BooleanVar(value=False)
        self.save_data_var = ttkbst.BooleanVar(value=False)
        self.spc_file_path = "D:\\DATA\\Project_DATA\\@_M56\\TOOLS\\1_DASEUL\\RF_Cal\\M566B\\제조사양서\\Test\\SM-M566B_OPEN_CALIBRATION_Ver_3.2.31.0T9.spc.dec"
        self.mtm_folder_path = "D:\\DATA\\Project_DATA\\@_M56\\TOOLS\\2_MTM\\Default_Cal\\"

        self.root.bind("<F2>", lambda event: [func.browse_spc_path(self.spc_path, self.text_area), self.spc_click()])
        self.root.bind("<F3>", lambda event: [func.browse_mtm_path(self.mtm_folder, self.text_area), self.mtm_click()])
        self.root.bind("<F1>", lambda event: [func.Common_daseul_log(self.list_file), self.Dclick()])
        self.root.bind("<F4>", lambda event: [func.Common_mtm_log(self.list_file), self.Mclick()])
        self.root.bind(
            "<F5>",
            lambda event: [
                threading.Thread(
                    target=Lstart.start,
                    args=(
                        self.list_file,
                        self.option_var,
                        self.spc_path,
                        self.mtm_folder,
                        self.selected_tool,
                        self.debug_var,
                        self.raw_data_var,
                        self.get_data_var,
                        self.das_select,
                        self.mtm_select,
                        self.cable_spec_var,
                        self.rx_gain_spec_var,
                        self.fbrx_meas_var,
                        self.fbrx_code_var,
                        self.apt_spec_var,
                        self.et_psat_var,
                        self.et_pgain_var,
                        self.et_freq_var,
                        self.et_power_var,
                        self.bw_cal_spec_var,
                        self.rfic_spec_var,
                        self.rx_gain_3g_spec_var,
                        self.fbrx_3g_spec_var,
                        self.rx_gain_2g_spec_var,
                        self.gmsk_spec_var,
                        self.gtxl_spec_var,
                        self.gcode_spec_var,
                        self.epsk_spec_var,
                        self.etxl_spec_var,
                        self.ecode_spec_var,
                        self.save_data_var,
                        self.bluetick_var,
                        self.blue_3g_ch_var,
                        self.blue_3g_offs_var,
                        self.blue_nr_ch_var,
                        self.blue_nr_offs_var,
                        self.text_area,
                    ),
                ).start()
            ],
        )
        self.root.bind(
            "<F8>",
            lambda event: [
                self.get_data_var.set(True),
                threading.Thread(
                    target=Lget.get_data,
                    args=(
                        self.list_file,
                        "",
                        self.selected_tool,
                        4,
                        self.save_data_var.get(),
                        self.debug_var.get(),
                        self.raw_data_var.get(),
                        self.get_data_var.get(),
                        self.text_area,
                    ),
                ).start(),
            ],
        )
        self.create_widgets()

    def Dclick(self):
        self.selected_tool = "Daseul"
        self.mtm_select.set(False)
        self.das_select.set(True)
        self.option_var.set(2)

    def Mclick(self):
        self.selected_tool = "MTM"
        self.mtm_select.set(True)
        self.das_select.set(False)
        self.option_var.set(3)

    def spc_click(self):
        self.das_select.set(True)

    def mtm_click(self):
        self.mtm_select.set(True)

    def change_theme(self):
        self.themename = self.root.getvar("themename")
        self.root.style.theme_use(self.themename)

    def lna_config(self):
        ChildWin_lna = ttkbst.Toplevel(title="NR LNA Bias / Gain Stage Config.")
        ChildWin_lna.attributes("-topmost", True)
        ChildWin_lna.geometry("715x445")
        ChildWin_lna.resizable(False, False)
        ChildWin_lna.focus()
        colors = ChildWin_lna.style.colors

        Est_rowdata1 = [
            ("n1", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n1", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n1", "RX2", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n1", "RX3", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n3", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n3", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n3", "RX2", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n3", "RX3", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n7", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n7", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n7", "RX2", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n7", "RX3", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n8", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n8", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n12", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n12", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n13", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n13", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n20", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n20", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n25", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n25", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n25", "RX2", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n25", "RX3", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n26", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n26", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n28", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n28", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n39", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n39", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n71", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n71", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n75", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n75", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n77", "RX0", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n77", "RX1", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n77", "RX2", 1, 3, 2, 3, 4, 5, 10, 0),
            ("n77", "RX3", 1, 3, 2, 3, 4, 5, 10, 0),
        ]
        Est_coldata1 = [
            {"text": "Band", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Path", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Gain 1", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Bias 1", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Gain 2", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Bias 2", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Gain 3", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Bias 3", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Gain 4", "anchor": "center", "width": 70, "stretch": False},
            {"text": "Bias 4", "anchor": "center", "width": 70, "stretch": False},
        ]

        Est_table1 = Tableview(
            master=ChildWin_lna,
            coldata=Est_coldata1,
            rowdata=Est_rowdata1,
            paginated=False,
            searchable=True,
            autoalign=False,
            bootstyle=PRIMARY,
            height=16,
            stripecolor=(colors.light, None),
        )
        Est_table1.place(x=5, y=5, width=705, height=410)
        # Est_table1.autofit_columns()

        # try:
        #     ChildWin_lna.destroy()
        # except:
        #     pass

    def create_widgets(self):
        self.create_left_frame()
        self.create_scrolled_text_frame()

    def create_left_frame(self):
        self.left_frame = ttkbst.Frame(self.root)
        self.left_frame.place(x=0, y=0, width=640, height=600)

        self.create_list_frame()
        self.create_path_frame()
        self.create_option_frame()
        self.create_cal_spec_frame()
        self.create_execution_frame()

    def create_scrolled_text_frame(self):
        scrolled_txt_frame = ttkbst.Frame(self.root)
        scrolled_txt_frame.place(x=640, y=0, width=780, height=600)

        self.text_area = st.ScrolledText(scrolled_txt_frame, font=("Consolas", 9))
        self.text_area.place(x=0, y=5, width=780, height=545)

        right_run_frame = ttkbst.Frame(scrolled_txt_frame)
        right_run_frame.place(x=640, y=550, width=780, height=50)

        Btn_lna = ttkbst.Button(right_run_frame, text="NR LNA Config", bootstyle="info")
        Btn_lna.config(command=lambda: [self.list_lna_setting.clear(), self.lna_config()])
        Btn_lna.place(x=0, y=5, width=160, height=40)

        # p_var = tk.DoubleVar()
        # progressbar = ttkbst.CTkProgressBar(right_run_frame, variable=p_var, fg_color="#dbdbdb", corner_radius=5)
        # progressbar.place(x=0, y=5, width=770, height=45)

        author = ttkbst.Label(right_run_frame, text="dongsub.roh@samsung.com", anchor="w")
        author.place(x=620, y=5, width=160, height=40)

    def create_list_frame(self):
        btn_add_file1 = ttkbst.Button(
            self.left_frame, text="Daseul log 추가 (F1)", command=lambda: [func.Common_daseul_log(self.list_file), self.Dclick()]
        )
        btn_add_file1.place(x=5, y=5, width=150, height=35)

        btn_add_file2 = ttkbst.Button(
            self.left_frame, text="MTM log 추가 (F4)", command=lambda: [func.Common_mtm_log(self.list_file), self.Mclick()]
        )
        btn_add_file2.place(x=510, y=5, width=125, height=35)

        list_frame = ttkbst.Labelframe(self.left_frame, text=" Calibration log ", bootstyle=PRIMARY)
        list_frame.place(x=5, y=45, width=630, height=85)
        scrollbar = ttkbst.Scrollbar(list_frame, orient="vertical")
        scrollbar.place(x=600, y=0, width=23, height=62)
        self.list_file = tk.Listbox(list_frame, height=5, yscrollcommand=scrollbar.set)
        self.list_file.place(x=5, y=0, width=595, height=62)

        scrollbar.config(command=self.list_file.yview)

        # Cal log : log 폴더의 CSV 파일 자동 입력
        for filename in glob.glob("C:\\DGS\\LOGS\\*.csv"):
            self.list_file.insert(tk.END, filename)

    def create_path_frame(self):
        path_frame = ttkbst.Labelframe(self.left_frame, text=" SPC File Path ", bootstyle=PRIMARY)
        path_frame.place(x=5, y=135, width=630, height=120)

        spc_chkbox = ttkbst.Checkbutton(path_frame, text="SPC", style="info.TCheckbutton", variable=self.das_select)
        spc_chkbox.place(x=10, y=10, width=45, height=30)

        self.spc_path = ttkbst.Entry(path_frame)
        self.spc_path.insert(0, self.spc_file_path)
        self.spc_path.place(x=65, y=10, width=455, height=30)

        btn_spc_path = ttkbst.Button(
            path_frame,
            text="SPC (F2)",
            style="info.TButton",
            command=lambda: [func.browse_spc_path(self.spc_path, self.text_area), self.spc_click()],
        )
        btn_spc_path.place(x=530, y=10, width=90, height=30)

        mtm_chkbox = ttkbst.Checkbutton(path_frame, text="MTM", style="info.TCheckbutton", variable=self.mtm_select)
        mtm_chkbox.place(x=10, y=55, width=45, height=30)

        self.mtm_folder = ttkbst.Entry(path_frame)
        # spc 파일 경로 사전입력
        self.mtm_folder.insert(0, self.mtm_folder_path)
        self.mtm_folder.place(x=65, y=55, width=455, height=30)

        btn_mtm = ttkbst.Button(
            path_frame,
            text="MTM (F3)",
            style="info.TButton",
            command=lambda: [func.browse_mtm_path(self.mtm_folder, self.text_area), self.mtm_click()],
        )
        btn_mtm.place(x=530, y=55, width=90, height=30)

    def create_option_frame(self):

        radio_btn_frame = ttkbst.Labelframe(self.left_frame, text=" Options ", bootstyle=PRIMARY)
        radio_btn_frame.place(x=5, y=260, width=630, height=105)

        btn_Option1 = ttkbst.Radiobutton(radio_btn_frame, text="Cal Spec 조정", value=1, variable=self.option_var)
        btn_Option1.place(x=10, y=10, width=100, height=25)

        btn_Option2 = ttkbst.Radiobutton(radio_btn_frame, text="Cal 산포 적용", value=2, variable=self.option_var)
        btn_Option2.place(x=120, y=10, width=100, height=25)
        btn_Option2.invoke()

        btn_Option3 = ttkbst.Radiobutton(radio_btn_frame, text="MTM Default Cal Data", value=3, variable=self.option_var)
        btn_Option3.place(x=230, y=10, width=140, height=25)

        chkbox1 = ttkbst.Checkbutton(radio_btn_frame, text="Save Data to Excel", variable=self.save_data_var)
        chkbox1.place(x=495, y=10, width=120, height=25)
        # chkbox1.configure(state="!selected")

        chkbox2 = ttkbst.Checkbutton(radio_btn_frame, text="Save Raw Data", variable=self.raw_data_var)
        chkbox2.place(x=495, y=30, width=120, height=25)
        # chkbox2.configure(state="!selected")

        chkbox3 = ttkbst.Checkbutton(radio_btn_frame, text="Debug Option", variable=self.debug_var)
        chkbox3.place(x=495, y=50, width=120, height=25)
        # chkbox3.configure(state="!selected")
        # ? ======================================== Bluetick for 호주향 ========================================
        bluetick_chkbx = ttkbst.Checkbutton(radio_btn_frame, text="Bluetick for AU", variable=self.bluetick_var)
        bluetick_chkbx.place(x=10, y=45, width=120, height=25)

        # ! There's an even easier way than select() and deselect()!
        # ! If you properly link a checkbutton to a tkinter int or boolean variable, the checkbutton will automatically check and uncheck
        # ! if it's given 1/True or 0/False values, respectively

        blue_label_3g = ttkbst.Label(radio_btn_frame, text="3G", anchor="w")
        blue_label_nr = ttkbst.Label(radio_btn_frame, text="LTE", anchor="w")
        blue_label_3goffs = ttkbst.Label(radio_btn_frame, text="dB", anchor="w")
        blue_label_nroffs = ttkbst.Label(radio_btn_frame, text="dB", anchor="w")
        blue_label_3g.place(x=120, y=45, width=20, height=25)
        blue_label_nr.place(x=248, y=45, width=25, height=25)
        blue_label_3goffs.place(x=215, y=45, width=20, height=25)
        blue_label_nroffs.place(x=348, y=45, width=20, height=25)

        self.blue_3g_ch_var = ttkbst.Entry(radio_btn_frame, justify="right")
        self.blue_nr_ch_var = ttkbst.Entry(radio_btn_frame, justify="right")
        self.blue_3g_offs_var = ttkbst.Entry(radio_btn_frame, justify="right")
        self.blue_nr_offs_var = ttkbst.Entry(radio_btn_frame, justify="right")
        self.blue_3g_ch_var.place(x=140, y=45, width=45, height=25)
        self.blue_nr_ch_var.place(x=273, y=45, width=45, height=25)
        self.blue_3g_offs_var.place(x=190, y=45, width=25, height=25)
        self.blue_nr_offs_var.place(x=323, y=45, width=25, height=25)

        self.blue_3g_ch_var.insert(tk.END, "4436")
        self.blue_nr_ch_var.insert(tk.END, "9410")
        self.blue_3g_offs_var.insert(tk.END, "3")
        self.blue_nr_offs_var.insert(tk.END, "3")

        # ? Get Data option을 4로 처리해서 get_data 리턴이 없도록 한다.
        Get_Data_btn = ttkbst.Button(
            radio_btn_frame,
            text="Get_data\n    (F8)",
            command=lambda: [
                self.get_data_var.set(True),
                threading.Thread(
                    target=Lget.get_data,
                    args=(
                        self.list_file,
                        "",
                        self.selected_tool,
                        4,
                        self.save_data_var.get(),
                        self.debug_var.get(),
                        self.raw_data_var.get(),
                        self.get_data_var.get(),
                        self.text_area,
                    ),
                ).start(),
            ],
        )
        Get_Data_btn.place(x=400, y=12, width=80, height=60)

    def create_cal_spec_frame(self):
        cal_spec_frame = ttkbst.Labelframe(self.left_frame, text=" Cal Spec ", bootstyle=PRIMARY)
        cal_spec_frame.place(x=5, y=365, width=630, height=185)

        Cable_Spec_label = ttkbst.Label(cal_spec_frame, text="Cable Check", anchor="e")
        RFIC_Spec_label = ttkbst.Label(cal_spec_frame, text="RFIC_Gain", anchor="e")
        APT_Spec_label = ttkbst.Label(cal_spec_frame, text="APT_Spec", anchor="e")
        BW_Cal_Spec_label = ttkbst.Label(cal_spec_frame, text="BW_Cal", anchor="e")
        FBRX_Meas_label = ttkbst.Label(cal_spec_frame, text="FBRX Meas", anchor="e")
        GMSK_Spec_label = ttkbst.Label(cal_spec_frame, text="GMSK Spec", anchor="e")
        GTxL_Spec_label = ttkbst.Label(cal_spec_frame, text="GMSK TxL", anchor="e")
        GCode_Spec_label = ttkbst.Label(cal_spec_frame, text="GMSK Code", anchor="e")
        FBRX_Code_label = ttkbst.Label(cal_spec_frame, text="FBRX Code", anchor="e")
        EPSK_Spec_label = ttkbst.Label(cal_spec_frame, text="EPSK Spec", anchor="e")
        ETxL_Spec_label = ttkbst.Label(cal_spec_frame, text="EPSK TxL", anchor="e")
        ECode_Spec_label = ttkbst.Label(cal_spec_frame, text="EPSK Code", anchor="e")
        FBRX_3G_Spec_label = ttkbst.Label(cal_spec_frame, text="3G FBRX", anchor="e")
        RX_Gain_label = ttkbst.Label(cal_spec_frame, text="NR RX Gain", anchor="e")
        RX_Gain_3G_label = ttkbst.Label(cal_spec_frame, text="3G RX Gain", anchor="e")
        RX_Gain_2G_label = ttkbst.Label(cal_spec_frame, text="2G RX Gain", anchor="e")
        ET_Psat_label = ttkbst.Label(cal_spec_frame, text="ET_Psat", anchor="e")
        ET_Pgain_label = ttkbst.Label(cal_spec_frame, text="ET_Pgain", anchor="e")
        ET_Freq_label = ttkbst.Label(cal_spec_frame, text="ET_Freq", anchor="e")
        ET_Power_label = ttkbst.Label(cal_spec_frame, text="ET_Power", anchor="e")
        Cable_Spec_label.place(x=10, y=10, width=75, height=25)
        RFIC_Spec_label.place(x=10, y=45, width=75, height=25)
        APT_Spec_label.place(x=10, y=80, width=75, height=25)
        BW_Cal_Spec_label.place(x=10, y=115, width=75, height=25)
        FBRX_Meas_label.place(x=140, y=10, width=70, height=25)
        GMSK_Spec_label.place(x=140, y=45, width=70, height=25)
        GTxL_Spec_label.place(x=140, y=80, width=70, height=25)
        GCode_Spec_label.place(x=140, y=115, width=70, height=25)
        FBRX_Code_label.place(x=265, y=10, width=70, height=25)
        EPSK_Spec_label.place(x=265, y=45, width=70, height=25)
        ETxL_Spec_label.place(x=265, y=80, width=70, height=25)
        ECode_Spec_label.place(x=265, y=115, width=70, height=25)
        FBRX_3G_Spec_label.place(x=390, y=10, width=70, height=25)
        RX_Gain_label.place(x=390, y=45, width=70, height=25)
        RX_Gain_3G_label.place(x=390, y=80, width=70, height=25)
        RX_Gain_2G_label.place(x=390, y=115, width=70, height=25)
        ET_Psat_label.place(x=515, y=10, width=60, height=25)
        ET_Pgain_label.place(x=515, y=45, width=60, height=25)
        ET_Freq_label.place(x=515, y=80, width=60, height=25)
        ET_Power_label.place(x=515, y=115, width=60, height=25)

        self.fbrx_meas_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.gmsk_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.gtxl_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.gcode_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.fbrx_code_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.epsk_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.etxl_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.ecode_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.fbrx_3g_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.rx_gain_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.rx_gain_3g_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.rx_gain_2g_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.et_psat_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.cable_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.et_pgain_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.rfic_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.et_freq_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.apt_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.bw_cal_spec_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.et_power_var = ttkbst.Entry(cal_spec_frame, justify="right")
        self.fbrx_meas_var.place(x=215, y=10, width=40, height=25)
        self.gmsk_spec_var.place(x=215, y=45, width=40, height=25)
        self.gtxl_spec_var.place(x=215, y=80, width=40, height=25)
        self.gcode_spec_var.place(x=215, y=115, width=40, height=25)
        self.fbrx_code_var.place(x=340, y=10, width=40, height=25)
        self.epsk_spec_var.place(x=340, y=45, width=40, height=25)
        self.etxl_spec_var.place(x=340, y=80, width=40, height=25)
        self.ecode_spec_var.place(x=340, y=115, width=40, height=25)
        self.fbrx_3g_spec_var.place(x=465, y=10, width=40, height=25)
        self.rx_gain_spec_var.place(x=465, y=45, width=40, height=25)
        self.rx_gain_3g_spec_var.place(x=465, y=80, width=40, height=25)
        self.rx_gain_2g_spec_var.place(x=465, y=115, width=40, height=25)
        self.et_psat_var.place(x=580, y=10, width=40, height=25)
        self.cable_spec_var.place(x=90, y=10, width=40, height=25)
        self.et_pgain_var.place(x=580, y=45, width=40, height=25)
        self.rfic_spec_var.place(x=90, y=45, width=40, height=25)
        self.et_freq_var.place(x=580, y=80, width=40, height=25)
        self.apt_spec_var.place(x=90, y=80, width=40, height=25)
        self.bw_cal_spec_var.place(x=90, y=115, width=40, height=25)
        self.et_power_var.place(x=580, y=115, width=40, height=25)

        self.cable_spec_var.insert(tk.END, "2")
        self.rfic_spec_var.insert(tk.END, "5")
        self.apt_spec_var.insert(tk.END, "0.5")
        self.bw_cal_spec_var.insert(tk.END, "3")
        self.fbrx_meas_var.insert(tk.END, "5")
        self.gmsk_spec_var.insert(tk.END, "5")
        self.gtxl_spec_var.insert(tk.END, "2")
        self.gcode_spec_var.insert(tk.END, "50")
        self.fbrx_code_var.insert(tk.END, "750")
        self.epsk_spec_var.insert(tk.END, "5")
        self.etxl_spec_var.insert(tk.END, "2")
        self.ecode_spec_var.insert(tk.END, "50")
        self.fbrx_3g_spec_var.insert(tk.END, "4")
        self.rx_gain_spec_var.insert(tk.END, "5")
        self.rx_gain_3g_spec_var.insert(tk.END, "5")
        self.rx_gain_2g_spec_var.insert(tk.END, "5")
        self.et_psat_var.insert(tk.END, "1.5")
        self.et_pgain_var.insert(tk.END, "1.5")
        self.et_freq_var.insert(tk.END, "3")
        self.et_power_var.insert(tk.END, "3")

    def create_execution_frame(self):
        execution_frame = ttkbst.Frame(self.left_frame)
        execution_frame.place(x=5, y=550, width=630, height=40)

        self.theme = tk.Menubutton(execution_frame, text="Select a theme")
        menu = tk.Menu(self.theme)
        self.theme["menu"] = menu

        for t in self.theme_options:
            menu.add_radiobutton(label=t, variable="themename", command=self.change_theme)

        self.theme.place(x=0, y=5, width=150, height=40)

        btn_start = ttkbst.Button(
            execution_frame,
            text="Start (F5)",
            command=lambda: [
                threading.Thread(
                    target=Lstart.start,
                    args=(
                        self.list_file,
                        self.option_var,
                        self.spc_path,
                        self.mtm_folder,
                        self.selected_tool,
                        self.debug_var,
                        self.raw_data_var,
                        self.get_data_var,
                        self.das_select,
                        self.mtm_select,
                        self.cable_spec_var,
                        self.rx_gain_spec_var,
                        self.fbrx_meas_var,
                        self.fbrx_code_var,
                        self.apt_spec_var,
                        self.et_psat_var,
                        self.et_pgain_var,
                        self.et_freq_var,
                        self.et_power_var,
                        self.bw_cal_spec_var,
                        self.rfic_spec_var,
                        self.rx_gain_3g_spec_var,
                        self.fbrx_3g_spec_var,
                        self.rx_gain_2g_spec_var,
                        self.gmsk_spec_var,
                        self.gtxl_spec_var,
                        self.gcode_spec_var,
                        self.epsk_spec_var,
                        self.etxl_spec_var,
                        self.ecode_spec_var,
                        self.save_data_var,
                        self.bluetick_var,
                        self.blue_3g_ch_var,
                        self.blue_3g_offs_var,
                        self.blue_nr_ch_var,
                        self.blue_nr_offs_var,
                        self.text_area,
                    ),
                ).start()
            ],
        )
        btn_start.place(x=430, y=5, width=200, height=40)

# %%
if __name__=="__main__":
    app=ttkbst.Window(themename="cosmo")
    win=Win_GUI(app)
    app.mainloop()
