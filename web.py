from flask import Flask, json
import time
import mariadb

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    data_connection = mariadb.connect(
    	host='db', 
    	user='user', 
    	password='tpos_password', 
    	database='tpos_database'
    )
    data_cursor = data_connection.cursor()
    data_cursor.execute("SELECT * FROM users")
    tpos_data = {}
    for line in data_cursor:
        name = line[0]
        age = line[1]
        tpos_data[name] = age
    data_cursor.close()
    data_connection.close()
    return json.dumps(tpos_data), 200

@app.route('/health', methods=['GET'])
def health_check():
    return json.dumps({"status": "OK"}), 200


@app.errorhandler(404)
def other_ask(e):
    return json.dumps({"error": "Not Found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
