from django.http import HttpResponse
from django.shortcuts import render

MENU = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}

def main_page(request):
    #menu = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}
    data = {"menu": MENU}
    return render(request,"./index.html", context=data)

def about_page(request):
    #menu = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}
    data = {"menu": MENU}
    return render(request,"./about.html", context=data)

def catalog_page(request):
    #menu = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}
    data = {"menu": MENU}
    return render(request,"./catalog.html", context=data)

def post_page(request):
    resp = f'Post id: {id}, category: {category}'
    menu = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}
    data = {"menu": menu}
    return render(request,"./post.html", context=data)
