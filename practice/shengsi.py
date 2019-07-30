def yuesefu(nums,step,stay):
    #nums:总人数  step:步长   stay:剩余的人数
    lists = list( range(1,nums+1) )
    #check = 0
    while len(lists) > stay:
        i = 1
        while i<step:
            lists.append(lists.pop(0))
            #print(lists)
            i+=1
            #print(i)
        print("{:2d}号要下船了".format(lists.pop(0)))
stays = yuesefu(30,9,15)