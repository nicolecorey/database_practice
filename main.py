import sqlite3

database = sqlite3.connect('practice.db')
cursor = database.cursor()

# sql_query = "CREATE TABLE IF NOT EXISTS students (last_name TEXT, first_name TEXT, grad_year INT)"
# cursor.execute(sql_query)

# last_name = input("Enter your last name:").capitalize()
# first_name = input("Enter your first name:").capitalize()
# grad_year = input("Enter your grad year:").capitalize()

# sql_query = "INSERT INTO students (last_name, first_name, grad_year) VALUES (?, ?, ?)"
# cursor.execute(sql_query, (last_name, first_name, grad_year))
# database.commit()

# sql_query = "SELECT * FROM students"
# results = list(cursor.execute(sql_query))
# results.sort()

# print("Last Name\tFirstName\tGraduation Year")
# for result in results:
#    # Each entry in 'results' contains 2 values, result[0] and result[1].
#    row = f"{result[0]}\t\t{result[1]}\t\t{result[2]}"
#    print(row)

#    # Add the recent_grad column to the students table.
# sql_query = "ALTER TABLE students ADD COLUMN recent_grad TEXT"
# cursor.execute(sql_query)

# # Fill each cell in the column with a 'Yes' string.
# sql_query = "UPDATE students SET recent_grad = 'Yes'"
# cursor.execute(sql_query)
# database.commit()

# sql_query = "UPDATE students SET recent_grad = 'No' WHERE grad_year < 2017"
# cursor.execute(sql_query)
# database.commit()

sql_query = "DELETE FROM students WHERE recent_grad == 'No' "
cursor.execute(sql_query)
database.commit()
