import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import xlwings as xw
df = pd.read_excel('方差分析.xlsx')
df = df[['A型号','B型号','C型号','D型号','E型号']]
df_melt = df.melt()
df_melt.columns = ['Treat', 'Value']
df_describe = pd.DataFrame()  
df_describe['A型号'] = df['A型号'].describe()
df_describe['B型号'] = df['B型号'].describe()
df_describe['C型号'] = df['C型号'].describe()
df_describe['D型号'] = df['D型号'].describe()
df_describe['E型号'] = df['E型号'].describe()
model = ols('Value~C(Treat)', data = df_melt).fit()
anova_table = anova_lm(model, typ = 3)
app = xw.App(visible = False)
workbook = app.books.open('方差分析.xlsx')
worksheet = workbook.sheets['单因素方差分析']  
worksheet.range('H2').value = df_describe.T 
worksheet.range('H14').value = '方差分析'
worksheet.range('H15').value = anova_table
workbook.save()
workbook.close()
app.quit()