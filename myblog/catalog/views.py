from django.shortcuts import render
from .models import Post


MENU = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}

def catalog_page(request):
    posts = Post.objects.all()
    data = {"menu": MENU, "posts": posts}
    return render(request,"./catalog.html", context=data)
