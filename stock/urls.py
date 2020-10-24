from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
    path('',views.login, name='login'),
    path('about',views.about, name='about'),
    path('skill',views.skill, name='skill'),
    path('education',views.education, name='education'),
    path('contact',views.contact, name='contact'),
]