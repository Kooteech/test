# Generated by Django 3.1 on 2020-08-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbs_app', '0005_auto_20200813_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childdata',
            name='sex',
            field=models.CharField(blank=True, choices=[('boy', 'М'), ('girl', 'Ж')], max_length=10, null=True),
        ),
    ]
