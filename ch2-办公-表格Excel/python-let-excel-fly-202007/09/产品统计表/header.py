import xlwings as xw
def header():
    workbook = xw.Book.caller()
    worksheet = workbook.sheets[0]
    i = worksheet.range('F100').value
    sheet = workbook.sheets[i]
    sheet.range('A1').value = '单号'
    sheet.range('B1').value = '产品名称'
    sheet.range('C1').value = '成本价(元/个)'
    sheet.range('D1').value = '销售价(元/个)'
    sheet.range('E1').value = '销售数量(个)'
