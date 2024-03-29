# Generated by Django 3.2 on 2021-07-29 05:57

from django.db import migrations, models
import django.db.models.deletion
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('app2021', '0006_alter_link_link_ext'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseInfoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('body', martor.models.MartorField(null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2021.case')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
