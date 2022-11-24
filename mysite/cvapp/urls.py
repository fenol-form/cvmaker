from django.urls import path, include

from .views import *

urlpatterns = [ 
    path("", Home.as_view(), name="home"),
    path("cvs/", cvs, name="cvs"),
    path("sign_in/", Sign_in.as_view(), name="sign_in"),
    path("add_cv/", add_cv, name="add_cv"),
    path("sign_up/", Sign_up.as_view(), name="sign_up"),
    path("sign_out/", sign_out, name="sign_out")
]


