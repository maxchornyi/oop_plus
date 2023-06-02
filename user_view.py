class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.login_attempts=0
    def describe_user(self):
        print(self.first_name,self.last_name)
    def greeting_user(self):
        print('Welcome',self.first_name,self.last_name,self.age,self.country)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts=0


user=User('Max','Derun',18,'Ukraine')
user2=User('Enot','Derun',10,'Ukraine')
user3=User('Nastia','Tractor',28,'Ukraine')
#A
user.describe_user()
user.greeting_user()

user2.describe_user()
user2.greeting_user()

user3.describe_user()
user3.greeting_user()
#B
user.increment_login_attempts()
user.increment_login_attempts()
print('Count:',user.login_attempts)
user.reset_login_attempts()
print('Reset:',user.login_attempts)