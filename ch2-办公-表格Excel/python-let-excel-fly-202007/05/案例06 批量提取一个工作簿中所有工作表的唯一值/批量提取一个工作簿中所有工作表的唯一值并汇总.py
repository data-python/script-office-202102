import os
import xlwings as xw
app = xw.App(visible = True, add_book = False)
wb = app.books.open('上半年销售统计表.xlsx')
data = list()
for i, sht in enumerate(wb.sheets):
    values = sht['A2'].expand('table').value
    data = data + values
sales = dict()
for i in range(len(data)):
    name = data[i][0]
    sale = data[i][1]
    if name not in sales:
        sales[name] = sale
    else:
        sales[name] += sale
dictlist = list()
for key, value in sales.items():
    temp = [key, value]
    dictlist.append(temp)
dictlist.insert(0, ['书名', '销量'])
new_workbook = xw.books.add()
new_worksheet = new_workbook.sheets.add('销售统计')
new_worksheet['A1'].value = dictlist
new_worksheet.autofit()
new_workbook.save('销售统计.xlsx')
wb.close()
app.quit()
