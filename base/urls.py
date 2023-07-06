from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('book',views.book,name='book'),
    path('dep',views.dep,name='dep'),
    path('doc',views.doctor,name='doc'),
]