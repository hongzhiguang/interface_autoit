from util.ExcelUtil import *
from config.ProjVar import *
from data.data import *
from action.Reset import clear_cells
from openpyxl import Workbook

date_pth = time.strftime('%Y%m%d%H%M', time.localtime())

test_excel = ParseExcel(testExcel_path)
test_excel.set_sheet_by_name(test_sheet)

for api in opera_API:
    for cell in test_excel.get_col(test_case_sheet_col_no)[1:]:
        test_excel.set_sheet_by_name(test_sheet)
        if api == cell.value:
            # print(api)
            test_excel.set_sheet_by_name(api)
            for cell in test_excel.get_col(case_response_data_col_no)[1:]:
                test_case_no = str(cell.row)
                if not cell.value:
                    pass
                response_1 = test_excel.get_cell_value(cell.row, cell.column)
                if not response_1:
                    continue
                response = eval(response_1)
                if not os.path.exists(os.path.normpath(os.path.join(restore_path,date_pth))):
                    os.makedirs(os.path.normpath(os.path.join(restore_path,date_pth)))
                restore_file = os.path.normpath(os.path.join(restore_path,date_pth,api+".xlsx"))

                if not os.path.exists(restore_file):
                    wb_new = Workbook()
                    wb_new.save(restore_file)
                    resp_excel = ParseExcel(restore_file)

                resp_excel.create_new_sheet(test_case_no)
                resp_excel.set_sheet_by_name(test_case_no)
                # print(test_case_no)

                # 遍历第二层：判断是data对应的值是否是字典型，开始遍历
                if isinstance(response,dict):
                    row = 1
                    for k2,v2 in response.items():
                        if isinstance(v2,dict):
                            pass
                        elif isinstance(v2,list):
                            for i in response[k2]:
                                if isinstance(i,dict):
                                    col = 1
                                    for k3,v3 in i.items():
                                        in_row = 0
                                        if isinstance(v3,str):
                                            print(row, col, v3)
                                            resp_excel.write_cell(row, col, v3)
                                            col += 1
                                            in_row = 1
                                        elif isinstance(v3,dict):
                                            pass
                                        elif isinstance(v3,list):
                                            for j in v3:
                                                in_row += 1
                                                for k4,v4 in enumerate(j.values()):
                                                    if str(v4) == "-":
                                                        v4 = "N/A"
                                                    # print(row+in_row-1,k4+col,str(v4))
                                                    resp_excel.write_cell(row+in_row-1,k4+col,str(v4))
                                    row += in_row
                                    # print(row)
                elif isinstance(response,list):
                    for d in response:
                        pass
                        # print(d)