import sqlite3

# Создаем подключение к базе данных (файл database_check_bot.db будет создан)


connection = sqlite3.connect('database_check_bot.db', check_same_thread=False)
cursor = connection.cursor()




# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
now_time TEXT NOT NULL,
answear TEXT NOT NULL
)
''')
# Создаем индекс для столбца "email"
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_answear ON Users (answear)')


# Добавляем данные
def add_data(lst):
    return cursor.execute('INSERT INTO Users (username, now_time, answear) VALUES (?, ?, ?)', (lst[-3], lst[-1], lst[-2])), connection.commit()



def view_users():
    # Выбираем всех пользователей
    cursor.execute('''
    SELECT username FROM Users
    ORDER BY username DESC
    LIMIT 1
    ''')
    users = cursor.fetchall()
    all_username = []
    # Выводим результаты
    for user in users:
        all_username.append(user)
    return all_username


def view_time():
    # Выбираем всех пользователей
    cursor.execute('''
    SELECT now_time FROM Users
    ORDER BY now_time DESC
    LIMIT 1
    ''')
    users = cursor.fetchall()
    all_now_time = []
    # Выводим результаты
    for user in users:
        all_now_time.append(user)
    return all_now_time

def view_answear():
    # Выбираем всех пользователей
    cursor.execute('''
    SELECT answear FROM Users
    ORDER BY answear DESC
    LIMIT 1
    ''')
    users = cursor.fetchall()
    all_answear = []
    # Выводим результаты
    for user in users:
        all_answear.append(user)
    return all_answear


def get_all():
    # records = []
    message_text = ""
    cursor.execute('SELECT * FROM Users')
    rows = cursor.fetchall()
    for res in rows:
        message_text += "{0} | {1} | {2} \n".format(res[1], res[2], res[3])
    return message_text


# Сохраняем изменения и закрываем соединение
connection.commit()
# connection.close()

