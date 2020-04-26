import sqlite3

dbase = sqlite3.connect('Food_and_Exercises.db')
dbase1 = sqlite3.connect('My_Diet_and_Workout_info.db')
c = dbase.cursor()
c1 = dbase1.cursor()


class Fooditem:

    def __init__(self, resultset):
        self.fooditem = resultset

    def calculate(self):
        servings = int(input('enter the number of servings you ate:'))
        self.fooditem[0] = list(self.fooditem[0])
        self.fooditem[0][1] = self.fooditem[0][1] * servings
        self.fooditem[0][2] = self.fooditem[0][2] * servings
        self.fooditem[0][3] = self.fooditem[0][3] * servings
        self.fooditem[0][4] = self.fooditem[0][4] * servings
        self.fooditem[0][5] = self.fooditem[0][5] * servings
        self.fooditem[0][6] = self.fooditem[0][6] * servings
        self.fooditem[0][7] = self.fooditem[0][7] * servings
        self.fooditem[0] = tuple(self.fooditem[0])

    def insert_into_db(self):
        c1.executemany('insert into myDiet_info values (?,?,?,?,?,?,?,?)', self.fooditem)
        dbase1.commit()


class Exercise:

    def __init__(self, exercise_info):
        self.exercise_info = exercise_info

    def insert(self):
        c1.executemany('insert into myWorkout_info values (?,?)', self.exercise_info)
        dbase1.commit()
