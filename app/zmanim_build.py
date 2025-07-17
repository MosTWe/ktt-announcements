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

    zman_list = ["Plag Mincha", "Candle Lighting", "Shkia", "Shacharis", "Latest Shema", "Mincha", "Maariv", "Mommy and Me", "Youth Groups", "Eretz Yisrael Seder", "Havdalah"]
    calendar = calendar.loc[(calendar['Type']=="Parsha") | (calendar['Name'].isin(zman_list))]

    friday_day = dates[0].strftime('%B %d')
    shabbos_day = dates[1].strftime('%B %d')
    sunday_day = dates[2].strftime('%B %d')

    friday = calendar[calendar['English Date'] == friday_day]
    shabbos = calendar[calendar['English Date'] == shabbos_day]
    sunday = calendar[calendar['English Date'] == sunday_day]

    friday_dict = {
        "english_date": friday_day,
        "english_day": friday['English Day'].unique()[0],
        "english_ordinality": friday['English Ordinality'].unique()[0],
        "english_month": friday['English Month'].unique()[0],
        "hebrew_date": friday['Hebrew Date'].unique()[0],
        "hebrew_day": friday['Hebrew Day'].unique()[0],
        "hebrew_ordinality": friday['Hebrew Ordinality'].unique()[0],
        "hebrew_month": friday['Hebrew Month'].unique()[0],
        "early_shabbos": (friday[friday['Name'] == 'Plag Mincha']['Time'] - timedelta(minutes=20)).dt.strftime('%-I:%M %p').to_string(index=False),
        "plag_mincha": friday[friday['Name'] == 'Plag Mincha']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "candle_lighting": friday[friday['Name'] == 'Candle Lighting']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "shkia": friday[friday['Name'] == 'Shkia']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "shacharis": friday[friday['Name'] == 'Shacharis']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "maariv": friday[friday['Name'] == 'Maariv']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
    }
    print("Early Shabbos: ", friday_dict['early_shabbos'])
    shabbos_dict = {
        "english_date": shabbos_day,
        "english_day": shabbos['English Day'].unique()[0],
        "english_ordinality": shabbos['English Ordinality'].unique()[0],
        "english_month": shabbos['English Month'].unique()[0],
        "hebrew_date": shabbos['Hebrew Date'].unique()[0],
        "hebrew_day": shabbos['Hebrew Day'].unique()[0],
        "hebrew_ordinality": shabbos['Hebrew Ordinality'].unique()[0],
        "hebrew_month": shabbos['Hebrew Month'].unique()[0],
        "shacharis": shabbos[shabbos['Name'] == 'Shacharis']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "zman_kriyas_shema": shabbos[shabbos['Name'] == 'Latest Shema']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "mincha": shabbos[shabbos['Name'] == 'Mincha']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "shkia": shabbos[shabbos['Name'] == 'Shkia']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "havdalah": shabbos[shabbos['Name'] == 'Havdalah']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "maariv": shabbos[shabbos['Name'] == 'Maariv']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "mommy_and_me": shabbos[shabbos['Name'] == 'Mommy and Me']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "youth_groups": shabbos[shabbos['Name'] == 'Youth Groups']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "eretz_yisrael_seder": shabbos[shabbos['Name'] == 'Eretz Yisrael Seder']['Time'].dt.strftime('%-I:%M %p').to_string(index=False)
    }

    sunday_dict = {
        "english_date": sunday_day,
        "english_day": sunday['English Day'].unique()[0],
        "english_ordinality": sunday['English Ordinality'].unique()[0],
        "english_month": sunday['English Month'].unique()[0],
        "hebrew_date": sunday['Hebrew Date'].unique()[0],
        "hebrew_day": sunday['Hebrew Day'].unique()[0],
        "hebrew_ordinality": sunday['Hebrew Ordinality'].unique()[0],
        "hebrew_month": sunday['Hebrew Month'].unique()[0],
        "shacharis": sunday[sunday['Name'] == 'Shacharis']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "zman_kriyas_shema": sunday[sunday['Name'] == 'Latest Shema']['Time'].dt.strftime('%-I:%M %p').to_string(index=False),
        "maariv": sunday[sunday['Name'] == 'Maariv']['Time'].dt.strftime('%-I:%M %p').to_string(index=False)
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