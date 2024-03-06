import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blah-blah-blah'

def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']

        if not name:
            flash('User name is required!')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?',
                        (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user

@app.route('/edit/<int:id>/', methods=('GET', 'POST'))
def edit_user(id):
    user = get_user(id)

    if request.method == 'POST':
        name = request.form['name']

        if not name:
            flash('Username is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE users SET name = ?'
                         ' WHERE id = ?',
                         (name, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', user=user)

@app.route('/delete/<int:id>/', methods=('POST',))
def delete_user(id):
    user = get_user(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(user['name']))
    return redirect(url_for('index'))

def main():
   app.run(host='127.0.0.1', port=9999)

if __name__ == "__main__":
   main()