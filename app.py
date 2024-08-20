from flask import Flask, request, jsonify, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a real secret key
app.config['SESSION_TYPE'] = 'filesystem'

from flask_session import Session
Session(app)

# Simulated user database
users = {
    'admin': {'password': 'admin', 'role': 'admin'},
    'student1': {'password': 'student1', 'role': 'student'},
    'student2': {'password': 'student2', 'role': 'student'},
}

passes = []

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', role=session['role'])
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
            return redirect(url_for('home'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('home'))

@app.route('/apply', methods=['POST'])
def apply_pass():
    data = request.json
    data['status'] = 'Pending'
    passes.append(data)
    return jsonify({'message': 'Pass applied successfully!'}), 200

@app.route('/passes', methods=['GET'])
def get_passes():
    return jsonify(passes), 200

@app.route('/approve/<int:pass_id>', methods=['POST'])
def approve_pass(pass_id):
    if 'role' in session and session['role'] == 'admin':
        if 0 <= pass_id < len(passes):
            passes[pass_id]['status'] = 'Approved'
            return jsonify({'message': 'Pass approved successfully!'}), 200
        return jsonify({'message': 'Invalid pass ID'}), 400
    return jsonify({'message': 'Unauthorized'}), 403

@app.route('/reject/<int:pass_id>', methods=['POST'])
def reject_pass(pass_id):
    if 'role' in session and session['role'] == 'admin':
        if 0 <= pass_id < len(passes):
            passes[pass_id]['status'] = 'Rejected'
            return jsonify({'message': 'Pass rejected successfully!'}), 200
        return jsonify({'message': 'Invalid pass ID'}), 400
    return jsonify({'message': 'Unauthorized'}), 403

if __name__ == '__main__':
    app.run(debug=True)
