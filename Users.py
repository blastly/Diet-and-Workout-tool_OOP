import sqlite3
import operator
import functools

dbase2 = sqlite3.connect('Users.db')
c2 = dbase2.cursor()


class Users:

    authentication_result = 0
    username = ''
    password = ''

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        c2.execute('''SELECT password FROM Users WHERE username = ?''', [self.username])
        search_result = c2.fetchone()

        if search_result is None:
            # print('wrong username, you are not yet a member of this tool')
            self.authentication_result = 1

        else:
            search_result = functools.reduce(operator.add, search_result)
            if search_result == self.password:
                # print('you are logged in YAY!')
                self.authentication_result = 2
            else:
                # print('wrong password try again')
                self.authentication_result = 3

        return self.authentication_result

# D = Users()
# D.get_username()
# D.authenticate()
# print(D.u)
