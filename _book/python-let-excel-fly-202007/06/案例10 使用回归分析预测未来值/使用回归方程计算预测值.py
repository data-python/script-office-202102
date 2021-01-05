import pandas as pd
from  sklearn import linear_model
df = pd.read_excel('回归分析.xlsx', header = None)
df = df[2:]
df.columns = ['月份', '电视台广告费', '视频门户广告费', '汽车当月销售额']
x = df[['视频门户广告费', '电视台广告费']]
y = df['汽车当月销售额']
model = linear_model.LinearRegression()
model.fit(x,y)
coef = model.coef_
model_intercept = model.intercept_
result = 'y={}*x1+{}*x2{}'.format(coef[0], coef[1], model_intercept)
print('线性回归方程为：', '\n', result)
a = 30
b = 20
y = coef[0] * a + coef[1] * b + model_intercept
print(y)
