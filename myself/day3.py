import os
import os.path
def search_file(search_path,target_file):
    os.chdir(search_path)#修改路径到目标路径下
    for each_file in os.listdir(os.curdir):
        if each_file==target_file:
            print(os.getcwd()+os.sep+each_file)
        #each_file=os.path.join(search_path,each_file)
        if os.path.isdir(each_file):
            search_file(each_file,target_file)
            os.chdir(os.pardir)
start_path=input("请输入查找目录：")
target_file=input("请输入查找文件：")
search_file(start_path,target_file)

