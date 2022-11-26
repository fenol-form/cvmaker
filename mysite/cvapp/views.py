from django.contrib.auth.mixins import LoginRequiredMixin
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
        context = super(Home, self).get_context_data()
        context.update(self.get_context_mixin(request=self.request, **kwargs))
        return context


class ListOfCV(LoginRequiredMixin, Mixin, ListView):
    model = CV
    template_name = "cvs.html"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_context_mixin(request=self.request, **kwargs))
        return context


class Add_CV(LoginRequiredMixin, Mixin, CreateView):
    form_class = AddCVForm
    template_name = "add_cv.html"
    success_url = reverse_lazy("add_cv")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_context_mixin(request=self.request, **kwargs))
        return context


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