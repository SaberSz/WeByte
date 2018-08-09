from flask import redirect, url_for, request, render_template, flash, session, escape
from CodeArena import app
from datetime import timedelta
import re
from CodeArena.db import userdbop

user_db = None


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
    elif 'times' in session:
        if session['times'] >= 3:
            return redirect(url_for('logout'))

    error = ""
    if request.method == "POST":
        global user_db
        em = request.form['email']
        pw = request.form['password']
        print(f'{em} and {pw} 1')
        if user_db is None:
            user_db = userdbop()
        if user_db.logincheck(em, pw):
            print(f'{em} and {pw} 2')
            flash(f'Welcome back {em}')
            print(f'{em} and {pw}')
            session['username'] = em
            session['times'] = 0
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
    session.pop('_flashes', None)
    global user_db
    user_db.__del__()
    print(f'{session.items()} present in logout')
    return redirect(url_for('indexs'))


@app.route('/')
@app.route('/home')
def indexs():
    error = ""
    return render_template("index.html")


@app.route("/home", methods=['GET', 'POST'])
def homesugg():
    global user_db
    error = ""
    try:
        if request.method == "POST":
            print("\nsdfsadfasdfasdfasdf\n")
            name = request.form['conname']
            email = request.form['conmail']
            sub = request.form['consel']
            msg = request.form['message']
            if user_db is None:
                user_db = userdbop()
            if user_db.contactus(name, email, sub, msg):
                flash(f'Thank you {name} for getting in touch with us. We will get back you shortly.')
                flash('Scroll')
            else:
                flash(f'Opps! Something went wrong:(')
                flash('Scroll')
            return redirect(url_for('indexs'))
    except:
        flash(f'Opps! Something went wrong:(')
        flash('Scroll')
        return redirect(url_for('indexs'))


usr_details = {
    "name": "apples",
    "email": "apples@gmail.com",
    "golds": 5,
    "silver": 7,
    "bronze": 9,
    "style": "Python",
    "programming languages used": ["Python"],
    "Join date": "2018-08-12",
    "battles": 15
}


@app.route('/acc')
def accs():
    global user_db
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        # call a method that returns all the details of the user as a dictionary given the email id
        usr_details = user_db.fetchaccountdetailsofuser(username_session)
        return render_template('acc.html',
                               session_user_name=username_session,
                               dets=usr_details)

    return redirect(url_for('login1'))


@app.route('/acc', methods=['GET', 'POST'])
def accs2():
    error = ""
    global user_db
    if 'times' in session:
        print("entered 1")
        if session['times'] >= 3:
            print("entered 2")
            return redirect(url_for('logout'))
    if 'username' in session:
        print("entered 3")

        if request.method == "POST":
            print("entered 4")
            oldpass = request.form['oldpass']
            newpass = request.form['newpass']
            renewpass = request.form['renewpass']
            if user_db is None:
                user_db = userdbop()
            username_session = escape(session['username']).capitalize()
            usr_details = user_db.fetchaccountdetailsofuser(username_session)

            if renewpass == newpass and newpass != oldpass:  # and newpass satisfies password constraints
                # print(f'{em} and {pw}')
                # function that returns true or false with old pass and email
                #
                if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', newpass):
                    error = "Weak Password"
                    flash(error)
                    return render_template("acc.html", title="Login", dets=usr_details)
                em = escape(session['username']).capitalize()
                if user_db.logincheck(em, oldpass):

                    # send new pass and email and change the password
                    # if success
                    user_db.makepwdupdate(em, newpass)
                    flash(f'Success')
                    return render_template("acc.html", title="Login", dets=usr_details)
                else:
                    error = "Old Password"
                    flash(error)
                    session['times'] += 1
                    return render_template("acc.html", title="Login", dets=usr_details)
            else:
                error = "Password Not Match"
                flash(error)
                return render_template("acc.html", title="Login", dets=usr_details)
    else:
        return redirect(url_for('logout'))


upcoming = [
    {
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "up or on": "Ongoing",
        "duration": "3 hours",
        "dates": "2018-08-12",
        "Number of Problems": 4,
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    },
    {
        "cid": 12323,
        "pic": "loft.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "up or on": "Ongoing",
        "duration": "3 hours",
        "dates": "2018-08-12",
        "Number of Problems": 4,
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    },
    {
        "cid": 12323,
        "pic": "building.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "up or on": "Upcoming",
        "duration": "3 hours",
        "dates": "2018-08-12",
        "Number of Problems": 4,
        "Type of Comp": "Competitive",
        "times": "20:00:00",
        "org": "Cognizant"
    },
    {
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "up or on": "Upcoming",
        "duration": "3 hours",
        "dates": "2018-08-12",
        "Number of Problems": 4,
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    },
    {
        "cid": 12323,
        "pic": "building.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "up or on": "Upcoming",
        "duration": "3 hours",
        "dates": "2018-08-12",
        "Number of Problems": 4,
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    }, {
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "up or on": "Upcoming",
        "duration": "3 hours",
        "dates": "2018-08-12",
        "Number of Problems": 4,
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    }, {
        "cid": 12323,
        "pic": "building.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "up or on": "Upcoming",
        "duration": "3 hours",
        "dates": "2018-08-12",
        "Number of Problems": 4,
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    },
]


@app.route('/fight')
def fights():
    global user_db
    if 'username' in session:

        em = escape(session['username']).capitalize()
        print(f'the passed value is {em}')
        # make call to database and get all upcoming competitions as a list and return the list
        upcoming = user_db.fetchupcomingbattles()
        return render_template('compete.html',
                               session_user_name=em,
                               upcoming=upcoming)
    else:
        return redirect(url_for('login1'))


@app.route('/signup')
def cre():
    error = ""
    return render_template("create.html")


@app.route('/signup', methods=['GET', 'POST'])
def cre2():
    error = ""
    global user_db
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
        if pw != pw2:
            flash(f'Password')
            error = "Passwords don't match."
            print(error)
            return redirect(url_for('cre'))
        if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', pw):
            error = "Weak Password"
            flash(error)
            print(error)
            return redirect(url_for('cre'))
        user_db = userdbop()
        res = user_db.registration(em, name, pw)
        if res == "Pass":
            print(f' inside {em} and {pw}\n {name} and {pw2}')
            return redirect(url_for('fights'))
        elif res == "Username":
            print("Username")
            flash(f'Username')
        elif res == "Email":
            print("Email")
            flash(f'Email')

        return redirect(url_for('cre'))


@app.route('/problem')
def prob():
    global user_db
    if 'username' in session:
        cid = request.args.get('name')
        print(f'The value of cid is {cid}')

        username_session = escape(session['username']).capitalize()

        return render_template('progs.html',
                               session_user_name=username_session)
    return redirect(url_for('login1'))


resultant = [
    {
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "dates": "2018-08-12",
        "Type of Comp": "Competitive",
        "times": "20:00:00",
        "org": "Cognizant"
    },
    {
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "dates": "2018-08-12",
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    },
    {
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "dates": "2018-08-12",
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    },
    {
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "dates": "2018-08-12",
        "Type of Comp": "Hiring",
        "times": "20:00:00",
        "org": "Cognizant"
    },
]


@app.route('/results')
def rs():
    global user_db
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        resultant = user_db.fetchfinishedbattles()
        return render_template('result.html',
                               session_user_name=username_session,
                               resultant=resultant)
    return redirect(url_for('login1'))


@app.route('/restab')
def rst():
    global user_db
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
