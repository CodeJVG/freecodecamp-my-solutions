def add_time(start, duration, day=""):
    start_time = list()
    start_time.append(start.split()[0].split(":")[0])
    start_time.append(start.split()[0].split(":")[1])
    start_time.append(start.split()[1])

    add = list()
    add.append(duration.split(":")[0])
    add.append(duration.split(":")[1])

    for i in range(2):
        start_time[i] = int(start_time[i])
        add[i] = int(add[i])

    new_time = list()
    for i in range(2): new_time.append(start_time[i] + add[i])
    if start_time[2] == "PM":
        new_time.append(1)
    else:
        new_time.append(0)

    new_time.append(0)

    new_time[0] += int(new_time[1] / 60)
    new_time[1] = new_time[1] % 60
    print(new_time)

    new_time[2] += int(new_time[0] / 12)
    new_time[0] %= 12
    print(new_time)

    if new_time[0] == 0:
        new_time[0] += 12

    new_time[3] = int(new_time[2] / 2)
    new_time[2] %= 2

    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    week1 = [", Monday", ", Tuesday", ", Wednesday", ", Thursday", ", Friday", ", Saturday", ", Sunday"]
    ampm = ["AM", "PM"]

    if day != "":
        i_day = 0
        for i in range(len(week)):
            if week[i] == day.lower():
                i_day = i
        new_day = week1[(i_day + new_time[3]) % 7]
    else:
        new_day = ""

    new_time[0] = str(new_time[0])
    new_time[1] = "0" * (2 - len(str(new_time[1]))) + str(new_time[1])
    new_time[2] = ampm[new_time[2]]

    if new_time[3] == 0:
        new_time[3] = ""
    elif new_time[3] == 1:
        new_time[3] = " (next day)"
    else:
        new_time[3] = " (" + str(new_time[3]) + " days later)"

    new_time = new_time[0] + ":" + new_time[1] + " " + new_time[2] + new_day + new_time[3]

    return new_time