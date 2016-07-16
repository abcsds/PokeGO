import telnetlib

HOST = "192.168.1.67"
PORT = 5554

tn = telnetlib.Telnet(HOST,PORT)

lat = -101.63976788520813
lon = 21.1025680275321
d   = 0.000000001
loc = "geo fix "+str(lat)+" "+str(lon)+"\n"

tn.read_until('OK')
print "OK"
tn.write(loc)

while True:
    key = raw_input()
    if key == ',':
        lon += d
    elif key == 'o':
        lon -= d
    elif key == 'e':
        lat += d
    elif key == 'a':
        lat -= d
    elif key == 'q':
        break
    loc = "geo fix "+str(lat)+" "+str(lon)+"\n"
    print loc
    tn.write(loc)
    tn.read_until('OK')
    print "OK"


print tn.read_all()
