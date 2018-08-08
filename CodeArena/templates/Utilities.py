from datetime import datetime, timedelta


def is_day_after_current(string_input_with_date, string_input_with_time):
    pastd = datetime.strptime(string_input_with_date, "%d/%m/%Y")
    pastt = datetime.strptime(string_input_with_time, "%H:%M")
    event_time = pastd + timedelta(hours=pastt.hour, minutes=pastt.minute)
    present = datetime.now()
    return (event_time < present)
