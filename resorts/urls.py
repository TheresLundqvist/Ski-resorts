from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.ResortList.as_view(), name='home'),
    path('<slug:slug>/', views.ResortDetail.as_view(), name='resort_detail'),
]

urlpatterns += staticfiles_urlpatterns()
