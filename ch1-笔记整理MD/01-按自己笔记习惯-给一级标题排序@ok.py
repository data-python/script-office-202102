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
        self.content = self.content.replace("---", "")
        sharp1 = self.content.split('#')
        del(sharp1[0]) # 移除第一个空元素

        for i in sharp1:
            i = i.lstrip(" ")
            key = i[0:2]
            if key in self.data.keys():
                self.data[key].append('# '+i.strip('\n').lstrip(" "))
            else:
                self.data[key] = ['# ' + i.strip('\n').lstrip(" ")]

        # print(self.data)
        # self.title = self.data
        # del(self.data[0])
        # self.data.sort()
        # self.data['sharp1'].insert(0, title) # 标题部分拿到最前面
        # print(self.data)

    def save2file(self, name):
        s2 = self.title
        for key in self.data:
            self.data[key].sort()
            self.data[key].append("---")
            s2 = s2 + "\n\n" + "\n\n".join(self.data[key])
        print(s2)
        BaseMethod.write_file(name, s2)

f="F:\\workspace-note\\note-web\\arch\[1-1]course\\2021\\srv\\03-[调查]xxx-2021@vip"

def main():
    md = SortMD(f + ".md")
    md.split_now()
    md.save2file(f + "-output.md")

if __name__ == "__main__":
    main()
