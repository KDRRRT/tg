import sqlite3

# если в строке есть точка, то str.split(".")
# вернет список с двумя элементами
# добавление в базу данных (дв языка)

with open("slov.txt", encoding="utf-16-le") as file:
    for line in file.readlines():
        if "." in line:
            w = line.split(".")
            print(w)
            con = sqlite3.connect('diction.db')
            cur = con.cursor()

            cur.execute(
                f"""
                        INSERT INTO diction
                        (word, translate)
                        VALUES( '{w[0]}', '{w[1]}');
                    """
            )
            con.commit()
            con.close()

        else:
            print(line)




