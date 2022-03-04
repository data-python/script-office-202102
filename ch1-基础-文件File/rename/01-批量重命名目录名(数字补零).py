# -*- coding:utf-8 -*- 
from encodings import utf_8
import os
import re
import sys

from sqlalchemy import null  # 导入模块


def add_prefix_subfolders():  # 定义函数名称
    mark = 'test-'  # 准备添加的前缀内容
    old_names = os.listdir(path)  # 取路径下的文件名，生成列表

    for old_name in old_names:  # 遍历列表下的文件名
        if old_name != sys.argv[0]:  # 代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名

            dir_name = os.path.join(path, old_name)
            if os.path.isdir(dir_name):

                after_name = old_name.replace("代码", "").replace("文章", "ch")
                
                nums = re.findall('\d+', old_name)
                if nums != null:
                    for num in nums:
                        after_name = after_name.replace(num, str(num).zfill(2))

                os.rename(dir_name, os.path.join(path, after_name))  # 子文件夹重命名

                print(
                    old_name, "has been renamed successfully! New name is: ", after_name)


if __name__ == '__main__':
    path = r'E:\workspace-laurel\geekbang-oa-practice-202102'  # 运行程序前，记得修改主文件夹路径！
    add_prefix_subfolders()  # 调用定义的函数
