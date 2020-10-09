# Generated by Django 2.2.8 on 2020-09-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('ELECTRONICS', 'ELECTRONICS'), ('FASHION', 'FASHION'), ('BOOKS', 'BOOKS'), ('BEAUTY', 'BEAUTY'), ('KITCHEN', 'KITCHEN')], max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=256)),
                ('country_of_orgin', models.CharField(choices=[('INDIA', 'INDIA'), ('CHINA', 'CHINA'), ('EUROPE', 'EUROPE'), ('RUSSIA', 'RUSSIA'), ('MEXICO', 'MEXICO')], max_length=20)),
                ('Rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=20)),
                ('feedback', models.TextField()),
            ],
        ),
    ]