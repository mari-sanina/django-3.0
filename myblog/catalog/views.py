from django.shortcuts import render
from .models import Post, PostComment


MENU = {"о блоге": "/about", "conspirology.": "/", "каталог": "/catalog"}

def catalog_page(request):
    posts = Post.objects.all()
    data = {"menu": MENU, "posts": posts}
    return render(request,"./catalog.html", context=data)

def comment_page(request):
    posts = Post.objects.values("id", "name")
    title = "Добавить комментарий"
    data = {"title": title, "menu": MENU, "posts": posts}
    return render(request,"./comment.html", context=data)

def comments(request):
    posts = PostComment.objects.all()
    new = Post.objects.values('id','title')
    title = "Комментарии"
    data = {"title": title, "menu": MENU, "posts": posts, 'new':new}
    return render(request, "./comments.html", context=data)


def tnx_page(request):
    user_name = request.POST["user_name"]
    email = request.POST["email"]
    comment = request.POST["comment"]
    post = Post.objects.get(pk=request.POST["post"])
    PostComment.objects.create(user_name=user_name, email=email, comment=comment, post=post)
    title = "Вы замечательный человек!"
    data = {"title": title, "menu": MENU, "user_name": user_name}
    return render(request,"./tnx.html", context=data)