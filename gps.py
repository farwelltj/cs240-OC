import random
import math

def gpsGetLongLat():
    longitude = (random.random() * 360) - 180
    latitude = 0.0
    return longitude, latitude

class Waypoint(object):
    def __init__(self, latitude, longitude, name=''):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

class Path(object):
    def __init__(self, name =''):
        self.waypoints = []
        self.name = name

    def add_waypoint(self, waypoint):
        self.waypoints.append(waypoint)

    def distance(self):
        radius = 6371 #kilometers

        if len(self.waypoints) < 2:
            return 0
        distance1 = 0
        
        for index in range(1,len(self.waypoints)):
            w1=self.waypoints[index-1]
            w2=self.waypoints[index]
            
            #Converts our coordinates into radians
            distancelatitude = math.radians(w2.latitude-w1.latitude)
            distancelongitude = math.radians(w2.longitude-w1.longitude)
            a = math.sin(distancelatitude/2) * math.sin(distancelatitude/2) + math.cos(math.radians(w1.latitude)) \
            * math.cos(math.radians(w2.latitude)) * math.sin(distancelongitude/2) * math.sin(distancelongitude/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            distance1 += radius * c
        return distance1


w1 = Waypoint(0, 0)
print w1.latitude # display 0
print w1.longitude # display 0
print w1.name # display ''
w1.latitude = 40
print w1.latitude # display 40

w2 = Waypoint(39.83333, -98.5833, 'Middle of the USA')
w3 = Waypoint(40.0755, -76.3299, 'Olivet, MI')
w4 = Waypoint(3, 5, 'Mexico')
w5 = Waypoint(3, 8, 'Right Here')

p1 = Path('Here to Lebanon, KS')
p1.add_waypoint(w3)
p1.add_waypoint(w2)

p2 = Path('Here and Back Again')
p2.add_waypoint(w4)
p2.add_waypoint(w1)

p3 = Path('Taco Stand')
p3.add_waypoint(w1)
p3.add_waypoint(w5)

print p1.distance()
print p2.distance()
print p3.distance()

