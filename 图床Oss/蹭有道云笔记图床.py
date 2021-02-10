# https://github.com/DescartesM/UsefulPythonScript/blob/master/PictureBed.py
from tkinter import *
import keyboard
import pyperclip
import json
import re
import requests


def converUrl(url):
    reg = r'id=(.*?)&'
    s = re.search(reg, url)
    if s is not None:
        url = "http://note.youdao.com/yws/public/note/%s?editorType=0&cstk=orBX-yw0" % s.group()[3:-1]
        return url
    else:
        return None


def getHtml(url):
    r = requests.get(url=url)
    # print(r.status_code)
    # print(r.text)
    return r.text;


def getImageUrls(url):
    html = getHtml(url)
    try:
        js = json.loads(html)
        ss = js["content"]
    except Exception:
        return None
    reg = r'src="(.*?)"'
    pattern = re.compile(reg)
    ret = re.findall(pattern, ss)
    return ret


class MainWindow:
    def button_ok_listener(self, event):
        url = self.text_name.get('1.0', END)
        url = converUrl(url)
        list = getImageUrls(url)
        if list is not None:
            self.text_sex.delete('1.0', END)
            self.text_sex.insert(INSERT, list[-1:])
            pyperclip.copy("".join(list[-1:]))

    def button_save_listener(self, event):
        url = self.text_name.get('1.0', END)
        dict = {"LastUrl": url}
        '''
        updateConfig(dict)
        '''

    def Listener(self):
        url = self.text_name.get('1.0', END)
        url = converUrl(url)
        list = getImageUrls(url)
        if list is not None:
            self.text_sex.delete('1.0', END)
            self.text_sex.insert(INSERT, list[-1:])
            pyperclip.copy("".join(list[-1:]))

    def __init__(self):
        self.frame = Tk()

        self.label_name = Label(self.frame, text="youdao_url:")
        self.label_sex = Label(self.frame, text="image_url:")

        self.text_name = Text(self.frame, height="1", width=30)
        '''
        if getRecURL() is not None:
            self.text_name.insert("1.0", getRecURL())
        '''
        self.text_name.insert("1.0",
                              "http://note.youdao.com/noteshare?id=64555904ce9f98d61db1e5e07f91564c&sub=24810946B5AF400F887A6A0F50F2B75F")

        self.text_sex = Text(self.frame, height="1", width=30)

        self.label_name.grid(row=0, column=0)
        self.label_sex.grid(row=1, column=0)

        self.button_save = Button(self.frame, text="save", width=10)
        self.button_ok = Button(self.frame, text="ok", width=10)

        self.text_name.grid(row=0, column=1)
        self.text_sex.grid(row=1, column=1)

        self.button_save.grid(row=0, column=2, padx=10)
        self.button_ok.grid(row=1, column=2, padx=10)

        self.button_ok.bind("<ButtonRelease-1>", self.button_ok_listener)
        self.button_save.bind("<ButtonRelease-1>", self.button_save_listener)
        keyboard.add_hotkey('ctrl+shift+a', self.Listener)
        self.frame.mainloop()


frame = MainWindow()
