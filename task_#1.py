import datetime

def get_days_from_today(date):

    try :
        input_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.datetime.now().date()
        diff_in_days = (current_date - input_date).days
        return diff_in_days

    except ValueError :
        pass
        
    
    

