# -*- coding:utf-8 -*-

import requests
import json

# https://www.starbucks.co.kr


def getSiDo():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)

    sido_json = resp.json()['list']
    sido_code = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    sido_dict = dict(zip(sido_code, sido_name))
    return sido_dict


def getGuGun(sido_code):
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url, data={'sido_cd': sido_code})
    gugun_json = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)),
                          list(map(lambda x: x['gugun_nm'], gugun_json))))
    return gugun_dict


def getStore(sido_code='', gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={
        'ins_lat' : '37.56682',
        'ins_lng': '126.97685',
        'p_sido_cd' : sido_code,
        'p_gugun_cd' : gugun_code,
        'in_biz_cd' : '',
        'set_date' : ''
    })

    store_json = resp.json()['list']
    store_dict = dict()
    store_list = list()
    stroe_list_dict = dict()
    count = 0
    for store in store_json:
        store_dict = {'s_name': store['s_name'], 'doro_address': store['doro_address'], 'lat': store['lat'], 'lot': store['lot']}
        store_list.append(store_dict)
        count += 1

    stroe_list_dict['store_list'] = store_list
    stroe_list_dict['count'] = count

    store_list_dict_json = json.dumps(stroe_list_dict, ensure_ascii=False)

    return store_list_dict_json

if __name__ == '__main__':
    print(getSiDo())

    sido = input('도시 코드 : ')
    if sido == '17':
        pass
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드 : ')
        print(getStore(gugun_code=gugun))