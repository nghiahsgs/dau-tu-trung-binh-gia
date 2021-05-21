import pandas as pd
import datetime
import matplotlib.pyplot as plt


folder_save = "BTC"
# folder_save = "GOLD"
file_csv = '%s.csv'%folder_save

df = pd.read_csv(file_csv)
df.Date =  pd.to_datetime(df.Date)




usd_bank = 0
usd_amount = 0
btc_amount  = 0
trade_amount = 250 # khoang 7 tr vao thi truong
intest_bank = 0.06 # lai ngan hang la 6% 1 nam

L_usd_bank = []
L_usd_amount = []
L_btc_amount = []
L_btc_value = []
for i_row in range(df.shape[0]):
    Date = df.iloc[i_row,:].Date
    Open = df.iloc[i_row,:].Open
    # neu la ngay nhan luong
    if Date.day == 10:
        usd_amount+=trade_amount
        btc_amount+=trade_amount/Open
    # neu do la ngay 20/5 hang nam, nap them tien vao bank
    if Date.day == 20 and Date.month == 5:
        usd_bank+=intest_bank*usd_bank+trade_amount*12
    
    L_usd_bank.append(usd_bank)
    L_usd_amount.append(usd_amount)
    L_btc_amount.append(btc_amount)
    L_btc_value.append(btc_amount*Open)

df['usd_bank'] = L_usd_bank
df['usd_amount'] = L_usd_amount
df['btc_amount'] = L_btc_amount
df['btc_value'] = L_btc_value

# ve do thi
# df = df.set_index('Date')
fig = plt.figure()
plt.plot(df['Date'],df['Open'])
fig.suptitle('Giá cổ phiếu theo thời gian', fontsize=12)
plt.xlabel('Thời gian', fontsize=12)
plt.ylabel('Giá trị theo USD', fontsize=12)
plt.savefig('%s/Open.jpg'%folder_save)


fig = plt.figure()
plt.plot(df['Date'],df['usd_bank'])
fig.suptitle('Tiền trong ngân hàng theo thời gian, lãi suất 6% 1 năm (có cả lãi kép)', fontsize=12)
plt.xlabel('Thời gian', fontsize=12)
plt.ylabel('Tiền của bạn', fontsize=12)
plt.savefig('%s/usd_bank.jpg'%folder_save)

fig = plt.figure()
plt.plot(df['Date'],df['usd_amount'])
fig.suptitle('Tiền nếu chỉ thuần tiết kiệm, không đầu tư', fontsize=12)
plt.xlabel('Thời gian', fontsize=12)
plt.ylabel('Tiền của bạn', fontsize=12)
plt.savefig('%s/usd_amount.jpg'%folder_save)


fig = plt.figure()
plt.plot(df['Date'],df['btc_amount'])
fig.suptitle('Số lượng cổ phiếu tích lũy được theo thời gian', fontsize=12)
plt.xlabel('Thời gian', fontsize=12)
plt.ylabel('Số lượng cổ phiếu', fontsize=12)
plt.savefig('%s/btc_amount.jpg'%folder_save)


fig = plt.figure()
plt.plot(df['Date'],df['btc_value'])
fig.suptitle('Tiền đầu tư kiếm được', fontsize=12)
plt.xlabel('Thời gian', fontsize=12)
plt.ylabel('Tiền của bạn', fontsize=12)
plt.savefig('%s/btc_value.jpg'%folder_save)