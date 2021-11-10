class Vehicle:

    def cover_distance(self, distance):
        raise NotImplementedError("Abstract method should be implemented")

    def set_avg_speed_ph(self, speed):
        self._avg_speed_ph = speed

    def _cover_distance_formula(self, distance, rnd=2):
        return round(distance / self._avg_speed_ph, rnd)

class Bike(Vehicle):

    def __init__(self, avg_speed_ph=25):
        self._avg_speed_ph = avg_speed_ph

    def cover_distance(self, distance):
        return f"I am a bike. It takes me about {self._cover_distance_formula(distance)} hours"


# bike = Bike()
#
# bike.cover_distance(15)
# bike.set_avg_speed_ph(20)
# bike.cover_distance(15)
