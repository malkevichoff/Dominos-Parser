from pprint import pprint

import requests
import json


def get_json(url):
    req = requests.get(url)
    todos = json.loads(req.text)
    return todos


def write_json(data):
    with open('result2.json', 'a') as result_file:
        result_file.write(json.dumps(data, indent=4))


alist = []


def get_page_data(json):
    for i in json['entities']['modifications'].keys():
        alist.append(i)

    for i in alist:
        title = (json['entities']['modifications'][str(i)]['title'])
        weight = (json['entities']['modifications'][str(i)]['weight']['formatted'])
        price = (json['entities']['modifications'][str(i)]['price']['formatted'])
        size = (json['entities']['modifications'][str(i)]['size']['formatted'])
        print(json['entities']['modifications'][str(i)]['nutritionalInfo'].keys())
        proteins = (json['entities']['modifications'][str(i)]['nutritionalInfo']['proteins']['value'])
        carbohydrates = (json['entities']['modifications'][str(i)]['nutritionalInfo']['carbohydrates']['value'])
        nutritionalvalue = (json['entities']["modifications"][str(i)]['nutritionalInfo']['nutritionalValue']['value'])

        data = {'title': title,
                'weight': weight,
                'price': price,
                'size': size,
                'proteins': proteins,
                'carbohydrates': carbohydrates,
                'nutritionalValue': nutritionalvalue}

        write_json(data)


def main():
    url = 'https://dominos.by/web-api/products?city_id=2&lang=ru'
    json = get_json(url)
    get_page_data(json)


if __name__ == '__main__':
    main()