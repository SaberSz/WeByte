from flask import redirect, url_for, request, render_template, flash, session, escape
from CodeArena import app
from datetime import timedelta


@app.before_request
def make_session_active():
    session.modified = True


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/login')
def login1():
    error = ""
    return render_template("login.html")


@app.route("/login", methods=['GET', 'POST'])
def login2():
    print(f"\n{session.items()}")
    if 'username' in session:
        return redirect(url_for('fights'))

    error = ""
    if request.method == "POST":
        em = request.form['email']
        pw = request.form['password']
        print(f'{em} and {pw}')
        if em == "admin@gmail.com" and pw == "admin":
            print(f'{em} and {pw}')
            flash(f'Welcome back {em}')
            print(f'{em} and {pw}')
            session['username'] = em
            print(f"\n{session.items()}")
            next_page = request.args.get('next')
            return redirect(url_for('fights')) if next_page else redirect(url_for('fights'))

        else:
            error = "Error"
            flash(error)
            return redirect(url_for('login1'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    print(f'{session.items()} present in logout')
    return redirect(url_for('indexs'))


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
        flash(f'Thank you {name} for getting in touch with us. We will get back you shortly.')
        flash('Scroll')
        return redirect(url_for('indexs'))


@app.route('/acc')
def accs():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        return render_template('acc.html', session_user_name=username_session)
    return redirect(url_for('login1'))


@app.route('/acc', methods=['GET', 'POST'])
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
            return render_template("acc.html", title="Login")


upcoming = [
    {
        "cid": 12323,
        "pic": "desk.jpg",
        "name": "Infinity Code Wars",
        "des": "apples, pineapples, greenapples and  oranges for me. ",
        "duration": "3 hours",
        "dates": "12/08/2018",
        "Number of Problems": 4,
        "Number of Registed People": 256,
        "Type of Comp": "Hiring",
    },
    {
        "cid": 12323,
        "pic": "loft.jpg",
        "name": "Infinity Code Wars",
        "des": "apples, pineapples, greenapples and  oranges for me. ",
        "duration": "3 hours",
        "dates": "12/08/2018",
        "Number of Problems": 4,
        "Number of Registed People": 256,
        "Type of Comp": "Hiring",
    },
    {
        "cid": 12323,
        "pic": "1.jpg",
        "name": "Infinity Code Wars",
        "des": "apples, pineapples, greenapples and  oranges for me. ",
        "duration": "3 hours",
        "dates": "12/08/2018",
        "Number of Problems": 4,
        "Number of Registed People": 256,
        "Type of Comp": "Hiring",
    },
]


@app.route('/fight')
def fights():

    if 'username' in session:

        em = escape(session['username']).capitalize()
        print(f'the passed value is {em}')
        # make call to database and get all upcoming competitions as a list and return the list
        return render_template('compete.html', session_user_name=em, upcoming=upcoming)
    else:
        return redirect(url_for('login1'))


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

        return redirect(url_for('cre'))


@app.route('/problem')
def prob():
    if 'username' in session:
        cid = request.args.get('name')
        print(f'The value of cid is {cid}')
        username_session = escape(session['username']).capitalize()
        return render_template('progs.html', session_user_name=username_session)
    return redirect(url_for('login1'))


@app.route('/results')
def rs():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        return render_template('result.html', session_user_name=username_session)
    return redirect(url_for('login1'))


@app.route('/restab')
def rst():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        return render_template('resultstab.html', session_user_name=username_session)
    return redirect(url_for('login1'))

# @app.route('/home', methods=['POST'])
# def indexs1():
#     error = ""
#     if request.method == "POST":
#         return render_template("login.html")


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
