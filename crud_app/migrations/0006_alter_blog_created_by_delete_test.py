# Generated by Django 4.0.3 on 2022-10-28 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud_app', '0005_rename_tagline_blog_body_text_remove_entry_body_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
