# https://blog.csdn.net/qq_41248959/article/details/110097464
# 报错 PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected. [pdf.py:1736]
# 但暂时不影响
from PyPDF2 import PdfFileReader as pdf_read

#每个书签的索引格式
#{'/Title': '书签名', '/Page': '指向的目标页数', '/Type': '类型'}

directory_str = ''

def bookmark_listhandler(list):
    global directory_str
    for message in list:
        if isinstance(message, dict):
            directory_str += "# " + message['/Title'] + '\n\n'
            # @todo 替换名称
            # message.__setitem__("/Title", str(message['/Title']).replace('广告文案', ''))
            # print(message['/Title'])
        else:
            bookmark_listhandler(message)

pdf_path = "D:\\dl-nut\\我的坚果云\\[7-6]xxxx\\yyyy-201108"
with open(pdf_path + '.pdf', 'rb') as f:
    pdf = pdf_read(f)
    #检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
    text_outline_list = pdf.getOutlines()
    bookmark_listhandler(text_outline_list)

with open(pdf_path + '.txt', 'w', encoding='utf-8') as f:
    f.write(directory_str)