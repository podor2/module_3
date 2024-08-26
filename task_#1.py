import datetime
import re


def get_days_from_today(date):

    input_date = re.search(r'(\d{4})\-(\d{2})\-(\d{2})', date)
    if input_date:
        input_date = datetime.date(year=int(input_date.group(1)), month=int(
            input_date.group(2)), day=int(input_date.group(3)))
    else:
        print(
            'The date format is not correct. Please use format "YYYY-MM-DD" and try again')

    current_date = datetime.datetime.now().date()

    diff_in_days = current_date - input_date
    return diff_in_days
