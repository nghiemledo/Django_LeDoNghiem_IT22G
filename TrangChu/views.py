from django.shortcuts import render
from .models import BaiViet
from django.views import generic 
from django.http import HttpResponseRedirect
from .forms import Registration

def index(request):
    context = {'Posts' : BaiViet.objects.all().order_by('-created_at')}
    return render(request, 'home.html', context)

def post(request, id):
    post = BaiViet.objects.get(id=id)
    return render(request, 'chitietbaiviet.html', {'post':post})

def register(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form':form})