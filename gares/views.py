from django.shortcuts import render
from .forms import station_form
from .models import Station
import pandas as pd

# Create your views here.


	 
def ratp_gares(request):

	if request.method == 'POST':
		form = station_form(request.POST)
		if form.is_valid():    
			ligne = form.cleaned_data['Lignes']
			GARES = Station.objects.all().values('name','line')
			GARES = pd.DataFrame.from_records(GARES)
			GARES = GARES['name'].value_counts().rename_axis('Gares').reset_index(name='Correspondance').sort_values(by=['Gares'])
			if ligne != 'All':
				GARES_filterd = pd.DataFrame.from_records(Station.objects.filter(line=ligne).values('name')) 
				GARES =  GARES_filterd.merge(GARES,  left_on='name', right_on='Gares',how='left')
				del GARES['name']


			GARES['Correspondance'] = (GARES['Correspondance'] - 1)
	
			return render(request, 'station_form.html',{'GARES': GARES.reset_index(drop=True).to_html()})
 
	else:
		 form = station_form()
 

	return render(request, 'station_form.html', {'form':form})
