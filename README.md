#   py-mysql-client


py-mysql-client是mysql-python-connector库的简易版，基于mysql官方开源库mysql-python-connector实现

- 无cursor,执行query后立即获取数据,模拟mysql命令行客户端执行query的过程
- 支持prepare stmt
- 支持设置自动提交事务
- 支持debug模式:日志输出与mysql server从建联到执行query的整个过程step及mysql报文


### 建连与执行查询


###### from easymysql.connector import MySQLClient

###### db = MySQLClient()
###### db.connect(host="121.4.60.147",port=3306,user="root",password="jsak")
###### print db.execute("show databases;")
###### 输出:
###### [(u'information_schema',), (u'mysql',), (u'performance_schema',), (u'stock',), (u'sys',)]



### 执行dml 事务自行提交

###### db.execute("drop table if exists testmy")
###### db.execute("create table if not exists testmy(id int(11),name varchar(10))")
###### db.execute("insert into testmy (id,name) values(1,'mamo')")
###### db.commit()


### 执行dml 事务自动提交

###### db.autocommit = True
###### db.execute("drop table if exists testmy")
###### db.execute("create table if not exists testmy(id int(11),name varchar(10))")
###### db.execute("insert into testmy (id,name) values(1,'mamo')")


### 执行prepare stmt


###### db.connect(host="121.4.60.147",port=3306,user="root",password="Yrj1993718!",database="jsak")
###### db.prepare()
###### db.execute("select * from stock_daily where stock_code = ?",(601318,))

### 设置debug模式

###### db = MySQLClient()
###### db.set_debug()
###### db.connect(host="121.4.60.197",port=3306,user="root",password="Yrj1993718!",database="stock")









