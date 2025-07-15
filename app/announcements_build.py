from docx import Document
from datetime import date

def write_announcements(zmanim):

    week = date.today().isocalendar()[1]
    parsha = zmanim['parsha']
    document = Document(f'resources/{week}+{parsha.replace(' ','')}.docx')
    
    p = document.add_paragraph()
    p.add_run(f'Erev Shabbos, {zmanim['Friday']['English Date']} ({zmanim['Friday']['Hebrew Date']})').underline = True