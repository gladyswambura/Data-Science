# Object-Oriented Programming (OOP) is a programming paradigm that focuses on organizing code using objects and classes. It helps to create more modular, reusable, and maintainable code.

# Classes and objects:
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.

# An object is an instance of a class. It has its own set of attributes and can use the methods defined in its class.

# To create a class in Python, you use the class keyword followed by the class name. Class names are typically written in CamelCase.

class Person:
  #  constructor access object attribute

    # attributes
    gender = 'male'

    def __init__(self, name, age):  # initializing instance variable 
        self.name = name  # Attribute
        self.age = age    # Attribute

    def say_hello(self):  # Method
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

student1=Person('Adrian',35)
student2 = Person('Lona', 22)
student1.say_hello()
print(student1.name)

# accesing attributes inside the class
print('This is an attribute', Person.gender)



# Example 2
class Email:
    __read = False   # __ means private underscore
    
    def __init__(self, subject, body):
      self.subject = subject
      self._body = body

    def mark_as_read(self):
      self.__read = True

    def is_read(self):
      return self.__read

    def is_spam(self):
      return "you won 1 million" in self.subject

e = Email("Check this out", "There are a bunch of free online course here: https://course.online")
print(e.is_spam()) # False
print(e.mark_as_read())
print(e.is_read()) # True

# Inheritance: Python supports inheritance, allowing you to create a new class that inherits the attributes and methods of an existing class. This facilitates code reuse and the creation of specialized classes.

# inheritance example 1
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Calling the parent class constructor
        self.student_id = student_id  # Adding a new attribute

    def study(self):
        print(f"{self.name} is studying.{self.age}, {self.student_id}")


# inheritance example 2
class EmailWithAttachment(Email):
  def __init__(self, subject, body, attachment):
    super(EmailWithAttachment, self).__init__(subject, body)
    self.__attachment = attachment

  def get_attachment_size(self):
    return len(self.__attachment)

email_with_attachment = EmailWithAttachment("you won 1 million dollars", "open attachment to win", "one million.pdf")
print(email_with_attachment.is_spam()) # True
print(email_with_attachment.get_attachment_size()) # 15


# Private Variables: In Python, you can use double underscores (__) before an attribute name to make it private. Private attributes are intended to be accessed only within the class, and they are name-mangled to prevent accidental access from outside the class.

class MyClass:
    def __init__(self):
        self.__private_var = 42

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())  # Accessing the private variable through a method
# print(obj.__private_var)     # This would raise an AttributeError

# Encapsulation
# polymorphism


