from django.shortcuts import render,redirect
from django.views import View
from allauth.account import views
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserInfo, Like
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.urls import reverse_lazy
from allauth.socialaccount.models import SocialAccount
import json
from . import forms

class Top(View):
  def get(self, request):
    return render(request, 'main/top.html')


class DashBoard(View, LoginRequiredMixin):
  def get(self, request):
    context = {}
    socialAccount = SocialAccount.objects.get(user=request.user).extra_data
    context["user_detail"] = socialAccount
    return render(request, 'main/dashboard.html', context)


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


class UserList(View, LoginRequiredMixin):
  paginate_by = 20

  def get(self, request, **kwargs):
    form = forms.Paginate(request.GET or None)
    if 'paginate_by' in request.GET:
      request.session['paginate_by'] = request.GET['paginate_by']

    context = {}
    queryset = UserInfo.objects.all()
    queryset = queryset.order_by('-followers_count')
    liked_user = Like.objects.filter(user=request.user).values_list('twitter_user', flat=True)
    socialAccount = SocialAccount.objects.get(user=request.user).extra_data
    context["user_detail"] = socialAccount

    if 'paginate_by' in request.session:
      self.paginate_by = request.session['paginate_by']
    # TODO: per page can be change
    paginator = Paginator(queryset, self.paginate_by)
    try:
      contents = paginator.page(kwargs['page'])
    except PageNotAnInteger:
      contents = paginator.page(1)
    except EmptyPage:
      contents = paginator.page(paginator.num_pages)
    context['contents'] = contents
    context['liked_user'] = liked_user
    context['form'] = form
    context['paginate_by'] = self.paginate_by

    return render(request, 'main/user_list.html', context)


class Favorite(View, LoginRequiredMixin):
  def post(self, request, *args, **kwargs):
    twitter_user = UserInfo.objects.get(id=kwargs['twitter_id'])
    is_like = Like.objects.filter(user=request.user).filter(twitter_user=twitter_user).count()
    if is_like > 0:
      liking = Like.objects.get(twitter_user__id=kwargs['twitter_id'], user=request.user)
      liking.delete()
      twitter_user.like_num -= 1
      twitter_user.save()
      return redirect(request.META['HTTP_REFERER'])

    twitter_user.like_num += 1
    twitter_user.save()
    like = Like()
    like.user = request.user
    like.twitter_user = twitter_user
    like.save()

    return redirect(request.META['HTTP_REFERER'])


class LikeList(View, LoginRequiredMixin):
  def get(self, request, *args, **kwargs):
    like_twitter_user = Like.objects.filter(user=request.user)
    paginator = Paginator(like_twitter_user, 20)
    try:
      contents = paginator.page(kwargs['page'])
    except PageNotAnInteger:
      contents = paginator.page(1)
    except EmptyPage:
      contents = paginator.page(paginator.num_pages)
    context={}
    context['contents'] = contents
    socialAccount = SocialAccount.objects.get(user=request.user).extra_data
    context["user_detail"] = socialAccount
    return render(request, 'main/like_list.html', context)
