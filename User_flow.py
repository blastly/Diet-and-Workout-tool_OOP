from Users import*
from fw import *


print('enter your username ans password')
print('you have three tries')


def get_username():
    username = input('enter your username:')
    password = input('enter your password:')
    return username, password


for i in range(0, 3):
    (user_name, pass_word) = get_username()
    user_object = Users(user_name, pass_word)
    authentication_result = user_object.authenticate()
    if authentication_result == 2:
        print('You have logged in YAY!')
        break
    else:
        print('wrong username or password')
        continue

print('Press 1 to enter fooditem you ate')
print('Press 2 to enter exercise you did')
print('Press 3 to view your Diet info')
print('Press 4 to view your Workout info')

Press_number = int(input('enter number:'))

if Press_number == 1:

    no_of_items = int(input('enter the number of fooditems you ate:'))

    for i in range(0, no_of_items):

        def take_user_input():

            result = 0
            fooditem = ''
            user_input = input('enter an item:')
            c.execute('''SELECT content FROM Food WHERE content = ?''', [user_input])
            search_result = c.fetchone()
            if search_result is None:
                result = 1
            else:
                c.execute('''SELECT * FROM Food WHERE content = ?''', [user_input])
                fooditem = c.fetchall()

            return result, fooditem

        (res_ult, food_item) = take_user_input()
        if res_ult == 1:
            print('No such fooditem found in our database')
        else:
            fooditem_object = Fooditem(food_item)
            fooditem_object.calculate()
            fooditem_object.insert_into_db()


elif Press_number == 2:

    no_of_exercises = int(input('enter the number of exercises you have done:'))

    for a in range(0, no_of_exercises):
        def get_exercise_info():
            exercise_info = ''
            resul_tant = 0
            exercise_name = input('enter your exercise:')
            c.execute('''SELECT exercise_name FROM Exercises WHERE exercise_name = ?''', [exercise_name])
            result = c.fetchone()
            if result is None:
                resul_tant = 1
            else:
                c.execute('''SELECT * FROM Exercises WHERE exercise_name = ?''', [exercise_name])
                exercise_info = c.fetchall()

            return resul_tant, exercise_info


        (resultant, exer_info) = get_exercise_info()
        if resultant == 1:
            print('No such exercise found in our database')
        else:
            obj = Exercise(exer_info)
            obj.insert()

elif Press_number == 3:
    c1.execute('SELECT* FROM myDiet_info')
    s = (c1.fetchall())
    for i in s:
        print(i)

elif Press_number == 4:
    c1.execute('SELECT* FROM myWorkout_info')
    s = (c1.fetchall())
    for i in s:
        print(i)

else:
    print('you have entered wrong number')
