from databaseFiles.database import open_connection


async def executeUser(sql_query, params):
    conn = await open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query, params)
        conn.commit()
    except Exception as e:
        print(f"Error adding user: {e}")
    finally:
        cursor.close()
        conn.close()
