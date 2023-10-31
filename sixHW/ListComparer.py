class ListComparer:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        if not all(isinstance(num, (int, float)) for num in lst):
            return None
        if len(lst) == 0:
            return None
        return sum(lst) / len(lst)

    def compare_lists(self):
        average1 = self.calculate_average(self.list1)
        average2 = self.calculate_average(self.list2)

        if average1 is None or average2 is None:
            return "Некорректные данные"

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average2 > average1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


# Пример использования программы
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
comparer = ListComparer(list1, list2)
result = comparer.compare_lists()
print(result)