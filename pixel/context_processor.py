from .models import Cities
from signup.models import Franchise
import json


def city_list(request):
    cities = Cities.objects.all().order_by('name')
    city_flag = request.session.get('flag_in_session', False)
    franchises = Franchise.objects.all()
    is_franchise = False
    franchise = ''
    if city_flag:
        try:
            city_name = Cities.objects.get(flag=city_flag)
            city_coords = Cities.objects.get(flag=city_flag).coords
            city_zoom = Cities.objects.get(flag=city_flag).zoom
        except:
            try:
                city_name = Franchise.objects.get(flag=city_flag)
                city_coords = Franchise.objects.get(flag=city_flag).coords
                city_zoom = Franchise.objects.get(flag=city_flag).zoom
                is_franchise = True
                franchise = Franchise.objects.get(flag=city_flag)
            except:
                city_name = Cities.objects.get(flag='all')
                city_coords = Cities.objects.get(flag='all').coords
                city_zoom = Cities.objects.get(flag='all').zoom
    else:
        city_name = Cities.objects.get(flag='all')
        city_coords = Cities.objects.get(flag='all').coords
        city_zoom = Cities.objects.get(flag='all').zoom

    # формируем нужный вид для координат
    s = ''
    for symb in city_coords:
        if symb != '[' and symb != ']':
            s += symb
    city_coords_list = [float(i) for i in list(s.split(','))]
    city_coords_json = json.dumps(city_coords_list)

    all_cities_chose = False
    if str(city_name) == 'Все города':
        all_cities_chose = True

    context = {
        'cities': cities,
        'city_name': city_name,
        'city_coords': city_coords_json,
        'city_zoom': city_zoom,
        'all_cities_chose': all_cities_chose,
        'franchises': franchises,
        'is_franchise': is_franchise,
        'franchise': franchise,
    }
    return context
