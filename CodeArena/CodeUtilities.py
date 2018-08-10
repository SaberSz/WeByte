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


def convert_to_file(text_input):
    name = ''.join(choice(ascii_uppercase) for i in range(30))
    name += ".txt"
    name1 = os.path.join('.', 'SubmissionFiles', name)
    f = open(name1, "w+")
    f.write(text_input.strip())
    f.close()
    return name
