import os
file_path = 'e:\\table\\产品销售表' 
file_list = os.listdir(file_path)
old_book_name = '销售表'
new_book_name = '分部产品销售表'
for i in file_list:
    if i.startswith('~$'):
        continue
    new_file = i.replace(old_book_name, new_book_name)
    old_file_path = os.path.join(file_path, i)
    new_file_path = os.path.join(file_path, new_file)
    os.rename(old_file_path, new_file_path)
