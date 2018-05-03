import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')


import django
django.setup()


import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()
        User.objects.get_or_create(first_name= fake_firstname, last_name= fake_lastname, email= fake_email)[0]


if __name__ == '__main__':
    print('populating database')
    populate(20)
    print('database population complete!')