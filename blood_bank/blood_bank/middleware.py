import re

from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

EXCEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXCEMPT_URLS'):
    EXCEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXCEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')

        url_is_excempt = any(url.match(path) for url in EXCEMPT_URLS)

        if path == reverse('sign-out').lstrip('/'):
            logout(request)
            
        if request.user.is_authenticated and url_is_excempt:
            return None

        elif request.user.is_authenticated or url_is_excempt:
            return None

        else:
            return None