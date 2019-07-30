#查询用户借款分期表riskt_borrow_installment
import pymysql
conn = pymysql.connect(host="101.37.106.150", user="riskc_user", password="Lz@091988", database="arc_lz", port=3306,charset="utf8")
db=conn.cursor()
db.execute("select * from riskt_borrow_installment WHERE borrow_no='jkbUJ4G95107522100046'")
result=db.fetchall()
for i in result:
    print(i)
db.execute("select status from arc_borrow_pay_info WHERE borrowNo='jkbUJ4G95107522100046'")  #查询弱风控记录表中
result1=db.fetchone()
print(result1)