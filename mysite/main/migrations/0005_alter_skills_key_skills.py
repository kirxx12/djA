# Generated by Django 4.1.5 on 2023-01-10 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='key_skills',
            field=models.IntegerField(),
        ),
    ]
