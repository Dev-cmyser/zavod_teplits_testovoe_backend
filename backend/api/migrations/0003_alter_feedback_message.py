# Generated by Django 4.1.5 on 2023-01-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_feedback_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(verbose_name='Отзыв'),
        ),
    ]