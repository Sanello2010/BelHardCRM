from django.shortcuts import render

# Create your views here.


def vacancy(request):
    salary = '400'
    return render(request, 'client/index.html', context={'salary' : salary})