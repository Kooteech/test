# Generated by Django 3.1 on 2020-08-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbs_app', '0016_auto_20200817_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='teacher',
            field=models.ManyToManyField(related_name='Педагог', to='dbs_app.TeacherData'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
