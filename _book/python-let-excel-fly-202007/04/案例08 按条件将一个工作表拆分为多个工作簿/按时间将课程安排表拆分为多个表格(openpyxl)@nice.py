# https://segmentfault.com/a/1190000018597501
import pprint

import openpyxl
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

file_path = './教师课程安排.xlsx'
sheet_name = 'Sheet2'

workbook = openpyxl.load_workbook(file_path)
worksheet = workbook[sheet_name]

df = pd.read_excel(file_path
                   , sheet_name=sheet_name
                   , index_col=[0, 1])
df.reset_index()

data = dict()
rows = dataframe_to_rows(df)

for r_idx, row in enumerate(rows, 1):
    if r_idx < 4:
        continue

    date_name = row[0][1]
    # 如果没有这个键值, 初始化为字典
    if date_name not in data:
        data[date_name] = dict()

    teacher_name = row[0][0]
    # 如果没有这个键值, 初始化为数组
    if teacher_name not in data[date_name]:
        data[date_name][teacher_name] = []
    data[date_name][teacher_name].append(row[1:])


pp = pprint.PrettyPrinter(compact=True)
pp.pprint(data)

workbook.create_sheet(title='输出结果2')
sheet2 = workbook['输出结果2']

for key,value in data.items():
    # print(key)
    sheet2.append(("日期: " + key, None,None,None))
    # 加入表头
    sheet2.append(('Time', 'Student',	'TA', 'Classrooms'))

    for key2, value2 in value.items():
        sheet2.append(('教师: ' + key2, None, None, None))
        for index in range(0, len(value2)):
            # print(value2[index])
            sheet2.append(value2[index])

    # 加一行空行
    sheet2.append((None, None, None, None))

workbook.save(file_path)