import calendar_build as cal
from datetime import date, timedelta
from announcements_build import write_announcements
import json

def get_announcements_dates():   
    today = date.today()
    current_weekday = (today.weekday())
    days_until_friday = 4 - current_weekday 
    friday =  today + timedelta(days=days_until_friday)
    shabbos = friday + timedelta(days=1)
    sunday = shabbos + timedelta(days=1)
    return [friday, shabbos, sunday]

def get_announcements_zmanim(dates, calendar):
    calendar = calendar[calendar['English Date'].isin([date.strftime('%B %d') for date in dates])]

    zman_list = ["Plag Mincha", "Candle Lighting", "Shkia", "Shacharis", "Zman Kriyas Shema", "Mincha", "Maariv", "Mommy and Me", "Youth Groups", "Eretz Yisrael Seder"]
    calendar = calendar.loc[(calendar['Type']=="Parsha") | (calendar['Name'].isin(zman_list))]

    friday_day = dates[0].strftime('%B %d')
    shabbos_day = dates[1].strftime('%B %d')
    sunday_day = dates[2].strftime('%B %d')

    friday = calendar[calendar['English Date'] == friday_day]
    shabbos = calendar[calendar['English Date'] == shabbos_day]
    sunday = calendar[calendar['English Date'] == sunday_day]

    friday_dict = {
        "date": friday_day,
        "plag_mincha": friday[friday['Name'] == 'Plag Mincha']['Time'].to_string(index=False),
        "candle_lighting": friday[friday['Name'] == 'Candle Lighting']['Time'].to_string(index=False),
        "shkia": friday[friday['Name'] == 'Shkia']['Time'].to_string(index=False),
        "shacharis": friday[friday['Name'] == 'Shacharis']['Time'].to_string(index=False),
        "zman_kriyas_shema": friday[friday['Name'] == 'Zman Kriyas Shema']['Time'].to_string(index=False),
        "maariv": friday[friday['Name'] == 'Maariv']['Time'].to_string(index=False),
    }

    shabbos_dict = {
        "date": shabbos_day,
        "shacharis": shabbos[shabbos['Name'] == 'Shacharis']['Time'].to_string(index=False),
        "zman_kriyas_shema": shabbos[shabbos['Name'] == 'Zman Kriyas Shema']['Time'].to_string(index=False),
        "maariv": shabbos[shabbos['Name'] == 'Maariv']['Time'].to_string(index=False),
        "mommy_and_me": shabbos[shabbos['Name'] == 'Mommy and Me']['Time'].to_string(index=False),
        "youth_groups": shabbos[shabbos['Name'] == 'Youth Groups']['Time'].to_string(index=False),
        "eretz_yisrael_seder": shabbos[shabbos['Name'] == 'Eretz Yisrael Seder']['Time'].to_string(index=False)
    }

    sunday_dict = {
        "date": sunday_day,
        "shacharis": sunday[sunday['Name'] == 'Shacharis']['Time'].to_string(index=False),
        "zman_kriyas_shema": sunday[sunday['Name'] == 'Zman Kriyas Shema']['Time'].to_string(index=False),
        "maariv": sunday[sunday['Name'] == 'Maariv']['Time'].to_string(index=False)
    }

    zmanim = {
        "parsha": calendar[calendar['Type'] == 'Parsha']['Name'].to_string(index=False),
        "friday": friday_dict,
        "shabbos": shabbos_dict,
        "sunday": sunday_dict
    }

    return zmanim

def format_announcements(zmanim):
    print("Formatting announcements for the week")



def build_announcements():
    """Builds the announcement flyer for the week"""
    calendar = cal.get_calendar_data('july')
    dates = get_announcements_dates()


    
    # Fetch zmanim for the week
    zmanim = get_announcements_zmanim(dates, calendar)   
    
    announcements = write_announcements(zmanim)

    # print(zmanim)


build_announcements()