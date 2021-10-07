import mysql
import mysql.connector

def database_authentication(username,password):
    db_access =  mysql.connector.connect(host = "localhost", user = "root", password = "nj111205", database = "passwordmanager")
    db_pointer = db_access.cursor()

    sql_code1 = "select * from logInformation where username = %s and user_password = %s"
    db_pointer.execute(sql_code1,[(username),(password)])
    results = db_pointer.fetchall()
    if results:
        return True
    else:
        return False