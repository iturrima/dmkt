from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'home'
    })

def about(request):
    return render(request, 'mainapp/noi.html', {
        'title':'noi'
    })