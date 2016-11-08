#coding=utf-8
#根据数据包格式生成表和进行后台sql
# 先做select 返回0条纪录 前段 进行insert，返回1条 update
#               见兴趣爱好交易 "xingqu" : "健身 跑步",

#生日                 xingqu待定是否"111000"
#更具界面拼音全拼显示字段
import woclasss 
import sys

def  getwocustinfo(obname):
        
        return wocustinfo;
     
wocustinfotest={
                "nicheng": "孤独狼" ,
                "xingbie": 1,#1男0女
                "nianling":"19790309" ,
                "gexingqianming":"我的个性签名我是狼",
                "shengao":165,
                "tizhong":78.5,
                "userid":1
               }   

wocustinfo={
                "nicheng":"varchar(60)" ,
                "xingbie":"smallint",#1男0女
                "nianling":"varchar(8)" ,
                "gexingqianming":"varchar(100)",
                "shengao":"smallint",
                "tizhong":"smallint",
                "userid":"integer not null unique"
               } 
wotablessql={"wocustinfo":wocustinfo}
wotables={"wocustinfo":wocustinfo} 
 
def woselectinterfacein (cmd,woobject,sourceobject):   
          
        woselectin={
             "cmd":cmd ,
             "dml":"select",
             "woobject":"custinfo",
             "dataset":wocustinfo
             }
        print("in:"+ str( woselectin  )    )
        return woselectin
def woselectinterfaceout (cmd,woobject):   

        woselectout={
                     "code":100,
                     "msg":"成功",
                     "dml":cmd ,
                     "woobject":woobject,
                     "dataset":locals()[woobject]
                     }
        print("out"+ str( woselectout  )    )
        return woselectout


      
def wogetcreatesql(tablename):
    sql="create table "+  tablename+"   ("
    wotable=wotables[tablename]#locals()
    
    for key in wotable :
       sql=sql+ " "+key +"  "+ wotable[key]+" ,  "
    sql=sql+" );"
    print(sql)   
 
def wogetupdatesql(tablename):
    wotable=wotables[tablename]#locals()

    sql="update"+  tablename+"  "
    a=str(wotable.keys()).replace("'","")
    b=str(wotable.values())

    sql=sql+a+"  values "+b
    sql=sql.replace("[","(").replace("]",")")
    
    return sql
   
def wogetinsertsql(tablename,wotable):
   
#    wotable=wotables[tablename]#locals()
    if tablename=="wousers":
        sql=("insert into wousers  (username,password,userid )  VALUES(%s, %s)", (wotable["username"],wotable["password"]))
        print sql
        return sql

    sql="insert into "+  tablename+"  "
    
    
    
    s=b="("
    
    for key in wotable :
        s=s+key+","
        b=b+" ""+str(wotable[key])+"","
    s=s[:-1]  
    b=b[:-1]
       
    sql=sql+s+" )"
    
    c=str(wotable.values())
    print c
    c=c.replace("[","(").replace("]",")")
    sql=sql+"  values "+c +")"
    print("insert :"+sql) 
     
    return sql
 
 
def testcall():        
#生dict    
#    aaa=woselectinterfacein("select","wocustinfo",wotablessql["wocustinfo"])   
#    print("aaa's name     "+aaa.__delattr__('name')+"values:" + str(aaa))   
#    wogetupdatesql(aaa)
    if sys.argv[1]=="create":
        return wogetcreatesql(sys.argv[2])
    elif sys.argv[1]=="update"  :  
        return  wogetupdatesql(sys.argv[2])
    elif sys.argv[1]=="insert"  :  
        return wogetinsertsql(sys.argv[2])    
    elif sys.argv[1]=="select" : 
    
        return execselectsql(sys.argv[2])

def getsql(dml,tablename,table):        
#生dict    
#    aaa=woselectinterfacein("select","wocustinfo",wotablessql["wocustinfo"])   
#    print("aaa's name     "+aaa.__delattr__('name')+"values:" + str(aaa))   
#    wogetupdatesql(aaa)
    
    wheresql=" where userid="+str(table["userid"])

    if dml=="create":
        sql=wogetcreatesql(tablename)
        sql=sql+";"
    elif dml=="update"  :  
        sql=  wogetupdatesql(tablename,table)
        sql=sql+wheresql
    elif dml=="insert"  :  
        sql= wogetinsertsql(tablename,table)  
#        sql=sql+""  
    elif dml=="select" : 
    
        sql= wogetselect(tablename)
        sql=sql+wheresql
    return sql
            
        
def execselectsql(tablename):    #生dict输入json转换dict
    
#查询
    wheresql=" where userid="+wotables[tablename]["userid"]
    return  wogetselect(tablename,wheresql)
    
     
def wogetselect (table_name):
    wotable=wotables[table_name]
 
    columns=str(wotable.keys()).replace("'","").replace("[","").replace("]","")
    

    sql="select   "+columns+" from "+  table_name+" "
 
    return sql
     
         
    
           
#testcall(   )      
        
     
 

