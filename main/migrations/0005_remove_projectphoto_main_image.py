# Generated by Django 4.0.5 on 2022-07-03 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_projectphoto_main_image_alter_project_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectphoto',
            name='main_image',
        ),
    ]
