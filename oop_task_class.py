"""This module is for practicing class creation and class inheritance."""
from abc import ABC, abstractmethod
from copy import copy, deepcopy


class Engine:
    """This is the parent class from which 4 classes inherit"""
    def __init__(self, engine_type):
        """This method initializes the fields engine of the class Engine"""
        self.engine = engine_type

    @staticmethod
    def desc():
        """This method is static method of the class Engine"""
        print("Vehicle engines can be gasoline, diesel, gas, electric and hybrid")

    def __get__(self, instance, owner):
        """Allows you to define the value obtained when accessing
        the attribute of the owner class pointing to the descriptor."""
        return self.engine

    def __set__(self, instance, engine):
        """Allows you to define behavior when an attempt is made to assign
        a value to an attribute of the owning class pointing to a descriptor."""
        self.engine = engine


class Transport(ABC):
    """This is the parent class from which 4 classes inherit"""
    VERSION = "1.0.1"
    DESCRIPTOIN = "some description"

    def __init__(self, type_transport, number_seats):
        """This method initializes the fields type_transport, number_seats of the class Transport"""
        self.type_transport = type_transport
        self.number_seats = number_seats
        self.__some_val = "SOME VALUE!"
        self.running = False

    def __str__(self):
        """This method displays information about the class object"""
        return "This transport is {} with {} seats".format(self.type_transport, self.number_seats)

    def invert_running(self):
        """Method for stopping or starting transport"""
        self.running = not self.running

        if self.running:
            print("Now running")
        else:
            print("Now stopped")

    @abstractmethod
    def print_info(self):
        """This method is abstract method of the class Transport"""
        print("this is abstract method")

    @property
    def some_val(self):
        """This decorator is used to give "special" functionality to a method some_val
        so that it acts like a getter."""
        return self.__some_val.lower()


class Car(Transport, Engine):
    """This is a descendant class of the Transport class"""
    OBJECTS = 0

    def __init__(self, type_transport, number_seats, brand, characteristics):
        """This method initializes the fields brand, characteristics of the class Car
        and refers to the initialization of the ancestor"""
        self.brand = brand
        self.characteristics = characteristics
        Transport.__init__(self, type_transport=type_transport, number_seats=number_seats)
        Engine.__init__(self, engine_type="hybrid")
        Car.OBJECTS = Car.OBJECTS + 1

    def __str__(self):
        """This method displays information about the class object"""
        return "This transport is {} with {} seats, this is {} brand with ch-cs {}"\
        .format(self.type_transport, self.number_seats, self.brand, self.characteristics)

    def print_info(self):
        """This method is abstract method of the class Transport"""
        print("Just something for class Car")

    def __call__(self, brand):
        """This magic method allows you to call an instance of a class as a function"""
        self.brand = brand

    def __copy__(self):
        """This method allows you to override the behavior when you try to use
        the copy () function from the copy module that performs shallow copying
        on an instance of the class."""
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        """This method allows you to override the behavior when you try to deep
        copy the deepcopy () function from the copy module to an instance of the class."""
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for iter_1, iter_2 in self.__dict__.items():
            setattr(result, iter_1, deepcopy(iter_2, memo))
        return result

    def __contains__(self, item):
        """Should return True if the specified element is contained
        in the object, otherwise False."""
        return item in self.characteristics

    def __index__(self):
        """Allows the object to be used as an index"""
        return 0

    @classmethod
    def count_objects(cls):
        """This method is classmethod of the class Car,
        it is a method that is attached to a class, not an instance of the class"""
        print("Objects: ", cls.OBJECTS)


class Bus(Transport, Engine):
    """This is a descendant class of the Transport class"""

    def __init__(self, type_transport, number_seats, trip_price):
        """This method initializes the field trip_price of the class Bus
        and refers to the initialization of the ancestor"""
        self.trip_price = trip_price
        Transport.__init__(self, type_transport=type_transport, number_seats=number_seats)
        Engine.__init__(self, engine_type="diesel")

    def __str__(self):
        """This method displays information about the class object"""
        return "This transport is {} with {} seats, the trip will cost {}"\
        .format(self.type_transport, self.number_seats, self.trip_price)

    def print_info(self):
        """This method is abstract method of the class Transport"""
        print("Just something for class Bus")

    def __call__(self, trip_price):
        """This magic method allows you to call an instance of a class as a function"""
        self.trip_price = trip_price

    def __index__(self):
        """Allows the object to be used as an index"""
        return 1


