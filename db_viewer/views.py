from django.shortcuts import render
from django_tables2 import RequestConfig
from dbs_app.models import ChildData
from db_viewer.forms import AgeForm
from django.http import HttpResponseRedirect
import datetime
import time
from itertools import chain


def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((datetime.date.today() - birthDate).days / days_in_year)
    return age


def get_childdata(request):
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            age_from = form.cleaned_data.get("age_from")
            age_to = form.cleaned_data.get("age_to")
            my_obj_list = list()
            table = ChildData.objects.all()
            if (age_from == 0) & (age_to == 0):
                context = {'table': table}
            else:
                for obj in table:
                    if (calculateAge(obj.date_birth) >= age_from) and (calculateAge(obj.date_birth) <= age_to):
                        my_obj_list.append(obj)
                none_qs = ChildData.objects.none()
                qs = list(chain(none_qs, my_obj_list))
                context = {'table': qs}
            return render(request, 'db_viewer/table.html', context)
    else:
        form = AgeForm()
    return render(request, 'db_viewer/search.html', {'form': form})
