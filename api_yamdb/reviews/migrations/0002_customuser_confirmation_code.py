# Generated by Django 3.2 on 2023-10-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
    ]