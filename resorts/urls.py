from . import views
from django.urls import path


urlpatterns = [
    path('', views.ResortList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('edit_comment/<int:comment_id>/<slug:slug>/', views.edit_comment, name='edit_comment'),  # noqa
    path('delete_comment/<int:comment_id>/<slug:slug>/', views.delete_comment, name='delete_comment'),  # noqa
    path('<slug:slug>/', views.ResortDetail.as_view(), name='resort_detail'),
]
