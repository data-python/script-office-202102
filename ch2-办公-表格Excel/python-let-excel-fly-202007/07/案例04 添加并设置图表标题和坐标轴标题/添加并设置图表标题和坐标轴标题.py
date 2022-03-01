import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('销售业绩表.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['月份']
y = df['销售额']
plt.bar(x, y, color = 'black')
plt.title(label = '各月销售额对比图', fontdict = {'family' : 'KaiTi', 'color' : 'red', 'size' : 30}, loc = 'left')
plt.xlabel('月份', fontdict = {'family' : 'SimSun', 'color' : 'black', 'size' : 20}, labelpad = 20)
plt.ylabel('销售额', fontdict = {'family' : 'SimSun', 'color' : 'black', 'size' : 20}, labelpad = 20)
plt.show()
