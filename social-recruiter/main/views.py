from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class Top(View):
  def get(self, request):
    return render(request, 'main/top.html')

class Home(View):
  def get(self, request):
    return render(request, 'main/home.html')
