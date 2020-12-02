# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:10:32 2020

@author: user
"""
import numpy as np
import json

with open('D:\\predict1.json') as f:
    data = json.load(f)
with open('D:\\test.json') as f:
    test = json.load(f)
file_name = test['images']
for i in range(0, 100):
    f = data[i]['image_id']   
    for j in range(0, 100):
        ff = file_name[j]['file_name']
        if (f == ff[0:-4]):
            data[i]['image_id'] = file_name[j]['id']

json_file = []        
for i in range(0, 100):
    out = {}
    if(len(data[i]['score']) == 1):
        out['image_id'] = data[i]['image_id']
        out['score'] = float(np.asarray(data[i]['score']))
        out['category_id'] =int(np.asarray(data[i]['category_id']))
        out['segmentation'] = data[i]['segmentation']
        
        json_file.append(out)
    else:
        for j in range(len(data[i]['score'])):
            out['image_id'] = data[i]['image_id']
            out['score'] = float(np.asarray(data[i]['score'][j]))
            out['category_id'] = int(np.asarray(data[i]['category_id'][j]))
            out['segmentation']= data[i]['segmentation'][j]
            json_file.append(out)
            
with open('D:\\309551033_1.json', 'w') as f:
    json.dump(json_file, f)
