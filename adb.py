from os import system
import json

with open('ingres.json') as f:
    data = json.load(f)

points = []
for cuadrant in data['result']['map']:
    try:
        for entity in data['result']['map'][cuadrant]['gameEntities']:
            e = entity[2]
            if isinstance(e , list):
                # print "Third instance is list"
                if e[0] == u'p':
                    points.append([e[2]/1000000.0,e[3]/1000000.0,e[8]])
    except:
        continue

lat = 21.1025680275321
lon = -101.63976788520813
d   = 0.0000000001
loc = "adb shell am broadcast -a com.example.amotz.mockLocationForDeveloper.updateLocation  -e lat "+str(lat)+" -e lon "+str(lon)+"\n"

print lat, lon
system(loc)

while True:
    key = raw_input()
    if key == 'n':
        n = points.pop()
        lat = n[0]
        lon = n[1]
        print n[2]
    # if key == ',':
    #     lon += d
    # elif key == 'o':
    #     lon -= d
    # elif key == 'e':
    #     lat += d
    # elif key == 'a':
    #     lat -= d
    elif key == 'q':
        break
    loc = "adb shell am broadcast -a com.example.amotz.mockLocationForDeveloper.updateLocation  -e lat "+str(lat)+" -e lon "+str(lon)+"\n"
    print lat, lon
    system(loc)

system('adb  shell am broadcast -a com.example.amotz.mockLocationForDeveloper.stopMock')
