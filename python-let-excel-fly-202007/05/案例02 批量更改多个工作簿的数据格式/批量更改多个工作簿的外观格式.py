import os
import xlwings as xw
file_path = '销售表'
file_list = os.listdir(file_path)
app = xw.App(visible = False, add_book = False)
for i in file_list:
    if i.startswith('~$'):
        continue
    file_paths = os.path.join(file_path, i)
    workbook = app.books.open(file_paths)
    for j in workbook.sheets: 
        j['A1:H1'].api.Font.Name = '宋体'  
        j['A1:H1'].api.Font.Size = 10  
        j['A1:H1'].api.Font.Bold = True		 
        j['A1:H1'].api.Font.Color = xw.utils.rgb_to_int((255,255,255))  
        j['A1:H1'].color = xw.utils.rgb_to_int((0,0,0))  
        j['A1:H1'].api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter  
        j['A1:H1'].api.VerticalAlignment = xw.constants.VAlign.xlVAlignCenter  
        j['A2'].expand('table').api.Font.Name = '宋体'  
        j['A2'].expand('table').api.Font.Size = 10  
        j['A2'].expand('table').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignLeft 
        j['A2'].expand('table').api.VerticalAlignment = xw.constants.VAlign.xlVAlignCenter   
        for cell in j['A1'].expand('table'):  
            for b in range(7,12): 
                cell.api.Borders(b).LineStyle = 1  
                cell.api.Borders(b).Weight = 2   
    workbook.save()
    workbook.close()
app.quit()
