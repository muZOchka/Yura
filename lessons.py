import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladnes = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladnes -= 3


    def to_sleep(self):
        print("Time to sleep")
        self.gladnes += 3



    def to_chill(self):
        print("Time to chill")
        self.progress -= 0.1
        self.gladnes += 5




    def is_alive (self):
        if self.progress < -0.5:
            print("Cats out")
            self.alive = False
        elif self.gladnes <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Pass externally...")
            self.alive = False


    def end_of_day(self):
        print(f"Gladeness = {self.gladnes}")
        print(f"Progress = {round(self.progress, 2)}")



    def live(self, Day):
        day = "Day" + str(Day) + "of" + self.name + "life"
        print(f'{Day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()



stuent1 = Student(name="Vasya")


for day in range(365):
    if stuent1.alive == False:
        break
    stuent1.live(day)

