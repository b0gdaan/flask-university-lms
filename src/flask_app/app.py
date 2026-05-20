from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    "admin": {"password": "adminpass", "role": "admin"},
    "professor": {"password": "professorpass", "role": "professor"},
    "student": {"password": "studentpass", "role": "student"},
    "guest": {"password": "guestpass", "role": "guest"}
}

materials = []

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for(user['role']))
        else:
            return "Incorrect username or password"
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if session.get('role') != 'admin':
        return "Access is denied"

    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            users[username]['role'] = 'professor'
            return f"{username} appointed Professor"
        else:
            return "The user was not found"

    return render_template('admin.html', users=users)

@app.route('/professor', methods=['GET', 'POST'])
def professor():
    if session.get('role') != 'professor':
        return "Access is denied"

    if request.method == 'POST':
        action = request.form['action']
        if action == 'upload':
            material = request.form['material']
            materials.append(material)
        elif action == 'edit':
            index = int(request.form['index'])
            new_text = request.form['new_text']
            if 0 <= index < len(materials):
                materials[index] = new_text

    return render_template('professor.html', materials=materials)

@app.route('/student')
def student():
    if session.get('role') == 'student':
        return render_template('student.html', materials=materials)
    return "Access is denied"

@app.route('/guest')
def guest():
    if session.get('role') == 'guest':
        return render_template('guest.html')
    return "Access is denied"

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)