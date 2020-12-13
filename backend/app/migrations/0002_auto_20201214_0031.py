# Generated by Django 3.1.4 on 2020-12-13 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airlines',
            options={'verbose_name_plural': 'Airlines'},
        ),
        migrations.AlterModelOptions(
            name='bookedtours',
            options={'verbose_name_plural': 'Booked_Tours'},
        ),
        migrations.AlterModelOptions(
            name='cities',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='countries',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='hotels',
            options={'verbose_name_plural': 'Hotels'},
        ),
        migrations.AlterModelOptions(
            name='insurances',
            options={'verbose_name_plural': 'Insurances'},
        ),
        migrations.AlterModelOptions(
            name='tourcatalog',
            options={'verbose_name_plural': 'Tour_Catalog'},
        ),
        migrations.AlterModelOptions(
            name='tourists',
            options={'verbose_name_plural': 'Tourists'},
        ),
        migrations.AlterModelOptions(
            name='typeofdocuments',
            options={'verbose_name_plural': 'Type_Of_Documents'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
    ]
