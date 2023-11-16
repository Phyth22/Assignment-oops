#Definition
# bject-Oriented Programming is a type of programming approach that uses the concepts of objects and classes.

# ADVANTAGES OF OOPS

#Troubleshooting is easier with the OOP language
#Code Reusability
#Productivity
#Data Redundancy
#Code Flexibility
#Solving problems
#Security

 #CLASES
 #Difinition
 # In object-oriented programming, a class is a set of related objects with common characteristics.
 
 #DIFINITION OF OBJECTS
# an object is a combination of variables, functions, and data structures

#INSTANCE
#an instance is one occurrence of a class or object
 
 #Creating a user class with  properties ie name , age ,location
 
class Student:
  def __init__(self,name,age, Location):
    self.name = name
    self.age = age
    self.Location = Location
    
Student1 = Student("Agatha", 30 , "Kampala")
 
print(Student1.name)
print(Student1.age)
print(Student1.Location)

#creating a new instance of the user  class (a new class)

Student2 = Student("faith", 40,"Nakawa")
print(Student2.name)
print(Student2.age)
print(Student2.Location)

Student = Student1.name
Student = Student1.age

print(f"name:{Student1.name}")
print(f"age: {Student1.age}")

def my_location(my):
    print("my Location:",my)
my_location("kampala")
