"""

"""

import mysql.connector

connection=None
cursor_object=None
def create_connection(username,password,host,port=None):
    """
    Used to connect to the database.
    """
    try:
        global connection
        if port==None:
            connection=mysql.connector.connect(user=username,
                                          passwd= password,
                                          host=host)
        else:
            connection=mysql.connector.connect(user=username,
                                          passwd= password,
                                          host=host,
                                          port=port)
    
        if connection.is_connected():
            global cursor_object
            cursor_object=connection.cursor()
            return 1,"Connecton sucessful."
    except mysql.connector.errors.ProgrammingError:
        return 0, "Incorrect credentials "
    
    except mysql.connector.errors.InterfaceError:
        return 0,"the server is down or the host details are incorrect"
    
    except mysql.connector.errors.DatabaseError:
        return 0, "network issues or timeout settings"




def get_user_name():
    """
    Used to fetch the user name.

    """
    try:
        global cursor_object
        cursor_object.execute("SELECT user();")
        return cursor_object.fetchone()[0].split('@')[0]
    except Exception as e:
        return f"{e}"


def execute_query(query):
    """
    """
    try:
        cursor_object.execute(query)
        return cursor_object.fetchall() 
    except Exception as e:
        return f"{e}"

def save_changes():
    """
    """
    try:
        global cursor_object
        cursor_object.execute('COMMIT;')
        return "Commited Succesffuly!"
    except Exception as e:
        return f"{e}"

def close_connection():
    """
    """
    try:
        global cursor_object
        global connection
        connection.close()
        return "Connection Closed Succesffuly"
    except Exception as e:
        return f"{e}"

if __name__=='__main__':
    print(create_connection('root','admin','localhost'))
    print(get_user_name())
    cursor_object.execute('use a_n_d;')
    cursor_object.execute('select * from users;')
    print(cursor_object.fetchall())