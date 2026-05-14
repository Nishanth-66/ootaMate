class Student:
     
     # class variable - access with the help of class name or refrence variable
    institute = "KodNest"


     # Instance variable - access with the help of refrence variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

      # instance variable & Instance method (self)
    def study(self):
        print(f"{self.name} Studies")

    # class method - (cls) - classname, refrance variable
    @classmethod
    def institute_change(cls, new_institute):
       cls.institute = new_institute


      # static method - classname, ref
    @staticmethod
    def student_trip():
        print("Student like to go for a trip")


Student.institute_change("KodNest Private Limited")
s1 = Student("Abhi", 21)
print(f"{s1.name}, {s1.age}, {s1.institute}")
print(Student.institute)
s1.study()

s2 = Student("Viju", 22)
print(f"{s2.name}, {s2.age}, {s2.institute}")
s2.student_trip()
s2.study()
