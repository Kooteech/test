# Generated by Django 3.1 on 2020-08-17 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('certificate_num', models.CharField(max_length=100, verbose_name='Номер сертификата')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Номер телефона')),
                ('sex', models.CharField(choices=[('boy', 'М'), ('girl', 'Ж')], default='Sex is not set', max_length=10, verbose_name='Пол')),
                ('udo_status', models.CharField(blank=True, choices=[('not_avail', 'Не посещает'), ('Yes', 'Посещающий'), ('No', 'Домашний')], default='not_avail', max_length=20, null=True, verbose_name='Посещение УДО')),
                ('udo_name', models.CharField(blank=True, default='---', max_length=50, verbose_name='Название УДО')),
                ('municipal_status', models.CharField(blank=True, choices=[('not_avail', 'Не посещает'), ('Yes', 'Посещающий'), ('No', 'Семейное обучение')], default='not_avail', max_length=20, null=True, verbose_name='Посещение МООУ')),
                ('municipal_name', models.CharField(blank=True, default='---', max_length=50, null=True, verbose_name='Название МООУ')),
                ('class_number', models.CharField(blank=True, default='---', max_length=50, null=True, verbose_name='№ класса')),
                ('spo_name', models.CharField(blank=True, default='---', max_length=50, null=True, verbose_name='Название СПО')),
                ('spo_number', models.CharField(blank=True, default='---', max_length=50, null=True, verbose_name='№ курса (соответствующий классу в МООУ)')),
                ('he_name', models.CharField(blank=True, default='---', max_length=50, null=True, verbose_name='Название учреждения ВО')),
                ('he_number', models.CharField(blank=True, default='---', max_length=50, null=True, verbose_name='№ курса')),
                ('family_status', models.CharField(blank=True, choices=[('status1', 'Малообеспеченная семья'), ('status2', 'Многодетная семья'), ('status3', 'Сирота'), ('status4', 'Под опекой'), ('status5', 'ОВЗ'), ('status6', 'Инвалид')], default='status0', max_length=10, verbose_name='Семейный статус')),
                ('diagnose', models.TextField(blank=True, default='---', max_length=100, verbose_name='Диагноз (если выбран статус "ОВЗ" или "Инвалид"')),
                ('special_status', models.CharField(choices=[('no_spec', 'Не состоит'), ('ooy_spec', 'Состоит в ООУ'), ('pdn_spec', 'Состоит в ПДН')], default='no_spec', max_length=10, verbose_name='Состоит на учёте?')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data', models.TextField()),
            ],
            options={
                'verbose_name': 'Объединение',
                'verbose_name_plural': 'Объединения',
            },
        ),
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_birth', models.DateField(verbose_name='Date of birth')),
            ],
            options={
                'verbose_name': 'Педагог',
                'verbose_name_plural': 'Педагоги',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, verbose_name='Название группы')),
                ('children', models.ManyToManyField(to='dbs_app.ChildData', verbose_name='Дети')),
                ('group_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbs_app.section', verbose_name='Объединение')),
                ('teacher', models.ManyToManyField(to='dbs_app.TeacherData', verbose_name='Педагоги')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]