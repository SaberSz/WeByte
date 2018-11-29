'''1. email and hash of pwd
   verify email and pwd'''
from CodeArena import bcrypt
import mysql.connector as ms
from CodeArena.CodeUtilities import convert_to_file, get_countdown_time
import os


class userdbop:

    def logincheck(self, email, pwd):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        # print(email)
        # print("pwd sent=", pwd)
        try:
            cur = cnx.cursor()
            # print(f'here is d 1')
            # print("ohhhhdwhfhefhewfh")
            # pw_hash = bcrypt.generate_password_hash('frgvsfbfsbvrwrvdf').decode('utf-8')
            # print("hash pass", pw_hash)
            stmt = f'Select `Password` from `users` where `Email` ="{email}" and actives = 1'
            cur.execute(stmt)
            # print(f'here is d 1')
            d = cur.fetchall()
            # print(f'here is d {d}')
            if d:
                t = d[0]
            else:
                return False
            # print(t)
            # print("list is=", d)
            a = bcrypt.check_password_hash(bytes(t[0], 'utf-8'), pwd)
            return a
        except ms.Error as e:
            # print(e)
            return False

        except TypeError as e:
            # print(e)
            return False

    def verifyemail(self, email):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        try:
            cur = cnx.cursor()
            stmt = f'Select `Password` from `users` where `Email` ="{email}" and actives = 1'
            cur.execute(stmt)
            # print(f'here is d 1')
            d = cur.fetchall()
            # print(f'here is d {d}')
            if d:
                return True
            else:
                return False

        except ms.Error as e:
            # print(e)
            return False

        except TypeError as e:
            # print(e)
            return False

    def update_regitration(self, email):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        try:
            cur = cnx.cursor()
            st = f'UPDATE `users` SET actives= 1 WHERE `Email`="{email}"'
            cur.execute(st)
            cnx.commit()
            return True
        except ms.Error as e:
            # print(e)
            return False

        except TypeError as e:
            # print(e)
            return False

    def registration(self, email, usn, pwd):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        try:
            cur = cnx.cursor()
            u = []
            e = []
            flu, fle = False, False
            st = f'Select * from `users` where `Email`= "{email}"'
            cur.execute(st)
            u = cur.fetchall()
            if not u:  # if list empty
                flu = True
                st1 = f'Select * from `users` where `Username`= "{usn}"'
                cur.execute(st1)
                e = cur.fetchall()
                if not e:
                    fle = True
                if flu is True and fle is True:
                    z = bcrypt.generate_password_hash(pwd).decode('utf - 8')
                    cur = cnx.cursor(prepared=True)
                    stm21t = f'INSERT INTO `users`(`Email`, `Username`, `Password`) VALUES (%s,%s,%s)'
                    cur.execute(stm21t, (email, usn, z))
                    cnx.commit()
                    return f'Pass'
                else:
                    return f'Username'

            else:  # list not empty so user has already registered.
                return f'Email'

        except ms.Error as e:
            # print("db error")
            return False

        except TypeError as e:
            # print(e)
            return False

    def contactus(self, name, email, sub, mess):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        try:
            cur = cnx.cursor(prepared=True)
            stmt = f'INSERT INTO `contactus`(`Name`, `Email`, `Subject`, `Message`) VALUES (%s,%s,%s,%s)'
            cur.execute(stmt, (name, email, sub, mess))
            cnx.commit()
            return True
        except ms.Error as e:
            # print(e)
            return False

        except TypeError as e:
            # print(e)
            return False

    def fetchupcomingbattles(self):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT Compid,imgs,cName,Des,Typecmp,duration,Date,horc,Time1,Org FROM `competitions` where Typecmp = 1 or Typecmp = 2  ORDER BY `Date` ASC, `Time1` ASC'
            cur.execute(stmt)
            d = cur.fetchall()
            res = []
            for i in d:
                var = dict(zip(('cid', 'pic', 'name', 'des', 'up or on', 'duration', 'dates', 'Type of Comp', 'times', 'org'), i))
                if var['up or on'] == 1:
                    var['up or on'] = "Ongoing"
                else:
                    var['up or on'] = "Upcoming"
                if var['Type of Comp'] == 1:
                    var['Type of Comp'] = "Competitive"
                else:
                    var['Type of Comp'] = "Hiring"
                var['dates'] = str(var['dates'])
                var['times'] = str(var['times'])
                res.append(var)
            # print(res)
            return res
        except ms.Error as e:
            # print("db error")
            return None
        except TypeError as e:
            # print(e)
            return None

    def fetchfinishedbattles(self):
        '''
        "cid": 12323,
        "pic": "sample-1.jpg",
        "name": "Infinity Code Wars",
        "des": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "dates": "2018-08-12",
        "Type of Comp": "Competitive",
        "times": "20:00:00",
        "org": "Cognizant"
        '''
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT Compid,imgs,cName,Des,Date,horc,Time1,Org FROM `competitions` where Typecmp = 0 ORDER BY `Date` DESC, `Time1` DESC'
            cur.execute(stmt)
            d = cur.fetchall()
            res = []
            for i in d:
                var = dict(zip(('cid', 'pic', 'name', 'des', 'dates', 'Type of Comp', 'times', 'org'), i))
                var['dates'] = str(var['dates'])
                var['times'] = str(var['times'])
                if var['Type of Comp'] == 1:
                    var['Type of Comp'] = "Competitive"
                else:
                    var['Type of Comp'] = "Hiring"
                res.append(var)
            # print(res)
            return res
        except ms.Error as e:
            # print("db error")
            return None
        except TypeError as e:
            # print(e)
            return None

    def fetchaccountdetailsofuser(self, email):
        d = []
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        mx = []
        dick = {}
        try:
            cur = cnx.cursor()
            stmt1 = f'SELECT `Username`,`joindate` FROM `users` WHERE `Email`="{email}"'
            cur.execute(stmt1)
            # print("d")
            d = cur.fetchone()
            if d:
                dick['name'] = d[0]
                dick['Join date'] = str(d[1].date())
            dick['email'] = email
            stmt2 = f'SELECT count(*) FROM `ranks` r,`users`u WHERE u.`Email`=r.`Email`and r.`Email`="{email}" and r.`Rank`=1'
            cur.execute(stmt2)
            gold = cur.fetchone()
            if gold:
                dick['golds'] = gold[0]
            else:
                dick['golds'] = 0

            stmt3 = f'SELECT count(*) FROM `ranks` r,`users`u WHERE u.`Email`=r.`Email`and r.`Email`="{email}" and r.`Rank`=2'
            cur.execute(stmt3)
            silver = cur.fetchone()
            if silver:
                dick['silver'] = silver[0]
            else:
                dick['silver'] = 0

            stmt4 = f'SELECT count(*) FROM `ranks` r,`users`u WHERE u.`Email`=r.`Email`and r.`Email`="{email}" and r.`Rank`=3'
            cur.execute(stmt4)
            bronze = cur.fetchone()
            if bronze:
                dick['bronze'] = bronze[0]
            else:
                dick['bronze'] = 0

            stmt5 = f'select r.`Language`,count(r.`Language`) as a FROM `results` r WHERE r.`Email`="{email}" GROUP BY r.`Language`ORDER BY a DESC'
            cur.execute(stmt5)
            # print("fifth statement")
            mx = cur.fetchall()
            dick['programming languages used'] = []
            if mx:
                maxlange = mx[0][0]
                for i in mx:
                    dick['programming languages used'].append(i[0])
                dick['style'] = maxlange
            else:
                dick['programming languages used'].append("None")
                dick['style'] = "Python"

            stmt6 = f'SELECT COUNT(DISTINCT(`competitionsid`)) FROM `results` WHERE Email="{email}"'
            cur.execute(stmt6)
            battlesfought = cur.fetchone()
            if battlesfought:
                dick['battles'] = battlesfought[0]
            else:
                dick['battles'] = 0
            # print(dick)
            return dick
        except ms.Error as e:
            # print(e)
            return None
        except TypeError as e:
            # print(e)
            return None

    def checkauthenticowner(self, email, pwd):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        try:
            cur = cnx.cursor()
            d = []
            st = f'Select * from `users` where `Email`= "{email}" and `Password`=""'
            cur.execute(st)
            d = cur.fetchall()
            if d:  # if list empty
                return False
            else:
                return True
        except ms.Error as e:
            # print(e)
            return None
        except TypeError as e:
            # print(e)
            return None

    def makepwdupdate(self, email, pwd):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        try:
            cur = cnx.cursor()
            z = bcrypt.generate_password_hash(pwd).decode('utf - 8')
            st = f'UPDATE `users` SET `Password`="{z}" WHERE `Email`= "{email}"'
            cur.execute(st)
            cnx.commit()
            return True
        except ms.Error as e:
            print(e)
            return None
        except TypeError as e:
            print(e)
            return None

    def fetch_problem_statments(self, cid, pno):
        '''
        "cid": 12323,
        "problem name": "sample-1.jpg",
        "problem statement": "Infinity Code Wars",
        "input": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "output": "2018-08-12",

        '''
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT  `probno`, `probstmt`, `probname`, `probinput`, `proboutput`, c.`Time1`, c.`duration` FROM `problems`p  join `competitions` c on c.`Compid` =p.`Compid` WHERE p.`Compid`= {cid} and `testcase` = 1 ORDER BY `probno` ASC'
            cur.execute(stmt)
            d = cur.fetchall()
            res = []
            endsat = None
            for i in d:
                var = dict(zip(('problem number', 'problem statment', 'problem name', 'input', 'output', 'time', 'dur'), i))
                var['input'] = open(os.path.join('.', 'SubmissionFiles', var['input'])).read()
                var['output'] = open(os.path.join('.', 'SubmissionFiles', var['output'])).read()
                if var['problem number'] == int(pno):
                    endsat = get_countdown_time(str(var['time']), var['dur'])
                    var["show"] = "show active"
                else:
                    var["show"] = " "
                res.append(var)
            # print(res)
            return (cid, endsat, res)
        except ms.Error as e:
            # print("db error")
            return None
        except TypeError as e:
            # print(e)
            return None

    def fetch_test_cases(self, cid, pn):
        '''
        "cid": 12323,
        "problem name": "sample-1.jpg",
        "problem statement": "Infinity Code Wars",
        "input": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "output": "2018-08-12",

        '''
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT   `testcase`, `probinput`, `proboutput` FROM `problems` WHERE `probno` = {pn} and `Compid`= {cid}'
            cur.execute(stmt)
            d = cur.fetchall()
            res = []
            for i in d:
                var = dict(zip(('testcase', 'input', 'output',), i))
                if ".txt" not in var['input'][len(var['input']) - 4:]:
                    var['input'] = convert_to_file(var['input'])
                if ".txt" not in var['output'][len(var['output']) - 4:]:
                    var['output'] = convert_to_file(var['output'])
                res.append(var)
            # print(res)
            return res
        except ms.Error as e:
            # print("db error")
            return None
        except TypeError as e:
            # print(e)
            return None

    def is_time_left(self, cid):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT `Typecmp` FROM `competitions` WHERE `Compid` = "{cid}"'
            cur.execute(stmt)
            d = cur.fetchall()
            # print(d)
            if d[0][0] == 0:
                return False
            if d[0][0] == 1:
                return True
        except ms.Error as e:
            # print(e)
            return None
        except TypeError as e:
            # print(e)
            return None

    def is_new_version_better(self, cid, pno, email, prg, op):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT `Solved` FROM `results` WHERE `competitionsid` = "{cid}" and `Email` = "{email}" and `problemid` = "{pno}"'
            cur.execute(stmt)
            d = cur.fetchall()
            # print(d)
            # print("asdasdasd-----#####-")
            if len(d) != 0:
                if d[0][0] == 0:
                    # print("better")
                    submit_the_sheets(cid, pno, email, prg, op)
                else:
                    if op == 1:
                        # print("better")
                        submit_the_sheets_updated(cid, pno, email, prg, op)
            else:
                # print("first one")
                submit_the_sheets(cid, pno, email, prg, op)
            # print("asdasdasd-----####((((#-")
            # no submiting if the solution in the db is correct and the currently enetred on is incorrect
        except ms.Error as e:
            # print(e)
            return None
        except TypeError as e:
            # print(e)
            return None

    def if_previous_submitted(self, cid, email):
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT `problemid`,`submission` FROM `results` WHERE `competitionsid` = "{cid}" and `Email` = "{email}" '
            cur.execute(stmt)
            d = cur.fetchall()
            # print(d)
            res = []
            if d:
                for i in d:
                    var = dict(zip(('problem number', 'submission'), i))
                    res.append(var)
            else:
                res = None
            return res
        except ms.Error as e:
            # print(e)
            return None
        except TypeError as e:
            # print(e)
            return None

    def get_ranks(self, cid):
        '''
        "cid": 12323,
        "problem name": "sample-1.jpg",
        "problem statement": "Infinity Code Wars",
        "input": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
        "output": "2018-08-12",

        '''
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        d = []
        try:
            cur = cnx.cursor()
            stmt = f'SELECT g.cName,k.Email ,k.Username, r.`Rank`, s.`Problem 1`, s.`Problem 2` , s.`Problem 3` , s.`Problem 4` , s.`Total marks` FROM `ranks` r JOIN resulttrack s on r.`Email`=s.Email and r.`Competionid` = s.CompId join users k on k.Email=s.Email join competitions g on g.Compid=s.CompId  WHERE r.`Competionid` = "{cid}" ORDER BY r.`Rank` ASC'
            cur.execute(stmt)
            d = cur.fetchall()
            res = []
            cname = None
            for i in d:
                var = dict(zip(('Comp Name', 'Email', 'Username', 'Rank', 'Problem 1', 'Problem 2', 'Problem 3', 'Problem 4', 'Total',), i))
                cname = var['Comp Name']
                res.append(var)
            # print(res)
            return cname, res
        except ms.Error as e:
            # print("db error")
            return None
        except TypeError as e:
            # print(e)
            return None


