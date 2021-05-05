"""This module is for practicing class creation and class inheritance."""


class Transport:
    """This is the parent class from which 4 classes inherit"""

    def __init__(self, type_transport, number_seats):
        """This method initializes the fields type_transport, number_seats of the class Transport"""
        self.type_transport = type_transport
        self.number_seats = number_seats
        self.running = False

    def show_description(self):
        """This method displays information about the class object"""
        print(f"This transport is {self.type_transport} with {self.number_seats} seats")


    def invert_running(self):
        """Method for stopping or starting transport"""
        self.running = not self.running
        print("Now " + ["stopped", "running"][self.running])


class Car(Transport):
    """This is a descendant class of the Transport class"""

    def __init__(self, type_transport, number_seats, color, brand):
        """This method initializes the fields color, brand of the class Car
        and refers to the initialization of the ancestor"""
        self.color = color
        self.brand = brand
        super().__init__(type_transport, number_seats)

    def show_description(self):
        """This method displays information about the class object"""
        print(f"This transport is {self.type_transport} with {self.number_seats} seats, \
            this is {self.color} color, {self.brand} brand")


class Bus(Transport):
    """This is a descendant class of the Transport class"""

    def __init__(self, type_transport, number_seats, trip_price):
        """This method initializes the field trip_price of the class Bus
        and refers to the initialization of the ancestor"""
        self.trip_price = trip_price
        super().__init__(type_transport, number_seats)

    def show_description(self):
        """This method displays information about the class object"""
        print(f"This transport is {self.type_transport} with {self.number_seats} seats, \
            the trip will cost {self.trip_price}")


class Motorcycle(Transport):
    """This is a descendant class of the Transport class"""

    def __init__(self, type_transport, number_seats, max_speed):
        """This method initializes the field max_speed of the class Motorcycle
        and refers to the initialization of the ancestor"""
        self.max_speed = max_speed
        super().__init__(type_transport, number_seats)

    def show_description(self):
        """This method displays information about the class object"""
        print(f"This transport is {self.type_transport} with {self.number_seats} seats \
            and {self.max_speed} maximum speed")


class Train(Transport):
    """This is a descendant class of the Transport class"""

    def __init__(self, type_transport, number_seats, trip_price, num_of_cars):
        """This method initializes the fields trip_price, num_of_cars of the class Train
        and refers to the initialization of the ancestor"""
        self.trip_price = trip_price
        self.num_of_cars = num_of_cars
        super().__init__(type_transport, number_seats)

    def show_description(self):
        """This method displays information about the class object"""
        print(f"This transport is {self.type_transport} with {self.number_seats} seats \
            and {self.num_of_cars} cars, the trip will cost {self.trip_price}")


car = Car("private", 5, "black", "Mazda")
car.show_description()
car.invert_running()

bus = Bus("urban", 30, 45)
bus.show_description()
bus.invert_running()

motorcycle = Motorcycle("private", 2, 300)
motorcycle.show_description()
motorcycle.invert_running()

train = Train("urban", 100, 70, 3)
train.show_description()
train.invert_running()
