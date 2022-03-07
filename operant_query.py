###Packages###
import os
import requests
import yaml
import parse
import numpy as np
import json
import csv
###Create URL with Parameters from Yaml file###
with open(r'operant_data_query.yml') as file:
    query_parameters=yaml.safe_load(file)
parameters = query_parameters['query']
base_url = query_parameters['base_url']
info = requests.get(base_url, params = parameters)
url = info.url
data = info.text
info_json = json.loads(data)
keys = list(info_json[0])

###Pull Data to Json File###
with open ('{}.csv'.format(query_parameters['query']['subject']),'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys, extrasaction = 'ignore')
    writer.writeheader()
    n = 1
    while n < 2:
        r = requests.get(url)
        print (r.url)
        data = r.text
        parse_json = json.loads(data)
        writer.writerows(parse_json)
        if r.links.get('next') is None:
            break
        else:
            url = r.links['next']['url']
