## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal that takes self and name parameters
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ?Cat is-a Animal that takes self and name parameters
class Cat(Animal):

    def __init__(self, name):
        ## ?? 
        self.name = name

## Person is-a object that takes self and name parameters
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person that takes self, name and salary parameters
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## First is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog and has-a name Rover
rover = Dog("Rover")

## satan is-a Cat and has-a name Satan
satan = Cat("Satan")

## mary is-a Person and has-a name Mary
mary = Person("Mary")

## mary has-a pet of class Cat satan
mary.pet = satan

## frank is a employee and has-a name Frank and salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet of class Dog rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse =  Salmon()

## harry is-a Halibut
harry = Halibut