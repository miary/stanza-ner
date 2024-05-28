from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('page1/', views.convert_page_one, name='page1')
]
