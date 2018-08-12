from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from CodeArena import app, mail
import re
from flask_mail import Message


ts = Serializer(app.config["SECRET_KEY"], 86400)


def send_mail(email, subject, html):
    # token = ts.dumps({'user_id': email}).decode('utf-8')
    msg = Message(subject,
                  sender='noreply@WeByte.com',
                  recipients=[email])
    msg.body = f''' Hey, this is the TechLead. You made a great decision by signing up on WeByte. To activate your account click here {html}

    If you did not make this request then simply ignore this email and no changes will be made
    '''
    mail.send(msg)
    # print("Mail sent")


def send_mail_content(email, subject, html):
    msg = Message(subject,
                  sender='noreply@WeByte.com',
                  recipients=[email])
    msg.body = html
    mail.send(msg)
    # print("Mail sent")


def check_pass_strength(password):
    flag = 0
    if (len(password) < 8):
        flag = -1
        # print("z1")
    elif not re.search("[a-z]", password):
        flag = -1
        # print("z2")
    elif not re.search("[A-Z]", password):
        flag = -1
        # print("z3")
    elif not re.search("[0-9]", password):
        flag = -1
        # print("z4")
    elif not re.search("[_@$#]", password):
        flag = -1
        # print("z5")
    elif re.search("\s", password):
        flag = -1
        # print("z6")
    else:
        flag = 0
        return True

    if flag == -1:
        return False
