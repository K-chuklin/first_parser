def number_of_vacancies(vacancies_list, number):
    """
    Метод возвращает заданное пользователем количество объектов с информацией о вакансии.
    """
    list_vacancies_counter = []
    try:
        list_vacancies_counter = [x for x in vacancies_list[:number]]
    except IndexError:
        print(f"Длина списка({len(vacancies_list)}) меньше указанного количества вакансий({number})!")
    return list_vacancies_counter


def sorting_vacancies(vacancies_list):
    """Функция для сортировки вакансий по з/п """
    vacancies_list.sort(reverse=True)
    return vacancies_list