def submit_the_sheets(cid, pno, email, prg, op):
    '''
    "cid": 12323,
    "problem name": "sample-1.jpg",
    "problem statement": "Infinity Code Wars",
    "input": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
    "output": "2018-08-12",

    '''
    cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
    d = []
    try:
        cur = cnx.cursor(prepared=True)
        stmt = f'DELETE FROM `results` WHERE `competitionsid` = "{cid}" and `Email` = "{email}" and `problemid` = "{pno}"'
        cur.execute(stmt)
        cnx.commit()
        stmt = f'INSERT INTO `results`(`competitionsid`, `Email`, `problemid`, `submission`, `Solved`) VALUES ("{cid}","{email}","{pno}",%s,{op})'
        # INSERT INTO `results`(`competitionsid`, `Email`, `problemid`, `submission`, `Solved`, `Submettime`, `Language`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7])
        cur.execute(stmt, (prg,))
        cnx.commit()
    except ms.Error as e:
        # print(e)
        return None
    except TypeError as e:
        # print(e)
        return None


def submit_the_sheets_updated(cid, pno, email, prg, op):
    '''
    "cid": 12323,
    "problem name": "sample-1.jpg",
    "problem statement": "Infinity Code Wars",
    "input": "You can’t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.",
    "output": "2018-08-12",

    '''
    cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
    d = []
    try:
        cur = cnx.cursor(prepared=True)
        stmt = f'UPDATE `results` SET `submission`= %s,`Solved`="{op}" WHERE `competitionsid`="{cid}",`Email`="{email}",`problemid`="{pno}",")'
        cur.execute(stmt, (prg,))
        cnx.commit()
    except ms.Error as e:
        # print("db error")
        return None
    except TypeError as e:
        # print(e)
        return None
# user1.registration("admin@gmail.com", "apple", "admin123")
