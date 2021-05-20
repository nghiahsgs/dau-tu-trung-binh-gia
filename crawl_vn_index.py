import requests
import pandas as pd
from high_order_framework_requests_python import utils_class

string_Interact1 = utils_class.String_Interact()

list_date = []
list_price = []

for i_page in range(1,51+1):
    print('i_page',i_page)
    #B1: get data
    url  = 'https://www.cophieu68.vn/historyprice.php?currentPage=%s&id=^vnindex'%i_page

    headers= {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }
    data = requests.get(url,verify=False).text

    #B2: tach data
    listCSSSelector = [
        '.stock tr'
    ]
    listeAttr = [
        'innerHTML'
    ]
    list_row, = string_Interact1.extractListTextByCSSSelector(data,listCSSSelector,listeAttr)
    list_row = list_row[1:]

    for row in list_row:
        listCSSSelector = [
            'td'
        ]
        listeAttr = [
            'innerText'
        ]
        list_col, = string_Interact1.extractListTextByCSSSelector(row,listCSSSelector,listeAttr)
        list_date.append(list_col[1])
        list_price.append(list_col[2])

df = pd.DataFrame.from_dict({'date':list_date,'price':list_price})
df['date'] = pd.to_datetime(df['date'])
# df.set_index('date',inplace=True)

# df['2011-05-20':'2021-05-20']

# df['2021-05']

import datetime
start_time_str = '2011-05-20 00:00:00'
start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
end_time_str = '2021-05-20 00:00:00'
end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
df[df['date']>start_time]