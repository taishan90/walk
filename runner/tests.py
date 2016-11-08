#coding=utf-8
"""
__author__ = 'qiongmiaoer'
import psycopg2
# 数据库连接参数
conn = psycopg2.connect(database="walk", user="postsql", password="2931", host="localhost", port="5432")
cur = conn.cursor()
 cur.execute("CREATE TABLE test1(id serial PRIMARY KEY, num integer,data varchar);")
# insert one item
cur.execute("INSERT INTO test1(num, data)VALUES(%s, %s)", (1, 'aaa'))
cur.execute("INSERT INTO test1(num, data)VALUES(%s, %s)", (2, 'bbb'))
cur.execute("INSERT INTO test1(num, data)VALUES(%s, %s)", (3, 'ccc'))
 cur.execute("SELECT * FROM test1;")
names = [row[0] for row in cursor.fetchall()]
db.close()
return render_to_response{'names': names}
 rows = cur.fetchall()        # all rows in table
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()


mport MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
    cur=conn.cursor()
     
    cur.execute('create database if not exists python')
    conn.select_db('python')
    cur.execute('create table test(id int,info varchar(20))')
     
    value=[1,'hi rollen']
    cur.execute('insert into test values(%s,%s)',value)
     
    values=[]
    for i in range(20):
        values.append((i,'hi rollen'+str(i)))
         
    cur.executemany('insert into test values(%s,%s)',values)
 
    cur.execute('update test set info="I am rollen" where id=3')
 
    conn.commit()
    cur.close()
    conn.close()
 
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
"""

def p( ):
  
    a={
                "nicheng": "孤独狼" ,
                "xingbie": 1,#1男0女
                "nianling":"19790309" ,
                "gexingqianming":"我的个性签名我是狼",
                "shengao":165,
                "tizhong":78.5,
                "userid":1
               }   
    b=a.values()
    
    sql=("b%s",b)
    print sql
p()