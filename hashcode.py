import copy

class Ride:
    def __init__(self, id, startX, startY, finishX, finishY, earliestTime, latestTime):
        self.id = id
        self.startX = startX
        self.startY = startY
        self.finishX = finishX
        self.finishY = finishY
        self.earliestTime = earliestTime
        self.latestTime = latestTime

    def distance(self):
        distanceX = abs(self.startX-self.finishX)
        distanceY = abs(self.startY-self.finishY)
        return distanceY+distanceX



class Car:
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0
        self.rides = []
        self.chosedRides = []
        self.counter = 0

    def distance_to_start_ride(self, ride):
        distanceX = abs(ride.startX-self.x)
        distanceY = abs(ride.startY-self.y)
        return distanceY+distanceX

    def choose_ride(self, r1, r2):
        rideTotal1 = r.distance + self.distance_to_start_ride(r1)
        rideTotal2 = r.distance + self.distance_to_start_ride(r2)

        if(rideTotal1>rideTotal2): return rideTotal1
        else: return rideTotal2

    def remove_rides(self, remainingSteps, actualStep):
        ridesCopy = copy.copy(self.rides)
        for ride in ridesCopy:
            if(self.distance_to_start_ride(ride)+ride.distance()>=remainingSteps
                    or ride.latestTime<=actualStep): self.rides.remove(ride);


file  = open("inputs/a_example.in", "r")
lines=[]
for line in file:
    lines.append(line)


rows, columns, vehiclesNum, ridesNum, bonus, steps = lines[0].split(" ")
allRides = []
vehicles = []

for index, ln in enumerate(lines[1:]):
    startX, startY, finishX, finishY, earliestTime, latestTime = ln.split(" ")
    ride = Ride(index, startX, startY, finishX, finishY, earliestTime, latestTime)
    allRides.append(ride)

for i in range(0, vehiclesNum):
    car = Car(i)
    vehicles.append(car)


'''STEPS'''
for s in range(steps):
    if not rides:
        break
    remaining_steps = steps-s

    for car in vehicles:
        car.rides = copy.copy(allRides)
        car.remove_rides(remaining_steps, s)
        '''sort rides'''
