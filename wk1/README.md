# Objects and Python classes

Classes give you the ability to logically group data and functions together in a way that's easy to reuse. When using classes the pieces of data that they hold are called `attributes` and the functions inside a class are called `methods`. Classes are often described as blueprints that let you create objects that model something. 

## Useful terms when talking about classes
* A Class - a blueprint for creating objects
* Objects - (everything in Python) Anything that has attributes and methods
* Attributes - pieces of data that belong to an object
* Methods - functions that belong to and object

## Basics of creating and instantiating classes
Below we'll walk through the basics of creating a class by modeling the data and functions (actions) that a bicycle might have. In the example below the `Bicycle` class is a blueprint that we can use to create an object that models a bicycle, but that blueprint by itself is not an actual bicycle object.  

When you say something is an `instance` of a certain class it means that the object you're talking about was created by using an existing class blueprint like the one below.

```Python
#An example of a class that makes bicycles
class Bicycle:
    def __init__(self, size, color, noise):
        self.size = size
        self.color = color
        self.noise = noise
        
    def ring_bell(self):
        return self.noise
        
# making an instance of the Bicycle class
bike_1 = Bicycle(5, "blue", "Clang")

# calling the ring_bell method
bike_1.ring_bell() 

# output: "Clang"
```

### Pair programming exercise
With the person you’re sitting next to you take turns creating a simple class that is different than the one shown above. Make the class have at least three attributes in its `__init__` method and at least one method that combines two of these attributes in some way. Create an instance of your class to check your results. Please put this work inside the `student-work/<your_name>/week_1/working_with_classes.py` file. 

__Not required but try if you'd like an extra challenge:__ look up `special method names` for Python classes and add one or two to the class you created.  

## Class variables 
Class variables are a way to share the same attributes across all of the instances that you've created from your class. Seeing how they work will give us some intution into how and instance of a class finds things that are related to itself. 

```Python 
class Bicycle:
    # class variables
    sprinting_speed = 1.5
    num_of_bicycles = 0
    
    def __init__(self, speed):
        self.speed = speed
        Bicycle.num_of_bicycles += 1
        
    def top_speed(self):
        return int(self.speed * self.sprinting_speed)
```

In the code snippet above notice how you can access the class variables using `self` and `Bicycle`. What you you think the are differences between both approaches? Make an instance of the class and print out the `__dict__` for the instance and the class. 

```Python
# Example of printing __dict__ for a class instance and a class
print(Bicycle.__dict__)
print(bike_1.__dict__)
```
Quick note on the use of `object.__dict__`, all this does is print out a dict of the attributes and methods to which an object has access.  

### quick 5-10 minute individual exercise
Add a class variable to the class you've been working on and use that variable in a method in your class and play around with the `__dict__` attribute and see the differences when you add new class variables. 

__Not required but try if you'd like an extra challenge:__ Look over this [blog post](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods) about static, class, and abstract methods and try to add some to the classes you've been working on over the weekend. Remember to submit a PR to the class repo with your work if you do.

## Class inheritance
Inheritance allows a class to inherit attributes and methods from a parent class. This allows us to build objects that can be combined with one another to increase code reusability. We'll also see inheritance used heavily when we start building our own APIs with the Django REST Framework. 

```Python 
# example of using inheritance to give us different bicycle types

class BaseBicycle:
    def __init__(self, size, color, noise):
            self.size = size
            self.color = color
            self.noise = noise
            
    def ring_bell(self):
        return self.noise
        
class Tricycle(BaseBicycle):
    def __init__(self, size, color, noise, num_wheels):
        super().__init__(size, color, noise)
        self.num_wheels = num_wheels
        
    def paint_tricycle(self, new_color):
        # this method only exists in the Tricycle class
        self.color = new_color  
```
Try adding this line `print(help(Tricycle))` to your file using whatever class name you've created and print out the results from the `help()` function. 

Notice the use of the `super()` function in the example above. What that is doing is calling the `__init__` method of the parent class with the arguments that the parent needs for its `__init__` method. Some advantages to using `super()` is that it lets you avoid referring to the base class explicitly and helps when dealing with multiple inheritance. In class we will only really need to use `super()` if we're overriding methods on Django classes we're inheriting from but that will be covered at a later date.

### Group exercise putting it all together
Look inside the `student-work/<your_name>/week_1/group-challenge/` directory. Inside this directory you'll find a code challenge and instructions on how to work through it. It will be made up of a few parts, you'll be asked to build a class that models the people in a classroom and the actions that they can perform. Please see the README inside of the directory for more details. 


# Group challenge

This will be a three part challenge that everyone will be working in small groups of three to solve. Please talk with your group about what you're doing and help each other if you get stuck along the way. Below you'll find an outline of the problem requirements. 

## Challenge requirements
* make a group of three classes that model students and a teacher in a usual classroom. You should use a base class for the shared characteristics and between both Student and Teacher classes. 

* Shared attributes and methods for both classes:
    * Shared attributes: first_name, last_name, email
    * Shared methods: ask_a_question
    
* Student attributes and methods that need to be added in addition to those shared above:
    * Student attributes: books_dict - create a dictionary that contains the books a student owns.
    * Student methods: 
        * add_book - this method will add a book to the student's books_dict.
        * remove_book - this method will remove a book from the student's books_dict.
        * show_books - this method will print out all of the books a student owns.
        
* Teacher attributes and methods that need to be added in addition to those shared above:
    * Teacher attributes: student_list - create a list of student names 
    * Teacher methods:
        * shuffle_class - this method will take all of the students in the student list and put them in work groups (see names_challenge problem below)
        
### Names challenge function 

The goal of this challenge is to create a function that will take a list of 
names and a bin size and then shuffle those names and return them in a 
list of lists where the length of the inner lists match the bin size. 

For example calling the function with a list of names and size 2 should return 
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is 
remaining add that name to another inner list. 

Also note that there is a test file called `names_challenge_test.py` that has a number of tests which will help give feedback when solving this part of the problem. 

Once you have completed this part of the challenge try to add the function you created as a method on the Teacher class above. 
        
