from django.shortcuts import render

from .models import Vacancy



def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'client/index.html', context={'vacancies': vacancies})


def vacancy_detail(request, id):
    vacancy = Vacancy.objects.get(id__iexact=id)
    return render(request, 'client/vacancy_detail.html', context={'vacancy': vacancy})


