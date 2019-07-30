from pymongo import MongoClient

# client = MongoClient('172.16.157.239',6383)
client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
db = client.admin  # mydb数据库，同上解释
# db.authenticate("root", "2ICb6XyPJgdv")
db.authenticate("root", "c4N3pVMN8zfBwhOC")
collection = db.bailin_user_index
result=collection.find({'projectCode':'SHBT_JingDongYunPei_app1'})
# list=[]
with open('data.log','a+') as f:
    for res in result:
        f.write('\n'+res['projectUserId'])

