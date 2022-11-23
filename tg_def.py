# 1 функция по нахождению слова
# 2 is_word_exists - если такого слова нет - отображать это
import sqlite3


def get_word(r_word):
    con = sqlite3.connect('diction.db')
    cur = con.cursor()

    res = cur.execute(
        f"""
               SELECT word
                FROM diction WHERE "translate" LIKE  "%{r_word}%";

            """
    )
    translate = res.fetchone()
    con.close()
    return translate
