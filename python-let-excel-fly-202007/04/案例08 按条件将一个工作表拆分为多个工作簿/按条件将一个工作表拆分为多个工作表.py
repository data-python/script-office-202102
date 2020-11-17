import xlwings as xw
import pandas as pd
app = xw.App(visible = True, add_book = False)
workbook = app.books.open('e:\\table\\产品统计表.xlsx')
worksheet = workbook.sheets['统计表']
value = worksheet.range('A1').options(pd.DataFrame, header = 1, index = False, expand = 'table').value 
data = value.groupby('产品名称') 
for idx, group in data: 
    new_worksheet = workbook.sheets.add(idx) 
    new_worksheet['A1'].options(index = False).value = group 
workbook.save()
workbook.close()
app.quit()
