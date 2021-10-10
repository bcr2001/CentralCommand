import mysql.connector


def database_authentication(username, password):
    db_access = mysql.connector.connect(host = "localhost", user = "root", password = "nj111205", database = "passwordmanager")

    db_pointer = db_access.cursor()

    the_query = "select * from existingUsers where username = %s and user_password = %s"
    db_pointer.execute(the_query,[(username),(password)])
    result = db_pointer.fetchall()

    if result:
        return True
    else:
        return False

# database_authentication("brian","rotu")