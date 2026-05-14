class Mentor:
    def define_states(self):
        self.name = "Gamana"
        self.tech = "Python"
        self.age = 20
    def teach(self):
        print("mentor teaches")
    def groom(self):
        print("mentor grooms")
m = Mentor()
m.teach()
m.groom()   
m.define_states()
print(f"Name: {m.name}")
print(f"Tech: {m.tech}")
print(f"Age: {m.age}")   
      