# Generated by Django 4.1.5 on 2023-01-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(max_length=254, verbose_name='Отзыв'),
        ),
    ]
