from faker import Faker


def generate_user_data():
    fake = Faker('ru_RU')
    email = fake.email()
    name = fake.name()
    password = fake.password(length=9)
    return {'email': email,
            'password': password,
            'name': name}

