import time
import mysql.connector as ms
from datetime import date
from datetime import datetime
from datetime import timedelta


def is_day_after_current(string_input_with_date, string_input_with_time, dura):
    pastd = datetime.strptime(string_input_with_date, "%Y-%m-%d")
    pastt = datetime.strptime(string_input_with_time, "%H:%M:%S")
    event_time = pastd + timedelta(hours=pastt.hour + dura, minutes=pastt.minute)
    # print(event_time)
    present = datetime.now()
    return (event_time <= present)


def job2():
    cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
    try:
        cur = cnx.cursor()
        res = []
        stmt = 'Select `Date`, `Time1`,`Compid` FROM `competitions` WHERE `Typecmp`=2'
        cur.execute(stmt)
        d = cur.fetchall()
        for i in range(len(d)):
            # print("dsfgdfgdf")
            if is_day_after_current(str(d[i][0]), str(d[i][1]), 0):
                res.append(d[i][2])
        # print(res)
        for i in range(len(res)):
            stmt1 = f'UPDATE `competitions` SET `Typecmp`= 1 WHERE `Compid`= "{res[i]}"'
            cur.execute(stmt1)
            cnx.commit()
        cnx.close()
        # print(f'{res[i]} updated')
        # print("done running update db")

    except ms.Error as e:
        print("bub")
        print(e)


def job():
    # print("running update db")
    cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
    try:
        cur = cnx.cursor()
        res = []
        stmt = 'Select `Date`, `Time1`, `duration`,`Compid` FROM `competitions` WHERE `Typecmp`=1'
        cur.execute(stmt)
        d = cur.fetchall()
        # print(d)
        dur = []
        res = []
        for i in range(len(d)):
            # print("dsfgdfgdf")
            if is_day_after_current(str(d[i][0]), str(d[i][1]), 3):
                res.append(d[i][3])
        # print(res)
        for i in range(len(res)):
            stmt1 = f'UPDATE `competitions` SET `Typecmp`= 3 WHERE `Compid`= "{res[i]}"'
            cur.execute(stmt1)
            cnx.commit()
        cnx.close()
        for i in range(len(res)):
            eval_res(res[i])
            # print(f'{res[i]} updated')
        # print("done running update db")
        job2()
    except ms.Error as e:
        print(e)


def eval_res(compid):
    cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
    try:
        cur = cnx.cursor()
        smt = f'select distinct(`Email`) from `results` where `competitionsid`="{compid}"'
        cur.execute(smt)  # no of users
        emails = cur.fetchall()
        oxf = {}
        for i in range(len(emails)):
            oxf[str(emails[i][0])] = None
        smt = f'select k.em, k.cnt ,l.pid ,l.`Yes or NO`, l.`Time1`from (Select count(`Email`) as cnt , `Email` as em from results where `competitionsid`="{compid}" group by `email`) as k join (Select `Email` as m, `problemid` as pid, `Solved` as `Yes or NO`, `Submettime` as `Time1` from results where `competitionsid`="{compid}") as l on k.em=l.m'
        cur.execute(smt)  # no of users
        userdets = cur.fetchall()
        d = dict()
        # finalist = []
        for i in userdets:
            if(d.get(i[0], None)):
                probm = 0
                # print(type(i[2]))
                if(i[3] == 1 and i[2] == 1):
                    probm = 70
                elif(i[3] == 1 and i[2] == 2):
                    probm = 80
                elif(i[3] == 1 and i[2] == 3):
                    probm = 90
                elif(i[3] == 1 and i[2] == 4):
                    probm = 100
                d[i[0]][i[2]] = [probm, i[4]]
                d[i[0]]['tot'] += probm
            else:
                probm = 0
                d[i[0]] = dict()
                d[i[0]]['tot'] = 0
                if(i[3] == 1 and i[2] == 1):
                    probm = 70
                elif(i[3] == 1 and i[2] == 2):
                    probm = 80
                elif(i[3] == 1 and i[2] == 3):
                    probm = 90
                elif(i[3] == 1 and i[2] == 4):
                    probm = 100
                d[i[0]][i[2]] = [probm, i[4]]
                d[i[0]]['tot'] += probm
            lst = [1, 2, 3, 4]
            for j in lst:
                if not d[i[0]].get(j, False):
                    d[i[0]][j] = [0, "NULL"]
        count = 0
        cur = cnx.cursor(prepared=True)
        for i in d.keys():
            k = d[i]
            # print(k)
            smt1 = f'INSERT INTO `resulttrack`(`CompId`, `Email`, `Problem 1`, `Problem 2`, `Problem 3`, `Problem 4`, `Time1`, `Time2`, `Time3`, `Time4`, `Total marks`) VALUES ("{compid}","{i}","{[k[1]][0][0]}","{[k[2]][0][0]}","{[k[3]][0][0]}","{[k[4]][0][0]}",%s,%s,%s,%s,"{[k[1]][0][0]+[k[2]][0][0]+[k[3]][0][0]+[k[4]][0][0]}")'
            cur.execute(smt1, ([k[1]][0][1], [k[2]][0][1], [k[3]][0][1], [k[4]][0][1]))
            cnx.commit()
        cnx.close()
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='codearena')
        cur = cnx.cursor()
        smt111 = f'SELECT rt.`CompId`,rt.`Email` FROM `resulttrack` rt JOIN (SELECT MAX(rq.`Submettime`) as best,rq.`competitionsid` as cid ,rq.`Email` as em FROM `results` rq GROUP BY rq.`competitionsid`, rq.`Email`) eh ON rt.`CompId`=eh.cid AND rt.`Email`=eh.em WHERE CompId="{compid}" ORDER BY rt.`Total marks` DESC,eh.best ASC'
        cur.execute(smt111)
        rankst = cur.fetchall()
        # print(rankst)
        count = 1
        for i in rankst:
            srank = f'INSERT INTO `ranks`(`Email`, `Competionid`, `Rank`) VALUES("{i[1]}", "{i[0]}", "{count}")'
            cur.execute(srank)
            cnx.commit()
            count += 1

        finalst = f'UPDATE `competitions` SET `Typecmp`= 0 WHERE `Compid`= "{compid}"'
        cur.execute(finalst)
        cnx.commit()
    except ms.Error as e:
        print(e)

        # schedule.every(1).minutes.do(job)

        # job()
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)

        # SELECT rt.`CompId`,rt.`Email` FROM `resulttrack` rt JOIN (SELECT MAX(rq.`Submettime`) as best,rq.`competitionsid` as cid ,rq.`Email` as em FROM `results` rq GROUP BY rq.`competitionsid`, rq.`Email`) eh ON rt.`CompId`=eh.cid AND rt.`Email`=eh.em WHERE CompId='3' ORDER BY rt.`Total marks` DESC,eh.best ASC
