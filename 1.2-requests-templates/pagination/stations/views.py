from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def read_csv():
    info = []

    with open('./data-398-2018-08-30.csv') as file:
        r = csv.reader(file)
        for el in r:
            if el[1] != 'Name' or el[4] != 'Street' or el[6] != 'District':
                info.append({
                    'Name': el[1],
                    'Street': el[4],
                    'District': el[6]
                })

    return info



def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    info = read_csv()

    p_name = Paginator(info, 10)
    current_page = request.GET.get('page', 1)
    page = p_name.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
