import pymysql

def getSqlConnection():
    dataBase = pymysql.connect(user="root",password="",host="localhost",database="getworksql", autocommit=True)
    sql = dataBase.cursor()
    return sql
    