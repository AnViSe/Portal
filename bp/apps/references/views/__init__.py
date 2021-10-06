from django.shortcuts import render

# from .country import *
# from .region import *
from .employee import *
from .person import *
from .subdivision import *


def index(request):
    return render(request, template_name='references/index.html')
