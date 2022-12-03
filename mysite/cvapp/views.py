from typing import Dict, Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from jinja2 import Environment, FileSystemLoader
import pdfkit
import base64

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
    template_name = "cvs_exp.html"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_context_mixin(request=self.request, **kwargs))
        return context


class Add_CV(LoginRequiredMixin, Mixin, CreateView):
    form_class = AddCVForm
    template_name = "add_cv.html"
    success_url = reverse_lazy("add_cv")

    initial = last_changed_cv

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_context_mixin(request=self.request, **kwargs))
        return context

    # Trying to add data in DB that has been excluded from the form
    def post(self, request, *args, **kwargs):
        form = AddCVForm(request.POST, request.FILES)
        if (form.is_valid()):
            username = User.objects.get(id=request.user.id)
            if "button submit" in request.POST:
                instance = form.save(commit=False)

                # username field in CV's model MUST be a USER INSTANCE
                instance.username = username
                instance.save()
                return super().form_valid(form)
            else:
                data = form.cleaned_data
                last_changed_cv.clear()
                last_changed_cv.update(data)
                return redirect("home")


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

def get_image_file_as_base64_data(filepath):
    with open(filepath, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode()

def load(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("cvapp/templates/pdf.html")

    if (cv.image):
        path_to_image = cv.image.url
        if path_to_image[0] == '/':
            path_to_image = path_to_image[1:]

        enc_image = get_image_file_as_base64_data(path_to_image)
    else:
        enc_image = ''

    pdf_template = template.render({"cv" : cv, "enc" : enc_image})
    pdfkit.from_string(pdf_template, 'cvapp/pdf_outputs/out.pdf')
    return FileResponse(open('cvapp/pdf_outputs/out.pdf', 'rb'))
