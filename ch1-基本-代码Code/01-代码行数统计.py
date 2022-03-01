# https://github.com/DescartesM/UsefulPythonScript/blob/master/CountingCodeLines.py
# coding=utf-8
import os
import time
# 设定根目录
basedir = 'F:\workspace-laurel\laurel-demo-office-practice\爬虫'
filelists = []
# 指定想要统计的文件类型
whitelist = ['py', 'cpp']

#遍历文件, 递归遍历文件夹中的所有
def getFile(basedir):
    global filelists
    for parent,dirnames,filenames in os.walk(basedir):
        for filename in filenames:
            ext = filename.split('.')[-1]
            #只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent,filename))
#统计一个的行数
def countLine(fname):
    count = 0
    # 把文件做二进制看待,read.
    for file_line in open(fname, 'rb').readlines():
        if file_line != '' and file_line != '\n': #过滤掉空行
            count += 1
    print (fname + '----' , count)
    return count

if __name__ == '__main__' :
    startTime = time.process_time()
    getFile(basedir)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print ('total lines:',totalline)
    print ('Done! Cost Time: %0.2f second' % (time.process_time() - startTime))