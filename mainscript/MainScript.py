# encoding=utf-8

from time import sleep
from util.ExcelUtil import *
from config.ProjVar import cycles
from util.KeyBoard import *
from action.convert import *
from action.MouseControlTool import *
import json

cycles_num = cycles

# 运行restfultool
autoit.run(restfulTool_path + "\startRESTfulAPITestTool.bat", restfulTool_path)
time.sleep(5)

while cycles_num > 0:

    # 第一部分：操作测试用例
    # 解析测试用例获取可以执行的API
    test_excel = ParseExcel(testExcel_path)
    # 设置当前操作的sheet为测试用例
    test_excel.set_sheet_by_name(test_sheet)

    # 获取所有可执行的sheet
    testCases = []
    for cell in test_excel.get_col(test_case_sheet_col_no)[1:]:
        testCases.append(test_excel.get_cell_value(cell.row, cell.column))
    # print(testCases)

    # 获取可以执行的sheet
    caseExecs = {}
    for cell in test_excel.get_col(test_case_is_exec_col_no)[1:]:
        case_method_url = []
        if cell.value == "Y":
            case_method_url.append(testCases[cell.row - 2])
            case_method_url.append(test_excel.get_cell_value(cell.row, test_case_request_method_col_no))
            case_method_url.append(test_excel.get_cell_value(cell.row, test_case_request_url_col_no))
            caseExecs[cell.row - 1] = case_method_url
    # print(caseExecs)

    # 遍历可执行的sheet
    for case_no, case_method_url in caseExecs.items():
        case_sheet = caseExecs[case_no][0]
        case_request_method = caseExecs[case_no][1]
        case_request_url = caseExecs[case_no][2]
        print(case_sheet, case_request_method, case_request_url)

        # 第二部分：操作每个测试用例表中可执行的sheet
        test_excel.set_sheet_by_name(case_sheet)
        if case_request_method.lower() == "get":
            selectGetMethod()
        else:
            selectPostMethod()
        moveToUrl()
        selectAll()
        # 将请求的url先复制剪切板中，后粘贴到URL输入框中
        sleep(0.5)
        copyByText(case_request_url)
        sleep(0.5)
        paste()

        # 获取可执行的case
        itemExecs = {}
        result = []
        for cell in test_excel.get_col(case_is_exec_col_no)[1:]:
            No_inputPara = []
            if cell.value == "Y":
                check_point = test_excel.get_cell_value(cell.row, case_check_point_col_no)
                No_inputPara.append(cell.row - 1)
                No_inputPara.append(test_excel.get_cell_value(cell.row, case_input_param_col_no))
                itemExecs[cell.row - 1] = No_inputPara
                if No_inputPara[1] == None:
                    sleep(0.5)
                    moveToInputParam()
                    selectAll()
                    copyByText("")
                    getContent = getText()
                    sleep(0.5)
                    paste()
                    sleep(1)
                    moveTosignButton()
                    sleep(1)
                    moveToSendButton()
                    sleep(1)
                    moveToResponse()
                    sleep(2)
                    # 全选返回的结果，复制到剪切板中，并解析结果写入测试用例中
                    selectAll()
                    sleep(0.5)
                    copyByKey()
                    sleep(1)
                    responseContent = getText()
                    sleep(0.5)
                    responseContent.decode("utf-8")
                    responseCode, responseMessage, responseData = \
                        convert(responseContent.decode("utf-8"))
                    test_excel.write_cell(cell.row, case_request_code_col_no, responseCode)
                    test_excel.write_cell(cell.row, case_request_message_col_no, responseMessage)
                    test_excel.write_cell(cell.row, case_response_data_col_no, json.dumps(responseData, indent=4))
                    if responseCode == check_point:
                        test_excel.write_cell(cell.row,case_status_col_no,"pass")
                        result.append("pass")
                    else:
                        test_excel.write_cell(cell.row, case_status_col_no, "fail")
                        result.append("fail")
                else:
                    inputParam = test_excel.get_cell_value(cell.row, case_input_param_col_no)
                    # print(inputParam)
                    # 移动到input parameter输入框，并复制粘贴测试用例中的input param
                    sleep(0.5)
                    moveToInputParam()
                    selectAll()
                    copyByText(inputParam)
                    getContent = getText()
                    sleep(0.5)
                    paste()
                    sleep(1)
                    moveTosignButton()
                    sleep(1)
                    moveToSendButton()
                    sleep(1)
                    moveToResponse()
                    sleep(2)
                    responseContent = getText()
                    count_t = 0
                    while getContent == responseContent:
                        time.sleep(1)
                        count_t += 1
                        # 处理返回的响应
                        selectAll()
                        sleep(0.5)
                        copyByKey()
                        sleep(0.5)
                        responseContent = getText()
                        sleep(0.5)
                    # print(count_t)
                    responseContent.decode("utf-8")
                    responseCode, responseMessage, responseData = \
                        convert(responseContent.decode("utf-8"))
                    test_excel.write_cell(cell.row, case_request_code_col_no, responseCode)
                    test_excel.write_cell(cell.row, case_request_message_col_no, responseMessage)
                    test_excel.write_cell(cell.row, case_response_data_col_no, json.dumps(responseData, indent=4))
                    if responseCode == check_point:
                        test_excel.write_cell(cell.row, case_status_col_no, "pass")
                        result.append("pass")
                    else:
                        test_excel.write_cell(cell.row, case_status_col_no, "fail")
                        result.append("fail")
            else:
                pass
        test_excel.set_sheet_by_name(test_sheet)
        test_excel.write_cell_datetime(case_no+1,test_case_exec_time_col_no)
        if "fail" in result:
            test_excel.write_cell(case_no+1,test_case_exec_res_col_no,"fail")
        else:
            test_excel.write_cell(case_no + 1, test_case_exec_res_col_no, "pass")

    cycles_num -= 1