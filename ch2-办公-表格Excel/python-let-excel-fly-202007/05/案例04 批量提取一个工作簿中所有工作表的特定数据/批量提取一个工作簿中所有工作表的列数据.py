import xlwings as xw
import pandas as pd
app = xw.App(visible = False, add_book = False) 
workbook = app.books.open('采购表.xlsx')
worksheet = workbook.sheets 
column = ['采购日期', '采购金额']
data = []
for i in worksheet:
    values = i.range('A1').expand().options(pd.DataFrame, index = False).value
    filtered = values[column]  
    data.append(filtered)
new_workbook = xw.books.add()  
new_worksheet = new_workbook.sheets.add('提取数据') 
new_worksheet.range('A1').value = pd.concat(data, ignore_index = False).set_index(column[0])
new_workbook.save('提取表.xlsx') 
workbook.close()
app.quit()
