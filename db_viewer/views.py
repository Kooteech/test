from django.shortcuts import render
from dbs_app.models import ChildData, Group
from db_viewer.forms import AgeForm
import datetime
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
                for obj in table:
                    if obj.sex == "boy":
                        obj.sex = "М"
                        my_obj_list.append(obj)
                    else:
                        my_obj_list.append(obj)
                        obj.sex = "Ж"
                none_qs = ChildData.objects.none()
                qs = list(chain(none_qs, my_obj_list))
                context = {'table': qs}
            else:
                for obj in table:
                    if (calculateAge(obj.date_birth) >= age_from) and (calculateAge(obj.date_birth) <= age_to):
                        if obj.sex == "boy":
                            obj.sex = "М"
                            my_obj_list.append(obj)
                        else:
                            my_obj_list.append(obj)
                            obj.sex = "Ж"
                none_qs = ChildData.objects.none()
                qs = list(chain(none_qs, my_obj_list))
                context = {'table': qs}
            return render(request, 'db_viewer/table.html', context)
    else:
        form = AgeForm(initial={"age_from": 0, "age_to": 0})
    return render(request, 'db_viewer/search.html', {'form': form})


def get_more_info(request):
    my_obj_list = list()
    if request.method == "GET":
        child_id = request.GET.get('id')
        if not child_id:
            form = AgeForm(initial={"age_from": 0, "age_to": 0})
            return render(request, 'db_viewer/search.html', {'form': form})
        else:
            data = ChildData.objects.get(id=child_id)
            groups = Group.objects.filter(children=child_id)
            if data.sex == "boy":
                data.sex = "М"
            else:
                data.sex = "Ж"
            return render(request, 'db_viewer/moreinfo.html', {'data': data, 'groups': groups})
