import sys
sys.path.insert(0,r'S:\interview\getwork')
from connection.sqlConnection import getSqlConnection

sql = getSqlConnection()

def __getUser(emailAddress , password):

    if emailAddress and password:
        userQuery = f'SELECT * FROM user WHERE email = "{emailAddress}" AND password = "{password}"'
        sql.execute(userQuery)
        queryResult = (sql.fetchone())
        if queryResult!=None:
            if queryResult[1].lower() == "admin":
                return [True ,"you are now logined as Admin"]
            else:
                return [True , f"welcome {queryResult[2]}"]
        else:
            return [False , "Invalid email and password !"]

    # return 

# __getUser("testEmail@gmail.com","25d55ad283aa40af464c76d713c07ad")