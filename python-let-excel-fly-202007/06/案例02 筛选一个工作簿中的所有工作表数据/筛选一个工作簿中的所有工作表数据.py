import xlwings as xw
import pandas as pd
app = xw.App(visible = False, add_book = False)
workbook = app.books.open('采购表.xlsx')
worksheet = workbook.sheets
table = pd.DataFrame() 
for i, j in enumerate(worksheet): 
    values = j.range('A1').options(pd.DataFrame, header=1, index=False, expand='table').value 
    data = values.reindex(columns=['采购物品', '采购日期', '采购数量', '采购金额'])
    table = table.append(data, ignore_index = True)
table = table.groupby('采购物品')
new_workbook = xw.books.add() 
for idx, group in table:
    new_worksheet = new_workbook.sheets.add(idx) 
    new_worksheet['A1'].options(index = False).value = group 
    last_cell = new_worksheet['A1'].expand('table').last_cell 
    last_row = last_cell.row 
    last_column = last_cell.column 
    last_column_letter = chr(64 + last_column) 
    sum_cell_name = '{}{}'.format(last_column_letter, last_row+1) 
    sum_last_row_name = '{}{}'.format(last_column_letter, last_row) 
    formula = '=SUM({}2:{})'.format(last_column_letter, sum_last_row_name)
    new_worksheet[sum_cell_name].formula = formula 
    new_worksheet.autofit() 
new_workbook.save('采购分类表.xlsx')
workbook.close()
app.quit()
