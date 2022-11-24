from .models import *

enter_menu = [{"title" : "Sign in", "url" : "sign_in"},
        {"title" : "Sign up", "url" : "sign_up"},
        {"title" : "Main page", "url" : "home"}]

exit_menu = [{"title" : "Sign out", "url" : "sign_out"}]


class Mixin:
    def get_context_data(self, request=None, **kwargs):
        context = kwargs
        if request and request.user.is_authenticated:
            context["menu"] = exit_menu
        else:
            context["menu"] = enter_menu
        return context