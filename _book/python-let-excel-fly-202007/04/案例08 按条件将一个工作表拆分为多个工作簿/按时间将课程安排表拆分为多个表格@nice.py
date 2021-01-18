# https://segmentfault.com/a/1190000018597501
import pprint

import tablib
import xlwings as xw
import pandas as pd

file_path = './教师课程安排.xlsx'
sheet_name = 'Sheet2'

app = xw.App(visible = True, add_book = False)
workbook = app.books.open(file_path)
worksheet = workbook.sheets[sheet_name]
data = dict()


# info = worksheet.used_range
# nrows = info.last_cell.row
# ncols = info.last_cell.column
#
# print("行高")
# print(nrows)
# print("列宽")
# print(ncols)


df = pd.read_excel('教师课程安排.xlsx'
                   ,sheet_name="Sheet2"
                   ,index_col=[0,1])

df.reset_index()
# print(df)

new_worksheet = workbook.sheets.add("输出")
new_worksheet['A1'].value = df
print(df)

# workbook.save()

value = workbook.sheets["输出"].range('A3').expand('table').value
for i in range(len(value)):
    # print(i)
    # print(value[i])
    date_name = value[i][1]
    # print(teacher_name)

    # print(date_name)
    if date_name not in data:
        data[date_name] = dict()

    teacher_name = value[i][0]
    if teacher_name not in data[date_name]:
        data[date_name][teacher_name] = []
    data[date_name][teacher_name].append(value[i])

pp = pprint.PrettyPrinter(compact=True)
pp.pprint(data)





workbook.sheets.add("教师课程安排-转置表")
i = 0
list = tablib.Dataset()

for key,value in data.items():
    print(key)
    list.append(("日期: " + key, None,None,None))
    list.append(('Time', 'Student',	'TA', 'Classrooms'))


    for key2, value2 in value.items():
        print(key2)
        list.append(('教师: ' + key2, None, None, None))
        for index in range(0, len(value2)):
            # print(value2[index][2:])
            # new_worksheet2.range('A' + str(i)).expand('table').value = value2[index][2:]
            # new_worksheet2[f'A{i}'].options(index = False).value = [1,32]
            # workbook.sheets['教师课程安排-转置表'].value = value2[index][2:]
            i = i+1
            tup = tuple(value2[index][2:])
            print(tup)
            list.append(tup)

        i = i+1
    # 空行
    list.append((None, None, None, None))


with open('教师课程安排-转置表.xlsx', 'wb') as f:#exl是二进制数据
    f.write(list.export('xlsx'))

# workbook.save()
workbook.close()

app.quit()