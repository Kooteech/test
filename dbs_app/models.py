from django.db import models
from django.utils import timezone
import datetime
from django import forms
from multiselectfield import MultiSelectField
from django.contrib.admin.widgets import FilteredSelectMultiple


class ChildData(models.Model):
    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Ученики'

    personal_number = models.CharField(max_length=15, verbose_name="Номер личного дела", default="Не присвоен", blank=True)
    first_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Отчество')
    date_birth = models.DateField(verbose_name='Дата рождения')
    parent = models.CharField(max_length=100, verbose_name='ФИО родителя', default='')
    certificate_num = models.CharField(max_length=100, verbose_name='Номер сертификата')
    phone_number = models.CharField(max_length=15, null=True, verbose_name='Номер телефона')
    adress = models.CharField(max_length=100, verbose_name='Адрес', default='')
    sex = models.CharField(max_length=10,
                           choices=(('boy', 'М'), ('girl', 'Ж')), default='Пол не выбран', verbose_name='Пол')
    teach_status = models.CharField(max_length=20,
                                    choices=(('free', 'Бюджет'), ('pay', 'Платник')), default='',
                                    verbose_name='Тип обучения')
    udo_status = models.CharField(max_length=20, blank=True, choices=(
        ('not_avail', 'Не посещает'),
        ('Yes', 'Посещающий'),
        ('No', 'Домашний')
    ),
                                  verbose_name='Посещение УДО', null=True, default='not_avail')
    udo_name = models.CharField(max_length=50, blank=True, default='', verbose_name='Название УДО')
    udo_group = models.CharField(max_length=20, blank=True, default='', verbose_name='Группа')
    municipal_status = models.CharField(max_length=20, blank=True,
                                        choices=(
                                            ('not_avail', 'Не посещает'),
                                            ('Yes', 'Посещающий'),
                                            ('No', 'Семейное обучение')
                                        ),
                                        verbose_name='Посещение МООУ', null=True, default='not_avail')
    municipal_name = models.CharField(max_length=50, blank=True, null=True, default='', verbose_name='Название МООУ')
    class_number = models.CharField(max_length=50, blank=True, null=True, default='', verbose_name='№ класса')
    spo_name = models.CharField(max_length=50, blank=True, null=True, default='', verbose_name='Название СПО')
    spo_number = models.CharField(max_length=50, blank=True, null=True, default='',
                                  verbose_name='№ курса (соответствующий классу в МООУ)')
    he_name = models.CharField(max_length=50, blank=True, null=True, default='',
                               verbose_name='Название учреждения ВО')
    he_number = models.CharField(max_length=50, blank=True, null=True, default='',
                                 verbose_name='№ курса')
    family_status_choices = (('status1', 'Малообеспеченная семья'),
                             ('status2', 'Многодетная семья'),
                             ('status3', 'Сирота'),
                             ('status4', 'Под опекой'),
                             ('status5', 'ОВЗ'),
                             ('status6', 'Инвалид')
                             )
    family_status = MultiSelectField(verbose_name='Семейный статус', blank=True, choices=family_status_choices)
    # family_status = models.CharField(max_length=10, blank=True,
    #                                  choices=(('status1', 'Малообеспеченная семья'),
    #                                           ('status2', 'Многодетная семья'),
    #                                           ('status3', 'Сирота'),
    #                                           ('status4', 'Под опекой'),
    #                                           ('status5', 'ОВЗ'),
    #                                           ('status6', 'Инвалид')
    #                                           ), default='status0',
    #                                  verbose_name='Семейный статус')
    diagnose_choices = (('cat_K', 'Категория К'), ('cat_O', 'Категория О'), ('cat_S', 'Категория С'), ('cat_G', 'Категория Г'))
    diagnose = MultiSelectField(verbose_name='Категория МГН', blank=True, choices=diagnose_choices)
    # diagnose = models.TextField(max_length=100, blank=True, default='',
    #                             verbose_name='Диагноз (если выбран статус "ОВЗ" или "Инвалид"')
    special_status_choices = (('ooy_spec', 'Состоит в ООУ'), ('pdn_spec', 'Состоит в ПДН'), ('kdn_spec', 'Состоит в КДН'))
    special_status = MultiSelectField(verbose_name="Учёт", blank=True, choices=special_status_choices)
    # special_status = models.CharField(max_length=10,
    #                                   choices=(('no_spec', 'Не состоит'), ('ooy_spec', 'Состоит в ООУ'),
    #                                            ('pdn_spec', 'Состоит в ПДН')), default='no_spec',
    #                                   verbose_name='Состоит на учёте?')
    doc_zayavl_checkbox = models.BooleanField(verbose_name="Заявление", blank=True, default=False)
    doc_dogovor_checkbox = models.BooleanField(verbose_name="Договор", blank=True, default=False)
    doc_opd_checkbox = models.BooleanField(verbose_name="Согласие на ОПД", blank=True, default=False)
    doc_soprovod_checkbox = models.BooleanField(verbose_name="З-ние о сопр. (до 12 лет)", blank=True,
                                                default=False)
    doc_svid_checkbox = models.BooleanField(verbose_name="Копия св-ва о рождении", blank=True, default=False)


class TeacherData(models.Model):
    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField('Date of birth')


class Section(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объединение'
        verbose_name_plural = 'Объединения'

    name = models.CharField(max_length=100)
    data = models.TextField()


class Group(models.Model):
    def __str__(self):
        return '{} ({})'.format(self.group_name, self.group_section)

    group_name = models.CharField(max_length=50,
                                  verbose_name='Название группы')
    group_section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                      verbose_name='Объединение')
    teacher = models.ManyToManyField(TeacherData, verbose_name='Педагоги')

    children = models.ManyToManyField(ChildData, verbose_name='Дети')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
