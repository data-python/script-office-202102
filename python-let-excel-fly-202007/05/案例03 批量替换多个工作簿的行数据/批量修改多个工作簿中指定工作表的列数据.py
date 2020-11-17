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
    worksheet = workbook.sheets['产品分类表'] 
    value = worksheet['A2'].expand('table').value 
    for index, val in enumerate(value): 
        val[2] = val[2] * (1 + 0.05) 
        value[index] = val 
    worksheet['A2'].expand('table').value = value 
    workbook.save()
    workbook.close()
app.quit()
