# 导入模块
import openpyxl

# 读取excel内容操作
# 基于excel文件路径，打开excel，默认打开的文件都是workbook
excel = openpyxl.load_workbook('demo.xlsx')
print(type(excel))

# # 获取excel的sheet
names = excel.sheetnames
print(type(names))
for name in names:
    print(name)

# 获取第一个sheet页面
# sheet = excel['name[0]']
sheet = excel['Sheet1']

# 获取sheet中的内容
print(sheet.values)
for value in sheet.values:
    print(value)

# excel写入
sheet['A3'] = '123'
sheet['G10'] = '456'
# 保存机制，如果有写入，必须先关闭文件，再执行操作
excel.save('demo.xlsx')
# 释放资源
excel.close()
