# Generated by Django 3.2 on 2021-07-27 11:08

import app2021.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2021', '0005_alter_case_preview_deskx2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_ext',
            field=models.CharField(default=app2021.models.random_string, max_length=20),
        ),
    ]
