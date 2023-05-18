# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    """
    Глобальная функция, содержащая в себе локальную функцию local_function
    @return: Измененная в local_function локальная перемененная на новую переменную
    """
    msg = 1

    def local_function():
        """
        Локальная функция, необходимая для изменения локальной переменной из глобальной функции global_function
        """
        nonlocal msg
        msg = 2

    local_function()
    return msg

global_function()


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')