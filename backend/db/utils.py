import databases
from db.session import SQLALCHEMY_DATABASE_URL


async def check_db_connected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
        print("...Подключение к базе данных выполнено успешно")
    except Exception as e:
        print("...Проблема с подключением к базе данных!")
        raise e


async def check_db_disconnected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if database.is_connected:
                await database.disconnect()
        print("...Отключение от базы данных выполнено успешно")
    except Exception as e:
        raise e
