
# this function creates a connection to my passwordmanager database in mysql.
# it fetches the data from the database that is used to verify user authentication
import mysql.connector

#this function is used to gain access to the passwordmanager database and return True if a user exists and False if they do not exist
def database_authentication(username, password):
    db_access = mysql.connector.connect(host = "localhost", user = "root", password = "nj111205", database = "passwordmanager")
    db_pointer = db_access.cursor()
    the_request = "select * from personalInformation where username = %s and User_Password = %s "
    db_pointer.execute(the_request,[(username),(password)])
    results = db_pointer.fetchall()
    if results:
        return True
    else:
        return False


#this functions add the a new user into the database by taking what ever data they provided from the create account window
def data_sql_adder(username, password, fname, middlename, lname, phone,email):
    db_access = mysql.connector.connect(host = "localhost", user = "root", password = "nj111205", database = "passwordmanager")
    db_pointer = db_access.cursor()


    the_action = "insert into personalInformation values(%s,%s,%s,%s,%s,%s,%s)"
    db_pointer.execute(the_action, [(username), (password), (fname), (middlename), (lname), (phone),(email)])

    db_access.commit()