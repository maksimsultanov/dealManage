from bitrix24 import *


if __name__ == '__main__':
    bx24 = Bitrix24('https://b24-lvyl0a.bitrix24.ru/rest/1/sqdjgv7coroazipt/')
    deals = bx24.callMethod('crm.deal.list')
    print(deals)
    list_deals = []
