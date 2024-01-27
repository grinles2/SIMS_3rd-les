import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_house(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand["strength"]]
        self.consumption = brand_list[self.brand]["Consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car broke down")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.water_bill = 0
        self.energy_bill = 0
        self.gas_bill = 0


brands_of_car = {"BMW": {"fuel": 100, "strength": 120, "consumption": 14},
                 "Porsche": {"fuel": 170, "strength": 90, "consumption": 99},
                 "Ferrari": {"fuel": 10, "strength": 100, "consumption": 11},
                 "Lamborghini": {"fuel": 60, "strength": 20, "consumption": 1991}}
