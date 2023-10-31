from unitFourHW.sixHW.ListComparer import ListComparer

class TestListComparer:
    def test_compare_lists_average1_greater(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 10]
        comparer = ListComparer(list1, list2)
        result = comparer.compare_lists()
        assert result == "Второй список имеет большее среднее значение"

    def test_compare_lists_average2_greater(self):
        list1 = [6, 7, 8, 9, 10]
        list2 = [1, 2, 3, 4, 5]
        comparer = ListComparer(list1, list2)
        result = comparer.compare_lists()
        assert result == "Первый список имеет большее среднее значение"

    def test_compare_lists_averages_equal(self):
        list1 = [1, 2, 3]
        list2 = [2, 2, 2]
        comparer = ListComparer(list1, list2)
        result = comparer.compare_lists()
        assert result == "Средние значения равны"

    def test_compare_lists_incorrect_list(self):
        list1 = []
        list2 = [1, 2, 3]
        comparer = ListComparer(list1, list2)
        result = comparer.compare_lists()
        assert result == "Некорректные данные"

    def test_compare_lists_empty_list(self):
        list1 = ['dgfd']
        list2 = [1, 2, 3]
        comparer = ListComparer(list1, list2)
        result = comparer.compare_lists()
        assert result == "Некорректные данные"

    def test_calculate_average_empty_list(self):
        lst = []
        comparer = ListComparer([], [])
        average = comparer.calculate_average(lst)
        assert average is None
    def test_compare_lists_negative_numbers(self):
        list1 = [-1, -2, -3]
        list2 = [-4, -5, -6]
        comparer = ListComparer(list1, list2)
        result = comparer.compare_lists()
        assert result == "Первый список имеет большее среднее значение"

    def test_compare_lists_decimal_numbers(self):
        list1 = [1.5, 2.5, 3.5]
        list2 = [4.5, 5.5, 6.5]
        comparer = ListComparer(list1, list2)
        result = comparer.compare_lists()
        assert result == "Второй список имеет большее среднее значение"

    def test_calculate_average_single_element_list(self):
        lst = [5]
        comparer = ListComparer([], [])
        average = comparer.calculate_average(lst)
        assert average == 5.0

    

class TestListComparerIntegration:
    def test_compare_lists_with_external_data(self):
        # Подготовка данных из внешнего файла
        list1 = []
        list2 = []
        with open("data.txt", "r") as file:
            for line in file:
                values = line.strip().split(",")
                list1.append(int(values[0]))
                list2.append(int(values[1]))

        comparer = ListComparer(list1, list2)

        result = comparer.compare_lists()

        assert result == "Второй список имеет большее среднее значение"


 

    


