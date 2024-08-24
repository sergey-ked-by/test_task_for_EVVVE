import random
import string

domains = ["example.com", "mail.com", "test.org", "domain.net"]
first_names = ["Ivan", "Petr", "Sidor"]
last_names = ["Ivanov", "Petrov", "Sidorov"]
passwords = ["password_1", "password_2", "password_3"]


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))


def generate_random_first_name():
    return random.choice(first_names)


def generate_random_last_name():
    return random.choice(last_names)


def generate_random_email():
    username = generate_random_string(10)
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_random_password():
    return random.choice(passwords)


def user_data():
    return {
        'new_user': {
            'first_name': generate_random_first_name(),
            'last_name': generate_random_last_name(),
            'email': generate_random_email(),
            'password': generate_random_password(),
        }
    }
