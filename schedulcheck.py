import schedule
import time
import mysql.connector as ms
from datetime import date
from datetime import datetime
from datetime import timedelta


def is_day_after_current(string_input_with_date, string_input_with_time, dura):
    pastd = datetime.strptime(string_input_with_date, "%Y-%m-%d")
    pastt = datetime.strptime(string_input_with_time, "%H:%M:%S")
    event_time = pastd + timedelta(hours=pastt.hour + dura, minutes=pastt.minute)
    present = datetime.now()
    return (event_time <= present)


def job():
    cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
    try:
        cur = cnx.cursor()
        res = []
        stmt = f'Select `Date`, `Time1`, `duration`,`Compid` FROM `competitions` WHERE 1'
        cur.execute(stmt)
        d = cur.fetchall()
        dur = []
        res = []
        for i in range(len(d)):
            if(is_day_after_current(str(d[i][0]), str(d[i][1]), 3)):
                res.append(d[i][3])
        for i in range(len(res)):
            stmt1 = f'UPDATE `competitions` SET `Typecmp`= 3 WHERE `Compid`= "{res[i]}"'
            cur.execute(stmt1)
            eval_res(res[i])
            cnx.commit()
    except ms.Error as e:
        print(e)


def eval_res(compid):
    cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
    try:
        cur = cnx.cursor()
        smt = f'select distinct(`Email`) from `results` where `competitionsid`="{compid}"'
        cur.execute(smt)  # no of users

        emails = cur.fetchall()
        usersinfo = [None] * len(emails)
        print("below lies your answer bo")
        # print(len(emails))
        actualres = []
        oxf = {}
        for i in range(len(emails)):
            oxf[str(emails[i][0])] = None
            actualres.append(oxf)
        # print(f'userinfo={usersinfo}')

        print(f'here is your final list:{actualres}')
        #     usersinfo[i] = dict([(key, []) for key in keys])
        smt = f'select k.em, k.cnt ,l.pid ,l.`Yes or NO`, l.`Time1`from (Select count(`Email`) as cnt , `Email` as em from results where `competitionsid`="3" group by `email`) as k join (Select `Email` as m, `problemid` as pid, `Solved` as `Yes or NO`, `Submettime` as `Time1` from results where `competitionsid`="3") as l on k.em=l.m'
        cur.execute(smt)  # no of users
        userdets = cur.fetchall()
        finalist = []
        for i in userdets:
            print(i)
            print()
        for i in range(len(userdets)):
            finalist.append(str(userdets[i][i]))
        for i in userdets:
            probm1, probm2, probm3, probm4 = 0, 0, 0, 0
            if(int(finalist[3]) == 1 and finalist[2] == 1):
                probm1 = 70
            if(int(finalist[3]) == 1 and finalist[2] == 2):
                probm2 = 80
            if(int(finalist[3]) == 1 and finalists[2] == 3):
                probm3 = 90
            if(int(finalist[3]) == 1 and finalist[2] == 4):
                probm4 = 100
            # if(finalist)
            smt1 = f'INSERT INTO `resulttrack`(`CompId`, `Email`, `Problem 1`, `Problem 2`, `Problem 3`, `Problem 4`,`Total marks`) VALUES ({compid},{finalist[0]},{probm1},{probm2},{prob3},{prob4},{prob1+prob2+prob3+prob4})'
            cur.execute(smt1)
            cnx.commit()
            smt = f'select `Email` from `results` where `competitionsid`="{compid}"'
            cur.execute(smt)
            rowsupreq = cur.fetchall()
            for i in rowsupreq):
                if(emails == rowsupreq[0]):
                    st=UPDATE `resulttrack` SET `Time1`={finalist[4]} WHERE `Email`={rowsupreq[0]}
                    cur.execute(st)
                    cur.commit()
    except ms.Error as e:
        print(e)


schedule.every(1).seconds.do(job)
eval_res(3)


while True:
    schedule.run_pending()
    time.sleep(1)
