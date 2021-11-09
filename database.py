
# this function creates a connection to my passwordmanager database in mysql.
# it fetches the data from the database that is used to verify user authentication
import mysql.connector
import os

# this function is used to gain access to the passwordmanager database and return True if a user exists and False if they do not exist

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")



def database_authentication(username, password):
    db_access = mysql.connector.connect(
        host="localhost", user=f"{db_user}", password=f"{db_pass}", database="passwordmanager")
    db_pointer = db_access.cursor()
    the_request = "select * from personalInformation where username = %s and User_Password = %s "
    db_pointer.execute(the_request, [(username), (password)])
    results = db_pointer.fetchall()
    if results:
        return True
    else:
        return False


# this functions add the a new user into the database by taking what ever data they provided from the create account window
def data_sql_adder(username, password, fname, middlename, lname, phone, email):
    db_access = mysql.connector.connect(
        host="localhost", user=f"{db_user}", password=f"{db_pass}", database="passwordmanager")
    db_pointer = db_access.cursor()

    the_action = "insert into personalInformation values(%s,%s,%s,%s,%s,%s,%s)"
    db_pointer.execute(the_action, [
                       (username), (password), (fname), (middlename), (lname), (phone), (email)])

    db_access.commit()


def get_name_user(username):
    db_access = mysql.connector.connect(
        host="localhost", user=f"{db_user}", password=f"{db_pass}", database="passwordmanager")
    db_pointer = db_access.cursor()
    try:
        name_of_user_from_db = "select First_name from personalinformation where username = %s"
        db_pointer.execute(name_of_user_from_db, [(username)])
        name_result = db_pointer.fetchone()
        print(name_result[0])
    except mysql.connector.Error as err:
        print(f"{err} happened sorry :(")


#fetched the users entire data from the database and returns the said data in form of a list.
def retrive_users_data(username):
    db_access = mysql.connector.connect(host="localhost",
                                        user=f"{db_user}", 
                                        password=f"{db_pass}",
                                        database="passwordmanager")
    db_pointer = db_access.cursor()

    data_retival_code = "select * from personalInformation where username = %s"
    

    db_pointer.execute(data_retival_code,[(username)])
    result = db_pointer.fetchall()

    users_datalist = []
    for e in result:
        for i in e:
            users_datalist.append(i)
    
    return users_datalist
    

#this fucntion is repsonsible for deleting the users information.
def database_erase(username):
    db_access = mysql.connector.connect(
        host="localhost", user=f"{db_user}", password=f"{db_pass}", database="passwordmanager")
    db_pointer =db_access.cursor()

    try:
        delete_user_code = "delete from personalInformation where username = %s "
        db_pointer.execute(delete_user_code,[(username)])
        db_access.commit()
    except mysql.connector.Error as err:
        print("Something went wrong :(")
