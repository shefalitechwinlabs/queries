# Generated by Django 4.0.3 on 2022-10-28 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0003_remove_author_author_name_remove_entry_mod_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='blog',
        ),
    ]
