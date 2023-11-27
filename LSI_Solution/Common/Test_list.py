def get_test_list(Selected_spc):
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
            # 인덱스가 필요하기 때문에 int로 변환
            list_a = map(int, [v for v in list_a if v])
            # 인덱스 값과 일치시키고 list_a를 list_b로 변환
            list_b = ["1", "2", "5", "4", "8"]
            ent = {i: k for i, k in enumerate(list_b)}
            result = list(map(ent.get, list_a))
            Test_List.update({"HSPA": result})
            Check_HSPA = False
        elif Search_2G == line:
            Check_2G = True
        elif Check_2G and line.startswith("Cal_Band="):
            item_2G = line.strip().replace("=", ",").split(",")
            key = dict.fromkeys(["GSM"])
            list_a = item_2G[1 : len(item_2G)]
            # 인덱스가 필요하기 때문에 int로 변환
            list_a = map(int, [v for v in list_a if v])
            # 인덱스 값과 일치시키고 list_a를 list_b로 변환
            list_b = ["G09", "G18", "G19", "G085"]
            ent = {i: k for i, k in enumerate(list_b)}
            result = list(map(ent.get, list_a))
            Test_List.update({"GSM": result})
            Check_2G = False
            break
        else:
            continue

    return Test_List, read_stage, data_lines
