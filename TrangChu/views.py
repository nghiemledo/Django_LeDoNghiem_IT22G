from django.shortcuts import render
from .models import BaiViet
from django.views import generic 

def index(request):
    context = {'Posts' : BaiViet.objects.all().order_by('-created_at')}
    return render(request, 'home.html', context)

def post(request, id):
    post = BaiViet.objects.get(id=id)
    return render(request, 'chitietbaiviet.html', {'post':post})