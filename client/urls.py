from django.urls import path

from .views import *


urlpatterns = [
    path('', vacancies_list),
    prth('vacancy/<id>/', vacancy_detail, name='vacancy_detail_url'),
]