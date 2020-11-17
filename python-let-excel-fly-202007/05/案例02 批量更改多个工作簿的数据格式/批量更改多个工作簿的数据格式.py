import os
import xlwings as xw
file_path = '采购表'
file_list = os.listdir(file_path)
app = xw.App(visible = False, add_book = False)
for i in file_list:
    if i.startswith('~$'):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    for j in workbook.sheets: 
        row_num = j['A1'].current_region.last_cell.row
        j['A2:A{}'.format(row_num)].number_format = 'm/d'
        j['D2:D{}'.format(row_num)].number_format = '¥#,##0.00'
    workbook.save()
    workbook.close()
app.quit()