from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.http.request import MultiPartParser

class MyClass:
    #@csrf_exempt  # To avoid CSRF token issues for demonstration
    def handle_my_request(self, request):
        print("OK")
