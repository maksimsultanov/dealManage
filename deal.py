from client import Client


class Deal():
    def __init__(self):
        """
        """
        self.__title = ""
        self.__description = ""
        self.__client = Client()
        self.__products = []
        self.__delivery_address = ""
        self.__delivery_date = ""
        self.__delivery_code = ""

    def set_deal(self, title, description, client, products, address, date, code):
        """
        :param title:
        :param description:
        :param client:
        :param products:
        :param address:
        :param date:
        :param code:
        :return:
        """
        self.__title = title
        self.__description = description
        self.__client.set_client_from_json(client)
        self.__products = products
        self.__delivery_address = address
        self.__delivery_date = date
        self.__delivery_code = code

    def set_deal_from_json(self, deal):
        """
        :param deal:
        :return:
        """
        self.__title = deal['title']
        self.__description = deal['description']
        self.__client.set_client_from_json(deal['client'])
        self.__products = deal['products']
        self.__delivery_address = deal['delivery_address']
        self.__delivery_date = deal['delivery_date']
        self.__delivery_code = deal['delivery_code']

    def set_title(self, title):
        """
        :param title:
        :return:
        """
        self.__title = title

    def get_title(self):
        """
        :return:
        """
        return self.__title

    def set_description(self, description):
        """
        :param description:
        :return:
        """
        self.__description = description

    def get_description(self):
        """
        :return:
        """
        return self.__description

    def set_client_from_json(self, client):
        """
        :param client:
        :return:
        """
        self.__client.set_client_from_json(client)

    def get_client(self):
        """
        :return:
        """
        return self.__client.get_client()

    def set_products(self, products):
        """
        :param products:
        :return:
        """
        for product in products:
            self.__products.append(product)

    def get_products(self):
        """
        :return:
        """
        return self.__products

    def set_address(self, address):
        """
        :param address:
        :return:
        """
        self.__delivery_address = address

    def get_address(self):
        """
        :return:
        """
        return self.__delivery_address

    def set_date(self, date):
        """
        :param date:
        :return:
        """
        self.__delivery_date = date

    def get_date(self):
        """
        :return:
        """
        return self.__delivery_date

    def set_code(self, code):
        """
        :param code:
        :return:
        """
        self.__delivery_code = code

    def get_code(self):
        """
        :return:
        """
        return self.__delivery_code


if __name__ == '__main__':
    print("""
    этот файл не является исполняемым, 
    и содержит описание класса Deal
    """)
