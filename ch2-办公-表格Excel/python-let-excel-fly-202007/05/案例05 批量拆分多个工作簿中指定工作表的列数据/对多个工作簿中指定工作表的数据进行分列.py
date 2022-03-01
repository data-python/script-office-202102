import os
import xlwings as xw
import pandas as pd
file_path = '产品记录表'
file_list = os.listdir(file_path)
app = xw.App(visible = False, add_book = False)
for i in file_list:
    if i.startswith('~$'):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    worksheet = workbook.sheets['规格表'] 
    values = worksheet.range('A1').options(pd.DataFrame, header = 1, index = False, expand = 'table').value 
    new_values = values['规格'].str.split('*', expand = True) 
    values['长(mm)'] = new_values[0] 
    values['宽(mm)'] = new_values[1] 
    values['高(mm)'] = new_values[2] 
    values.drop(columns =['规格'], inplace = True) 
    worksheet['A1'].options(index = False).value = values 
    worksheet.autofit() 
    workbook.save()
    workbook.close()
app.quit()
