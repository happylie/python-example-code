# -*- coding: utf-8 -*-
import datetime


def date2unix(date_time):
    """
    Date to Unix
    :param date_time: Date Time
    :return:
    """
    if not isinstance(date_time, datetime.date):
        date_time = datetime.datetime.now()
    unix_time = datetime.datetime.timestamp(date_time) * 1000
    return int(str(unix_time)[0:10])


def unix2date(unix_time):
    """
    Unix to Date
    :param unix_time: Unix Time
    :return:
    """
    date_time = datetime.datetime.fromtimestamp(int(unix_time))
    return date_time


if __name__ == "__main__":
    unix_time = date2unix(datetime.datetime.now())
    print(unix_time)
    print(unix2date(unix_time))
