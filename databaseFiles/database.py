import pypyodbc as odbc


async def open_connection():
    DRIVER_NAME = 'SQL Server'
    SERVER_NAME = 'monaa'
    DATABASE_NAME = 'TaskManager'

    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """

    conn = odbc.connect(connection_string)
    return conn
