import os
import time

# 工程目录
proj_path = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))

# 测试用例绝对路径
testExcel_path = os.path.join(proj_path,"data",u"测试用例.xlsx")

# RESTfulAPITestTool程序所在目录
restfulTool_path = os.path.join(proj_path,"restfultool","bin")

# 总测试用例表
test_sheet = u"测试用例"
test_case_sheet_col_no = 3
test_case_request_method_col_no = 4
test_case_request_url_col_no = 5
test_case_is_exec_col_no = 6
test_case_exec_time_col_no = 7
test_case_exec_res_col_no = 8

# 具体的测试用例表
case_is_exec_col_no = 4
case_input_param_col_no = 5
case_request_data_col_no = 6
case_request_code_col_no = 7
case_request_message_col_no = 8
case_response_data_col_no = 9
case_check_point_col_no = 10
case_status_col_no = 11

# 提取数据的原文件
data_path = os.path.normpath(os.path.join(proj_path,"data","data.py"))

# 鼠标操作
select_method_locate = (383, 192)
method_get_locate = (381,237)
method_post_locate = (381,212)
url_locate = (559,192)
input_param_locate = (536,317)
request_param_locate = (511,528)
sign_button_locate = (526,653)
send_button_locate = (594,653)
response_data_locate = (1017,455)

# 循环的次数
cycles = 1

# 需要处理结果的API列表
opera_API = ["Statistics","Inventory MNG"]
opera_API_1 = ["Statistics","Inventory MNG"]

# 存放理结果的路径
restore_path = os.path.normpath(os.path.join(proj_path,"data","res"))