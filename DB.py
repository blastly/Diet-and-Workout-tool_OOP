import sqlite3

# Create database
dbase = sqlite3.connect('Food_and_Exercises.db')
dbase1 = sqlite3.connect('My_Diet_and_Workout_info.db')
dbase2 = sqlite3.connect('Users.db')

# cursor
c = dbase.cursor()
c1 = dbase1.cursor()
c2 = dbase2.cursor()
# Create tables in database1

dbase.execute(''' CREATE TABLE Food
                                (content text,
                                carbohydrates integer,
                                fats integer,
                                fiber integer,
                                minerals integer,
                                proteins integer,
                                vitamins integer,
                                calories integer
                                )''')


dbase.execute(''' CREATE TABLE Exercises
                              (exercise_name text,
                              calories integer
                              )''')

# insert into table using function


def insert_record(content, carbohydrates, fats, fiber, minerals, proteins, vitamins, calories):
    dbase.execute('''INSERT INTO Food
                   VALUES (?,?,?,?,?,?,?,?) ''', (content, carbohydrates, fats, fiber, minerals, proteins, vitamins,
                                                  calories))


def insert(exercise_name, calories):
    dbase.execute('''INSERT INTO Exercises
                       VALUES (?,?) ''', (exercise_name, calories))


# Create tables in database2

dbase1.execute(''' CREATE TABLE myDiet_info
                                (content text,
                                total_carbohydrates integer,
                                total_fats consumed integer,
                                total_fiber consumed integer,
                                total_minerals consumed integer,
                                total_proteins consumed integer,
                                total_vitamins consumed integer,
                                total_calories consumed integer
                                )''')


dbase1.execute(''' CREATE TABLE myWorkout_info
                                (exercise_name text,
                                total_calories burnt integer
                                 )''')

# Create tables in database3

dbase2.execute(''' CREATE TABLE Users
                                (username text,
                                password text,
                                gender text,
                                age integer,
                                weight integer
                                )''')


def insert_record1(username, password, gender, age, weight):
    dbase2.execute('''INSERT INTO Users
                   VALUES (?,?,?,?,?) ''', (username, password, gender, age, weight))


insert_record('butter', 5, 6, 2, 8, 9, 9, 10)
insert_record('curd', 8, 3, 6, 2, 9, 6, 9)
insert_record('rice', 10, 7, 4, 8, 3, 9, 20)
insert_record('sambar', 9, 8, 4, 7, 10, 16, 20)
insert_record('dal', 8, 4, 6, 9, 5, 6, 10)
insert_record('kulcha', 10, 5, 9, 20, 6, 9, 10)
insert_record('chappati', 5, 6, 10, 7, 8, 9, 10)
insert_record('broccoli', 6, 8, 3, 10, 1, 9, 9)
insert_record('egg', 5, 7, 9, 4, 8, 9, 10)
insert_record('paneer', 4, 8, 6, 8, 10, 15, 20)

insert('pushups', 30)
insert('pullups', 35)
insert('bicep curls', 35)
insert('tricep curls', 35)
insert('squats', 30)
insert('lunges', 40)
insert('jogging', 100)
insert('sprinting', 200)

insert_record1('sumukh', 'sums', 'male', 23, 65)
insert_record1('manjula', 'mom', 'female', 53, 65)
insert_record1('suresh', 'dad', 'male', 58, 65)

dbase.commit()
dbase1.commit()
dbase2.commit()
