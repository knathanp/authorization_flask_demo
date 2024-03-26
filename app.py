# Demonstrate role-based access control (RBAC) in a flask web application

from flask import Flask, request, redirect, url_for, render_template, abort, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Dummy user database and roles
users = {
    'admin': {'password': 'adminpass', 'role': 'Admin'},
    'editor': {'password': 'editorpass', 'role': 'Editor'},
    'viewer': {'password': 'viewerpass', 'role': 'Viewer'}
}

# Role permissions
role_permissions = {
    'Admin': ['create', 'read', 'update', 'delete'],
    'Editor': ['read', 'update'],
    'Viewer': ['read']
}

@app.route('/')
def home():
    if 'username' in session:
        role = users[session['username']]['role']
        permissions = role_permissions[role]
        return f'Welcome {session["username"]}! Role: {role}. Permissions: {permissions}'
    return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return 'Invalid credentials'
    return render_template('login.html')  # Assume a simple login form in login.html

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

def check_permission(action):
    if 'username' not in session:
        abort(401)  # Unauthorized
    role = users[session['username']]['role']
    permissions = role_permissions[role]
    if action not in permissions:
        abort(403)  # Forbidden

@app.route('/create')
def create():
    check_permission('create')
    return 'Create content page'

@app.route('/edit')
def edit():
    check_permission('edit')
    return 'Edit content page'

@app.route('/delete')
def delete():
    check_permission('delete')
    return 'Delete content page'

if __name__ == '__main__':
    app.run(debug=True)
