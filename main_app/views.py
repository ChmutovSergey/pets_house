from os import environ
from django.shortcuts import render

YANDEX_MAP_API_KEY = environ.get('MAP_API_KEY')


def index_page(request):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}

    return render(request, 'main_app/index.html', context=data)


def hotels_page(request):
    data = {'yandex_map_api_key': YANDEX_MAP_API_KEY}

    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    print("RESULT  ", latitude, longitude)

    return render(request, 'main_app/hotels.html', context=data)
