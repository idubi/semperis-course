from flask import Flask,url_for,request,redirect

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s!' % name

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))

    if request.method == 'GET':
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(port=8000)