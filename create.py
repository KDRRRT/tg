import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect('diction.db')  # создаем соединение с базой данных

    cur = con.cursor()  # создаем курсор, который будет осуществлять запрос по базе даннх
    cur.execute(
        """
            CREATE TABLE diction 
            (
                id integer NOT NULL PRIMARY KEY, 
                word text,
                translate text
            )
        """
    )
    con.close()