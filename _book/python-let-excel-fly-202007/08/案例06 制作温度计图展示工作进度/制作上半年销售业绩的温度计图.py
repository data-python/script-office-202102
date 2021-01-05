import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('温度计图.xlsx')
sum = 0
for i in range(6):
    sum = df['销售业绩（万元）'][i] + sum  
goal = df['销售业绩（万元）'][13]  
percentage = sum / goal
plt.bar(1, 1, color = 'yellow')
plt.bar(1, percentage, color = 'cyan')
plt.xlim(0, 2)
plt.ylim(0, 1.2)
plt.text(1, percentage - 0.01, percentage, ha = 'center', va = 'top', fontdict = {'color' : 'black', 'size' : 20})
plt.show()
