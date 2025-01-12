from django.shortcuts import render
from .models import Post, PostComment


MENU = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}

def catalog_page(request):
    posts = Post.objects.all()
    checked_comments = PostComment.objects.filter(is_checked=True)
    data = {"menu": MENU, "posts": posts, "comments": checked_comments}
    return render(request,"./catalog.html", context=data)

def comment_page(request):
    posts = Post.objects.values("id", "name")
    title = "Добавить комментарий"
    data = {"title": title, "menu": MENU, "posts": posts}
    return render(request,"./comment.html", context=data)

def comments(request):
    title = "Проверенные Комментарии"
    checked_comments = PostComment.objects.filter(is_checked=True)
    data = {"title": title, "menu": MENU, 'comments': checked_comments}
    return render(request, "./comments.html", data)

def tnx_page(request):
    user_name = request.POST["user_name"]
    email = request.POST["email"]
    comment = request.POST["comment"]
    post = Post.objects.get(pk=request.POST["post"])
    PostComment.objects.create(user_name=user_name, email=email, comment=comment, post=post)
    title = "Вы замечательный человек!"
    data = {"title": title, "menu": MENU, "user_name": user_name}
    return render(request,"./tnx.html", context=data)