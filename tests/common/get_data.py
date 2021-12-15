from openpyxl import load_workbook
from setting import config
import json


def read_excel_dict(file, sheet_name):
    work_book = load_workbook(filename=file)
    sheet = work_book[sheet_name]
    # 将excel内容转换成列表
    values = list(sheet.values)
    print(values)
    # 获取title
    title = values[0]
    # 将title与值组成字典
    dict_value = [dict(zip(title,value)) for value in values[1:]]
    return dict_value


# a = read_excel_dict(r'E:\\pythonProject0926\tests\data\regi.xlsx', sheet_name="Sheet1")
# b = a[1]["expected"]
# print(b)
# print(json.loads(b))
#  print(read_excel_dict(r'E:\\pythonProject0926\teachercode\data\cases.xlsx', sheet_name="register"))
