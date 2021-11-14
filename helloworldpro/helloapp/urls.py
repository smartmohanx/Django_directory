
from django.contrib import admin
from django.urls import path
from helloapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('back', views.back, name='back'),
    # path('mainpage', views.mainpage, name='mainpage'),
    path('subpage', views.subpage, name='subpage'),
    path('addpage', views.addpage, name='addpage'),
    path('mulpage', views.mulpage, name='mulpage'),
    path('divipage', views.divipage, name='divipage'),
    path('subtract', views.subtract, name='subtract'),
    path('multi', views.multi, name='multi'),
    path('divide', views.divide, name='divide'),
    path('About', views.About, name='About'),
    path('Creator', views.Creator, name='Creator'),
    path('Contact', views.Contact, name='Contact')

]