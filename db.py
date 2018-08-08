'''1. email and hash of pwd
   verify email and pwd'''
from CodeArena import bcrypt
import mysql.connector as ms


class userdbop:
    def __init__(self):
        self.cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')

    def logincheck(self, email, pwd):
        print(email)
        print("pwd sent=", pwd)
        try:
            cur = self.cnx.cursor()
            # print("ohhhhdwhfhefhewfh")
            # pw_hash = bcrypt.generate_password_hash('frgvsfbfsbvrwrvdf').decode('utf-8')
            # print("hash pass", pw_hash)
            stmt = f'Select `Password` from `users` where `Email` ={email}'
            cur.execute(stmt)
            d = cur.fetchall()
            t = d[0]
            # print(t)
            # print("list is=", d)
            a = bcrypt.check_password_hash(bytes(t[0], 'utf-8'), 'frgvsfbfsbvrwrvdf')
            return a
        except ms.Error as e:
            print("db error")
            return False

        except TypeError as e:
            print(e)
            return False

    def registration(self, email, usn, pwd):
        try:
            cur = cnx.cursor()
            d = []
            # print("ohhhhdwhfhefhewfh")
            # pw_hash = bcrypt.generate_password_hash('frgvsfbfsbvrwrvdf').decode('utf-8')
            # print("hash pass", pw_hash)
            stmt = f'Select * from `users` where `Email` = {email} and `Password`= {pwd} and `Username`= {usn}'
            cur.execute(stmt)
            d = cur.fetchall()
            if not d:  # if list is empty
                u = []
                p = []
                e = []
                flu, flp, fle = False, False, False
                st = f'Select * from `users` where `Username`= {usn}'
                cur.execute(st)
                u = cur.fetchall()
                if u:
                    flu = True
                st1 = f'Select * from `users` where `Email`= {email}'
                cur.execute(st1)
                e = cur.fetchall()
                if e:
                    fle = True
                st2 = f'Select * from `users` where `Password`= {pwd}'
                cur.execute(st2)
                p = cur.fetchall()
                if p:
                    flp = True
                if flu == False and flp == False and fle == False:
                    stm21t = f'INSERT INTO `users`(`Email`, `Username`, `Password`) VALUES ({email},{usn},{pwd})'
                    cur.execute(stm21t)
                    self.cnx.commit()
                    return f'Pass'
                else:
                    if(flu):
                        return f'Username:{usn} already taken'
                    if(fle):
                        return f'Email:{email} already taken'
                    if(flp):
                        return f'Password:{pwd} already taken'

            else:  # list not empty so user has already registered.
                return f'User {usn} has already registered with Email: {email} and password as {pwd}'

        except ms.Error as e:
            print("db error")
            return False

        except TypeError as e:
            print(e)
            return False

    def contactus(self, name, email, sub, mess):
        try:
            cur = self.cnx.cursor()
            stmt = f'INSERT INTO `contactus`(`Name`, `Email`, `Subject`, `Desciption`) VALUES ({name},{email},{sub},{mess})'
            cur.execute(stmt)
            self.cnx.commit()
        except ms.Error as e:
            print("db error")
            return False

        except TypeError as e:
            print(e)
            return False

    def fetchupcomingbattles(self):
        d = []
        try:
            cur = self.cnx.cursor()
            stmt = f'SELECT Compid,imgs,cName,Des,Typecmp,duration,Date,horc,Time1,Org FROM `competitions` WHERE 1'
            cur.execute(stmt)
            d = cur.fetchall()
            res = []
            for i in d:
                var = dict(zip(('cid', 'pic', 'name', 'des', 'up or on', 'duration', 'dates', 'Type of Comp', 'times', 'org'), i))
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

    def fetchaccountdetailsofuser(self):
        d = []
        try:
            cur = self.cnx.cursor()
            stmt = f'SELECT Compid,imgs,cName,Des,Typecmp,duration,Date,horc,Time1,Org FROM `competitions` WHERE 1'
            cur.execute(stmt)
            d = cur.fetchall()
            res = []
            for i in d:
                var = dict(zip(('cid', 'pic', 'name', 'des', 'up or on', 'duration', 'dates', 'Type of Comp', 'times', 'org'), i))
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


user1 = userdbop()
user1.fetchupcomingbattles()

#               self.cnx.commit()
# "cid": 12323,
#       "pic": "desk.jpg",
#       "name": "Infinity Code Wars",
#       "des": "apples, pineapples, greenapples and  oranges for me. ",
#       "up or on": "Ongoing",
#       "duration": "3 hours",
#       "dates": "12/08/2018",
#       "Type of Comp": "Hiring",
#       "times": "14:00"
# org:
