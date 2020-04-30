# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.
print('Первый вариант решения')
import datetime
from time import sleep


class TrafficLight:
    count = 0

    def __init__(self, __color):
        self.__color = __color

    def running(self, seconds):
        time_delta = 0
        start = datetime.datetime.now()
        start_second = start.second
        print(self._TrafficLight__color)
        TrafficLight.count += 1

        while time_delta != seconds:
            if start_second + seconds <= 59:
                stop = datetime.datetime.now()
                stop_second = stop.second
                time_delta = abs(start_second - stop_second)
            else:
                stop = datetime.datetime.now()
                stop_second = stop.second + 60
                time_delta = abs(start_second - stop_second)
        else:
            if seconds == 7:
                self._TrafficLight__color = '\33[43m \33[33m___ \33[0m'
            elif seconds == 2:
                self._TrafficLight__color = '\33[42m \33[32m___ \33[0m'
            elif seconds == 5:
                pass


t = TrafficLight('\33[41m \33[31m___ \33[0m')
if t.count == 0 and t._TrafficLight__color == '\33[41m \33[31m___ \33[0m':
    t.running(7)

if t.count == 1 and t._TrafficLight__color == '\33[43m \33[33m___ \33[0m':
    t.running(2)

if t.count == 2 and t._TrafficLight__color == '\33[42m \33[32m___ \33[0m':
    t.running(5)
else:
    print('Ошибка. Нарушен порядок загорания сигналов')

# Более короткий вариант решения
print('Второй вариант решения')


class TrafficLight:
    count = 0

    def __init__(self, __color):
        self.__color = __color

    def running(self):
        print(self._TrafficLight__color)

        if TrafficLight.count == 0:
            self._TrafficLight__color = '\33[43m \33[33m___ \33[0m'
        elif TrafficLight.count == 1:
            self._TrafficLight__color = '\33[42m \33[32m___ \33[0m'
        else:
            pass
        TrafficLight.count += 1


t = TrafficLight('\33[41m \33[31m___ \33[0m')
if t.count == 0 and t._TrafficLight__color == '\33[41m \33[31m___ \33[0m':
    t.running()
    sleep(7)

if t.count == 1 and t._TrafficLight__color == '\33[43m \33[33m___ \33[0m':
    t.running()
    sleep(2)

if t.count == 2 and t._TrafficLight__color == '\33[42m \33[32m___ \33[0m':
    t.running()
    sleep(5)
else:
    print('Ошибка. Нарушен порядок загорания сигналов')

# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
