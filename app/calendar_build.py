import pandas as pd

def get_calendar_data(filename):
    df = pd.read_csv(f'resources/{filename}.csv')

    def ordinal_day(day):
        day=str(day)
        # To give: 1st, 2nd, 3rd, 21st, 22nd, 23rd, 31st, BUT 'th' for 11th, 12th, 13th, etc.
        suffix={'1':'st', '2':'nd', '3':'rd', '21':'st', '22':'nd', '23':'rd', '31':'st'}.get(day,'th')
        return suffix

    

    df = df[['Type','Name','Start','Hebrew Date']]
    df['Start'] = pd.to_datetime(df['Start'], format='mixed', dayfirst=True)
    df['English Date'] = df['Start'].dt.strftime('%B %d')
    df['English Month'] = df['Start'].dt.strftime('%B')
    df['English Day'] = df['Start'].dt.strftime('%-d')
    df['English Ordinality'] = df['English Day'].apply(lambda x: ordinal_day(x))
    df['Hebrew Date'] = df['Hebrew Date'].apply(lambda x: ' '.join(x.split(' ')[0:2]).strip())
    df['Hebrew Day'] = df['Hebrew Date'].apply(lambda x: x.split(' ')[0].strip())
    df['Hebrew Ordinality'] = df['Hebrew Day'].apply(lambda x: ordinal_day(x))
    df['Hebrew Month'] = df['Hebrew Date'].apply(lambda x: x.split(' ')[1].strip())
    df['Time'] = df['Start']

    return df[['Type', 'Name', 'English Date', 'English Day', 'English Ordinality', 'English Month', 'Hebrew Date', 'Hebrew Day', 'Hebrew Ordinality', 'Hebrew Month', 'Time']]

