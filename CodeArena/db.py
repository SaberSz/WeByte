'''1. email and hash of pwd
   verify email and pwd'''
from CodeArena import bcrypt
import mysql.connector as ms


class userdbop:
    def __init__(self):
        self.cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')

    def __del__(self):
        self.cnx.close()

    def logincheck(self, email, pwd):
        print(email)
        print("pwd sent=", pwd)
        try:
            cur = self.cnx.cursor()
            # print("ohhhhdwhfhefhewfh")
            # pw_hash = bcrypt.generate_password_hash('frgvsfbfsbvrwrvdf').decode('utf-8')
            # print("hash pass", pw_hash)
            stmt = f'Select `Password` from `users` where `Email` ="{email}"'
            cur.execute(stmt)
            d = cur.fetchall()
            print(f'here is d {d}')
            if d:
                t = d[0]
            else:
                return False
            # print(t)
            # print("list is=", d)
            a = bcrypt.check_password_hash(bytes(t[0], 'utf-8'), pwd)
            return a
        except ms.Error as e:
            print("db error")
            return False

        except TypeError as e:
            print(e)
            return False

    def registration(self, email, usn, pwd):
        try:
            cur = self.cnx.cursor()
            d = []
            u = []
            p = []
            e = []
            flu, flp, fle = False, False, False
            st = f'Select * from `users` where `Username`= "{usn}"'
            cur.execute(st)
            u = cur.fetchall()
            if not u:  # if list empty
                flu = True
                st1 = f'Select * from `users` where `Email`= "{email}"'
                cur.execute(st1)
                e = cur.fetchall()
                if not e:
                    fle = True
                if flu == True and fle == True:
                    z = bcrypt.generate_password_hash(pwd).decode('utf - 8')
                    stm21t = f'INSERT INTO `users`(`Email`, `Username`, `Password`) VALUES ("{email}","{usn}","{z}")'
                    cur.execute(stm21t)
                    self.cnx.commit()
                    return f'Pass'
                else:
                    return f'Email'

            else:  # list not empty so user has already registered.
                return f'Username'

        except ms.Error as e:
            print("db error")
            return False

        except TypeError as e:
            print(e)
            return False

    def contactus(self, name, email, sub, mess):
        try:
            cur = self.cnx.cursor()
            stmt = f'INSERT INTO `contactus`(`Name`, `Email`, `Subject`, `Message`) VALUES ("{name}","{email}","{sub}","{mess}")'
            cur.execute(stmt)
            self.cnx.commit()
            return True
        except ms.Error as e:
            print(e)
            return False

        except TypeError as e:
            print(e)
            return False

    def fetchupcomingbattles(self):
        d = []
        try:
            cur = self.cnx.cursor()
            stmt = f'SELECT Compid,imgs,cName,Des,Typecmp,duration,Date,horc,Time1,Org FROM `competitions` where Typecmp != 0 ORDER BY `Date` ASC, `Time1` ASC'
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
            print("db error")
            return None
        except TypeError as e:
            print(e)
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
        d = []
        try:
            cur = self.cnx.cursor()
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
            print("db error")
            return None
        except TypeError as e:
            print(e)
            return None

    def fetchaccountdetailsofuser(self, email):
        d = []
        mx = []
        dick = {}
        try:
            cur = self.cnx.cursor()
            stmt1 = f'SELECT `Username`,`joindate` FROM `users` WHERE `Email`="{email}"'
            cur.execute(stmt1)
            print("d")
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
            print("fifth statement")
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
            print(dick)
            return dick
        except ms.Error as e:
            print(e)
            return None
        except TypeError as e:
            print(e)
            return None

    def checkauthenticowner(self, email, pwd):
        try:
            cur = self.cnx.cursor()
            d = []
            st = f'Select * from `users` where `Email`= "{email}" and `Password`=""'
            cur.execute(st)
            d = cur.fetchall()
            if d:  # if list empty
                return False
            else:
                return True
        except ms.Error as e:
            print(e)
            return None
        except TypeError as e:
            print(e)
            return None

    def makepwdupdate(self, email, pwd):
        try:
            cur = self.cnx.cursor()
            z = bcrypt.generate_password_hash(pwd).decode('utf - 8')
            st = f'UPDATE `users` SET `Password`="{z}" WHERE `Email`="{email}"'
            cur.execute(st)
            self.cnx.commit()
            return True
        except ms.Error as e:
            print(e)
            return None
        except TypeError as e:
            print(e)
            return None


user1 = userdbop()
# user1.registration("admin@gmail.com", "apple", "admin123")
print(user1.fetchupcomingbattles())
