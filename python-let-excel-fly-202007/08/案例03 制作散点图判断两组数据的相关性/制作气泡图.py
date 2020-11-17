import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
df = pd.read_excel('气泡图.xlsx')
figure = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['销售量']
y = df['利润（万）']
z = df['产品名称']
plt.scatter(x, y, s = y * 100, color = 'red', marker = 'o')
plt.xlabel('销售量', fontdict = {'family' : 'Microsoft YaHei', 'color' : 'black', 'size' : 20}, labelpad = 20)
plt.ylabel('利润（万）', fontdict = {'family' : 'Microsoft YaHei', 'color' : 'black', 'size' : 20}, labelpad = 20)
plt.title('销售量与利润关系图', fontdict = {'family' : 'Microsoft YaHei', 'color' : 'black', 'size' : 30}, loc = 'center')
for a, b, c in zip(x, y, z):
    plt.text(a, b, c, ha = 'center', va = 'center', fontsize = 30, color = 'white')
plt.xlim(0, 800)
plt.ylim(0, 120)
app = xw.App(visible = False)
workbook = app.books.open('气泡图.xlsx')
worksheet = workbook.sheets[0]
worksheet.pictures.add(figure, name = '图片1', update = True, left = 200)
workbook.save('气泡图1.xlsx')
workbook.close()
app.quit()
