# Реализуйте базовый класс Car . У данного класса должны быть следующие атрибуты: speed ,
# color , name , is_police (булево). А также методы: go , stop , turn(direction) , которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar , SportCar , WorkCar , PoliceCar . Добавьте в базовый класс метод
# show_speed , который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed . При значении скорости свыше 60
# ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')

    def show_speed(self, speed):
        print(f'Скорость автомобиля: {speed}')


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'Скорость автомобиля: {speed}\nTownCar движется с превышением скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print(f'Скорость автомобиля: {speed}\nTownCar движется с превышением скорости')


class PoliceCar(Car):
    pass


tc = TownCar(120, 'Green', 'Lada', False)
print(f'Скорость: {tc.speed}')
print(f'Цвет: {tc.color}')
print(f'Название: {tc.name}')
print(f'Полицейская: {tc.is_police}')
tc.go()
tc.show_speed(62)
print('-' * 150)

sp = SportCar(210, 'Blue', 'Lexus', False)
print(f'Скорость: {sp.speed}')
print(f'Цвет: {sp.color}')
print(f'Название: {sp.name}')
print(f'Полицейская: {sp.is_police}')
sp.show_speed(0)
sp.stop()
print('-' * 150)

wc = WorkCar(110, 'Red', 'Mazda', False)
print(f'Скорость: {wc.speed}')
print(f'Цвет: {wc.color}')
print(f'Название: {wc.name}')
print(f'Полицейская: {wc.is_police}')
wc.go()
wc.show_speed(41)
print('-' * 150)

pc = PoliceCar(210, 'Black', 'Ford', True)
print(f'Скорость: {pc.speed}')
print(f'Цвет: {pc.color}')
print(f'Название: {pc.name}')
print(f'Полицейская: {pc.is_police}')
pc.go()
pc.show_speed(65)
pc.turn('лево')
pc.go()
pc.show_speed(25)
pc.show_speed(0)
pc.stop()
