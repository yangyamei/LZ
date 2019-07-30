# import easygui as g
# import os
# file_path=g.fileopenbox(default="*.txt")
# with open(file_path,encoding='utf-8') as f:
#     title=os.path.basename(file_path)
#     msg="文件【%s】的内容如下："% title
#     text=f.read()
#     g.textbox(msg,title,text)

import sys
def fibonacii(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacii(10)

while True:
    try:
        print(next(f),end=' ')
    except StopAsyncIteration:
        sys.exit()