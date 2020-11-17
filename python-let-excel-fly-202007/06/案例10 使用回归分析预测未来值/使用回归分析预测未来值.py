import pandas as pd
from sklearn import linear_model
df = pd.read_excel('回归分析.xlsx', header = None)
df = df[2:]
df.columns = ['月份', '电视台广告费', '视频门户广告费', '汽车当月销售额']
x = df[['视频门户广告费', '电视台广告费']]
y = df['汽车当月销售额']
model = linear_model.LinearRegression()
model.fit(x, y)
R2 = model.score(x, y) 
print(R2)
