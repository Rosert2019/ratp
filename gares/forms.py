from django import forms
from . models import Station

class station_form(forms.Form):
    stations_choises = [
    ]

    lines_choices = [('All', 'All'),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
    (9,9),(10,10),(11,11),(12,12),(13,13),(14,14),('7b','7b'),('M3bis','M3bis')
    ]

    Lignes = forms.ChoiceField(choices = lines_choices)