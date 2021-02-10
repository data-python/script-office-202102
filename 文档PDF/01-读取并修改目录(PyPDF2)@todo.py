# https://blog.csdn.net/qq_41248959/article/details/110097464
from PyPDF2 import PdfFileReader as pdf_read

#每个书签的索引格式
#{'/Title': '书签名', '/Page': '指向的目标页数', '/Type': '类型'}

directory_str = ''

def bookmark_listhandler(list):
    global directory_str
    for message in list:
        if isinstance(message, dict):
            directory_str += message['/Title'] + '\n'
            # @todo 替换名称
            # message.__setitem__("/Title", str(message['/Title']).replace('广告文案', ''))
            # print(message['/Title'])
        else:
            bookmark_listhandler(message)

with open('D:\\dl-nut\\我的坚果云\\[7-9]职业规划\\xxx@readonly.pdf', 'rb') as f:
    pdf = pdf_read(f)
    #检索文档中存在的文本大纲,返回的对象是一个嵌套的列表
    text_outline_list = pdf.getOutlines()
    bookmark_listhandler(text_outline_list)

with open('D:\\dl-nut\\我的坚果云\\[7-9]职业规划\\xxx@readonly.txt', 'w', encoding='utf-8') as f:
    f.write(directory_str)