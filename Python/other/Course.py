class Course:

    def __init__(self, id, name, description, price, class_room, professor):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.class_room = class_room
        self.professor = professor

    def welcome(self):
        return "Welcome to this course"

    def goodbye(self):
        print("Good bye, please comeback soon")

    def get_price_per_user(self, users, disscount):
        result = self.price * users
        result = result - disscount
        return result

    def new_teacher(self, first_name, last_name):
        full_name = first_name + " " + last_name
        return "This is the new teacher " + full_name


course_one = Course(1000, "POO", "Programacion Orientada a Objetos", 499.99, 5202, "Luis Guerra")
print(course_one.id)
