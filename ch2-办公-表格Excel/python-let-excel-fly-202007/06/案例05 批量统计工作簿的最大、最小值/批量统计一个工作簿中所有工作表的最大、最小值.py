import xlwings as xw  
import pandas as pd 
app = xw.App(visible = False, add_book = False)
workbook = xw.Book('产品销售统计表.xlsx')  
worksheet = workbook.sheets 
for i in worksheet:  
    values = i.range('A1').expand('table').options(pd.DataFrame).value  
    max = values['销售利润'].max()  
    min = values['销售利润'].min()  
    i.range('I1').value = '最大销售利润'  
    i.range('J1').value = max  
    i.range('I2').value = '最小销售利润'  
    i.range('J2').value = min
workbook.save()
workbook.close()
app.quit()
