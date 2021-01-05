import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('销售业绩表1.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['月份']
y1 = df['销售额']
y2 = df['利润']
plt.plot(x, y1, color = 'black', linewidth = 4)
plt.bar(x, y2, color = 'blue')
plt.show()
