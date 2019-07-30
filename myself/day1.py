import os
import os.path
txtcount=0
pngcount=0
pycount=0
doccount=0
dircount=0
for file in os.listdir():
    if os.path.isfile(file)==True: #判断文件是否文件，若是
        file,type=os.path.splitext(file) #获取文件后缀
        if type=='.txt':
            txtcount+=1
        elif type=='.png':
            pngcount+=1
        elif type=='.py':
            pycount+=1
        elif type=='.doc':
            doccount+=1
    else:  #不是文件，若是目录
        dircount+=1
print('txt文件有%s个'% txtcount)
print('png文件有%s个'% pngcount)
print('py文件有%s个'% pycount)
print('doc文件有%s个'% doccount)
print('文件夹有%s个'% dircount)


print(os.getcwd())







