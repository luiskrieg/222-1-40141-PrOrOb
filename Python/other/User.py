class User:
    '''
    id = 100
    full_name = "Full name"
    personal_email = "personal_email@gmail.com"
    '''
    def __init__(self, id, full_name, personal_email):
        self.id = id
        self.full_name = full_name
        self.personal_email = personal_email
        

object_user = User("02120123456", "Luis Guerra", "luis.guerra@gmail.com")
#print(object_user)
print("0" + str(object_user.id))
print(object_user.full_name)
print(object_user.personal_email)