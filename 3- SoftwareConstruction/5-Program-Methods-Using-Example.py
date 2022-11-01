if __name__ == '__main__':
    Anton = Consumer("Anton", "Pavlov", 314, 452262, (0.5, 0.6)) # Створюємо об'єкт Anton
    Anton.location_sharing() # Виводимо місцезнахождення споживача
    Example1 = Courses("Intoducing in Python") # Cтворюємо об'єкт Example1
    Example1.create_lesson() # створюємо заняття, вводячи після визову фунції значення змінних
    Example1.time_to_lesson(08.10) # визначаемо час до заняття задаючі за поточне 08.10
    Obzhora = Food("Obzhora", ["Cola", "Pepsi", "Lays", "Tea"], (0.2, 0.8), 5245)
    Obzhora.food_listing() # вивидом список замовленної їжі
    Lucky = Order(354, (0.5, 0.6), ["Cola", "Pepsi"], (0.2, 0.8), "Obzhora") # створюємо об'єкт Lucky - це інформація про наше замовлення
    Lucky.send_result((0.5, 0.6), (0.2, 0.8)) #Обчислюємо відстань між магазином та замовником
    Lucky.send_check() # Вивидимо чек замовнику
