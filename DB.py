import sqlite3

# connection
conn = sqlite3.connect("Cosmic_Defender.db")
print("Connection success")


# Table Creation
try:
    conn.execute('''
    CREATE TABLE Game_Info(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username varchar(20) UNIQUE NOT NULL,
        level1score INT,
        level2score INT,
        level3score INT
    )
    ''')
except Exception as e:
    print(e)


def insert_data(name, level, score):
    try:
        conn.execute('''
            INSERT INTO Game_Info (username, level{level}score)
            VALUES ('{name}',{score})
        '''.format(name=name, level=level, score=score))
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print(e)
        update_score(name, level, score)


def update_score(name, level, score):
    conn.execute('''
        UPDATE Game_Info SET level{level}score={score} WHERE username='{name}'
    '''.format(name=name, level=level, score=score))
    conn.commit()
    print("Data updated successfully")


def show_score():
    cursor = conn.execute('''
    SELECT u_name, score FROM Game_Info 
    ''')
    for i in cursor:
        print(i)
