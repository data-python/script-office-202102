import os
import xlwings as xw
app = xw.App(visible = False, add_book = False)
file_path = './销售表1'
file_list = os.listdir(file_path)  
workbook = app.books.open('./新增产品表.xlsx')
worksheet = workbook.sheets['新增产品']
value = worksheet.range('A1').expand('table')
start_cell = (2, 1)
end_cell = (value.shape[0], value.shape[1])
cell_area = worksheet.range(start_cell, end_cell).value
for i in file_list:  
    if os.path.splitext(i)[1] == '.xlsx': 
        try:
            workbooks = xw.Book(file_path + '\\' + i)  
            sheet = workbooks.sheets['产品分类表']
            scope = sheet.range('A1').expand()
            sheet.range(scope.shape[0] + 1, 1).value = cell_area
            workbooks.save()
        finally:
            workbooks.close()  
workbook.close()
app.quit()
