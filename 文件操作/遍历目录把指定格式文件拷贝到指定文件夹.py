# https://www.cnblogs.com/lyccc123/p/11534831.html

import os
import shutil

# 传入需要遍历的根目录和需要复制到的区域
def copy_file(path, target_area):
    path_list = os.listdir(path)
    for new_path in path_list:
        new_path = os.path.join(path, new_path)

        if os.path.isdir(new_path):
            copy_file(new_path, target_area)
            # print("目录")

        elif os.path.isfile(new_path):
            Suffix_name = os.path.splitext(new_path)[1]

            if Suffix_name in [".bmp", ".gif", ".png", ".jpg", ".mp3"]:  # 指定文件后缀名，从而指定文件格式
                shutil.copy(new_path, target_area)

            # print("文件")
        else:
            print("there is sth wrong")

copy_file(
    "F:\dl-nut-yun\我的坚果云\[1-2]口语听力\旅游",
    "F:\dl-nut-yun\我的坚果云\[1-2]口语听力\旅游2")
