import xlwings as xw
def table():
    workbook = xw.books.open('F:\产品统计表.xlsm')
    worksheet = workbook.sheets['统计表']
    value = worksheet.range('A2').expand('table').value
    data = dict()
    for i in range(len(value)):
        product_name = value[i][1]
        if product_name not in data:
            data[product_name] = []
        data[product_name].append(value[i])
    for key,value in data.items():
        new_workbook = xw.books.add()
        new_worksheet = new_workbook.sheets.add(key)
        new_worksheet['A1'].value = worksheet['A1:H1'].value
        new_worksheet['A2'].value = value
        new_workbook.save('F:\{}.xlsx'.format(key))
