from django import forms


class AgeForm(forms.Form):
    age_from = forms.IntegerField(label='От', min_value=1)
    age_to = forms.IntegerField(label='До', max_value=99)

