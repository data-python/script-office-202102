import xlwings as xw
import pandas as pd
app = xw.App(visible = False, add_book = False)
workbook = app.books.open('采购表.xlsx')
worksheet = workbook.sheets
table = pd.DataFrame() 
for i, j in enumerate(worksheet): 
    values = j.range('A1').options(pd.DataFrame, header = 1, index = False, expand = 'table').value 
    data = values.reindex(columns = ['采购物品', '采购日期', '采购数量', '采购金额'])
    table = table.append(data, ignore_index = True) 
product = table[table['采购物品'] == '保险箱'] 
new_workbook = xw.books.add() 
new_worksheet = new_workbook.sheets.add('保险箱') 
new_worksheet['A1'].options(index = False).value = product 
new_worksheet.autofit() 
new_workbook.save('保险箱.xlsx')
workbook.close()
app.quit()
