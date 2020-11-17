import xlwings as xw
workbook_name = 'e:\\table\\产品销售表.xlsx'  
app = xw.App(visible = False, add_book = False)
header = None    
all_data = []  
workbook = app.books.open(workbook_name)  
for i in workbook.sheets:
    workbook_split = app.books.add()   
    sheet_split = workbook_split.sheets[0]  
    i.api.Copy(Before = sheet_split.api)  
    workbook_split.save('{}'.format(i.name))  
app.quit()