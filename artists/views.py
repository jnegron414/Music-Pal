from django.shortcuts import render


def detail(request):
    context = {}
    return render(request, 'artists/detail.html', context)


def list(request):
    context = {}
    return render(request, 'artists/list.html', context)