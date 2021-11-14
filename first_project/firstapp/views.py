from django.shortcuts import render,HttpResponse

from firstapp.game_tic import game_tic_func

from firstapp.compiler import compiler_func

# Create your views here.
def defualt(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')

def game_func(request):
    return game_tic_func()
    #return HttpResponse("hello world, i am game page.")
def compiler_f(request):
    return compiler_func()