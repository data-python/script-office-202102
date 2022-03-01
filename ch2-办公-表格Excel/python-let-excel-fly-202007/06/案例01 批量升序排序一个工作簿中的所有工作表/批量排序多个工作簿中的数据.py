import os
import xlwings as xw
import pandas as pd  
app = xw.App(visible = False, add_book = False)
file_path = '产品销售统计表'
file_list = os.listdir(file_path)
for i in file_list:
    if os.path.splitext(i)[1] == '.xlsx':  
        workbook = app.books.open(file_path + '\\' + i)
        worksheet = workbook.sheets
        for j in worksheet:    
            values = j.range('A1').expand('table').options(pd.DataFrame).value  
            result = values.sort_values(by = '销售利润')  
            j.range('A1').value = result  
        workbook.save() 
        workbook.close()  
app.quit() 
