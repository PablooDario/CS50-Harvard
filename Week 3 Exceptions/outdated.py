# Implement a program that prompts the user for a date, in month-day-year order, formatted like 9/8/1636 or September 8, 1636 and convert it into year-month-day

def main():
    months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" :"09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
    }
    change_date(months)

def change_date(months):
    while True:
        date = input("Date: ").strip()
        try:
            month, day, year = map(int, date.split("/"))
            if month < 13 and day < 32:
                print(f"{year}-{month:02}-{day:02}")
                break
        except:
            month, day, year = date.split()
            day = int(day[:-1])
            if month in months and day < 32:
                month = months[month.title]
                print(f"{year}-{month}-{day:02}")
                break

main()
