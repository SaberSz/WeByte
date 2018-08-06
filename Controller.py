from flask import Flask, redirect, url_for, request, render_template, flash
app = Flask(__name__)
app.secret_key = b'some_secret'


@app.route('/login')
def login1():
    error = ""
    return render_template("login.html")


@app.route('/')
@app.route('/home')
def indexs():
    error = ""
    return render_template("index.html")


@app.route('/acc')
def accs():
    error = ""
    return render_template("acc.html")


@app.route('/fight')
def fights():
    error = ""
    return render_template("compete.html")


@app.route('/signup')
def cre():
    error = ""
    return render_template("create.html")


@app.route('/problem')
def prob():
    error = ""
    return render_template("progs.html")


@app.route('/results')
def rs():
    error = ""
    return render_template("result.html")


@app.route('/restab')
def rst():
    error = ""
    return render_template("resultstab.html")

# @app.route('/home', methods=['POST'])
# def indexs1():
#     error = ""
#     if request.method == "POST":
#         return render_template("login.html")


# @app.route("/login", methods=['POST'])
# def login2():
#     error = ""
#     if request.method == "POST":
#         user = request.form['eusn']
#         pwds = request.form['pwd']
#         print(f'{user} and {pwds}')
#         if user == "admin" and pwds == "admin":
#             print(f'{user} and {pwds}')
#             flash(f'Welcome back {user}')
#             print(f'{user} and {pwds}')
#             return redirect(url_for('prog'))

#         else:
#             error = "Invalid username or password"
#             flash(error)
#             return render_template("login.html", title="Login", error=error)


# @app.route("/contact", methods=['POST'])
# def con():
#     error = "error"
#     if request.method == "POST":
#         u = request.form['name']
#         e = request.form['email']
#         m = request.form['message']
#         s = request.form['subject']
#         print(f'{u} and {e} and {m} and {s} ')
#         return render_template("contact.html", title="Login")
#     else:
#         return render_template("contact.html", title="Login", error=error)


# @app.route("/contact")
# def con1():
#     return render_template("contact.html",)


# @app.route('/prog')
# def prog():

#     return render_template("prog.html", title="Programs")


# @app.route('/create')
# def create():
#     return render_template("create.html", title="Create an account")


if __name__ == '__main__':
    app.run(debug=True)
