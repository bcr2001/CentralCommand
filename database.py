
# this function creates a connection to my passwordmanager database in mysql.
# it fetches the data from the database that is used to verify user authentication
import mysql.connector


def database_authentication(username, password):
    db_access = mysql.connector.connect(host = "localhost", user = "root", password = "nj111205", database = "passwordmanager")
    db_pointer = db_access.cursor()
    the_request = "select * from personalInformation where username = %s and u_Password = %s "
    db_pointer.execute(the_request,[(username),(password)])
    results = db_pointer.fetchall()
    if results:
        return True
    else:
        return False
