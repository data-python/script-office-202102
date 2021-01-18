# https://segmentfault.com/a/1190000018597501
import pprint

import tablib
import xlwings as xw
import pandas as pd



# 1) 打开Excel
file_path = './教师课程安排.xlsx'
sheet_name = 'Sheet2'
app = xw.App(visible = True, add_book = False)
workbook = app.books.open(file_path)
worksheet = workbook.sheets[sheet_name]

# info = worksheet.used_range
# nrows = info.last_cell.row
# ncols = info.last_cell.column

# 2) 使用pandas读取数据与索引
data = dict()
df = pd.read_excel('教师课程安排.xlsx'
                   ,sheet_name="Sheet2"
                   ,index_col=[0,1])
df.reset_index()
# print(df)

# 将数据重构后输出到工作表
new_worksheet = workbook.sheets.add("输出")
new_worksheet['A1'].value = df
print(df)


# 3) 遍历数据, 按照日期+教师名称构建嵌套字典
value = workbook.sheets["输出"].range('A3').expand('table').value
for i in range(len(value)):
    date_name = value[i][1]
    # 如果没有这个键值, 初始化为字典
    if date_name not in data:
        data[date_name] = dict()

    teacher_name = value[i][0]
    # 如果没有这个键值, 初始化为数组
    if teacher_name not in data[date_name]:
        data[date_name][teacher_name] = []
    data[date_name][teacher_name].append(value[i])

# 格式化输出得到的嵌套字典
pp = pprint.PrettyPrinter(compact=True)
pp.pprint(data)

# 4) 用tablib临时输出Excel
list = tablib.Dataset()
for key,value in data.items():
    print(key)
    list.append(("日期: " + key, None,None,None))
    # 加入表头
    list.append(('Time', 'Student',	'TA', 'Classrooms'))

    for key2, value2 in value.items():
        print(key2)
        list.append(('教师: ' + key2, None, None, None))
        for index in range(0, len(value2)):
            # @todo xlwings目前导出一直会报错，先使用tablib临时输出Excel
            # print(value2[index][2:])
            # new_worksheet2.range('A' + str(i)).expand('table').value = value2[index][2:]
            # new_worksheet2[f'A{i}'].options(index = False).value = [1,32]
            # workbook.sheets['教师课程安排-转置表'].value = value2[index][2:]
            tup = tuple(value2[index][2:])
            print(tup)
            list.append(tup)

    # 加一行空行
    list.append((None, None, None, None))


# 输出excel
with open('教师课程安排-转置表.xlsx', 'wb') as f: #exl是二进制数据
    f.write(list.export('xlsx'))

# 保存与关闭
# workbook.save()
workbook.close()

# 退出
app.quit()