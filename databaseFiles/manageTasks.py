from aiogram import types

from databaseFiles.database import open_connection


async def addTask(task: str, description: str, message: types.Message):
    conn = await open_connection()
    cursor = conn.cursor()

    sql_query = """
        INSERT INTO Task VALUES
        (?, ?)
    """

    params = (task, description)

    try:
        cursor.execute(sql_query, params)
        conn.commit()
        await message.answer("Task was added successfully")
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()
