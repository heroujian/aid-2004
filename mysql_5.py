import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()
# with open ('im','rb') as f:
#     data = f.read()
# try :
#     sql='update cls set image=%s where id =1;'
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()
sql = 'select image from cls where id =1'
cur.execute(sql)
data = cur.fetchone()[0]
with open('bb.jpg', 'wb') as f:
    f.write(data)
cur.close()
db.close()
