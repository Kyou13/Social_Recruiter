import os

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView
from accounts.models import SocialUser
from app.models import UserInfo
from django.shortcuts import get_object_or_404,render,redirect
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
      twitterStatus ={'date': date, 'follows': follows, 'followers': followers}
      print(date)

      return render(request, self.template_name, {'user': user, 'social_data': socialAccount, 'twitterStatus': twitterStatus})

# class userProfilePage(LoginRequiredMixin, TemplateView):
#     template_name = '%s/user.html' % APP_NAME
# 
#     def get(self, request, *args, **kwargs):
#         user = UserSocialAuth.objects.get(user_id=request.user.id)
#         return render(request, self.template_name, {'user': user})
# 
# 
# 
class TablesPage(LoginRequiredMixin, ListView):
  template_name = '%s/tables.html' % APP_NAME
  model = UserInfo
  paginate_by = 10

  # 指定したクエリ発行
  def get_queryset(self):
    if self.request.GET.get('q'):
      q = self.request.GET.get('q')
      q_words = q.strip().split()
      person = UserInfo.objects.filter()

      for q_word in q_words:
        person=person.filter(description__icontains=q_word)
      return person

    else:
      return UserInfo.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['q'] = self.request.GET.get('q')
    context['count'] = self.get_queryset().count()
    context['page'] = self.request.GET.get('page')

    return context

# class GetMessage(View):
#     def post(self, request, *args, **kwargs):
# 
#         user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
#         mess = Message.objects.filter(user=user)
#         form = MessageForm(request.POST) # request.POSTに送られてきたデータがある
#         if not form.is_valid():
#             return render(request, 'app/form.html', {'form':form, 'mess':mess})
#         post = form.save(commit=False) # まだMessageモデルは保存しない
#         user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
#         post.user = user
#         post.save()
#         messages.success(request, "保存しました")
#         return redirect(reverse('app:create'))
# 
#     def get(self, request, *args, **kwargs):
#         context = {}
#         context['form'] = MessageForm()
#         user = get_object_or_404(UserSocialAuth, user_id=self.request.user.id)
#         context['mess'] = Message.objects.filter(user=user)
# 
#         return render(request, 'app/form.html', context)
# 
# class UpdateMessage(generic.UpdateView):
#     model = Message
#     form_class = MessageForm
#     template_name = "app/form_update.html"
#     success_url = "/message/create"
# 
# class DeleteMessage(generic.DeleteView):
#     model = Message
#     form_class = MessageForm
# 
#     success_url = reverse_lazy('app:create')
# 
#     def delete(self, request, *args, **kwargs):
#         result = super().delete(request, *args, **kwargs)
#         messages.success(
#             self.request, '削除しました'
#         )
# 
#         return result
# 
# class UserPage(View):
#     def post(self, request, *args, **kwargs):
#         user = get_object_or_404(UserSocialAuth, user_id=self.request.user.id)
#         form = IntroduceForm(request.POST)
# 
#         # フォームのバリデーションが正しくない
#         if not form.is_valid():
#             return render(request, 'accounts/top.html', {'form':form, 'user':user})
# 
#         if not Introduce.objects.filter(user=user).exists():
#             post = form.save(commit=False) # まだIntroduceモデルは保存しない
#             user = get_object_or_404(UserSocialAuth, user_id=request.user.id)
#             post.user = user
#             post.save()
#             messages.success(request, "保存しました")
#             return redirect(reverse('app:user'))
#         else:
#             intro = get_object_or_404(Introduce, user_id=request.user.id)
#             form = IntroduceForm(request.POST, instance=intro)
#             form.save()
#             return redirect(reverse('app:user'))
# 
#     def get(self, request, *args, **kwargs):
#         user = get_object_or_404(UserSocialAuth, user_id=self.request.user.id)
#         # 対応するIntroduceが無い
#         if not Introduce.objects.filter(user=user).exists():
#             form = IntroduceForm()
#         # 対応するIntroduceがあるなら、フォームは埋めておく
#         else:
#             intro = get_object_or_404(Introduce, user_id=request.user.id)
#             form = IntroduceForm(instance=intro)
# 
# 
#         return render(request, 'accounts/top.html', {'form':form, 'user':user})
# 
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
