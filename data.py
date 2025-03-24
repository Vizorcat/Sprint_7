class Data:
    valid_login = 'Artem1994'
    valid_password = 'qwerty123'
    valid_firstname = 'Artem'
    valid_courier_data = {'login': 'Artem1994', 'password': 'qwerty123', 'firstName': 'Artem'}
    courier_data_without_name = {'login': 'Artem1994', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Artem1994', 'password': '123456'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Игнат',
        'lastName': 'Больсикй',
        'address': 'Невский, 16',
        'metroStation': 8,
        'phone': '+78005553535',
        'rentTime': 3,
        'deliveryDate': '2023-06-26',
        'comment': 'Серость',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Мария',
        'lastName': 'Топыгина',
        'address': 'Московский, 18',
        'metroStation': 10,
        'phone': '+78888888889',
        'rentTime': 7,
        'deliveryDate': '2024-06-28',
        'comment': 'Чёрность',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Иван',
        'lastName': 'Иванов',
        'address': 'Чебоксарский, 15',
        'metroStation': 15,
        'phone': '+70009991122',
        'rentTime': 1,
        'deliveryDate': '2024-06-30',
        'comment': 'Чёрно-серо',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Мая',
        'lastName': 'Майская',
        'address': 'Нижегородская, 2',
        'metroStation': 20,
        'phone': '+77777777777',
        'rentTime': 2,
        'deliveryDate': '2024-06-27',
        'comment': 'Пустота',
        'color': []
    }