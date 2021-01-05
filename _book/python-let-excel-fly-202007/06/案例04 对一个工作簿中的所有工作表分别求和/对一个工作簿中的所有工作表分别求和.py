import xlwings as xw
import pandas as pd
app = xw.App(visible = False, add_book = False)
workbook = app.books.open('采购表.xlsx')
worksheet = workbook.sheets
for i in worksheet:  
    values = i.range('A1').expand('table')
    data = values.options(pd.DataFrame).value 
    sums = data['采购金额'].sum()  
    column = values.value[0].index('采购金额') + 1  
    row = values.shape[0] 
    i.range(row + 1, column).value = sums  
workbook.save()
workbook.close()
app.quit()
