from django.contrib import admin
from django.urls import path
from firstapp import views
from firstapp.game_tic import game_tic_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.defualt), 
    path('home', views.home),
    path('game', views.game_func),
    path('compiler', views.compiler_f)
]
