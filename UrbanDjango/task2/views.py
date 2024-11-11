from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
TEMPLATES_FLDR = 'secondtask/'

def func_views(request):
    return render(request, TEMPLATES_FLDR + 'func_template.html')

class ClassViews(TemplateView):
    template_name = TEMPLATES_FLDR + 'class_template.html'