import datetime


def output_date():
    start = datetime.datetime.strptime("06/21/2014", "%m/%d/%Y")
    end = datetime.datetime.strptime("07/07/2014", "%m/%d/%Y")
    date_generated = [
        start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    for date in date_generated:
        print(date.strftime("%m/%d/%Y"))


def format_date(date: str):
    return datetime.datetime.strptime(date, "%m/%d/%y").strftime("%m-%d-%Y") + ".csv"
