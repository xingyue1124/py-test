from openpyxl import *


class excelData:
    def getExcel(self):
        # 取workbook
        workbook = load_workbook("case.xlsx")
        # 取sheet
        sheet = workbook["Sheet1"]

        # 定义外层的list结构
        lists = []
        # 读取rows
        row_sheet = sheet.iter_rows()
        # 循环读取每一行，需要赋值每一行为一个list
        for item in row_sheet:
            # 如果取到第一行就跳出去直接取下一行
            if item[0].value == "url":
                continue
            list = []
            for col in item:
                list.append(col.value)
            lists.append(list)
        print(lists)
        return lists
