import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('销售业绩表.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['月份']
y = df['销售额']
plt.bar(x, y, color = 'red', label = '销售额')
plt.legend(loc = 'upper left', fontsize = 20)
plt.show()
