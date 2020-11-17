import xlwings as xw
app = xw.App(visible = False, add_book = False)
workbook = app.books.open('e:\\table\\采购表.xlsx')
for i in workbook.sheets:
    value = i.range('A1').expand('table')
    value.column_width = 12
    value.row_height = 20
workbook.save()
app.quit()