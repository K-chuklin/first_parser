import requests
import json

from abc import ABC, abstractmethod


class Engine(ABC):
    """Абстрактный класс для получения данных с сайта по API"""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Метод получающий данные через API """
        pass


class HeadHunter(Engine):
    """Класс получающий данные через API"""

    def get_vacancies(self, keyword):
        headers = 'User-Agent: MyApp/1.0 (my-app-feedback@example.com)'
        options = {"page": 1,
                   "pages": 50,
                   "per_page": 5,
                   "text": f"{keyword}"
                   }
        response = requests.get('https://api.hh.ru/vacancies/', params=options)
        print(response.text)
        data = response.content.decode()
        vacancies = json.loads(data)
        return vacancies


class SuperJob(Engine):
    """Класс получающий данные через API"""
    api_key = "v3.r.131060990.e1e400037fee737d9f825d44ec9cf3d738664f3f.a7909ca161e54d97b371b8bda2e52c1f6b22f010"

    def get_vacancies(self, keyword):
        options = {
            "keyword": keyword,
            "page": 1,
            "count": 10,

        }
        api = {"X-Api-App-Id": SuperJob.api_key}
        response = requests.get(f"https://api.superjob.ru/2.0/vacancies/", headers=api, params=options)
        data = response.content.decode()
        vacancies = json.loads(data)
        return vacancies
