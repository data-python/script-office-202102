import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
df = pd.read_excel('方差分析.xlsx')
df = df[['A型号', 'B型号', 'C型号', 'D型号', 'E型号']]
figure = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
df.boxplot(grid = False)  
app = xw.App(visible = False)
workbook = app.books.open('方差分析.xlsx')
worksheet = workbook.sheets['单因素方差分析']  
worksheet.pictures.add(figure, name = '图片1', update = True, left = 500, top = 10)
workbook.save('箱形图.xlsx')
workbook.close()
app.quit()