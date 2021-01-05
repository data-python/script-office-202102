import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('销售业绩表1.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x1 = df['月份']
y1 = df['销售额']
y2 = df['利润']
plt.plot(x1, y1, color = 'red', linewidth = 3, linestyle = 'solid')
plt.plot(x1, y2, color = 'black', linewidth = 3, linestyle = 'solid')
plt.show()