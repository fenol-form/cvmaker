from .models import *

enter_menu = [{"title" : "Sign in", "url" : "sign_in"},
        {"title" : "Sign up", "url" : "sign_up"},
        {"title" : "Main page", "url" : "home"}]

exit_menu = [{"title" : "Sign out", "url" : "sign_out"},
             {"title" : "Main page", "url" : "home"}]


last_changed_cv = dict()

class Mixin:
    def get_context_mixin(self, request=None, **kwargs):
        context = kwargs
        if request and request.user.is_authenticated:
            context["menu"] = exit_menu
        else:
            context["menu"] = enter_menu
        return context