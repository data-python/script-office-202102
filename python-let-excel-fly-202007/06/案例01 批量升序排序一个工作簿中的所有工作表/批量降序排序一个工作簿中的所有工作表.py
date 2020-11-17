import xlwings as xw
import pandas as pd  
app = xw.App(visible = False, add_book = False)
workbook = app.books.open('产品销售统计表.xlsx')   
worksheet= workbook.sheets  
for i in worksheet: 
    values = i.range('A1').expand('table').options(pd.DataFrame).value  
    result = values.sort_values(by = '销售利润', ascending = False)  
    i.range('A1').value = result  
workbook.save() 
workbook.close()  
app.quit()