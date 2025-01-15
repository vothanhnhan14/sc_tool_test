from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.request import MultiPartParser

class MyClass:
    def do_something_else(self, request):
        print("OK")
