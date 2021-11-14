from django.shortcuts import render

def home(request):
    return render(request, 'mainpage.html')

def back(request):
    return render(request, 'mainpage.html')

# def mainpage(request):
#     return render(request, 'mainpage.html' )


def addpage(request):
    return render(request, 'add.html')

def subpage(request):
    return render(request, 'subtract.html')

def mulpage(request):
    return render(request, 'multi.html')

def divipage(request):
    return render(request, 'divide.html')


def add(request):
    val1 = float(request.POST["num1"])
    val2 = float(request.POST["num2"])
    res = val1 + val2
    return render(request, 'result.html', {'result':res})


def subtract(request):
    val1 = float(request.POST["num1"])
    val2 = float(request.POST["num2"])
    res = val1 - val2
    return render(request, 'result.html', {'result1':res})

def multi(request):
    val1 = float(request.POST["num1"])
    val2 = float(request.POST["num2"])
    res = val1 * val2
    return render(request, 'result.html', {'result2':res})

def divide(request):
    val1 = float(request.POST["num1"])
    val2 = float(request.POST["num2"])
    res = val1 / val2
    return render(request, 'result.html', {'result3':res})

def About(request):
    return render(request, 'About.html')

def Creator(request):
    return render(request, 'Creator.html')

def Contact(request):
    return render(request, 'contact.html')


