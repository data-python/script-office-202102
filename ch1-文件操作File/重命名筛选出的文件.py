import os
import re


def get_file_name(path_string):
    """获取文件名称"""
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    data = pattern.findall(path_string)
    if data:
        return data[0]


def getFiles(dir, suffix):  # 查找根目录，文件后缀
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name, suf = os.path.splitext(filename)  # =>文件名,文件后缀
            if suf == suffix:
                res.append(os.path.join(root, filename))  # =>吧一串字符串组合成路径
    return res


for file in getFiles("f:/workspace-note/note-web/planb/", '.md'):  # =>查找以.md结尾的文件
    file_name = get_file_name(file)
    if not file.find("README") > -1:
        # print(file_name)
        if not file_name.find("@nice") > -1:
            print(file_name)
            os.rename(file, file[:-3] + "@nice.md")
