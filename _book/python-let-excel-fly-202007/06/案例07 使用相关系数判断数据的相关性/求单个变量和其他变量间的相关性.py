import pandas as pd
df = pd.read_excel('相关性分析.xlsx', index_col = '代理商编号')
result = df.corr()['年销售额（万元）']
print(result)
