from aiogram import types
from databaseFiles.database import open_connection


async def executeTask(message: types.Message, sql_query, params, text):
    conn = await open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query, params)
        conn.commit()
        await message.answer(text)
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()
