import json
from abc import ABC, abstractmethod


class ProcessingData(ABC):
    """Абстрактный класс, которые обрабатывают данные,
    полученные от API сайтов"""

    @abstractmethod
    def data_writer(self, data):
        pass

    @abstractmethod
    def data_getter(self):
        pass

    @abstractmethod
    def data_deleter(self):
        pass


class JSONFile(ProcessingData):
    """ Класс для работы с файлами, которые имеют расширение .json"""

    def data_writer(self, data, file_with_vacancy='vacancy.json'):
        with open(f"{file_with_vacancy}", "a+") as file:
            json.dump(data, indent=2, ensure_ascii=True, fp=file)

    def data_getter(self, vacancy_file='vacancy.json'):
        with open(f"{vacancy_file}") as file:
            data = json.load(file)
            return data

    def get_data_by_salary(self, salary, vacancy_file='vacancy.json'):
        """
        Метод для получения информации об вакансиях, с з/п, указанной пользователем
        """
        result_list = []
        # Разбиваем переданный диапазон з/п на два числа для последующего сравнения
        list_salary = salary.split('-')
        # Получаем данные из файла
        obj_with_vacancies = self.data_getter(vacancy_file)
        """
        Проверяем наличие ключей 'items' и 'objects'. 
        Первый ключ хранится в данных, полученных с сайта HeadHunter
        Второй ключ хранится в данных полученных с сайта SuperJob
        """
        # Проверяем наличие ключа 'items'
        if 'items' in obj_with_vacancies.keys():
            # перебираем список вакансий
            for element in obj_with_vacancies['items']:
                # Под ключом 'salary' могут находиться None значение, поэтому проверяем его наличие
                if element['salary'] is not None:
                    """
                    Если значение с ключом 'salary' не None, тогда проверяем,
                    содержат ли границы з/п None значения
                    """
                    if None in element['salary'].values():
                        # Если одно из значений None, то сразу сравниваем с оставшимся значением
                        if element['salary']['from'] is None:
                            if int(list_salary[0]) <= element['salary']['to'] <= int(list_salary[1]):
                                result_list.append(element)
                        if element['salary']['to'] is None:
                            if int(list_salary[0]) <= element['salary']['from'] <= int(list_salary[1]):
                                result_list.append(element)
                    else:
                        # Если оба значения не None, то из двух значений считаем среднее и сравниваем
                        # с заданным диапазоном з/п
                        average_salary = (element['salary']['from'] + element['salary']['to']) // 2
                        if int(list_salary[0]) <= average_salary <= int(list_salary[1]):
                            result_list.append(element)
        # Проверяем наличие ключа 'objects'
        elif 'objects' in obj_with_vacancies.keys():
            # Перебираем список вакансий
            for element in obj_with_vacancies['objects']:
                # Так же проверяем наличие None в значениях и при прохождении проверки складываем
                if element['payment_from'] is not None:
                    if int(list_salary[0]) <= element['payment_from'] <= int(list_salary[1]):
                        result_list.append(element)
                elif element['payment_to'] is not None:
                    if int(list_salary[0]) <= element['payment_to'] <= int(list_salary[1]):
                        result_list.append(element)
                else:
                    average_salary = (element['payment_from'] + element['payment_to'] // 2)
                    if int(list_salary[0]) <= average_salary <= list_salary[1]:
                        result_list.append(element)
        return result_list

    def data_deleter(self, vacancy_file='vacancy.json'):
        """Функция удаляет все данные из файла"""
        with open(f'{vacancy_file}', "w") as file:
            file.write('')
            print("Данные удалены")
