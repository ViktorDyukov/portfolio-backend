# Generated by Django 3.2 on 2021-07-31 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2021', '0008_auto_20210729_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='date',
        ),
        migrations.AddField(
            model_name='case',
            name='description',
            field=models.CharField(default='', max_length=40),
        ),
    ]
