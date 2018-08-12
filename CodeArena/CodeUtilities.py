from datetime import datetime, timedelta
from random import choice
from string import ascii_uppercase
import os


def is_day_after_current(string_input_with_date, string_input_with_time):
    pastd = datetime.strptime(string_input_with_date, "%Y-%m-%d")
    pastt = datetime.strptime(string_input_with_time, "%H:%M:%S")
    event_time = pastd + timedelta(hours=pastt.hour, minutes=pastt.minute)
    present = datetime.now()

    return (event_time < present)


def find_endtime(string_input_with_time, string_input_with_hours):

    startsat = datetime.strptime(string_input_with_time, "%H:%M:%S")
    hors = datetime.strptime(string_input_with_hours.split()[0], "%H")
    return str(startsat + timedelta(hours=hors.hour)).split()[1]


def get_countdown_time(string_input_with_date, string_input_with_time):
    print(string_input_with_time)
    pastd = datetime.strptime(string_input_with_date, "%H:%M:%S")
    pastt = datetime.strptime(string_input_with_time.split()[0], "%H")

    present = datetime.today()
    event_time = pastd + timedelta(hours=pastt.hour)
    # print(event_time)
    # event_time = present + timedelta(hours=event_time.hour, minutes=event_time.minute, seconds=event_time.second)
    # Jan 5, 2019 15:37:25
    return str(present.strftime("%c %d, %Y")).split()[1] + str(present.strftime(" %d, %Y")) + str(event_time.strftime(" %H:%M:%S"))
    # return (event_time < present)


def convert_to_file(text_input):
    name = ''.join(choice(ascii_uppercase) for i in range(30))
    name += ".txt"
    name1 = os.path.join('.', 'SubmissionFiles', name)
    f = open(name1, "w+")
    f.write(text_input.strip())
    f.close()
    return name
