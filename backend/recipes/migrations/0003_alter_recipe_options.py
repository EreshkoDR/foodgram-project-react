# Generated by Django 4.1.3 on 2022-12-05 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-create'], 'verbose_name': 'Список рецептов', 'verbose_name_plural': 'Список рецептов'},
        ),
    ]