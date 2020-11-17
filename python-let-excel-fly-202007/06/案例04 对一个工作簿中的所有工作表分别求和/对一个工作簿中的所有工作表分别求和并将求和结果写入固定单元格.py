import xlwings as xw
import pandas as pd
app = xw.App(visible = False, add_book = False)
workbook = app.books.open('采购表.xlsx')
worksheet = workbook.sheets
for i in worksheet:  
    values = i.range('A1').expand('table').options(pd.DataFrame).value
    sums = values['采购金额'].sum()
    i.range('F1').value = sums
workbook.save()
workbook.close()
app.quit()