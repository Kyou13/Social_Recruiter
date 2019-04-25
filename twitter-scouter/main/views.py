from django.shortcuts import render,redirect
from django.views import View
from allauth.account import views
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserInfo, Like
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.urls import reverse_lazy


class Top(View):
  def get(self, request):
    return render(request, 'main/top.html')


class DashBoard(View, LoginRequiredMixin):
  def get(self, request):

    return render(request, 'main/dashboard.html')


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
  def get(self, request, **kwargs):
    queryset = UserInfo.objects.all().order_by('-followers_count')
    liked_user = Like.objects.filter(user=request.user).values_list('twitter_user', flat=True)
    # TODO: per page can be change
    paginator = Paginator(queryset, 20)
    try:
      contents = paginator.page(kwargs['page'])
    except PageNotAnInteger:
      contents = paginator.page(1)
    except EmptyPage:
      contents = paginator.page(paginator.num_pages)
    return render(request, 'main/user_list.html', {'contents': contents, 'liked_user': liked_user})


class Favorite(View, LoginRequiredMixin):
  def post(self, request, *args, **kwargs):
    twitter_user = UserInfo.objects.get(id=kwargs['twitter_id'])
    is_like = Like.objects.filter(user=request.user).filter(twitter_user=twitter_user).count()
    if is_like > 0:
      liking = Like.objects.get(twitter_user__id=kwargs['twitter_id'], user=request.user)
      liking.delete()
      twitter_user.like_num -= 1
      twitter_user.save()
      messages.warning(request, 'いいねを取り消しました')
      return redirect(request.META['HTTP_REFERER'])
    twitter_user.like_num += 1
    twitter_user.save()
    like = Like()
    like.user = request.user
    like.twitter_user = twitter_user
    like.save()
    messages.success(request, 'いいね!しました')

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
    return render(request, 'main/like_list.html', {'contents': contents})
