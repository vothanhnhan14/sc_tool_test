from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class MyClass:
    @csrf_exempt  # To avoid CSRF token issues for demonstration
    def handle_request(self, request):
        print("OK")
