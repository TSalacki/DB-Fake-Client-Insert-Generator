import random
import datetime

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)


def quarter(date):
    return (date.month-1)//3 + 1


def semester(date):
    return (date.month-1)//6 + 1


def dateRow(date):
    insertInto = "insert into [dbo].[DimDate](Date, DayOfWeekNumber, DayOfWeekName, Month, MonthName, CalendarQuarter," \
            "CalendarSemester, CalendarYear) "
    values = "values(\'" + date.strftime("%m-%d-%Y") +"\', " + date.strftime("%d") + ", \'" + date.strftime("%A") + "\', " + \
             date.strftime("%m") + ", \'" + date.strftime("%B") + "\', " + str(quarter(date)) + ", " + \
            str(semester(date)) + ", " + date.strftime("%Y") + ");\n"
    return insertInto + values


def main():
    outputFile = open("sample.txt", "w")
    startDate = datetime.date(1990, 1, 1)
    endDate = datetime.date(2019, 1, 1)
    for dt in daterange(startDate, endDate):
        outputFile.write(dateRow(dt))

    outputFile.close()


if __name__ == "__main__":
    main()