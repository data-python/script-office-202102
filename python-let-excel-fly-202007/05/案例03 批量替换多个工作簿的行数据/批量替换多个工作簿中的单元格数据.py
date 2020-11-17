import os
import xlwings as xw
file_path = '分部信息'
file_list = os.listdir(file_path)
app = xw.App(visible = False, add_book = False)
for i in file_list:
    if i.startswith('~$'):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    for j in workbook.sheets: 
        value = j['A2'].expand('table').value 
        for index, val in enumerate(value): 
            if val[0] == '背包': 
                val[0] = '双肩包' 
                value[index] = val 
        j['A2'].expand('table').value = value 
    workbook.save()
    workbook.close()
app.quit()
