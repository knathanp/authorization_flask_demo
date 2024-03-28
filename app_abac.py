# Demonstrate attribute based access control (ABAC) in a flask web application

from flask import Flask, request, redirect, url_for, render_template, session, abort

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Dummy user data
users = {
    'alice': {'password': 'alicepass', 'attributes': {'role': 'editor', 'department': 'marketing'}},
    'bob': {'password': 'bobpass', 'attributes': {'role': 'viewer', 'department': 'finance'}},
    'carol': {'password': 'carolpass', 'attributes': {'role': 'admin', 'department': 'it'}}
}

@app.route('/')
def home():
    if 'username' in session:
        user_attrs = users[session['username']]['attributes']
        return f'Welcome {session["username"]}! Attributes: {user_attrs}'
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
    return render_template('login.html')  # A simple login form

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

def check_access(resource, action):
    if 'username' not in session:
        abort(401)  # Unauthorized

    user_attrs = users[session['username']]['attributes']
    
    # Example policy: Only 'editor' role in 'marketing' department can 'edit' marketing materials
    if resource == 'marketing_material' and action == 'edit':
        if user_attrs.get('role') == 'editor' and user_attrs.get('department') == 'marketing':
            return True
        else:
            abort(403)  # Forbidden
    return False

@app.route('/edit_marketing_material')
def edit_marketing_material():
    check_access('marketing_material', 'edit')
    return 'Editing marketing material.'


if __name__ == '__main__':
    app.run(debug=True)
