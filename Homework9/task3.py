# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open(r'C:\autotests_course\Homework9\folder_for_task3\task_3.txt', mode="r") as file:
    list_sum = [0]
    for i in file:
        if i == "\n":
            list_sum.append(0)
        else:
            list_sum[-1] += int(i.rstrip("\n"))
    list_sum.sort(reverse=True)
    three_most_expensive_purchases = sum(list_sum[0:3])

assert three_most_expensive_purchases == 202346