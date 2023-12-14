from d07.settings import RANDOM_NAMES
from random import choice
from django.http import HttpRequest
import time

class UserNameMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        expires_time = request.session.setdefault('user_name_expires', time.time())

        # print(f"expires_time: {time.time() - expires_time}")
        if time.time() - expires_time > 42:
            request.session.flush()
        
        request.session.setdefault('user_name', choice(RANDOM_NAMES))

        # Add the user name to the request context
        request.user_name = request.session['user_name']

        response = self.get_response(request)

        return response