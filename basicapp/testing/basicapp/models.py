from django.db import models

# Create your models here.
# from django_mysql.models import JSONField, Model
from django.db import models

# Create your models here.
class clothing(models.Model):
    SIZE_DICT=(('L','LARGE'),
                ('S','SMALL'),
                ('XL','XTRA-SMALL'),
    )
    name=models.CharField(max_length=30)
    size=models.CharField(max_length=2,choices=SIZE_DICT,default='L')
    

