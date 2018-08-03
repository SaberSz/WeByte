from flask import Flask, redirect, url_for, request, render_template, flash
app = Flask(__name__)
app.secret_key = b'some_secret'


@app.route('/')
@app.route('/login')
def login1():
    error = ""
    return render_template("login.html")


@app.route("/login", methods=['POST'])
def login2():
    error = ""
    if request.method == "POST":
        user = request.form['eusn']
        pwds = request.form['pwd']
        print(f'{user} and {pwds}')
        if user == "admin" and pwds == "admin":
            print(f'{user} and {pwds}')
            flash(f'Welcome back {user}')
            print(f'{user} and {pwds}')
            return redirect(url_for('prog'))

        else:
            error = "Invalid username or password"
            flash(error)
            return render_template("login.html", title="Login", error=error)


@app.route('/prog')
def prog():

    return render_template("prog.html", title="Programs")


@app.route('/create')
def create():
    return render_template("create.html", title="Create an account")


if __name__ == '__main__':
    app.run(debug=True)
