from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('home/', views.home),
    path('', views.home),
    path('add', views.add),
]