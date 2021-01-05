import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('销售业绩表2.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['月份']
y1 = df['销售额']
y2 = df['同比增长']
plt.bar(x, y1, color = 'grey', label = '销售额')
plt.legend(loc = 'upper left', fontsize = 20)
plt.twinx()
plt.plot(x, y2, color = 'black', linewidth = 3, label = '同比增长')
plt.legend(loc = 'upper right', fontsize = 20)
plt.show()
