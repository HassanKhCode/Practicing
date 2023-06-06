class Car:
    def __init__(self, man: str, mod: str, col: str, year, fuel_consumption, tank_capacity):
        self.manufacterer = man
        self.model = mod
        self.color = col
        self.year = year
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity
        self.km = 0
        self.fuel = 0
    def __str__(self):
        return f"{self.manufacterer}, {self.model}, {self.color}"

    def fill_tank(self, liters: int):
        if 0 < liters <= self.tank_capacity - self.fuel:
            self.fuel += liters
            return True
        return False

    def drive(self, km):
        if km > 0 and self.fuel * (100/self.fuel_consumption) >= km:
            self.km += km
            self.fuel -= (self.fuel_consumption/100) * km
            return True
        return False