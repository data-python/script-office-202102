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


for file in getFiles("f:/workspace-note/note-web/edu/", '.md'):  # =>查找以.md结尾的文件
    file_name = get_file_name(file).replace("@nice", "").replace("@vip", "")
    if not file.find("README") > -1:
        cont = "[专题]"
        file_name = "# " + (cont if not file_name.find("[") > -1 else "") + file_name[3:]
        # print(file_name)

        with open(file, 'r+', encoding='utf-8') as f:
            a = f.readlines()
            if not [c.strip().find("[") for c in a]:
                # print(get_file_name(file))
                f.write(file_name)

