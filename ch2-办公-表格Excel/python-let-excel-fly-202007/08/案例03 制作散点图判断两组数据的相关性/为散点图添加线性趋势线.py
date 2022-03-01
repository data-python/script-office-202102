import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
from sklearn import linear_model
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
model = linear_model.LinearRegression().fit(x.values.reshape(-1,1), y)
pred = model.predict(x.values.reshape(-1,1))
plt.plot(x, pred,  color = 'black', linewidth = '3', linestyle = 'solid', label = '线性趋势线')
plt.legend(loc = 'upper left')
app = xw.App(visible = False)
workbook = app.books.open('汽车速度和刹车距离表.xlsx')
worksheet = workbook.sheets[0]
worksheet.pictures.add(figure, name = '图片1', update = True, left = 200)
workbook.save('为散点图添加线性趋势线.xlsx')
workbook.close()
app.quit()
