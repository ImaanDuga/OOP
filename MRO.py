class Person:
    def info(self):
        print("I am a person.")

class Manager(Person):
    def info(self):
        print("I am a manager.")

class Engineer(Person):
    def info(self):
        print("I am an engineer.")

class TechLead(Manager, Engineer):
    pass

# Create a TechLead object
lead = TechLead()
lead.info()

# Check Method Resolution Order
print(TechLead.__mro__)