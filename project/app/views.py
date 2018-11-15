import os

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from accounts.models import SocialUser, Relationship
from app.models import UserInfo
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm
from allauth.socialaccount.models import SocialAccount
from project import settings
from datetime import datetime

APP_NAME = 'app'
LP_NAME = 'lp'

class DashboardPage(TemplateView):
  template_name = '%s/dashboard.html' % APP_NAME

  def get(self, request, *args, **kwargs):
    # ログインしていないとき
    if request.user.is_anonymous:
      self.template_name = '%s/top.html' % LP_NAME
      return render(request, self.template_name, {})

    # ログインしているとき
    elif request.user.is_authenticated:
      user = SocialUser.objects.get(id=request.user.id)
      socialAccount = SocialAccount.objects.get(user_id=user).extra_data
      userId = socialAccount['id_str']
      with open(os.path.join(settings.BASE_DIR,'log',userId + '.txt'),'r') as f:
        twitterStatus = [i.replace('\n','') for i in f.readlines()][:100]
      date = []
      follows = []
      followers = []
      for day in twitterStatus:
        date.append(datetime.strptime(day.split(',')[0], '%Y/%m/%d %H:%M:%S').strftime('%m/%d'))
        follows.append(int(day.split(',')[1]))
        followers.append(int(day.split(',')[2]))
      twitterStatus ={'date': date, 'follows': follows, 'followers': followers, 'followers_min': min(followers), 'followers_max': max(followers)}

      return render(request, self.template_name, {'user': user, 'social_data': socialAccount, 'twitterStatus': twitterStatus})

class TablesPage(LoginRequiredMixin, ListView):
  template_name = '%s/tables.html' % APP_NAME
  model = UserInfo
  paginate_by = 20

  # 指定したクエリ発行
  def get_queryset(self):
    # UserInfo objects
    liked_users = self.request.user.get_liked_users()
    users = UserInfo.objects.difference(liked_users)
    if self.request.GET.get('q'):
      q = self.request.GET.get('q')
      q_words = q.strip().split()
      users = users.filter()

      for q_word in q_words:
        users=users.filter(description__icontains=q_word)
      return users

    else:
      return users

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['q'] = self.request.GET.get('q')
    context['count'] = self.get_queryset().count()
    context['page'] = self.request.GET.get('page')

    return context

  def post(self, request, *args, **kwargs):
    ids = request.POST.getlist("checks[]")
    for id in ids:
      relation = Relationship(user=request.user, liked_user=UserInfo.objects.get(pk=id))
      relation.save()

    return redirect("app:tables")


class FavoritePage(ListView):
  template_name = '%s/favorite.html' % APP_NAME
  model = UserInfo
  paginate_by = 20

  def get_queryset(self):
    liked_users = self.request.user.get_liked_users()
    return liked_users

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['q'] = self.request.GET.get('q')
    context['count'] = self.get_queryset().count()
    context['page'] = self.request.GET.get('page')

    return context


class ContactView(FormView):
    template_name = "app/contactForm.html"
    form_class = ContactForm
    success_url = "/contact"

    def form_valid(self, form):
        result = super().form_valid(form)
        # formで定義したメソッド呼び出し
        form.send_email()
        messages.success(self.request, '送信完了')
        return result
