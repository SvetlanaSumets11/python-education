"""This module is designed to implement the work of a restaurant chain with all"""
from abc import ABC
import datetime


class Restaurant:
    """This is a restaurant class"""

    def __init__(self, restaurant_name: str, cuisine_type: str):
        """Initializing Class Fields"""
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__employee = []
        self.__menu = []
        self.__current_orders = []
        self.__completed_orders = []

    @staticmethod
    def info_restaurant():
        """Prints information about the restaurant"""
        print("""The restaurant is a public catering enterprise with a wide
                 range of complex dishes, including customized and branded ones.
                 Meals are usually served and eaten locally in a restaurant, but
                 many restaurants also offer takeaway and food delivery.""")

    def __str__(self):
        """Returns a string describing the entity"""
        return "This is restaurant with name {} \nRestaurant cuisin is {}" \
            .format(self.__restaurant_name, self.__cuisine_type)

    def append_employee(self, employee):
        """Adds an employee to the list of employees"""
        self.__employee.append(employee)

    def append_dish(self, dish):
        """Adds a dish to the list of dishes (menu)"""
        self.__menu.append(dish)

    def append_current_orders(self, order):
        """Adds an outstanding order to the list"""
        self.__current_orders.append(order)

    def append_completed_orders(self, order):
        """Adds a completed order to the list"""
        self.__completed_orders.append(order)

    @property
    def employee(self):
        """Special functionality to a method employee so that it acts like a getter."""
        return self.__employee

    @property
    def menu(self):
        """Special functionality to a method menu so that it acts like a getter."""
        return self.__menu

    @property
    def current_orders(self):
        """Special functionality to a method current_orders so that it acts like a getter."""
        return self.__current_orders

    @property
    def completed_orders(self):
        """Special functionality to a method completed_orders so that it acts like a getter."""
        return self.__completed_orders


class CustomerOutside:
    """This is the visitor entity class that orders food delivery"""
    def __init__(self, last_name: str, telephone: int, address: str):
        """Initializing Class Fields"""
        self.__last_name = last_name
        self.__telephone = telephone
        self.__address = address

    @property
    def last_name(self):
        """Special functionality to a method last_name so that it acts like a getter."""
        return self.__last_name

    @property
    def address(self):
        """Special functionality to a method address so that it acts like a getter."""
        return self.__address

    def __str__(self):
        """Returns a string describing the entity"""
        return "Customer name: {}\nTelephone: {}\nDelivery address: {}"\
        .format(self.__last_name, self.__telephone, self.__address)

    def change_adress(self, new_adress):
        """Changes delivery address"""
        self.__address = new_adress


class CustomerInside:
    """This is the entity class a visitor that eats in a restaurant"""
    def __init__(self, table_num: int):
        """Initializing Class Fields"""
        self.__table_num = table_num

    @property
    def table_num(self):
        """Special functionality to a method menu so that it acts like a getter."""
        return self.__table_num

    def __str__(self):
        """Returns a string describing the entity"""
        return f"Customer table: {self.__table_num}"

    def change_table(self, new_table_num):
        """Changes the table number"""
        self.__table_num = new_table_num


class Employee(ABC):
    """This is the restaurant worker entity class"""
    def __init__(self, *args):
        """Initializing Class Fields"""
        self._first_name = args[0]
        self._last_name = args[1]
        self._telephone = args[2]
        self._salary = args[2]
        args[4].append_employee(self)

    @property
    def first_name(self):
        """Special functionality to a method first_name so that it acts like a getter."""
        return self._first_name

    @property
    def last_name(self):
        """Special functionality to a method last_name so that it acts like a getter."""
        return self._last_name


class Cook(Employee):
    """This is a restaurant worker entity class chef"""
    def __init__(self, *args):
        """Initializing Class Fields"""
        Employee.__init__(self, *args[:-1])
        self.__cook_type = args[-1]

    def __str__(self):
        """Returns a string describing the entity"""
        return "First name: {}\nLast name: {}\nTelephone: {}\nSalary: {}\nCook type: {}"\
        .format(self._first_name, self._last_name, self._telephone, self._salary,self.__cook_type)


class Waiter(Employee):
    """This is the entity class of the restaurant worker waiter"""
    def __init__(self, *args):
        """Initializing Class Fields"""
        Employee.__init__(self, *args[:-1])
        self.__hall = args[-1]

    def __str__(self):
        """Returns a string describing the entity"""
        return "First name: {}\nLast name: {}\nTelephone: {}\nSalary: {}\nHall: {}"\
        .format(self._first_name, self._last_name, self._telephone, self._salary, self.__hall)


