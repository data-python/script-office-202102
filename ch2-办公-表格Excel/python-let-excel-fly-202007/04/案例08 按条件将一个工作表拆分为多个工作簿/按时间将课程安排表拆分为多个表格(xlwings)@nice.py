# https://www.kancloud.cn/gnefnuy/xlwings-docs/1127455
# https://segmentfault.com/a/1190000018597501
# https://blog.csdn.net/LaoYuanPython/article/details/107131574
import pprint
import pandas as pd
import xlwings as xw

# 1) 打开Excel
file_path = './教师课程安排.xlsx'
sheet_name = 'Sheet2'
app = xw.App(visible=True, add_book=False)
# app.display_alerts = True
# app.screen_updating = True

workbook = app.books.open(file_path)
origin_worksheet = workbook.sheets[sheet_name]

# info = origin_worksheet.used_range
# nrows = info.last_cell.row
# ncols = info.last_cell.column

# 2) 使用pandas读取数据与索引
data = dict()
df = pd.read_excel('教师课程安排.xlsx'
                   , sheet_name="Sheet2"
                   , index_col=[0, 1])
df.reset_index()
print(df)

# 将数据重构后输出到工作表
temp_worksheet = workbook.sheets.add("中间数据表")
temp_worksheet['A1'].value = df

output_worksheet = workbook.sheets.add("输出结果表")

# 3) 遍历数据, 按照日期+教师名称构建嵌套字典
value = temp_worksheet.range('A3').expand('table').value
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

# 4) 输出Excel
i = 1
for key, value in data.items():
    # print(key)
    output_worksheet[f'A{i}'].value = ["日期: " + key, None, None, None]
    output_worksheet[f'A{i}'].color = (120, 56, 30)
    i = i + 1

    # 加入表头
    output_worksheet[f'A{i}'].value = ['Time', 'Student', 'TA', 'Classrooms']
    output_worksheet[f'A{i}'].color = (120, 86, 30)
    i = i + 1

    for key2, value2 in value.items():
        # print(key2)
        # output_worksheet[f'A{i}'].column_width = 4
        # xw.Range(f'A{i}:A{i+3}').api.merge()
        output_worksheet[f'A{i}'].value = ['教师: ' + key2, None, None, None]
        output_worksheet[f'A{i}'].color = (220, 156, 30)
        i = i + 1

        for index in range(0, len(value2)):
            # print(value2[index][2:])
            output_worksheet[f'A{i}'].value = value2[index][2:]
            i = i + 1

    i = i + 1

# 保存与关闭
# workbook.save()
# workbook.close()
# 退出
# app.quit()