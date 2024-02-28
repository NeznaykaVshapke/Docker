import mariadb
import csv
import time


def waiting_db():
    while True:
        try:
            connection = mariadb.connect(
            	host='db', 
            	user='user', 
            	password='tpos_password', 
            	database='tpos_database'
            )
            connection.close()
            return
        except Exception as e:
            time.sleep(1)

def filler_of_database():
    with open("data.csv", 'r') as data_file:
        reader = csv.DictReader(data_file)
        data_connection = mariadb.connect(
        	host='db', 
        	user='user', 
        	password='tpos_password', 
        	database='tpos_database'
        )
        data_cursor = data_connection.cursor()
        data_cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(100), age INT)")
        for line in reader:   
            name = line['name']
            age = line['age']
            data_cursor.execute("INSERT INTO users(name, age) VALUES (?, ?)", [name, age])
        data_connection.commit()
        data_cursor.execute("SELECT * FROM users")
        ranks = data_cursor.fetchall()
        for rank in ranks:
            print(rank)
        data_cursor.close()
        data_connection.close()

if __name__ == "__main__":
    waiting_db()
    filler_of_database()
