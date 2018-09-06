from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home, name="job_home"),
    path('edit/<int:id>', update, name="job_update"),
    path('add/', add, name="job_add"),
    path('del/<int:id>', delete, name="job_delete"),
    path('login/', login_my_user, name="user_login"),
	path('signup/', add_my_user, name="user_register"),
	path('updt/', update_my_user, name="user_update"),
	path('user_details/', display_profile, name="user_details"),
	path('logout/', logout_my_user, name="user_logout"),
    # path('', ),
]

