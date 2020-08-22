from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'QLVB2_APP/taisan.html')