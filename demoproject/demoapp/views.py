from django.shortcuts import render,HttpResponse

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def add(request):
    no1 = int(request.GET["num1"])
    no2 = int(request.GET["num2"])
    res = no1 + no2
    return render(request,'home.html',{'name': res,'num1': no1, 'num2': no2})