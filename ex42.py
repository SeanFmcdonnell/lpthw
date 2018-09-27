## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal)

    def __init__(self, name):
        ## class Dog has a __init__ that takes self and name parameters
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    ## class CAt has a __init__ that takes self and name parameters
    def __init__(self, name):
        self.name = name

## class Person is-a object
class Person(object):

        ## Person has a __init__ that takes self and name parameters
        def__init__(self, name):
            self.name = name

            ## Person has-a pet of some kind
            self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        ## Return a proxy object that delegates method calls to a parent or sibling class of typeself.
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass

## Set rover to an instance of Class Dog, which has-a attribute name set to Rover. Class Dog was called with params self and Rover.
rover = Dog("Rover")

## Set sat to an instance of Class Cat and has-a attribute name set to Sat. Class Cat was called with params self and Sat.
sat = Cat("Sat")

## set mary to an instance of Person and has-a attribute name set to mary
mary = Person("Mary")

## from mary get the pet attribute and sit it to sat
mary.pet = sat

## frank is-a Employee instance has-a attribute name of Frank and attribute salary of 120000
frank = Employee("Frank", 120000)

## pet attribute of frank is-a rover
frank.pet = rover

## flipper is-a Fish instance
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## harry is a Halibut instance
harry = Halibut()
