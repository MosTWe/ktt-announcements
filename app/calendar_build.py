import pandas as pd

def get_calendar_data(filename):
    df = pd.read_csv(f'resources/{filename}.csv')

    df = df[['Type','Name','Start','Hebrew Date']]
    df['Start'] = pd.to_datetime(df['Start'], format='mixed', dayfirst=True)
    df['English Date'] = df['Start'].dt.strftime('%B %d')
    df['Time'] = df['Start'].dt.strftime('%-I:%M %p')
    
    return df[['Type', 'Name', 'English Date', 'Hebrew Date', 'Time']]

