from databaseFiles.database import open_connection


async def doesExist(user_id: str):
    conn = await open_connection()
    cursor = conn.cursor()

    sql_query = """
        SELECT 1 FROM Users 
        WHERE UserId = ?
    """

    params = (user_id,)

    try:
        cursor.execute(sql_query, params)
        result = cursor.fetchone()
        return bool(result)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


async def getMessage(user_id: str):
    conn = await open_connection()
    cursor = conn.cursor()
    sql_query = f"""
        SELECT LastMessage FROM Users
        WHERE UserId = ?
    """

    params = (user_id,)

    try:
        cursor.execute(sql_query, params)
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()
