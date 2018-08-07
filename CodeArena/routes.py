from flask import redirect, url_for, request, render_template, flash
from CodeArena import app


@app.route('/login')
def login1():
    error = ""
    return render_template("login.html")


@app.route("/login", methods=['GET', 'POST'])
def login2():
    error = ""
    if request.method == "POST":
        em = request.form['email']
        pw = request.form['password']
        print(f'{em} and {pw}')
        if em == "admin@gmail.com" and pw == "admin":
            print(f'{em} and {pw}')
            flash(f'Welcome back {em}')
            print(f'{em} and {pw}')
            return redirect(url_for('fights'))

        else:
            error = "Error"
            flash(error)
            return render_template("login.html", title="Login", error=error)


@app.route('/')
@app.route('/home')
def indexs():
    error = ""
    return render_template("index.html")


@app.route("/home", methods=['GET', 'POST'])
def homesugg():
    error = ""
    if request.method == "POST":
        print("\nsdfsadfasdfasdfasdf\n")
        name = request.form['conname']
        email = request.form['conmail']
        sub = request.form['consel']
        msg = request.form['message']
        print(f'{name} and {email} \n {sub} and {msg}')
        # print(f'{em} and {pw}')
        # if em == "admin" and pw == "admin":
        #     print(f'{em} and {pw}')
        #     flash(f'Welcome back {user}')
        #     print(f'{em} and {pw}')
        #     return redirect(url_for('compete'))

        # else:
        #     error = "Error"
        #     flash(error)
        flash(f'{name} and {email} \n {sub} and {msg}')
        return render_template("index.html")


@app.route('/acc')
def accs():
    error = ""
    return render_template("acc.html")


@app.route('/acc')
def accs2():
    error = ""
    if request.method == "POST":
        em = request.form['email']
        pw = request.form['password']
        print(f'{em} and {pw}')
        if em == "admin" and pw == "admin":
            print(f'{em} and {pw}')
            flash(f'Welcome back {user}')
            print(f'{em} and {pw}')
            return redirect(url_for('compete'))

        else:
            error = "Error"
            flash(error)
            return render_template("acc.html", title="Login", error=error)


@app.route('/fight')
def fights():
    error = ""
    return render_template("compete.html")


@app.route('/signup')
def cre():
    error = ""
    return render_template("create.html")


@app.route('/signup', methods=['GET', 'POST'])
def cre2():
    error = ""
    if request.method == "POST":
        name = request.form['name']
        em = request.form['email']
        pw = request.form['password']
        pw2 = request.form['confirm_password']
        print(f'{em} and {pw}\n {name} and {pw2}')
        # if em == "admin" and pw == "admin":
        #     print(f'{em} and {pw}')
        #     flash(f'Welcome back {user}')
        #     print(f'{em} and {pw}')
        #     return redirect(url_for('compete'))
        # else:
        #     error = "Error"
        #     flash(error)
        #     return render_template("login.html", title="Login", error=error)
        if name == "admin" and em == "admin@gmail.com" and pw == pw2:
            print(f' inside {em} and {pw}\n {name} and {pw2}')
            return redirect(url_for('fights'))
        if name != "admin":
            flash(f'Username')
        if em != "admin@gmail.com":
            flash(f'Email')
        if pw != pw2:
            print('asdfasdfasdfasdfasdhvufvasdidufvasiudvfiuasdvfusdavfiuavsdiufvsiaudvfiuvasidfv\n\n')
            flash(f'Password')
            error = "Passwords don't match."

        return render_template("create.html", error=error)


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


#


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
