import billboard
from django.shortcuts import render


def homepage(request):
    hot_100 = billboard.ChartData('hot-100')
    context = {
        'hot_100': hot_100
    }
    return render(request, 'homepage/homepage.html', context)
