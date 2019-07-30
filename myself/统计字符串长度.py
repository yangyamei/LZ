def finstr(desstr,sonstr):
    count=0
    length=len(desstr)
    if sonstr not in desstr:
        print("未找到")
    else:
        for each in range(length-1):
            if desstr[each]==sonstr[0]:
                if desstr[each+1]==sonstr[1]:
                    count+=1
        print("出现了%d次"% count)
desstr=input("请输入目标字符串：")
sonstr=input("请输入子字符串：")
finstr(desstr,sonstr)