class Dish:
    """This is the entity class of the menu item"""
    def __init__(self, *args):
        """Initializing Class Fields"""
        self.__dish_name = args[0]
        self.__ingredients = args[1]
        self.__dish_price = args[2]
        self.__dish_type = args[3]
        self.__cook = args[4]
        args[5].menu.append(self)

    def __str__(self):
        """Returns a string describing the entity"""
        return "Dish name: {}\nIgredients: {}\nPrice: {}\nType: {}"\
        .format(self.__dish_name, ', '.join(self.__ingredients),
            self.__dish_price, self.__dish_type)

    @property
    def dish_name(self):
        """Special functionality to a method dish_name so that it acts like a getter."""
        return self.__dish_name

    @property
    def dish_price(self):
        """Special functionality to a method dish_price so that it acts like a getter."""
        return self.__dish_price


class Order(ABC):
    """This is the order entity class"""
    def __init__(self, dishes: Dish, rest: Restaurant):
        """Initializing Class Fields"""
        self._date_order = datetime.datetime.now()
        self._dishes = dishes
        self._done = False
        rest.current_orders.append(self)

    @property
    def dishes(self):
        """Special functionality to a method dishes so that it acts like a getter."""
        return self._dishes

    @property
    def date_order(self):
        """Special functionality to a method date_order so that it acts like a getter."""
        return self._date_order

    @property
    def flag_done(self):
        """Special functionality to a method flag_done so that it acts like a getter."""
        return self._done

    @property
    def total_amount(self):
        """Special functionality to a method total_amount so that it acts like a getter."""
        return sum(dish.dish_price for dish in self._dishes)

    def change_flag_done(self, rest: Restaurant):
        """changes the order execution flag"""
        self._done = True
        rest.completed_orders.append(self)
        rest.current_orders.remove(self)


class OrderInside(Order):
    """This is the order entity class in a restaurant"""
    def __init__(self, dishes: Dish, customer: CustomerInside, waiter: Waiter, rest):
        """Initializing Class Fields"""
        Order.__init__(self, dishes, rest)
        self.__customer = customer
        self.__waiter = waiter

    def __str__(self):
        """Returns a string describing the entity"""
        dishes_names = ', '.join([dish.dish_name for dish in self._dishes])
        return "Dishes: {}\nTable numder: {}\nWaiter: {} {}"\
        .format(dishes_names, self.__customer.table_num,
            self.__waiter.first_name, self.__waiter.last_name)


class OrderOutside(Order):
    """This is the entity class ordering using food delivery"""
    def __init__(self, dishes: Dish, customer: CustomerOutside, rest):
        """Initializing Class Fields"""
        Order.__init__(self, dishes, rest)
        self.__customer = customer

    def __str__(self):
        """Returns a string describing the entity"""
        dishes_names = ', '.join([dish.dish_name for dish in self._dishes])
        return "Dishes: {}\nCustomer name: {}\nAdress: {}"\
        .format(dishes_names, self.__customer.last_name, self.__customer.address)



restaurant = Restaurant("Klod Mone", "Franch")

vlad = Cook("Петров", "Василий", 380966666666, 4000, restaurant, "сушеф")

soup = Dish("Суп харчо", ["говядина", "рис", "хмели-сунели"], 45, "холодные", vlad, restaurant)
salad = Dish("Салат Цезарь", ["листья салата", "куриное филе", "помидоры", "сыр пармезан"],
    34, "салаты", vlad, restaurant)

kirill = CustomerInside(10)
svetlana = CustomerOutside("Светлана", 380977777777, "ул. Гв.Широнинцев, д.1, кв.1")

anna = Waiter("Чигура", "Анна", 380999999999, 3000, restaurant, 1)

kirill_order = OrderInside([soup, salad], kirill, anna, restaurant)
svetlana_order = OrderOutside([soup, salad], svetlana, restaurant)
# print(len(restaurant.completed_orders))
# print(len(restaurant.current_orders))
# print(svetlana_order)
# print(kirill_order.total_amount)
# print(svetlana_order.date_order)
# print(kirill_order.flag_done)
# kirill_order.change_flag_done(restaurant)
# print(len(restaurant.completed_orders))
# print(len(restaurant.current_orders))
# print(kirill_order.flag_done)
# print(str(svetlana))
# print(str(kirill))
# svetlana.change_adress("ул. Гв.Широнинцев, д.222, кв.1")
# print(str(svetlana))
# print(str(soup))
# print(str(anna))
# print(soup.dish_name)
# print(str(kirill_order))
# print(restaurant.menu)
