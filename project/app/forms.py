from django import forms
# from .models import Message,Introduce
from django.core.mail import send_mail
from django.conf import settings

# class MessageForm(forms.ModelForm):
#
#     class Meta:
#         model = Message # どのモデルからformつくる？
#         fields = ('message',) # どのフィールドこのformで使う
#         labels = {
#             'message':'メッセージ内容',
#         }
#
# class IntroduceForm(forms.ModelForm):
#
#     class Meta:
#         model = Introduce
#         fields = ("company_name","recruiter",)
#         labels = {
#             'company_name':'会社名,部署名',
#             'recruiter':'採用者名',
#         }

class ContactForm(forms.Form):
    email = forms.EmailField(required=False, label="メールアドレス")
    message = forms.CharField(widget=forms.Textarea,label='お問い合わせ内容')

    def send_email(self):

        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER

        to = [settings.EMAIL_HOST_USER]

        send_mail("Social Recruiter:問い合わせ({})".format(email), message, from_email, to)
