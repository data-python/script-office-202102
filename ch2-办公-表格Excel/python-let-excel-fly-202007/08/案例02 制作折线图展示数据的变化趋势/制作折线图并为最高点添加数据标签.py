import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
df = pd.read_excel('月销售表.xlsx')
figure = plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['月份']
y = df['销售额']
plt.plot(x, y, color = 'red', linewidth = '3', linestyle = 'solid')
plt.title(label = '月销售额趋势图',fontdict = {'color' : 'black', 'size' : 30}, loc = 'center')
max1 = df['销售额'].max()
df_max = df[df['销售额'] == max1]
for a,b in zip(df_max['月份'], df_max['销售额']):
    plt.text(a, b + 0.05, (a, '%.0f' % b), ha = 'center', va = 'bottom', fontsize = 10)
plt.axis('off')
app = xw.App(visible = False)
workbook = app.books.open('月销售表.xlsx')
worksheet = workbook.sheets['Sheet1']
worksheet.pictures.add(figure, name = '图片1', update = True, left = 200)
workbook.save('显示最高点数据标签的折线图.xlsx')
workbook.close()
app.quit()
