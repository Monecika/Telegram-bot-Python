from aiogram import types

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


async def addUser(message: types.Message, user_id: str, last_message: str):
    if not await doesExist(message.from_user.id):
        conn = await open_connection()
        cursor = conn.cursor()

        sql_query = """
            INSERT INTO Users(UserId, LastMessage)
            VALUES (?, ?)
        """

        params = (user_id, last_message)

        try:
            cursor.execute(sql_query, params)
            conn.commit()
        except Exception as e:
            print(f"Error adding user: {e}")
        finally:
            cursor.close()
            conn.close()


async def updateUser(message: types.Message, user_id: str, last_message: str):
    print(await getMessage(user_id))
    conn = await open_connection()
    cursor = conn.cursor()

    sql_query = """
                UPDATE Users 
                SET LastMessage = ?
                WHERE UserId = ?
           """

    params = (last_message, user_id)

    try:
        cursor.execute(sql_query, params)
        conn.commit()
    except Exception as e:
        print(f"Error updating user: {e}")
    finally:
        cursor.close()
        conn.close()
