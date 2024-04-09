# Задание 1 - Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def unique_numbers(numbers):
    uniq_set = set(numbers)
    return list(uniq_set)


print(unique_numbers([1, 2, 3, 4,3,6, 7, 8, 6, 10,-1,0,-1]))

#Задание 2 - Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.

def easy_numbers(min_number, max_number):
    easy_numbers = []
    for number in range(min_number, max_number + 1):
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            easy_numbers.append(number)
    return easy_numbers

print(easy_numbers(1,16))


#Задание 3 -  Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    alpha = Point(1, 2)
    beta = Point(3, 4)

    print(alpha.distance_to(beta)) 


#Задание 4 - Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.


    def sort_by_length(stroks):
        stroks_up = sorted(stroks, key=len, reverse=False)
        stroks_down = sorted(stroks, key=len, reverse=True)        
        return stroks_up,stroks_down
     

    print(sort_by_length(['a', 'bbbbb', 'ccc', 'dddd']))


