from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog_page),
    path('comment/', comment_page),
    path('tnx/', tnx_page, name='tnx_page'),

]