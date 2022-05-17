from django.shortcuts import render

from .forms import FindForm
from .models import Application


def home_page(request):
    form = FindForm()
    city = request.GET.get('city')
    symptom = request.GET.get('symptom')
    qs = []
    if city or symptom:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if symptom:
            _filter['symptom__slug'] = symptom
        qs = Application.objects.filter(**_filter)

    return render(request, 'scraping/home_page.html',
                  {'object_list': qs, 'form': form})
