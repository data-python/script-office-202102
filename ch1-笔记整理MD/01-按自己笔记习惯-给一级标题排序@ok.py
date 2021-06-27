# 改编自 https://www.cnblogs.com/jkhere/p/10793100.html
import os
import subprocess

class BaseMethod:
    @staticmethod
    def run_cmd(cmd):
        retcode, output = subprocess.getstatusoutput(cmd)
        return retcode, output

    @staticmethod
    def write_file(filename, content):
        with open(filename, 'w', encoding='UTF-8')as tf:
            tf.write(content)

    @staticmethod
    def read_file(file_name, mode="r"):
        if not os.path.exists(file_name):
            raise IOError("No such file or directory: %s" % file_name)
        with open(file_name, mode, encoding='UTF-8')as fp:
            content = fp.read()
        return content


class SortMD:
    def __init__(self, filename):
        # self.filename = filename
        self.content = BaseMethod.read_file(filename)
        self.data = {}
        self.title = ""

    def split_now(self):
        sharp1 = self.content.split('#')
        del(sharp1[0]) # 移除第一个空元素

        for i in sharp1:
            if 'sharp1' in self.data.keys():
                self.data['sharp1'].append('# '+i.strip('\n').lstrip(" "))
            else:
                self.data['sharp1'] = ['# ' + i.strip('\n').lstrip(" ")]

        # print(self.data)
        self.title = self.data['sharp1'][0]
        del(self.data['sharp1'][0])
        self.data['sharp1'].sort()
        # self.data['sharp1'].insert(0, title) # 标题部分拿到最前面
        # print(self.data)

    def save2file(self, name):
        s2 = self.title + "\n\n" + "\n\n".join(self.data['sharp1'])
        data = s2
        print(data)
        BaseMethod.write_file(name, data)

f="F:\\workspace-note\\note-web\\arch\[1-1]course\\2021\\srv\\03-[调查]xxx-2021@vip"

def main():
    md = SortMD(f + ".md")
    md.split_now()
    md.save2file(f + ".md")

if __name__ == "__main__":
    main()
