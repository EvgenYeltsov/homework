class Vehicle():
    def cover_distance(self, distance):
        raise NotImplementedError("Method should be realised")

    def set_avg_speed_ph(self, speed):
        self.avg_speed_ph = speed

    def formula_distance(self, distance, rnd=2):
        return round(distance / self.avg_speed_ph, rnd)

    def __lt__(self, vehicle):
        return self.avg_speed_ph < vehicle.avg_speed_ph

    def __eq__(self, vehicle):
        return self.avg_speed_ph == vehicle.avg_speed_ph

class Bike(Vehicle):

    def __init__(self, avg_speed_ph=25):
        self.avg_speed_ph = avg_speed_ph

    def cover_distance(self, distance):
        print(f"I am Bike.It takes me {self.formula_distance(distance)} hours")
        pass


class Car(Vehicle):

    def __init__(self, avg_speed_ph=80):
        self.avg_speed_ph = avg_speed_ph

    def cover_distance(self, distance):
        print(f"I am Care.It takes me {self.formula_distance(distance)} hours")
        pass

class Plane(Vehicle):

    def __init__(self, avg_speed_ph=130):
        self.avg_speed_ph = avg_speed_ph

    def cover_distance(self, distance):
        print(f"I am Plane.It takes me {self.formula_distance(distance)} hours")
        pass


bike = Bike()
bike1 = Bike()
car = Car()
plane = Plane()

# for veh in [bike, car, plane]:
#     veh.cover_distance(60)

for veh, speed in zip([bike, car, plane], [25, 120, 500]):
    veh.set_avg_speed_ph(speed)

for veh in [bike, car, plane]:
    veh.cover_distance(1000)

print(car > bike)
print(bike < plane)
print(bike == bike1)
