# Generated by Django 3.2 on 2021-07-29 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2021', '0007_caseinfosection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='c1_body',
        ),
        migrations.RemoveField(
            model_name='case',
            name='c1_title',
        ),
        migrations.RemoveField(
            model_name='case',
            name='c2_body',
        ),
        migrations.RemoveField(
            model_name='case',
            name='c2_title',
        ),
        migrations.RemoveField(
            model_name='case',
            name='c3_body',
        ),
        migrations.RemoveField(
            model_name='case',
            name='c3_title',
        ),
        migrations.RemoveField(
            model_name='case',
            name='c4_body',
        ),
        migrations.RemoveField(
            model_name='case',
            name='c4_title',
        ),
    ]
