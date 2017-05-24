# encoding: utf-8

import gzip
import json


def extract_nation_text(nation_name):
    with gzip.open('jawiki-country.json.gz', 'r') as jawiki:
        for line in jawiki:
            wiki_dict = json.loads(line.strip(), encoding='utf-8')
            if wiki_dict['title'] == nation_name:
                return wiki_dict['text']
    #return list(filter(lambda x: x['title'] == nation_name, [json.loads(line.strip(), encoding='utf-8') for line in gzip.open('jawiki-country.json.gz', 'r')]))[0]['text']


if __name__ == '__main__':
    print(extract_nation_text('イギリス'))
