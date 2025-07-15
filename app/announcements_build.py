from docx import Document
from datetime import datetime,date,timedelta

def write_announcements(zmanim):

    parsha = zmanim['parsha']
    document = Document()
    
    weekstart = zmanim['sunday']['english_date']# + timedelta(days=1) 
    #convert weekstart to date object
    weekstart = datetime.strptime(weekstart, '%B %d').date() + timedelta(days=1)  # Assuming week starts on Sunday
    weekend = weekstart + timedelta(days=4)
    weekstart = weekstart.strftime('%B %d')
    weekend = weekend.strftime('%B %d')
    print(weekstart, weekend)

    p = document.add_paragraph()
    p.add_run(f'Erev Shabbos, {zmanim['friday']['english_date']} ({zmanim['friday']['hebrew_date']})\n').underline = True
    p.add_run(f'{zmanim['friday']['plag_mincha']} Plag Mincha/Kabbalas Shabbos\n').bold = True
    p.add_run(f'Early Candle Lighting not before 6:55pm\n(The ideal time for Plag Candle Lighting is roughly 30 minutes after the start of Mincha)').italic = True
    p.add_run('\n')
    p.add_run(f'{zmanim['friday']['candle_lighting']} Candle Lighting/Mincha\n').bold = True
    p.add_run(f'{zmanim['friday']['shkia']} Shkia\n')
    q = document.add_paragraph()
    q.add_run(f'Shabbos, {zmanim['shabbos']['english_date']} ({zmanim['shabbos']['hebrew_date']})\n').underline = True
    q.add_run(f'{zmanim['shabbos']['shacharis']} Shacharis\n').bold = True
    q.add_run(f'{zmanim['shabbos']['zman_kriyas_shema']} Zman Kriyas Shema\n')
    q.add_run('\n')
    q.add_run('8:45am Youth Groups \n')
    q.add_run('9:30am Open Playroom for Toddlers \n')
    q.add_run('10:15am Mommy and Me (ages 4 and younger) \n')
    q.add_run('\n')
    q.add_run('Hot Kiddush\n').bold = True
    q.add_run('Thank you to our Kiddush Sponsors listed in the announcemnts!\n ')
    q.add_run('\n')
    q.add_run(f'{zmanim['shabbos']['mincha']} Mincha \n').bold = True
    q.add_run('Seudas Shelishis\n')
    q.add_run('Sponsored by _________').italic = True
    q.add_run('in honor of _________\n').italic = True
    q.add_run('Topic: _________\n').italic = True
    q.add_run('\n')
    q.add_run(f'{zmanim['shabbos']['shkia']} Shkia\n')
    q.add_run(f'{zmanim['shabbos']['eretz_yisrael_seder']} Eretz Yisrael Seder \n')
    q.add_run(f'{zmanim['shabbos']['havdalah']} Maariv/Havdalah\n').bold = True
    r = document.add_paragraph()
    r.add_run(f'Sunday, {zmanim['sunday']['english_date']} ({zmanim['sunday']['hebrew_date']})\n').underline = True
    r.add_run(f'{zmanim['sunday']['shacharis']} Shacharis\n').bold = True
    r.add_run('\n')
    r.add_run(f'{zmanim['sunday']['zman_kriyas_shema']} Zman Kriyas Shema\n')
    r.add_run('Halacha Shiur & Breakfast\n')
    r.add_run('Sponsored by Steven Friedman\n').italic = True
    r.add_run('לעילוי נשמת חיה רחל בת נחמן דוד שיבדל לחיים טובים').italic = True
    r.add_run('Topic: _________\n').italic = True
    s = document.add_paragraph()
    s.add_run('Weekday Shacharis ({weekstart} - {weekend}) ').underline = True
    s.add_run('6:30am').bold = True
    s.add_run('Pre-Shacharis Shiur with Rabbi Davis\n')
    s.add_run('Coffee and light breakfast served daily, sponsored by Yael & Uri Segelman\n').italic = True
    s.add_run('6:35am').bold = True 
    s.add_run('Monday and Thursday\n')
    s.add_run('6:45am Tuesday, Wednesday, and Friday\n')

    t = document.add_page_break()
    heading = t.add_run('Announcements\n')
    heading.bold = True
    heading.underline = True
    t.add_run('\n')
    t.add_run('Thank you to our Kiddush Sponsors this week:\n')
    t.add_run('\n')
    plat = t.add_run('Platinum Sponsorship\n')
    plat.bold = True
    plat.underline = True
    t.add_run('\n')
    gold = t.add_run('Gold Sponsorship\n')
    gold.bold = True
    gold.underline = True
    t.add_run('\n')
    silver = t.add_run('Silver Sponsorship\n')
    silver.bold = True
    silver.underline = True
    t.add_run('\n')
    bronze = t.add_run('Bronze Sponsorship\n')
    bronze.bold = True
    bronze.underline = True
    t.add_run('\n')
    sponsorship = t.add_run('Sponsorship\n')
    sponsorship.bold = True
    sponsorship.underline = True
    t.add_run('\n')
    t.add_run('*	*	*	*\n')
    # t.add_run('Thank you very much to all who have thus far made dedications to the Shul!\n').bold = True
    # t.add_run('For available dedications, please click ').bold = True
    # t.add_hyperlink('here', address="https://www.torahtemima.org/dedications").bold = True
    # t.add_run('.\n').bold=True
    # t.add_run('*	*	*	*\n')
    # t.add_run('\n')
    # links = t.add_run('KTT Links\n')
    # links.bold = True
    # links.underline = True
    # t.add_hyperlink('KTT Whatsapp Groups', address="https://www.torahtemima.org/whatsapp").bold = True
    # t.add_run('\n')
    # t.add_hyperlink('Kiddush Sponsorship', address="https://www.torahtemima.org/form/Weekly-kiddush-sponsorships1.html").bold = True
    # t.add_run('\n')
    # t.add_hyperlink('Youth Fund', address='https://www.torahtemima.org/youth-fund').bold = True
    # t.add_run('\n')
    # t.add_hyperlink('Monthly Calendar', address='https://www.torahtemima.org/monthlycalendar').bold = True
    # t.add_run('\n')
    # t.add_hyperlink('KTT Board', address='https://www.torahtemima.org/ktt-board').bold = True
    # t.add_run('\n')
    document.save(f'resources/{parsha.replace(' ','')}.docx')
