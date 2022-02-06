import pprint
import json
import pandas as pd
with open('nber.json', 'r') as f:
        qe = json.load(f)



url=[]
source_name=[]
title=[]
for d in qe:
    v= d['results']

    for key in v:
        url.append(key['source']['url'])
        source_name.append(key['source']['title'])
        title.append(key['title'])

        # print(url,source_name,title)

# info=[title,url,source_name]
# print(info)

#         # z=key['source']
#         # for x in z:
#         #     print(x['title'])

df = pd.DataFrame(list(zip(title,url,source_name)),
               columns =['title', 'url','source_name'])
df.to_excel('CB_datasheet_NBER_20Aug.xlsx')