import winsound
import os
import pathlib
import time
import threading
import _thread
from tkinter import *

import threading
 
TIME_PER_MINUTE = 1

filepath = time.strftime('%Y-%m-%d') + '.log'
standard_class_time = 3
standard_rest_time = 4
is_resting = 0


def is_ok():
    if not os.path.exists('generator'):
        os.makedirs("generator") 
    if not os.path.exists('data'):
        os.makedirs("data") 
    if not os.path.exists('saying'):
        os.makedirs("saying") 

def touch_file():
    str  = filepath
    if not os.path.exists('data/'+str):
        pathlib.Path('data/'+str).touch()
        pathlib.Path('saying/'+str).touch()

def write_to_file(bas,dat):
    str  = filepath
    touch_file()
    with open(bas+'/'+str, 'a') as f:
        f.write(dat+"\n")

def play_music(filname):
    winsound.PlaySound(r""+filname,winsound.SND_FILENAME)

def getInput(title, message):
    def return_callback(event):
        pass
        root.quit()
    def close_callback():
        pass
    root = Tk(className=title)
    root.wm_attributes('-topmost', 1)
    screenwidth, screenheight = root.maxsize()
    width = 300
    height = 100
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)
    root.resizable(0, 0)
    lable = Label(root, height=2)
    lable['text'] = message
    lable.pack()
    entry = Entry(root)
    entry.bind('<Return>', return_callback)
    entry.pack()
    entry.focus_set()
    root.protocol("WM_DELETE_WINDOW", close_callback)
    root.mainloop()
    str = entry.get()
    root.destroy()
    return str
touch_file()
i = len(open("data/"+filepath,'r').readlines())
def countdown():
    current_time = 0
    while(1):
        while(not is_resting):
            global i
            i= i+1
            start = time.strftime('%H:%M:%S')
            print("正在进行第"+str(i)+"节课, 开始于"+start+".")
            _thread.start_new_thread( play_music,("D:\\music\\QQ\\aaa.wav",) )


            while (current_time <= standard_class_time):
                current_time  = current_time +1
                time.sleep(1*TIME_PER_MINUTE)
            current_time=0
            _thread.start_new_thread( play_music,("D:\\music\\QQ\\xk.wav",) )
            desc = getInput("本节结束","")
            end = time.strftime('%H:%M:%S')
            write_to_file(
                "data","第"+str(i)+"节"+"["+start + "-->" + end+"] " + desc
            )
            print(desc)
            print("结束于"+end+".")

            while (current_time <= standard_rest_time):
                current_time  = current_time +1
                time.sleep(1*TIME_PER_MINUTE)
            current_time = 0
            print("===========")

t = threading.Thread(target=countdown,daemon=True)



def configure_input(str):
    a = str.split(" ")
    if(a[0]=='c'):
        
        global standard_class_time
        standard_class_time = int(a[1])
        print(">> 工作时间已经更改为"+a[1])

    elif(a[0]=='r'):
        global standard_rest_time
        standard_rest_time = int(a[1])
        print(">> 休息时间已经更改为"+a[1])

    elif(a[0]=='b'):
        global is_resting
        is_resting = 1
        print(">> 停止循环. 将在休息完成之后结束循环.")

    elif(a[0]=='ub'):
        is_resting = 0
        print(">> 准备继续循环.")
    else:
        print("[帮助] \nc 更改上课时间到(分钟); \nr 更改休息时间到(分钟); \nb 停止循环; \nub 继续循环")
    




print("每日一言, 说点什么吧! ")
is_ok()
reason = input()
t.start()

write_to_file("saying",reason)


while(True):
    a = input()
    configure_input(a)
