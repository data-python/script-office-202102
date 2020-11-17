import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('销售业绩表.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = df['月份']
y = df['销售额']
plt.plot(x, y, color = 'black', linewidth = 3, linestyle = 'solid')
plt.grid(b = True, axis = 'y', color = 'red', linestyle = 'dashed', linewidth = 1)
plt.show()
