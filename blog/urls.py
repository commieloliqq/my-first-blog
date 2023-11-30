from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('mytest', views.my_test, name='my_test'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]