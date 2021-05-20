import requests
import pandas
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

df = pandas.DataFrame.from_dict({'data':list_date,'price':list_price})