import os
import xlwings as xw
file_path = './销售表'
file_list = os.listdir(file_path)
sheet_name = '产品销售区域'
app = xw.App(visible = False, add_book = False)
for i in file_list:
    if i.startswith('~$'):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    sheet_names = [j.name for j in workbook.sheets]
    if sheet_name not in sheet_names:
        workbook.sheets.add(sheet_name)
        workbook.save()
app.quit()