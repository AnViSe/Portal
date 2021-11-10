# import logging
from django.shortcuts import render

# logger = logging.getLogger('django_')


def index(request):
    # logger.error('Открытие страницы...')
    return render(request, template_name='welcome/index.html', )
