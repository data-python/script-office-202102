import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
df = pd.read_excel('汽车速度和刹车距离表.xlsx')
figure = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['汽车速度（km/h）']
y = df['刹车距离（m）']
plt.scatter(x, y, s = 400, color = 'red', marker = 'o', edgecolor = 'black')
plt.xlabel('汽车速度(km/h)', fontdict = {'family' : 'Microsoft YaHei', 'color' : 'black', 'size' : 20}, labelpad = 20)
plt.ylabel('刹车距离(m)', fontdict = {'family' : 'Microsoft YaHei', 'color' : 'black', 'size' : 20}, labelpad = 20)
plt.title('汽车速度与刹车距离关系图', fontdict = {'family' : 'Microsoft YaHei', 'color' : 'black', 'size' : 30}, loc = 'center')
app = xw.App(visible = False)
workbook = app.books.open('汽车速度和刹车距离表.xlsx')
worksheet = workbook.sheets[0]
worksheet.pictures.add(figure, name = '图片1', update = True, left = 200)
workbook.save('散点图.xlsx')
workbook.close()
app.quit()
