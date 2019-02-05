import requests
from model.Price import Price
from bs4 import BeautifulSoup

def printDatePrice(url):

    dom = requests.get(url)
    dom.encoding = "utf-8"
    soup = BeautifulSoup(dom.text, 'html.parser')
    first_table = soup.find_all('table',class_='fundpagetable')

    #抓class=row1 or class=row2 然後分兩個陣列，前三個放a 後三個放b
    rows_first = first_table[1].find_all('tr',class_='row1')
    rows_secord = first_table[1].find_all('tr', class_='row2')

    rows = []
    targetList = []
    rows.extend(rows_first)
    rows.extend(rows_secord)

    for elemnet in rows:
        index = 0
        tds = elemnet.find_all('td')
        oldObject = Price()
        newObject = Price()

        for td in tds:
            if index == 0:
                oldObject.set_date(td.text)

            if index == 1:
                oldObject.set_price(td.text)

            if index == 3:
                newObject.set_date(td.text)

            if index == 4:
                newObject.set_price(td.text)

            index = index + 1

        targetList.append(oldObject)
        targetList.append(newObject)

    sortList = sorted(targetList ,key=lambda x : x._date ,reverse=False)

    return sortList

# if __name__ == '__main__':
#     list = printDatePrice('http://www.stockq.org/funds/fund/jf/J226.php')
#     for element in list:
#         print("data:"+ element._date)