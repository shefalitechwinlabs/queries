# Generated by Django 4.0.3 on 2022-11-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0011_alter_entry_mod_date_alter_entry_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
