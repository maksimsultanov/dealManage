class Client():
    def __init__(self):
        """
        Конструктор класса
        Создаются атрибуты класса, инициализируются с пустым значением
        self.__name = ""        Имя клиента
        self.__surname = ""     Фамилия клиента
        self.__phone = ""       Телефон клиента
        self.__address = ""     Адрес клиента
        """
        self.__name = ""
        self.__surname = ""
        self.__phone = ""
        self.__address = ""

    def set_client(self, name, surname, phone, address):
        """
        Функция инициализации
        :param name:        Имя клиента
        :param surname:     Фамилия Клиента
        :param phone:       Телефон Клиента
        :param address:     Адрес клиента
        """
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        self.__address = address

    def set_client_from_json(self, client):
        """
        Функция инициализации из JSON
        :param client:      Данные переданные в формате JSON
        :return:            0 - если инициализация прошла успешно, 1 - если нет
        """
        try:
            self.__name = client["name"]
            self.__surname = client["address"]
            self.__phone = client["phone"]
            self.__address = client("address")
            return 0
        except:
            return 1

    def get_client(self):
        """
        Функция в формате словаря возращает значение атрибутов объекта
        """
        client = dict([("name", self.__name), ("surname", self.__surname),
                       ("phone", self.__phone), ("address", self.__address)])
        return client

    def get_name(self):
        """
        :return: значение атрибута __name Имя клиента
        """
        return self.__name

    def set_name(self, name):
        """
        Установка атрибута __name
        :param name:    Имя клиента
        :return:
        """
        self.__name = name

    def get_surname(self):
        """
        :return: self.__surname     Фамилия клиента
        """
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
