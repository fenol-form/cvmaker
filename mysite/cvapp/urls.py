from django.urls import path, include

from .views import *

urlpatterns = [ 
    path("", mainpage, name="home"), 
    path("cvs/", cvs, name="cvs"),
    path("sign_in/", sign_in, name="sign_in"),
    path("add_cv/", add_cv, name="add_cv"),
    path("sign_up/", Sign_up.as_view(), name="sign_up")
]


