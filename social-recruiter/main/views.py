from django.shortcuts import render,redirect
from django.views import View
from allauth.account import views

class Top(View):
  def get(self, request):
    return render(request, 'main/top.html')

class Home(View):
  def get(self, request):
    return render(request, 'main/home.html')


class SignoutView(views.LogoutView):
  def get(self, *args, **kwargs):
    return self.post(*args, **kwargs)

  def post(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      self.logout()
    return redirect('/')
