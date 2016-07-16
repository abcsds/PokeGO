import json

with open('ingres.json') as f:
    data = json.load(f)

for cuadrant in data['result']['map']:
    try:
        for entity in data['result']['map'][cuadrant]['gameEntities']:
            e = entity[2]
            if isinstance(e , list):
                # print "Third instance is list"
                if e[0] == u'p':
                    print e[8]
                    print e[2],e[3]

    except:
        continue
