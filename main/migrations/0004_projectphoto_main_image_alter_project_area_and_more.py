# Generated by Django 4.0.5 on 2022-07-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_project_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectphoto',
            name='main_image',
            field=models.ImageField(default=None, upload_to='gallery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='area',
            field=models.CharField(blank=True, default=None, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
