import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
df = pd.read_excel('销售业绩表.xlsx')
figure = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['月份']
y = df['销售额']
plt.bar(x, y, color = 'black')
app = xw.App(visible = False)
workbook = app.books.open('销售业绩表.xlsx')
worksheet = workbook.sheets['销售业绩']
worksheet.pictures.add(figure, left = 500)
workbook.save()
workbook.close()
app.quit()
