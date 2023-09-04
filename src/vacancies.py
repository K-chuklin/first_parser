from abc import ABC, abstractmethod


class Vacancies(ABC):
    @abstractmethod
    def __init__(self):
        pass


class HhVacancies(Vacancies):
    """ Класс описывает экземпляры вакансий, полученных с сайта HeadHunter """

    def __init__(self, id, name, url, salary, requirement, responsibility):

        self.id = id
        self.name = name
        self.url = url
        if salary is not None:
            self.salary = salary['from'] if salary['from'] is not None else salary['to']
        else:
            self.salary = 0
        self.requirement = requirement
        self.responsibility = responsibility

    @classmethod
    def init_item_hh(cls, data):
        vacancies = HhVacancies(data['id'], data['name'], data['url'], data['salary'],
                                data['snippet']['requirement'], data['snippet']['responsibility'])

        return vacancies

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, " \
               f"{self.name}, " \
               f"{self.url}, " \
               f"{self.salary}," \
               f"{self.requirement}, " \
               f"{self.responsibility})"

    def __str__(self):
        return f"Класс: {self.__class__.__name__}, " \
               f"вакансия: {self.name}, " \
               f"id: {self.id},\n" \
               f"Cсылка: {self.url}, З/п: {self.salary},\n" \
               f"требования: {self.requirement}, " \
               f"обязанности: {self.responsibility}"

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        else:
            return False

    def __le__(self, other):
        if self.salary <= other.salary:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.salary > other.salary:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.salary >= other.salary:
            return True
        else:
            return False


class SjVacancies(Vacancies):
    """Класс описывает экземпляры вакансий, полученных с сайта SuperJob"""

    def __init__(self, id, name, url, salary_from, salary_to, vacancies_info):

        self.id = id
        self.name = name
        self.url = url
        if salary_from == 0 and salary_to == 0:
            self.salary = 0
        self.salary = salary_from if salary_from != 0 else salary_to
        self.info = vacancies_info

    @classmethod
    def init_item_sj(cls, data):
        """Инициализатор экземпляров"""
        vacancy = SjVacancies(data['id'], data['profession'], data['link'], data['payment_from'],
                              data['payment_to'], data['candidat'])

        return vacancy

    def __repr__(self):
        """Информация об экземпляре для отладки"""
        return f"{self.__class__.__name__}({self.id}, " \
               f"{self.name}, " \
               f"{self.url}, " \
               f"{self.salary}," \
               f"{self.info})"

    def __str__(self):
        """Информация об экземпляре для пользователя"""
        return f"Класс: {self.__class__.__name__}, " \
               f"id: {self.id}, " \
               f"название: {self.name},\n" \
               f"Ссылка: {self.url}, З/п: {self.salary}, " \
               f"требования и обязанности: {self.info} "

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        else:
            return False

    def __le__(self, other):
        if self.salary <= other.salary:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.salary > other.salary:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.salary >= other.salary:
            return True
        else:
            return False
