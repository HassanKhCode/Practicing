class Person:
    def __init__(self, id: int, first_name: str, last_name: str, address: str, birth_year: int, phone_number = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.birth_year = birth_year

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_number}"

    def get_age(self) -> int:
        age = 2023 - self.birth_year
        return age

    def add_phone(self, number):
        self.phone_number = number

    def remove_phone(self):
        self.phone_number = None

if __name__ == '__main__':
    person = Person(123456, 'Hassan', 'Alkhanfa', 'hahohe', 2004)
    person.add_phone(13523245)
    person.remove_phone()
    print(person.__str__())