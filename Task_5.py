# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw . Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


stationery = Stationery('some object')
print(f'Наименование канцелярской принадлежности: {stationery.title}')
stationery.draw()
print('_' * 150)

pen = Pen('pen')
print(f'Наименование канцелярской принадлежности: {pen.title}')
pen.draw()
print('_' * 150)

pencil = Pencil('pencil')
print(f'Наименование канцелярской принадлежности: {pencil.title}')
pencil.draw()
print('_' * 150)

handle = Handle('handle')
print(f'Наименование канцелярской принадлежности: {handle.title}')
handle.draw()
