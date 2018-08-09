from datetime import datetime, timedelta
from random import choice
from string import ascii_uppercase


def is_day_after_current(string_input_with_date, string_input_with_time):
    pastd = datetime.strptime(string_input_with_date, "%Y-%m-%d")
    pastt = datetime.strptime(string_input_with_time, "%H:%M:%S")
    event_time = pastd + timedelta(hours=pastt.hour, minutes=pastt.minute)
    present = datetime.now()
    return (event_time < present)


def convert_to_file(text_input):
    name = ''.join(choice(ascii_uppercase) for i in range(30))
    name += ".txt"
    name1 = os.path.join('.', 'SubmissionFiles', name)
    f = open(name1, "w+")
    f.write(text_input)
    f.close()
    return name
