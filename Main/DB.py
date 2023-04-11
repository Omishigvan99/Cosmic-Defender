import sqlite3

# connection
conn = sqlite3.connect("Astro_game.db")
print("Connection success")


# # Table Creation
# conn.execute('''
# CREATE TABLE Game_Info (
#     username varchar(30) PRIMARY KEY NOT NULL,
#     u_name varchar(20) NOT NULL,
#     level int CHECk(level > 0 AND level <=3 ) NOT NULL,
#     score bigint NOT NULL
# )
# ''')
#

# Inserting Data
def insert_data():
    # def insert_data(a,b,c,d):
    conn.execute('''
    INSERT INTO Game_Info (username, u_name , level , score)
    values ('sda','dsda',2,2323)
    ''')


def update_score():
    conn.execute('''
    UPDATE Game_Info SET score = 'var' where u_name = 'var'
    ''')


def show_score():
    cursor = conn.execute('''
    SELECT u_name, score FROM Game_Info 
    ''')
    for i in cursor:
        print(i)


insert_data()
show_score()
