import classes.User;
import classes.Course;

public class Main {

    public static void main(String[] args) {
    
        //System.out.println("Learning Object Oriented Programming with Java");
        User object_user = new User(123, "Luis Guerra", "luis.guerra@gmail.com");
        System.out.println(object_user.id);
        Course course_one = new Course(1000, "POO", "Programacion Orientada a Objetos", 499.99, 5202, "Luis Guerra");
        System.out.println(course_one.id);
        System.out.println(course_one.welcome_course());
        course_one.goodbye_course();
        System.out.println(course_one.get_price_per_user(5, 0));
        System.out.println(course_one.get_price_per_user(5, 2499.95));

    }
}