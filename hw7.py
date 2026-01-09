# Base class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print()


# Trainer class (inherits from Employee)
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print()


# YogaInstructor class (inherits from Employee)
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)
        print()


# MultiTrainer class (inherits from Trainer and YogaInstructor)
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)
        print()


# Creating objects
emp = Employee("Ravi", "Staff Member")
trainer = Trainer("Anita", "Fitness Trainer", "Weight Training")
yoga = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")
multi = MultiTrainer("Karan", "Multi Trainer", "Cardio Training", "Vinyasa Yoga")

# Displaying details
emp.display()
trainer.display()
yoga.display()
multi.display()
