from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)
# Function to establish database connection
def get_db_connection():
 conn = sqlite3.connect('users.db')
 conn.row_factory = sqlite3.Row
 return conn
# Route to render the home page
@app.route('/')
def index():
 return render_template('index.html')
# Route to handle CRUD operations
@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
 conn = get_db_connection()
 cursor = conn.cursor()
 if request.method == 'GET':
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])
 elif request.method == 'POST':
    data = request.get_json()
    name = data['name']
    Id = data['Id']
    points = data['points']
    cursor.execute('INSERT INTO users (name, Id, points) VALUES (?, ?, ?)', (name, Id, points))
    conn.commit()
    conn.close()
    return 'User created successfully', 201
 elif request.method == 'PUT':
    data = request.get_json()
    Id = data['Id']
    points = data['points']
    cursor.execute('UPDATE users SET points = ? WHERE Id = ?', (points, Id))
    conn.commit()
    conn.close()
    return 'User updated successfully', 200
 elif request.method == 'DELETE':
    Id = request.args.get('Id')
    cursor.execute('DELETE FROM users WHERE Id = ?', (Id,))
    conn.commit()
    conn.close()
    return 'User deleted successfully', 200
# Run the Flask app
if __name__ == '__main__':
 app.run(debug=True)