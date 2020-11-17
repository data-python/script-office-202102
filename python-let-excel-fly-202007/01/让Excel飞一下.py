import xlwings as xw
app = xw.App(visible = True, add_book = False)
for i in range(1, 21):
    workbook = app.books.add()
    workbook.save(f'e:\\example\\01\\员工信息表\\分公司{i}.xlsx')
    workbook.close()
app.quit()