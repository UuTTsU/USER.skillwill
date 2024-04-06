from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users,name = 'user-list'),
    path('create/', views.create_users, name='create-user'),
    path('update/', views.update_users, name='update-user'),
    path('delete/', views.delete_users, name='delete-user')
]