import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
#атрибуты
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.thirst = 10
#методы
    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5


    def drink(self):
        if self.home.water <= 0:
            self.shopping("water")
            self.thirst -= 20
            self.home.water -= 5


    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                self.shopping("Fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Бензин")
            self.money -= 100
            self.car.fuel = 100
        elif manage == "food":
            print("Жраточки")
            self.money -= 50
            self.home.food += 50
        elif manage == "water":
            print("Водаааа")
            self.money -= 5
            self.home.water += 5





    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                self.shopping("Fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.glad
        self.satiety -= 5
        self.thirst -= 2


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


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.glad = job_list[self.job]["glad"]


job_list = {"Python dev": {"salary": 50, "glad": 12},
            "C++ dev": {"salary": 80, "glad": 6},
            "Php dev": {"salary": 35, "glad": 2}}#

brands_of_car = {"BMW": {"fuel": 100, "strength": 120, "consumption": 14},
                 "Porsche": {"fuel": 170, "strength": 90, "consumption": 99},
                 "Ferrari": {"fuel": 10, "strength": 100, "consumption": 11},
                 "Lamborghini": {"fuel": 60, "strength": 20, "consumption": 1991}}


#h = Human("Volodya")
#h.get_home()
#print(h.job)
#h.get_job()
#print(h.job.job)
