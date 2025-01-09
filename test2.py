from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def file_upload_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        # Process the uploaded file
        # ...
        return HttpResponse('File uploaded successfully')
    return HttpResponse('Please upload a file')
