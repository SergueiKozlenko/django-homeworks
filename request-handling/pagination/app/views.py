from django.shortcuts import render, redirect
from django.urls import reverse
from app.settings import BUS_STATION_CSV
import csv
from django.core.paginator import Paginator
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    csv.register_dialect('custom_scv', delimiter=',', quoting=csv.QUOTE_MINIMAL)
    with open(BUS_STATION_CSV, newline='', encoding="cp1251") as csv_file:
        reader = csv.DictReader(csv_file)
        content = []
        for i, row in enumerate(reader):
            content.append({'Name': row['Name'],
                            'Street': row['Street'],
                            'District': row['District']})

    paginator = Paginator(content, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    page_objects = page.object_list

    prev_page_url, next_page_url = None, None
    if page.has_previous():
        prev_page_number = page.previous_page_number()
        prev_page_url = reverse('bus_stations') + '?' + urlencode({'page': prev_page_number})
    if page.has_next():
        next_page_number = page.next_page_number()
        next_page_url = reverse('bus_stations') + '?' + urlencode({'page': next_page_number})

    return render(request, 'index.html', context={
        'bus_stations': page_objects,
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
