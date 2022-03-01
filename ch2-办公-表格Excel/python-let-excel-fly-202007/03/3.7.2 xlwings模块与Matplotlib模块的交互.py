import xlwings as xw
import matplotlib.pyplot as plt
figure = plt.figure()
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
app = xw.App(visible = False)
workbook = app.books.add()
worksheet = workbook.sheets.add('新工作表')
worksheet.pictures.add(figure, name = '图片1', update = True, left = 100)
workbook.save(r'e:\table.xlsx')
workbook.close()
app.quit()
