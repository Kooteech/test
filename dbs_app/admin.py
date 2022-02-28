from django.contrib import admin
from django import forms
from inline_actions.admin import InlineActionsModelAdminMixin
from django.shortcuts import redirect
from .models import ChildData, TeacherData, Section, Group


# Register your models here.
@admin.register(ChildData)
class ChildDataAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):
    inline_actions = ['view']

    def view(self, request, obj, parent_obj=None):
        url = '/viewer/childdata/moreinfo/?id={}'.format(obj.pk)
        return redirect(url)

    view.short_description = "Карточка"

    fieldsets = (
        ('Данные ученика', {
            'fields': ['personal_number', 'first_name', 'middle_name', 'last_name', 'date_birth', 'parent', 'sex', 'phone_number',
                       'adress', 'certificate_num', 'teach_status']
        }),
        ('Информация об УДО', {
            'fields': ['udo_status', 'udo_name', 'udo_group']
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
        ('Документы', {
            'fields': ['doc_zayavl_checkbox', 'doc_dogovor_checkbox', 'doc_opd_checkbox', 'doc_soprovod_checkbox',
                       'doc_svid_checkbox']
        }),
    )
    list_display = (
    'first_name', 'middle_name', 'last_name', 'date_birth', 'adress', 'certificate_num', 'doc_zayavl_checkbox',
    'doc_dogovor_checkbox', 'doc_opd_checkbox', 'doc_soprovod_checkbox', 'doc_svid_checkbox')
    search_fields = ('first_name', 'middle_name', 'adress', 'certificate_num')
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


@admin.register(Group)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 100
    filter_horizontal = ('teacher', 'children')
    list_display = ['group_section', 'group_name']


admin.site.register(Section)
