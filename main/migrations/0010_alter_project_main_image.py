# Generated by Django 4.0.5 on 2022-07-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_project_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=models.ImageField(blank=True, default=None, upload_to='attachments'),
        ),
    ]
