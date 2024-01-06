from databaseFiles.database import open_connection


async def selectData(user_id: str):
    conn = await open_connection()
    cursor = conn.cursor()

    sql_query = f"""
        SELECT TaskName, Descriptions FROM Task WHERE
        UserId = ?
    """

    params = (user_id,)

    try:
        cursor.execute(sql_query, params)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()