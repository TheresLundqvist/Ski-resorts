from . import views
from django.urls import path


urlpatterns = [
    path('', views.ResortList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.ResortDetail.as_view(), name='resort_detail'),
]
