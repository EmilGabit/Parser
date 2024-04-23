import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

def get_parse():

    url = 'https://api.retailrocket.ru/api/2.0/recommendation/popular/5ecce55697a525075c900196/?&stockId=1&categoryIds=&categoryPaths=%D0%A1%D1%8B%D1%80%2F%D0%A2%D0%B2%D0%B5%D1%80%D0%B4%D1%8B%D0%B5%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D1%83%D1%82%D0%B2%D0%B5%D1%80%D0%B4%D1%8B%D0%B5&session=648b4af8cd70f2a251c7b0aa&pvid=532176104123204&isDebug=false&format=json'
    headers = {
        'accept' : '*/*',
        'accept-language' : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin' : 'https://www.auchan.ru',
        'referer' : 'https://www.auchan.ru/',
        'sec-ch-ua' : '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile' : '?1',
        'sec-ch-ua-platform' : 'Android',
        'sec-fetch-dest' : 'empty',
        'sec-fetch-mode' : 'cors',
        'sec-fetch-site' : 'cross-site',
        'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',

    }

    response = requests.get(url = url, headers = headers)

    return response.json()


def parser(response):
    product = {}
    c = 0
    for i in response:
        c += 1
        product[c] = {'id': i['ItemId'], 'name': i['Name'], 'price': i['Price'], 'old_price': i['OldPrice'],
                      'url': i['Url']}

    return product


def create_json(product,  file = str):

    file_path = file

    with open(file_path, 'w') as file:
        json.dump(product, file, indent=4)



def main():
    response = get_parse()
    produsts = parser(response)
    create_json(produsts, 'data_ashan.json')


if __name__ == '__main__':
    main()