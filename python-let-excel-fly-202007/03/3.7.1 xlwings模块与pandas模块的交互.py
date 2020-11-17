import xlwings as xw
import pandas as pd
app = xw.App(visible = False)
workbook = app.books.add()
worksheet = workbook.sheets.add('新工作表')
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a', 'b'])
worksheet.range('A1').value = df
workbook.save(r'e:\table.xlsx')
workbook.close()
app.quit()
