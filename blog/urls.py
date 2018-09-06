from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home, name="blog_home"),
    path('<int:id>', detail, name="blog_detail"),
    path('edit/<int:id>', update, name="blog_update"),
    path('add/', add, name="blog_add"),
    path('del/<int:id>', delete, name="blog_delete")
    # path('', ),
]