class Motorcycle(Transport, Engine):
    """This is a descendant class of the Transport class"""

    def __init__(self, type_transport, number_seats, max_speed):
        """This method initializes the field max_speed of the class Motorcycle
        and refers to the initialization of the ancestor"""
        self.max_speed = max_speed
        Transport.__init__(self, type_transport=type_transport, number_seats=number_seats)
        Engine.__init__(self, engine_type="diesel")

    def __str__(self):
        """This method displays information about the class object"""
        return "This transport is {} with {} seats and {} maximum speed"\
        .format(self.type_transport, self.number_seats, self.max_speed)

    def print_info(self):
        """This method is abstract method of the class Transport"""
        print("Just something for class Motorcycle")

    def __call__(self, max_speed):
        """This magic method allows you to call an instance of a class as a function"""
        self.max_speed = max_speed

    def __index__(self):
        """Allows the object to be used as an index"""
        return 2


class Train(Transport, Engine):
    """This is a descendant class of the Transport class"""

    def __init__(self, type_transport, number_seats, trip_price, num_of_cars):
        """This method initializes the fields trip_price, num_of_cars of the class Train
        and refers to the initialization of the ancestor"""
        self.trip_price = trip_price
        self.num_of_cars = num_of_cars
        Transport.__init__(self, type_transport=type_transport, number_seats=number_seats)
        Engine.__init__(self, engine_type="electric")

    def __str__(self):
        """This method displays information about the class object"""
        return "This transport is {} with {} seats and {} cars, the trip will cost {}" \
        . format(self.type_transport, self.number_seats, self.num_of_cars, self.trip_price)

    def print_info(self):
        """This method is abstract method of the class Transport"""
        print("Just something for class Train")

    def __call__(self, trip_price, num_of_cars):
        """This magic method allows you to call an instance of a class as a function"""
        self.trip_price, self.num_of_cars = trip_price, num_of_cars

    def __index__(self):
        """Allows the object to be used as an index"""
        return 3


en = Engine("electric")
print(en.engine)
en.engine = "hybrid"
print(en.engine)

car11 = Car("private", 5, "Mazda", [78.6, 89.0, 44.1])
car22 = Car("private", 4, "Reno", [76.6, 83.0, 41.1])
car33 = Car("private", 6, "Lada", [54.6, 76.0, 34.1])
Car.count_objects()

car = Car("private", 5, "Mazda", [78.6, 89.0, 44.1])
car.invert_running()
car.print_info()
print(car.some_val)
print(str(car))
car("Fiat")
print(str(car))
car1, car2 = copy(car), deepcopy(car)
car.characteristics.append(11.23)
print("car1(copy): " + str(car1))
print("car2(deepcopy): " + str(car2))
print(78.6 in car)
print(78.7 in car)
lists = ['car', 'bus', 'motorcycle', 'train']
print(lists[car])

print("**************")
bus = Bus("urban", 30, 45)
bus.invert_running()
bus.print_info()
print(bus.some_val)
print(str(bus))
bus(79)
print(str(bus))
setattr(bus, "trip_price", 88)
print(str(bus))
print(lists[bus])

print("**************")
motorcycle = Motorcycle("private", 2, 300)
motorcycle.invert_running()
motorcycle.print_info()
print(motorcycle.some_val)
print(str(motorcycle))
motorcycle(250)
print(str(motorcycle))
setattr(motorcycle, "max_speed", 310)
print(str(motorcycle))
print(lists[motorcycle])

print("**************")
train = Train("urban", 100, 70, 3)
train.invert_running()
train.print_info()
print(motorcycle.some_val)
print(str(train))
train(57, 4)
print(str(train))
setattr(train, "trip_price", 44)
setattr(train, "num_of_cars", 6)
print(str(train))
print(lists[train])

print("**************")
Engine.desc()
Car.desc()
