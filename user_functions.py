
def get_gares(data, filtre):
    if filtre == 'All':
        return data.objects.all()
    else:
        data.objects.filter(line = filtre)
