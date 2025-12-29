def add_time(start, duration,day=""):
    star_time, startampm = start.split(" ")
    start_hours, start_minutes = star_time.split(":")
    if startampm == "PM":
        start_hours = int(start_hours) + 12
    duration_hours, duration_minutes = duration.split(":")
    new_hours = int(start_hours) + int(duration_hours)
    new_minutes = int(start_minutes) + int(duration_minutes)
    while new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60
    total_minutes = int(start_hours)*60 + int(duration_hours)*60 + int(start_minutes) + int(duration_minutes)
    total_hours = total_minutes / 60
    total_days = total_hours / 24
    if new_hours % 24 >= 12 :
        if startampm == "AM":
            new_ampm = "PM"
            if total_days < 1:
                what_day = ' (next day)'
            else:
                what_day = f" ({total_days} days later)"
        else:
            if total_days < 1:
                what_day = ' (next day)'
            else:
                what_day = f" ({total_days} days later)"
            new_ampm = "AM"
    else:
        new_ampm = startampm
    new_hours = new_hours % 24
    if new_hours == 0:
        new_hours = 12
    if len(str(new_minutes)) == 1:
        new_minutes = "0" + str(new_minutes)
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    if not day:
        new_time = f"{new_hours}:{new_minutes} {new_ampm}{what_day}"
    else:
        day = day.capitalize()
        if total_days < 1:
            day = day
        else:
            day = round((week.index(day) + total_days) % len(week))
            day = week[day]
        new_time = f"{new_hours}:{new_minutes} {new_ampm}, {day}{what_day}"


    return new_time

print(add_time('10:10 PM', '3:30'))