import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')

import django
django.setup()

import random
from apptwo.models import user
from faker import Faker

fakegen = Faker()


def populate (N=5):
    for entry in range(N):

        fake_firstName=fakegen.first_name()
        fake_last_Name=fakegen.last_name()
        fake_Email=fakegen.email()

        user_name=user.objects.get_or_create(FirstName=fake_firstName,LastName=fake_last_Name,Email=fake_Email)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating done!!!")