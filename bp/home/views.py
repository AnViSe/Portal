from django.shortcuts import render
from django.views import generic


def index(request):
    if request.user.is_authenticated:
        return render(request, template_name='home/index.html')
    else:
        return render(request, template_name='welcome/index.html')


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'
