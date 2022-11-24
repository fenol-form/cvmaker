from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy

from .models import *

from .forms import *

from .utils import *


class Home(Mixin, TemplateView):
    template_name = "mainpage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(request=self.request, **kwargs)
        return context


'''
def mainpage(request):
    if request.user.is_authenticated:
        print("AAAAAAAAAAAAA")

    context = {
            "menu" : enter_menu
    }
    return render(request, "mainpage.html", context=context)
'''

def cvs(request):
    list_of_cvs = CV.objects.all()
    context = {
            "list_of_cvs" : list_of_cvs,
            "menu" : exit_menu
    }
    return render(request, "cvs.html", context=context)


def add_cv(request):
    context = {"menu" : exit_menu}

    if request.method == "POST":
        form = AddCVForm(request.POST)
        if form.is_valid():
            form.save()
            print("AAAA")
            form = AddCVForm()
        else:
            form.add_error(None, "Incorrect fillings")
    else:
        form = AddCVForm()
    
    context["form"] = form
    return render(request, "add_cv.html", context=context)


class Sign_in(LoginView):
    form_class = AuthenticationForm
    template_name = "sign_in.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = enter_menu
        return context

    def get_success_url(self):
        return reverse_lazy("home")


class Sign_up(CreateView):
    form_class = NewUserForm
    template_name = "sign_up.html"
    success_url = reverse_lazy("sign_in")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = enter_menu
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")

def sign_out(request):
    logout(request)
    return redirect("home")