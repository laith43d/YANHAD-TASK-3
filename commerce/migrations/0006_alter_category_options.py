# Generated by Django 3.2.9 on 2021-12-20 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
