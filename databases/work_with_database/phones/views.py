from django.shortcuts import render
from phones.models import Phone


def home_view(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'name':
        sorted_phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        sorted_phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        sorted_phones = Phone.objects.all().order_by('-price')
    else:
        sorted_phones = Phone.objects.all()

    context = {'sort': sort, 'phones': sorted_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.all().filter(slug=slug)
    for obj in phone:
        print(obj.lte_exists)
    context = {'phone': phone}
    return render(request, template, context)
