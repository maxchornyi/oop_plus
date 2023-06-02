from user_view import User
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('Elite admin')
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self,first_name, last_name, age, country):
        super().__init__(first_name,last_name,age,country)
        self.privilege=Privileges(['Allowed to add message','Allowed to delete users','Allowed to ban users'])
#D
admin = Admin('Lana','God',37,'Heaven')
admin.privilege.show_privileges()