import pickle

# def save_file(boy,girl,count):
#     file_name_boy='boy_'+str(count)+'.txt'
#     file_name_girl = 'girl_' + str(count) + '.txt'
#     boy_file=open(file_name_boy,'wb')
#     girl_file=open(file_name_girl,'wb')
#     pickle.dump(boy,boy_file)
#     pickle.dump(girl,girl_file)
#     boy_file.close()
#     girl_file.close()
# def split_file(file_name):
#     count=1
#     boy=[]
#     girl=[]
#     f=open(file_name)
#     for each_line in f:
#         if each_line[:6]!='======':
#             (role,line_spoken)=each_line.split(':',1)
#             if role=='小甲鱼':
#                 boy.append(line_spoken)
#             if role=='小客服':
#                 girl.append(line_spoken)
#             else:
#                 save_file(boy,girl,count)
#
#                 boy=[]
#                 girl=[]
#                 count+=1
#     save_file(boy,girl,count)
#     f.close()
# split_file('record.txt')

a_dict={'a':1,'b':2,'c':3,'d':4}
string=pickle.dumps(a_dict)
print(string)

print(pickle.loads(string))