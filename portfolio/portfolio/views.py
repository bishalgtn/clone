from django.shortcuts import render, redirect



def homepage(request):
    return render(request, 'index.html')


def aboutpage(request):
    return render(request,'about.html')