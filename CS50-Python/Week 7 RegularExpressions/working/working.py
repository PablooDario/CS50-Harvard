import re

am_convertions = {
	           1 : "01", 2 : "02",
               3 : "03", 4 : "04",
               5 : "05", 6 : "06",
               7 : "07", 8 : "08",
               9 : "09", 10 : "10",
               11 : "11", 12 : "00"
               }

pm_convertions = {
	           1 : "13", 2 : "14",
               3 : "15", 4 : "16",
               5 : "17", 6 : "18",
               7 : "19", 8 : "20",
               9 : "21", 10 : "22",
               11 : "23", 12: "12"
               }


def check_hour(hour):
    if (hour < 0) or (hour > 23):
        raise ValueError


def check_minutes(minutes):
    if (minutes < 0) or (minutes > 59):
        raise ValueError


def find_hours(type, s):
    pattern = r"((\d+)(\:\d{2})?\sAM)"
    convertions = am_convertions

    if type == "PM":
        pattern = r"((\d+)(\:\d{2})?\sPM)"
        convertions = pm_convertions

    hours = re.findall(pattern, s)
    for time, hour, minutes in hours:
            aux = int(hour)
            check_hour(aux)
            hour = convertions[aux]
            idx = s.index(time)
            if minutes == '':
                time = hour + ":00"
            else:
                time = hour + minutes
                minutes = minutes.replace(':', '')
                check_minutes(int(minutes))

    return idx, time


def convert(s):
    time1, time2 = None, None
    idx1, idx2 = None, None

    # Ensure the string is in the correct format
    if not re.search(r"^\d{1,2}(\:\d{2})? (AM|PM) to \d{1,2}(\:\d{2})? (AM|PM)$", s):
        raise ValueError

    # Check for the AM hours
    idx1, time1 = find_hours("AM", s)

    # # Check for the PM hours
    idx2, time2 = find_hours("PM", s)

    return time1 + " to " + time2 if idx1 < idx2 else time2 + " to " + time1


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()
