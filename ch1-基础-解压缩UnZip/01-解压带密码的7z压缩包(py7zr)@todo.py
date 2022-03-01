# https://blog.csdn.net/erha11/article/details/108322833
from _lzma import LZMAError

import py7zr
import os
import re
import os.path

# 压缩包来源目录
source = 'D:\\dl-novel'
# 解压到（地址自行补充）
target_dir = 'D:\\dl-nut\\我的坚果云\\[8-5]小说\\解压缩'


def getFiles(dir, suffix):  # 查找根目录，文件后缀
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name, suf = os.path.splitext(filename)  # =>文件名,文件后缀
            if suf == suffix:
                res.append(os.path.join(root, filename))  # =>吧一串字符串组合成路径
    return res


def get_file_name(path_string):
    """获取文件名称"""
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    data = pattern.findall(path_string)
    if data:
        return data[0]


# files = os.listdir(source)
files = getFiles(source, '.7z')

for f in files:
    target = target_dir + os.sep + f.split("\\")[3]
    print("保存在" + ' ' + target)
    with py7zr.SevenZipFile(f, mode='r', password='xxxyyy') as z:
        z.extractall(target)
        print("保存在" + ' ' + target)


# fileSubfix = ['jpg', 'png', 'ilk', 'exp']
# for parent, dirnames, filenames in os.walk(target):
#     for filename in filenames:
#         delfile = os.path.join(parent, filename)
#
#         if os.path.splitext(filename)[1][1:] in fileSubfix:
#             print('删除:' + delfile)
#             os.remove(delfile)
