# Generated by Django 4.0.5 on 2022-07-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_project_id_projectimage_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='area',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
