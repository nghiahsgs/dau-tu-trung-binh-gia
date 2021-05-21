import pandas as pd
import datetime


# df = pd.read_csv('GOLD_raw.csv')
df = pd.read_csv('BTC_raw.csv')
df.Date =  pd.to_datetime(df.Date)

while True:
    L_Date = list(df['Date'])
    L_Open = list(df['Open'])
    L_High = list(df['High'])
    L_Low = list(df['Low'])
    L_Close = list(df['Close'])
    L_Volume = list(df['Volume'])

    is_break = False
    for i_row in range(1,df.shape[0]):
        delta_day = (df.iloc[i_row,:].Date-df.iloc[i_row-1,:].Date).days
        if delta_day>1:
            print('i_row',i_row,'delta_day',delta_day)
            new_date = L_Date[i_row-1]+datetime.timedelta(days = 1)
            L_Date.insert(i_row,new_date)
            L_Open.insert(i_row,L_Open[i_row-1])
            L_High.insert(i_row,L_High[i_row-1])
            L_Low.insert(i_row,L_Low[i_row-1])
            L_Close.insert(i_row,L_Close[i_row-1])
            L_Volume.insert(i_row,L_Volume[i_row-1])
            is_break = True
            break

    df = pd.DataFrame.from_dict({
        'Date':L_Date,
        'Open':L_Open,
        'High':L_High,
        'Low':L_Low,
        'Close':L_Close,
        'Volume':L_Volume
    })
    if not is_break:
        break



# df.to_csv('GOLD.csv')
df.to_csv('BTC.csv')