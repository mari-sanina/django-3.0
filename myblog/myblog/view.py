from django.http import HttpResponse
from django.shortcuts import render

MENU = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}

def main_page(request):
    data = {"menu": MENU}
    return render(request,"./index.html", context=data)

def about_page(request):
    data = {"menu": MENU}
    return render(request,"./about.html", context=data)

def post_page(request):
    data = {"menu": MENU}
    return render(request,"./post.html", context=data)
