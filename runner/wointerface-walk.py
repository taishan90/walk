#coding=utf-8
#根据数据包格式生成表和进行后台sql
#               见兴趣爱好交易 "xingqu" : "健身 跑步",

#生日                 xingqu待定是否"111000"
#更具界面拼音全拼显示字段
 
def  getwocustinfo(obname):
        
        return wocustinfo;
        
wocustinfotest={
                "nicheng":"孤独狼" ,
                "xingbie":1,#1男0女
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
                "userid":"integer"
               } 
wotablessql={"wocustinfo":wocustinfotest}
wotables={"wocustinfo":wocustinfo}
def woselectinterfacein (cmd,woobject,sourceobject):   
          
        woselectin={
             "cmd":cmd ,
             "woobject":woobject,
             "dataset":sourceobject
             }
        print("in:"+ str( woselectin  )    )
        return woselectin
def woselectinterfaceout (cmd,woobject):   

        woselectout={
                     "code":100,
                     "msg":"成功",
                     "cmd":cmd ,
                     "woobject":woobject,
                     "dataset":locals()[woobject]
                     }
        print("out"+ str( woselectout  )    )
        return woselectout


      
def wogetcreatesql(woobject):
    sql="create table "+  woobject+" "
    wotable=wocustinfostruc#locals()
    for key in locals()[dataset] :
       sql=sql+ " "+key +"  "+ locals()[woobject][key]+"   "
    print(sql)   
    
def wogetcreatesqlnew(woselectinterfacein):
    print("woselectinterfacein:"+str(woselectinterfacein))

    sql="create table "+  woselectinterfacein["woobject"]+"  ("
    
    wotable=woselectinterfacein["dataset"] 
    print(str(wotable))
    for key in wotable:
       sql=sql+ " "+key +"  "+wotable[key]+"  , "
    sql=sql+" );"
    print(sql)          
def wogetupdatesqlnew(dict_table):
    print("woselectinterfacein:"+str(dict_table))

    sql="insert into "+  dict_table["woobject"]+"  "
    a=str(dict_table["dataset"].keys()).replace("'","")
     
    b=str(dict_table["dataset"].values())

    sql=sql+a+"  values "+b
    sql=sql.replace("[","(").replace("]",")")
    
    print(sql)
#    sql=sql+ str(dict_table["dataset"].keys())+str(dict_table["dataset"].values())+";"
"""
    wotable=dict_table["dataset"] 
    keyall="("
    valueall="("
    print(str(wotable))
    for key in wotable:
       keyall=keyall+key +","
       
       valueall=keyall+wotable[key]
    sql=sql+keyall+") values"+valueall+" );"
"""    
   
def testcall():        
#生dict    
    aaa=woselectinterfacein("select","wocustinfo",wotablessql["wocustinfo"])   
#    print("aaa's name     "+aaa.__delattr__('name')+"values:" + str(aaa))   
    wogetupdatesqlnew(aaa)
           
testcall( )      
        
     
 

