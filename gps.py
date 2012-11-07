import random

def gpsGetLongLat():
    latitude = 0.0
    longitude = 0.0
    return longitude, latitude

class Waypoint(object):
    def __int__(self, latitude, longitude, name=''):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        

class Path(object):
    def __int__(self, name=''):
        self.waypoints = []
        self.name = name

    def add_waypoint(self, waypoint):
        self.waypoints.append(waypoint)



w1 = Waypoint(0, 0)
print w1.latitude
print w1.longitude
print w1.name
w1.latitude = 40
print w1.latitude

w2 = Waypoint(39.83333, -98.5833)
w2 = 'Middle of the USA'

w3 = Waypoint(40.0755, -76.3299, 'Olivet, MI')

w4 = Waypoint(3, 5)
w5 =(3, 8, 'right here')

p1 = Path('Here to Lebanon, KS')
p1.add_waypoint(w3)
p1.add_waypoint(w2)

p2 = Path('Here and Back Again')
p2.add_waypoint(w3)
p2.add_waypoint(w2)
p2.add_waypoint(w3)
