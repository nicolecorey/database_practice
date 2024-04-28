import sqlite3

database = sqlite3.connect('exercises.db')
cursor = database.cursor()

# sql_query = "CREATE TABLE IF NOT EXISTS games (game_id INT PRIMARY KEY, title TEXT, num_players TEXT, min_age INT, ranking FLOAT)"
# cursor.execute(sql_query)

# game_id= 1
# title = "Solitare"
# num_players= 1
# min_age = 12
# ranking = 10.0

# sql_query = "INSERT INTO games (game_id, title, num_players, min_age, ranking) VALUES (?, ?, ?, ?, ?)"
# cursor.execute(sql_query, (game_id, title, num_players, min_age, ranking))
# database.commit()

# title = "Qwirkle"
# num_players= 2-4
# min_age = 6
# ranking = 4.5

# sql_query = "INSERT INTO games (title, num_players, min_age, ranking) VALUES (?, ?, ?, ?)"
# cursor.execute(sql_query, (title, num_players, min_age, ranking))
# database.commit()

# games = [
#     [3, 'Uno', '2-4', 8, 7.5], 
#     [4, 'Monopoly', '2-6', 8, 9.5],
#     [5, 'Connect 4', '2', 6, 5.5]
# ]

# sql_query = "INSERT INTO games (game_id, title, num_players, min_age, ranking) VALUES (?, ?, ?, ?, ?)"

# for game in games:
#     game_id, name, players, age, rank = game[0], game[1], game[2], game[3], game[4]

#     cursor.execute(sql_query, (game_id, name, players, age, rank))

# database.commit()
# database.close()