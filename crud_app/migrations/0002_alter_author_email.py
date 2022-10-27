# Generated by Django 4.0.3 on 2022-10-27 11:32

import crud_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, validators=[crud_app.models.validate_google_mail]),
        ),
    ]
