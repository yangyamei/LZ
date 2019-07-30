# import pymysql
# db=pymysql.connect(host='101.37.106.150',
#                    port=3306,
#                    user='riskc_user',
#                    passwd='Lz@091988',
#                    db='arc_lz')
# cur=db.cursor()
# cur.execute("select *from arc_event  WHERE dev_id='864274039325341' group by phone")
# data=cur.fetchall()
# for column in data:
#     print(column)
# #print(data)
# db.close()

#print("{a} love {b}.{c}".format(a="I", b="FishC", c="com"))
d={
    1:'one',2:'two',3:'three'
}
for k,v in d.items():
    print(k,v)