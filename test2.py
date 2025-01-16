from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.request import MultiPartParser

class MyClass:
    @csrf_exempt  # To avoid CSRF token issues for demonstration
    def handle_multipart_form(self, request):
        if request.method == 'POST':
            # Using the MultiPartParser in Django to parse the request
            parser = MultiPartParser(request, request.META)
            try:
                # Parsing the multipart data
                data = parser.parse()
                # Do something with the data (e.g., save files)
                return HttpResponse("Received data")
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}", status=400)
        return HttpResponse("Only POST method is allowed", status=405)
