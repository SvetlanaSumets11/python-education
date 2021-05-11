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
        self._first_name, self._last_name, self._telephone, self._salary, _ = args
        args[-1].append_employee(self)

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
        self.__cooking_dish = []

    def __str__(self):
        """Returns a string describing the entity"""
        return "First name: {}\nLast name: {}\nTelephone: {}\nSalary: {}\nCook type: {}"\
            .format(self._first_name,
                    self._last_name,
                    self._telephone,
                    self._salary,
                    self.__cook_type)

    @property
    def cooking_dish(self):
        """Special functionality to a method cooking_dish so that it acts like a getter."""
        return self.__cooking_dish

    def change_flag_rediness(self, id_dish: int, order):
        """The chef changes the status of the dish to true (cooked), this dish is automatically
        removed from the chef's list of dishes to be prepared (which was added there when
        creating an order in the restaurant), and the prepared dish is added to the waiter's
        list of ready-to-go dishes."""
        order.flag_rediness[id_dish] = True
        self.cooking_dish.remove(order.dishes[id_dish])
        order.waiter.ready_take_out.append(order.dishes[id_dish])


class Waiter(Employee):
    """This is the entity class of the restaurant worker waiter"""
    def __init__(self, *args):
        """Initializing Class Fields"""
        Employee.__init__(self, *args[:-1])
        self.__hall = args[-1]
        self.__ready_take_out = []

    def __str__(self):
        """Returns a string describing the entity"""
        return "First name: {}\nLast name: {}\nTelephone: {}\nSalary: {}\nHall: {}"\
            .format(self._first_name, self._last_name, self._telephone, self._salary, self.__hall)

    @property
    def ready_take_out(self):
        """Special functionality to a method ready_take_out so that it acts like a getter."""
        return self.__ready_take_out

    def change_flag_rediness(self, id_dish: int, order):
        """the waiter changes the status of the dish to neutral, when the dish is taken out,
        it is automatically removed from the waiter's takeaway list"""
        order.flag_rediness[id_dish] = False
        self.ready_take_out.remove(order.dishes[id_dish])


class Dish:
    """This is the entity class of the menu item"""
    def __init__(self, *args):
        """Initializing Class Fields"""
        self.__dish_name, self.__ingredients, self.__dish_price, \
        self.__dish_type, self.__cook, _ = args
        args[-1].menu.append(self)

    def __str__(self):
        """Returns a string describing the entity"""
        return "Dish name: {}\nIgredients: {}\nPrice: {}\nType: {}"\
            .format(self.__dish_name,
                    ', '.join(self.__ingredients),
                    self.__dish_price,
                    self.__dish_type)

    @property
    def dish_name(self):
        """Special functionality to a method dish_name so that it acts like a getter."""
        return self.__dish_name

    @property
    def dish_price(self):
        """Special functionality to a method dish_price so that it acts like a getter."""
        return self.__dish_price

    @property
    def cook(self):
        """Special functionality to a method cook so that it acts like a getter."""
        return self.__cook


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
        self.__flag_rediness = [False] * len(dishes)
        for dish in dishes:
            dish.cook.cooking_dish.append(dish)

    def __str__(self):
        """Returns a string describing the entity"""
        dishes_names = ', '.join([dish.dish_name for dish in self._dishes])
        return "Dishes: {}\nTable numder: {}\nWaiter: {} {}" \
            .format(dishes_names,
                    self.__customer.table_num,
                    self.__waiter.first_name,
                    self.__waiter.last_name)

    @property
    def flag_rediness(self):
        """Special functionality to a method flag_rediness so that it acts like a getter."""
        return self.__flag_rediness

    @property
    def waiter(self):
        """Special functionality to a method waiter so that it acts like a getter."""
        return self.__waiter


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
salad = Dish("Салат Цезарь",
             ["листья салата", "куриное филе", "помидоры", "сыр пармезан"],
             34, "салаты", vlad, restaurant)

kirill = CustomerInside(10)
svetlana = CustomerOutside("Светлана", 380977777777, "ул. Гв.Широнинцев, д.1, кв.1")
anna = Waiter("Чигура", "Анна", 380999999999, 3000, restaurant, 1)
svetlana_order = OrderOutside([soup, salad], svetlana, restaurant)

# блюда заказа кирилла не приготовлены, они добавляются в список блюд повара, что нужно приготовить
kirill_order = OrderInside([soup, salad], kirill, anna, restaurant)
# смотрим статусы готовности блюд заказа
print(kirill_order.flag_rediness)
# смотрим список блюд повара, что нужно приготовить
print(vlad.cooking_dish)
# повар приготовил блюдо 1(салат) и меняет статус готовности,
# в список блюд, готовых на вынос официанта добавляется это блюдо
vlad.change_flag_rediness(1, kirill_order)
# смотрим статусы готовности блюд заказа
print(kirill_order.flag_rediness)
# смотрим список блюд повара, что нужно приготовить
print(vlad.cooking_dish)
# видим это блюдо в списке блюд готовых на вынос официанта
print(anna.ready_take_out)
# официант вынес блюдо, он меняет статус блюда, блюдо удаляется из списка на вынос
anna.change_flag_rediness(1, kirill_order)
# смотрим статусы готовности блюд заказа
print(kirill_order.flag_rediness)
# видим, что блюдо в списке блюд готовых на вынос официанта, отсутствует
print(anna.ready_take_out)
