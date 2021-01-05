import os  
import xlwings as xw  
import pandas as pd  
app = xw.App(visible = False, add_book = False) 
file_path = '销售表'  
file_list = os.listdir(file_path)  
for i in file_list: 
    if os.path.splitext(i)[1] == '.xlsx':  
        workbook = app.books.open(file_path + '\\' + i)  
        worksheet = workbook.sheets  
        for j in worksheet:    
            values = j.range('A1').expand('table').options(pd.DataFrame).value  
            values['销售利润'] = values['销售利润'].astype('float')
            result = values.groupby('销售区域').sum()
            j.range('J1').value = result['销售利润']
        workbook.save() 
        workbook.close()  
app.quit() 
