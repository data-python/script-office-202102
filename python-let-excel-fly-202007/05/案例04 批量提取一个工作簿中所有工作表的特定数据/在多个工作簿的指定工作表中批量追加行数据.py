import os
import xlwings as xw
newContent = [['双肩包', '64', '110'], ['腰包', '23', '58']]
app = xw.apps.add()
file_path = '分部信息'  
file_list = os.listdir(file_path)  
for i in file_list:  
    if os.path.splitext(i)[1] == '.xlsx':  
        workbook = app.books.open(file_path + '\\' + i)  
        worksheet = workbook.sheets['产品分类表']
        values = worksheet.range('A1').expand()
        number = values.shape[0]  
        worksheet.range(number + 1, 1).value = newContent  
        workbook.save()
        workbook.close()
app.quit()
