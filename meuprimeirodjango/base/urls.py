from django.urls import path

from meuprimeirodjango.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
