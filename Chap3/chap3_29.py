# encoding: utf-8

import requests
import chap3_28
import chap3_20


if __name__ == '__main__':
    eng_line = chap3_20.extract_nation_text('イギリス')
    tmp_dict = chap3_28.make_dict(eng_line.split('\n'))
    flag_name = tmp_dict['国旗画像']
    url = "https://en.wikipedia.org/w/api.php"
    params = {"action": "query",
              "titles": "File:"+flag_name,
              "prop": "imageinfo",
              "format": "json",
              "iiprop": "url"}
    flag_json = requests.get(url, params=params).json()
    print(flag_json['query']['pages']['23473560']['imageinfo'][0]['url'])
