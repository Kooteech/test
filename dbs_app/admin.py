from django.contrib import admin
from django import forms
from .models import ChildData, TeacherData, Section, Groups


# Register your models here.
@admin.register(ChildData)
class ChildDataAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Данные ученика', {
            'fields': ['first_name', 'middle_name', 'last_name', 'date_birth', 'sex', 'phone_number', 'certificate_num']
        }),
        ('Информация об УДО', {
            'fields': ['udo_status', 'udo_name']
        }),
        ('Информация о МООУ', {
            'fields': ['municipal_status', 'municipal_name', 'class_number']
        }),
        ('Информация о СПО', {
            'fields': ['spo_name', 'spo_number']
        }),
        ('Информация о высшем образовании', {
            'fields': ['he_name', 'he_number']
        }),
        ('Социальная характеристика', {
            'fields': ['family_status', 'diagnose', 'special_status']
        }),
    )
    list_display = ('first_name', 'middle_name', 'last_name', 'date_birth', 'certificate_num')
    search_fields = ('first_name', 'last_name', 'certificate_num')
    list_display_links = ['first_name', 'middle_name', 'last_name', 'certificate_num']


@admin.register(TeacherData)
class TeacherDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'date_birth')


"""class BigForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BigForm, self).__init__(*args, **kwargs)
        wtf = TeacherData.objects.all()
        w = self.fields['teacher'].widget
        choices = []
        print(choices)
        for choice in wtf:
            choices.append((choice.id, choice.first_name))
        w.choices = choices"""


class BigForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BigForm, self).__init__(*args, **kwargs)

    def teacher_form(self):
        wtf = TeacherData.objects.all()
        w = self.fields['teacher'].widget
        choices = []
        print(choices)
        for choice in wtf:
            choices.append((choice.id, choice.first_name))
        w.choices = choices

    def child_form(self):
        wtf = ChildData.objects.all()
        w = self.fields['children'].widget
        choices = []
        print(choices)
        for choice in wtf:
            choices.append((choice.id, choice.first_name))
        w.choices = choices


@admin.register(Groups)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 100
    filter_horizontal = ('teacher', 'children')
    list_display = ['group_section', 'group_name']


admin.site.register(Section)
