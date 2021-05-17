from .import views
from django.urls import path

urlpatterns = [
    path('', views.CheckList, name='checklist'),
    path('checkedit/<int:id>', views.CheckEdit, name='checkedit'),
    path('checkdetalhe/<int:id>', views.CheckDetalhe, name='checkdetalhe'),
    path('eventolist/', views.EventoList, name='eventolist')
]