from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.views import generic

app_name = 'accounts'

