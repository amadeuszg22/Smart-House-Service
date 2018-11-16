from django.urls import path
from . import views

urlpatterns = [
    path('', views.config_list, name='config_list'),
	path('new', views.config_new, name='config_new'),
    path('new_dev', views.config_new_dev, name='config_new_dev'),
    path('config/<int:pk>/edit/', views.config_edit, name='config_edit'),
    path('config/<int:pk>/edit_dev/', views.config_edit_dev, name='config_edit_dev'),
    path('config/<int:pk>/del/', views.config_del, name='config_del'),
    path('config/<int:pk>/del_dev/', views.config_del_dev, name='config_del_dev'),
]