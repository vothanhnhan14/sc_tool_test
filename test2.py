from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.request import MultiPartParser

class MyClass:
    def handle_multipart_form(self, request):
        print("OK")
