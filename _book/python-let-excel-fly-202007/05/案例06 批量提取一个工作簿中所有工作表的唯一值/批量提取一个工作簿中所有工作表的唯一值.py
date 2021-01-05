import xlwings as xw
app = xw.App(visible = True, add_book = False)
workbook = app.books.open('上半年销售统计表.xlsx')
data = []
for i, worksheet in enumerate(workbook.sheets):
    values = worksheet['A2'].expand('down').value
    data = data + values
data = list(set(data))
data.insert(0, '书名')
new_workbook = xw.books.add()
new_worksheet = new_workbook.sheets.add('书名')
new_worksheet['A1'].options(transpose = True).value = data
new_worksheet.autofit()
new_workbook.save('书名.xlsx')
workbook.close()
app.quit()