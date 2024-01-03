from aiogram import types

from databaseFiles.database import open_connection


async def addTask(user_id: str, task: str, description: str, message: types.Message):
    conn = await open_connection()
    cursor = conn.cursor()

    sql_query = """
        INSERT INTO Task VALUES
        (?, ?, ?)
    """

    params = (user_id, task, description)

    try:
        cursor.execute(sql_query, params)
        conn.commit()
        await message.answer("Task was added successfully")
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()


async def remove(task: str, user_id: str, message: types.Message):
    conn = await open_connection()
    cursor = conn.cursor()

    sql_query = f"""
        DELETE FROM Task WHERE
        TaskName = ? and UserId = ?
    """

    params = (task, user_id)

    try:
        cursor.execute(sql_query, params)
        conn.commit()
        await message.answer("Task deleted successfully")
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()


async def selectData(user_id: str):
    conn = await open_connection()
    cursor = conn.cursor()

    sql_query = f"""
        SELECT TaskName FROM Task WHERE
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
