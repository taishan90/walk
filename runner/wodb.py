#coding=utf-8


#from django.shortcuts import render_to_response
from django.db import connection,transaction
from django.shortcuts import render_to_response
import os,sys
from django.http import HttpResponse
import json
from evennia.utils import  logger
from evennia.utils.logger import log_trace
#from __future__ import division  
from twisted.internet.protocol import Protocol
import wointerface


#数据库连接作为全局变量，一旦connect，建立连接，disconnect 时断开数据库
""" 
    
"""

  

#    switch
"""
def woselectinterfacein (cmd,woobject,sourceobject):   
          
        woselectin={
             "cmd":cmd ,
             "woobject":woobject,
             "dataset":sourceobject
             }
        print("in:"+ str( woselectin  )    )
        return woselectin
"""
   

"""     
def infoUpload(self,cmd,data,text):      
        
        cursor = connection.cursor()            #获得一个游标(cursor)对象
         for key in data #字典每个值插入到他对应的字段里
         
             sql=("walk_run_info(%s) "+"name")
             sql="walk_run_info(%s) ",date["name"])
         
         values("
         
         
        cursor.execute("insert into walk_run_info(%s) VALUES(%s, %s)", (data[], 'aaa'))
#cur.execute("INSERT INTO test1(num, data)VALUES(%s, %s)", (1, 'aaa'))
        
    #    names = [row[0] for row in cursor.fetchall()]
        raw = cursor.fetchall() 
        jsonresult=json.dumps(raw) 

        
        
        aaa="filename:"+sys._getframe().f_code.co_filename+ " func: "+sys._getframe().f_code.co_name +" line:"+str(sys._getframe().f_lineno)

        log_zk(aaa+" ;raw:{"+str(jsonresult)+"}")
        retun str(raw)
     
"""        
def wodbconnect(self,cmd,data):
        
        try:
#            cmdname, args, kwargs = json.loads(data)
            
            
             
            logger.log_infomsg(str(data))
 


        except Exception:
            log_trace("Websocket malformed OOB request: %s" % data)
            raise
#        self.sessionhandler.data_in(self,"oob", oob=(cmd , args))
         
        aaa="filename:"+sys._getframe().f_code.co_filename+ " func: "+sys._getframe().f_code.co_name +" line:"+str(sys._getframe().f_lineno)

        self.log_zk(aaa+" ;mark:{"+cmd+"}")
        logger.log_file(aaa)
        
        cursor = connection.cursor()            #获得一个游标(cursor)对象
         
        cursor.execute("select username from  players_playerdb;")
        
    #    names = [row[0] for row in cursor.fetchall()]
        raw = cursor.fetchall() 
        jsonresult=json.dumps(raw) 

        
        
        aaa="filename:"+sys._getframe().f_code.co_filename+ " func: "+sys._getframe().f_code.co_name +" line:"+str(sys._getframe().f_lineno)

        log_zk(aaa+" ;raw:{"+str(jsonresult)+"}")
        self.sendLine(str(raw))
#        self.transport.write(line)
        

    #    return render_to_response( {'names':raw})
#        return HttpResponse(raw)
#    print('book_list.html', {'names': names})
#    return render_to_response('book_list.html', {'names': names})
def log_zk( text):
#        aaa="filename:"+sys._getframe().f_code.co_filename+ "  func: "+sys._getframe().f_code.co_name +" line:"+str(sys._getframe().f_lineno)
        logger.log_file(text,  "wolfzk.log")
    
#        operator = {'wodbconnect':wodbconnect}  
#scoket入口函数          
def wojosnin(self,data):
    
    aaa="filename:"+sys._getframe().f_code.co_filename+ " func: "+sys._getframe().f_code.co_name +" line:"+str(sys._getframe().f_lineno)
    log_zk(aaa)
    dataJson = json.loads(data)
    log_zk("data:"+data)
#    cmd = dataJson["cmd"]
    dml=dataJson["dml"]
    tablename="wo"+dataJson["woobject"]
    table = dataJson["dataset"]
    
#          
#    sql=wointerface.getsql(dml, tablename,table)     
    
#    switchdml={"select":wointerface.wogetselect} 
#    switchdml[dml](woobject)
    log_zk("input:"+dml+" "+tablename)
    result={"code":100,"msg":"成功","tag":dataJson["tag"]}

    cursor = connection.cursor()            #获得一个游标(cursor)对象
    if((dml=="insert")and (tablename=="wouser")):
        cursor.execute("insert into wousers  (username,password )  VALUES(%s, %s)", (table["username"],table["password"]))
    elif((dml=="select")and (tablename=="wouser")):
        sql=("select userid from  wousers where  username =%(username)s and password=%(password)s " %table)
        print sql
        cursor.execute(sql)
        raw = cursor.fetchone() 
        raw={"userid":raw}
        
    result["dataset"]=raw
 
     #    names = [row[0] for row in cursor.fetchall()]
    
 #    count=cursor.getCount()
#    count=cursor.rowcount
    
    
        
    print(str(result))    
         
    log_zk(" result:{"+str(result)+"}")
    return result;
#        self.sendLine(str(jsonresult)+"count:"+str(count))
#        sql=wointerface.testcall(dml,tablename,wotable)
        
    
#    wodbconnect(self,cmd,args)

"""    
    try 
        self.sendLine("succ" )

    except Exception:
            log_zk("执行命令失败t: %s" % data)
            raise
#    f(3,cmd,2) 
def f(x,o,y):  
    operator.get(o)(x,y)      
    
    
#	return render_to_response('book_list.html', {'names': names})
"""