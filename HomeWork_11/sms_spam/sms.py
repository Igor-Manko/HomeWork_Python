class Person:
    def __init__(self, name, lastname, secondname, dict_phone):
        self.name = name
        self.lastname = lastname
        self.secondname = secondname
        self.dict_phone = dict_phone

    def get_phone(self):
        return dict(self.dict_phone).get('private')  # метод get -> None если нет номера

    def get_name(self):
        return self.name

    def get_work_phone(self):
        return dict(self.dict_phone).get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.secondname}! Примите участие в розыгрыше для физических лиц!'


class Company:
    def __init__(self, name_company, type_company, dict_contact, *person):
        self.name_company = name_company
        self.type_company = type_company
        self.dict_contact = dict_contact
        self.person_list = person

    def get_phone(self):
        if dict(self.dict_contact).get('contact'):
            return self.dict_contact.get('contact')
        for person in self.person_list:
            number = person.get_work_phone()
            if number:
                return number

    def get_name(self):
        return f'{self.name_company}'

    def get_sms_text(self):
        return f'Для компании {self.name_company}! Конкурс для "{self.type_company}" компаний!'


def send_sms(*number):
    for num in number:
        if num.get_phone():
            print(f'Отправлено СМС на номер {num.get_phone()} с текстом: {num.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {num.get_name()}')


person1 = Person('Ivan', 'Ivanov', 'Ivanovich', {'private': 123, 'work': 456})
person2 = Person('Ivan', 'Petrov', 'Petrovich', {'private': 789})
person3 = Person('Ivan', 'Sidorov', 'Petrovich', {'work': 789})
person4 = Person('John', 'Doe', 'Unknown', {})

company1 = Company('Bell', 'OOO', {'contact': 111}, person3, person4)
company2 = Company('Cell', 'AO', {'non_contact': 222}, person2, person3)
company3 = Company('Dell', 'Ltd', {'non_contact': 333}, person2, person4)

send_sms(person1, person2, person3, person4, company1, company2, company3)
