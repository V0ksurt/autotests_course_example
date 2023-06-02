# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time


def func_log(file_log='log.txt'):
    """
    Декоратор, который создает файл по пути file_log где пишет название функции и время ее запуска
    :param file_log: Путь до файла
    :return: Результат выполнения функции
    """
    def log(func):
        """
        Обертка выполнения функции
        :param func: Функция
        :return: Результат выполнения функции
        """
        def wrapper(*args, **kwargs):
            """
            Обертка открывающая и заполняющая файл логов
            :param args: Параметры функции
            :param kwargs: Параметры функции
            :return: Результат выполнения функции
            """
            with open(file_log, mode="a", encoding="utf-8") as file:
                call_time = datetime.datetime.now().strftime("%d.%m %H:%M:%S")
                file.write(f"{func.__name__} вызвана {call_time}\n")

            res = func(*args, ** kwargs)
            return res

        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        wrapper.__wrapped__ = func
        return wrapper
    return log


@func_log()
def func1():
    """Здесь должен быть одинаковый текст"""
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    """Здесь должен быть одинаковый текст"""
    time.sleep(5)


def func_bez_decoratora():
    """Здесь должен быть одинаковый текст"""
    time.sleep(2)


func1()
func2()

help(func1)
help(func2)
help(func_bez_decoratora)