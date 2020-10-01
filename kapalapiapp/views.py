from django.shortcuts import render

def dashboard(request):
    context = {}
    return render(request, 'kapalapitemplate/dashboard.html', context)


def balai(request):
    context = {}
    return render(request, 'kapalapitemplate/balai/balai.html', context)


def paket(request):
    context = {}
    return render(request, 'kapalapitemplate/paket/paket.html', context)
