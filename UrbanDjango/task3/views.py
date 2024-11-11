from django.shortcuts import render

# Create your views here.
TMP_FLDR = 'third_task/'

def main_page(request):
    return render(request, TMP_FLDR+'main_page.html')

def second_page(request):
    return render(request, TMP_FLDR+'second_page.html')

def third_page(request):
    return render(request, TMP_FLDR+'third_page.html')