from src.utils import number_of_vacancies, sorting_vacancies
from src.vacancies import HhVacancies, SjVacancies
from src.api import HeadHunter, SuperJob
from src.data_handler import JSONFile


def main():

    user_keyword = input("Введите ключевое слов для поиска: ")
    vacancies_counter = int(input("Введите кол-во интересующих вакансий: "))
    selected_platform = int(input("1: HeadHunter, 2: SuperJob\nВыберите платформу для поиска: "))


    # Переменная для записи данных в файл и получения из файла
    writer_data = JSONFile()
    try:
        if selected_platform == 1:
            hh_api = HeadHunter()
            hh_vacancies = hh_api.get_vacancies(user_keyword)
            writer_data.data_writer(hh_vacancies)
            list_data = writer_data.data_getter()

            # Инициализируем список экземпляров класса
            list_vacancies = [HhVacancies.init_item_hh(element) for element in list_data['items']]
            # Сортируем список с вакансиями
            sorting_vacancies(list_vacancies)

            user_choose_output = input('Показать вакансий? (да/нет): ')
            if user_choose_output.lower() == "да":
                result = number_of_vacancies(list_vacancies, vacancies_counter)
                for vacancy in result:
                    print(vacancy)

            user_get_by_salary = input('Отсортировать вакнсии по з/п? (да/нет): ')
            if user_get_by_salary.lower() == 'да':
                users_salary = input('Введите диапазон з/п:')
                # Получаем список вакансий, подходящих по з/п под заданный диапазон
                result = writer_data.get_data_by_salary(users_salary)
                for vacancy in result:
                    print(vacancy)

        elif selected_platform == 2:
            sj_api = SuperJob()
            sj_vacancies = sj_api.get_vacancies(user_keyword)
            writer_data.data_writer(sj_vacancies)
            list_data = writer_data.data_getter()

            # Инициализируем список экземпляров класса
            list_vacancies = [SjVacancies.init_item_sj(element) for element in list_data['objects']]

            user_choose_output = input('Показать вакансий? (да/нет): ')
            if user_choose_output.lower() == 'да':
                result = number_of_vacancies(list_vacancies, vacancies_counter)
                for element in result:
                    print(element)

            user_get_salary_vacancies = input('Отсортировать вакнсии по з/п? (да/нет): ')
            if user_get_salary_vacancies.lower() == 'да':
                users_salary = input('Введите диапазон з/п: ')
                # Получаем список вакансий, подходящих по з/п под заданный диапазон
                result = writer_data.get_data_by_salary(users_salary)
                for vacancy in result:
                    print(vacancy)
    except Exception as error:
        print(error)
    finally:
        writer_data.data_deleter()


if __name__ == "__main__":
    main()
