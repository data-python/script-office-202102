import xlwings as xw
import pandas as pd
app = xw.App(visible = False, add_book = False) 
workbook = app.books.open('采购表.xlsx')  
worksheet = workbook.sheets
data = []
for i in worksheet:
    values = i.range('A1').expand().options(pd.DataFrame).value
    filtered = values[values['采购物品'] == '复印纸'] 
    if not filtered.empty: 
        data.append(filtered)
new_workbook = xw.books.add() 
new_worksheet = new_workbook.sheets.add('复印纸') 
new_worksheet.range('A1').value = pd.concat(data, ignore_index = False) 
new_workbook.save('复印纸.xlsx')
workbook.close()
app.quit()
