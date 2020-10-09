from django.db import models

# Create your models here.
class Feedback(models.Model):
    RATING_DIR=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    # name = models.CharField(max_length=34)
    # email = models.EmailField()
    # phone_number = models.CharField(max_length=15, blank=True)
    # rating = models.CharField(max_length=4, choices=RATING_CHOICES)
    # feedback = models.TextField()
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=20)
    Rating=models.CharField(max_length=20,choices=RATING_DIR)
    feedback=models.TextField()

class Productname(models.Model):
    CATEGORY_DIR=(
        ('ELECTRONICS','ELECTRONICS'),
        ('FASHION','FASHION'),
        ('BOOKS','BOOKS'),
        ('BEAUTY','BEAUTY'),
        ('KITCHEN','KITCHEN'),
    )
    RATING_DIR=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    COUNTRY_DIR=(
        ('INDIA','INDIA'),
        ('CHINA','CHINA'),
        ('EUROPE','EUROPE'),
        ('RUSSIA','RUSSIA'),
        ('MEXICO','MEXICO'),
    )
    productname=models.CharField(max_length=20)
    category=models.CharField(max_length=20,choices=CATEGORY_DIR)
    price=models.IntegerField()
    description=models.TextField(max_length=256)
    country_of_orgin=models.CharField(max_length=20,choices=COUNTRY_DIR)
    Rating=models.CharField(max_length=20,choices=RATING_DIR)
    feedback=models.TextField()

