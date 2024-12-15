from django.shortcuts import render
from .models import Post


MENU = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}

def catalog_page(request):
    posts = Post.objects.all()
    data = {"menu": MENU, "posts": posts}
    return render(request,"./catalog.html", context=data)

def comment_page(request):
    posts = Post.objects.all()
    title = "Добавить комментарий"
    data = {"title": title, "menu": MENU, "posts": posts}
    return render(request,"./comment.html", context=data)

def tnx_page(request):
    user_name = request.GET("user_name")
    title = "Вы замечательный человек!"
    data = {"title": title, "menu": MENU, "user_name": user_name}
    return render(request,"./tnx.html", context=data)