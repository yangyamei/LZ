# def file_view(file_name,file_line):
#     f=open(file_name,encoding='utf-8')
#    # count=0
#    # while count<=file_line:
#     for each in range(int(file_line)):
#         print(f.readline(),end='')
#        # count+=1
#     f.close()
# file_view('1.txt',2)


def file_view(file_name,file_num):
    if file_num.strip()==':':
        begin=1
        end=-1
    (begin,end)=file_num.split(':')
    if begin=="":
        begin=1
    if end=="":
        end=-1
    if begin==1 and end==-1:
        prompt="的全文"
    elif begin==1:
        prompt="从开始到%s"% end
    elif end==-1:
        prompt="从%s到结束"%begin
    else:
        prompt="从%s行到%s行"%(begin,end)
    begin=int(begin)-1
    end=int(end)
    lines=end-begin
    f=open(file_name)
    for i in range(begin):
        f.readline()
    if lines<0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline())
    f.close()
file_name=input("请输入文件名：")
line_num=input("请输入要查看的行数，如【2:5|：|：5|2：】：")
file_view(file_name,line_num)




