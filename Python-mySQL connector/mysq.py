import mysql.connector

def creat_cone(host, usuario, senha, base):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=base)

def close_cone(con):
    return con.close()

#You should to create a data base in you mySQL