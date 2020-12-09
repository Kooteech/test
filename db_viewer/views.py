from django.shortcuts import render
from django_tables2 import RequestConfig
from dbs_app.models import ChildData
from db_viewer.forms import AgeForm
from django.http import HttpResponseRedirect
from datetime import date


def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age


def get_childdata(request):
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            age_from = form.cleaned_data.get("age_from")
            age_to = form.cleaned_data.get("age_to")
            if (age_from == 0) & (age_to == 0):
                table = ChildData.objects.all()
                context = {'table': table}
                for data in table:
                    print(data)
                return render(request, 'db_viewer/table.html', context)
    else:
        form = AgeForm()
    return render(request, 'db_viewer/search.html', {'form': form})
