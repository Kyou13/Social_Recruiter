from django.shortcuts import render,redirect
from django.views import View
from allauth.account import views
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Top(View):
  def get(self, request):
    return render(request, 'main/top.html')


class DashBoard(View, LoginRequiredMixin):
  def get(self, request):

    return render(request, 'main/dashboard.html')


class UserList(View, LoginRequiredMixin):
  def get(self, request, page):
    queryset = UserInfo.objects.all()
    # TODO: per page can be change
    paginator = Paginator(queryset, 20)
    try:
      contents = paginator.page(page)
    except PageNotAnInteger:
      contents = paginator.page(1)
    except EmptyPage:
      contents = paginator.page(paginator.num_pages)
    return render(request, 'main/user_list.html', {'contents': contents})


class SigninView(views.LoginView):
  template_name = 'main/top.html'

  def dispatch(self, request, *args, **kwargs):
    response = super(SigninView, self).dispatch(request, *args, **kwargs)
    return response

  def form_valid(self, form):
    return super(SigninView, self).form_valid(form)


class SignoutView(views.LogoutView):
  def get(self, *args, **kwargs):
    return self.post(*args, **kwargs)

  def post(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      self.logout()
    return redirect('/')
