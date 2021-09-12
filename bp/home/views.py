from django.shortcuts import render, redirect
from django.views import generic


def index(request):
    if request.user.is_authenticated:
        return render(request, template_name='home/index.html')
    else:
        return render(request, template_name='welcome/index.html')


def handler403(request, exception):
    return render(request, 'errors/403.html')


def handler404(request, exception):
    return render(request, 'errors/404.html')


def handler500(request):
    return render(request, 'errors/500.html')


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'
