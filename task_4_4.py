list_1 = [32, 456, 2, 8, 56, 975467, 34526]
b = len(list_1) - 1  # присваиваем переменной значение индекса последнего элемента списка
list_new = []
index = 0
while index <= b:
    list_new.append(list_1[-b + index])  # присвоив переменной b отрицательное значение добавляем элементы в новый список начиная со второго элемента
    index += 1
print(list_new)


list_2 = [32, 456, 2, 8, 56, 975467, 34526]
d = len(list_2)  # присваиваем переменной значение кол-во элементов в списке
list_new_2 = []
for i in range(1, d):
    list_new_2.append(list_2[i])  #
list_new_2.append(list_2[0])
print(list_new_2)