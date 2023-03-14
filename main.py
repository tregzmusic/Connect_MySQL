import pymysql
from config import host, user, password, database

try:
    conn = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=database
    )
    print('Соединение с MySQL установлено...')

    try:
        # with conn.cursor() as cursor:
        #     create_table_users = 'CREATE TABLE IF NOT EXISTS `users` (' \
        #                          'id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,' \
        #                          'user VARCHAR(100) NOT NULL,' \
        #                          'password VARCHAR(100) NOT NULL,' \
        #                          'email VARCHAR(100) NOT NULL UNIQUE);'
        #     cursor.execute(create_table_users)
        #     print('Таблица создана')
        #     with conn.cursor() as cursor:
        #         insert_table_users = 'INSERT INTO `users` (user, password, email)' \
        #                              'VALUES' \
        #                              '("Tregz", "1234", "tregzmusic@mail.ru"),' \
        #                              '("Tregzcode", "1234", "tregzcode@gmail.com");'
        #         cursor.execute(insert_table_users)
        #         conn.commit()

            with conn.cursor() as cursor:
                show_data = 'SELECT * FROM `users`;'
                cursor.execute(show_data)
                row = cursor.fetchall()
                for i in row:
                    print(i)

            with conn.cursor() as cursor:
                delete_table = 'DROP TABLE `users`;'
                cursor.execute(delete_table)
                print('Таблица удалена')

    finally:
        conn.close()
except Exception as ex:
    print('Ошибка...')
    print(ex)


