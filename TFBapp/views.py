from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'TFBapp/index.html')

def gallery(request):
    return render(request, 'TFBapp/gallery.html')