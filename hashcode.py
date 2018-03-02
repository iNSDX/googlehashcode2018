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
        rideTotal1 = r1.distance + self.distance_to_start_ride(r1)
        rideTotal2 = r2.distance + self.distance_to_start_ride(r2)

        if(rideTotal1>rideTotal2): return rideTotal1
        else: return rideTotal2

    def get_total_distance_ride(self, ride):
        return ride.distance() + self.distance_to_start_ride(ride)

    def remove_rides(self, remainingSteps, actualStep):
        ridesCopy = copy.copy(self.rides)
        for ride in ridesCopy:
            if(self.distance_to_start_ride(ride)+ride.distance()>=remainingSteps
                    or ride.latestTime<=actualStep): self.rides.remove(ride);


file  = open("inputs/c_no_hurry.in", "r")
lines=[]
for line in file:
    lines.append(line)


rows, columns, vehiclesNum, ridesNum, bonus, steps = lines[0].split(" ")
rows = int(rows)
columns = int(columns)
vehiclesNum = int(vehiclesNum)
ridesNum = int(ridesNum)
bonus = int(steps)

allRides = []
vehicles = []

for index, ln in enumerate(lines[1:]):
    startX, startY, finishX, finishY, earliestTime, latestTime = ln.split(" ")
    startX = int(startX)
    startY = int(startY)
    finishX = int(finishX)
    finishY = int(finishY)
    earliestTime = int(earliestTime)
    latestTime = int(latestTime)
    
    ride = Ride(index, startX, startY, finishX, finishY, earliestTime, latestTime)
    allRides.append(ride)

for i in range(0, int(vehiclesNum)):
    car = Car(i)
    vehicles.append(car)


'''STEPS'''
for s in range(int(steps)):
    if not allRides:
        break
    remaining_steps = int(steps)-s

    for car in vehicles:
        car.rides = copy.copy(allRides)
        car.remove_rides(remaining_steps, s)
        sorted(car.rides, key=lambda ride: car.get_total_distance_ride(ride))
        if(car.counter == 0 and car.rides):
            chosed = car.rides[0]
            car.chosedRides.append(chosed)
            allRides.remove(chosed)
            car.x = chosed.finishX
            car.y = chosed.finishY
            car.counter = car.distance_to_start_ride(chosed)+ chosed.distance()
        car.counter = car.counter -1

writter  = open("inputs/c_no_hurry_output.in", "w")
for car in vehicles:
    ln = repr(len(car.chosedRides))
    for ride in car.chosedRides:
        ln = ln +" " + repr(ride.id)
    writter.write(ln + "\n")