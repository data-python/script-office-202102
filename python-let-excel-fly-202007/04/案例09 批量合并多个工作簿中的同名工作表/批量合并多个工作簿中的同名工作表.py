import os
import xlwings as xw
file_path = 'e:\\table\\销售统计'
file_list = os.listdir(file_path)
sheet_name = '产品销售统计'
app = xw.App(visible = False, add_book = False)
header = None
all_data = []
for i in file_list:
    if i.startswith('~$'):
        continue   
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    for j in workbook.sheets:
        if j.name == sheet_name:
            if header == None:
                header = j['A1:I1'].value
            values = j['A2'].expand('table').value
            all_data = all_data + values
new_workbook = xw.Book()
new_worksheet = new_workbook.sheets.add(sheet_name)   
new_worksheet['A1'].value = header
new_worksheet['A2'].value = all_data
new_worksheet.autofit()
new_workbook.save('e:\\table\\上半年产品销售统计表.xlsx')
app.quit()