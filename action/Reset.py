from util.ExcelUtil import *
from config.ProjVar import *
import traceback


def clear_cells(test_excel):
    try:
        # 设置当前操作的sheet
        test_excel.set_sheet_by_name(test_excel.wb.sheetnames[0])
        # 获取表格中有数据的列
        cols = test_excel.get_max_col()
        # print(cols)
        if cols:
            for col_no in range(cols):
                # 输入列号，以元组的形式返回一列所有的对象
                try:
                    clear_col = test_excel.get_col(col_no)
                except TypeError as e:
                    raise('NoneType object is not iterable.')
                # 遍历每列，并且清空单元格中的数据
                for cell in clear_col:
                    # print(cell.row,cell.column,"")
                    test_excel.write_cell(cell.row,cell.column,"")
    except:
        traceback.print_exc()
        return False


if __name__ == "__main__":
    # 解析表格
    print(excel_path)
    test_excel = ParseExcel(excel_path)
    clear_cells(test_excel)