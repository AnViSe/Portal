from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return render(request, template_name='home/index.html')
    else:
        return render(request, template_name='welcome/index.html')
