# Generated by Django 4.0.5 on 2022-07-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_visualization_visualizationimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualizationimage',
            name='orientation',
            field=models.CharField(default='horizontal', max_length=10),
        ),
    ]