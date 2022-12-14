class Consumer:
    def __init__(self, name, surname, consumer_id, credit_card, consumer_location):
        self.name = name
        self.surname = surname
        self.consumer_id = consumer_id
        self.credit_card = credit_card
        self.consumer_location = consumer_location

    def location_sharing(self):
        return print(self.consumer_location)

    def name_change(self):
        self.name = input("Введіть нове ім'я: ")
        return self.name


class Courses:
    def __init__(self, course_name):
        self.course_name = course_name
        self.lesson_name = "null"
        self.course_date = 0
        self.time = 0

    def create_lesson(self):
        lesson_name = input("Введіть назву заняття")
        course_date = input("Дата заняття")
        time = input("Час заняття")
        return course_date,time,lesson_name

    def time_to_lesson(self,current_time):
        time_to_les = current_time - self.time
        return time_to_les

    def data_change(self):
        self.course_date = input("Нова дата заняття")
        return self.course_date

    def time_change(self):
        self.time = input("Новий час заняття")
        return self.time

    def lesson_change(self):
        self.lesson_name = input("Новий назва заняття")
        return self.lesson_name
    
    def course_info(self):
        return self.course_name,self.course_date,self.lesson_name,self.time

    def machine_check(self):
        return self.course_info


class Lector(Consumer):

    def create_description(self):
        description = input("Введіть опис курсу: ")
        return print(description)


class Food:
    def __init__(self, market_name, food_list, market_location, store_card):
        self.market_name = market_name
        self.food_list = food_list
        self.market_location = market_location
        self.store_card = store_card

    def market_find(self):
        return print("Місцезнаходження магазину", self.market_location)

    def food_listing(self):
        return print("Список їжі магазину", self.food_list)


class Order(Consumer, Food):
    def __init__(self, consumer_id, consumer_location, food_list, market_location, market_name):
        super().__init__(consumer_id, consumer_location, food_list, market_location, market_name)
        self.order_list = food_list
        self.market = market_name
        self.customer = consumer_id
    def send_result(self, consumer_location, market_location):
        euclid = (((market_location[0] - consumer_location[0]) ** 2 + (market_location[1] - consumer_location[1]) ** 2) ** 0.5)
        print("Відстань до магазину", euclid, "км")
        return euclid

    def send_check(self):
        return print("|Чек \n|Магазин ", self.market, "\n|Замовлена їжа:", self.order_list, "\n|Id покупця:", self.customer)
