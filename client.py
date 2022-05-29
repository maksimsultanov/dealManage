class Client():
    def __init__(self):
        self.__name = ""
        self.__surname = ""
        self.__phone = ""
        self.__address = ""

    def set_client(self, name, surname, phone, address):
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        self.__address = address

    def set_client_from_json(self, client):
        try:
            self.__name = client["name"]
            self.__surname = client["address"]
            self.__phone = client["phone"]
            self.__address = client("address")
            return 0
        except:
            return 1

    def get_client(self):
        client = dict([("name", self.__name), ("surname", self.__surname),
                       ("phone", self.__phone), ("address", self.__address)])
        return client

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
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
