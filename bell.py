import winsound
import os
import pathlib
import time
import _thread
filepath = time.strftime('%Y-%m-%d') + '.log'


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

touch_file()
i = len(open("data/"+filepath,'r').readlines())
print("每日一言, 说点什么吧! ")
is_ok()
reason = input()

write_to_file("saying",reason)

while True:
    touch_file()
    print("cycle = " + str(i))
    i = i+1
    start = time.strftime('%H:%M:%S')
    _thread.start_new_thread( play_music,("D:\\music\\QQ\\aaa.wav",) )
    print("Start from"+start)
    time.sleep(40*60)
    _thread.start_new_thread( play_music,("D:\\music\\QQ\\xk.wav",) )
    
    desc = input()
    end = time.strftime('%H:%M:%S')
    write_to_file(
        "data","第"+str(i)+"节"+"["+start + "-->" + end+"] " + desc
    )
    print("End at"+end)
    time.sleep(10*60)
    print("===========")
