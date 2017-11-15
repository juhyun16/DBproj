from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic.base import TemplateView

# Create your views here.

def signup(request):
    context = dict()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()

    context["form"] = form

    return render(request, 'accounts/signup_form.html', context)



def login(request):
    pass


class ProfileView(TemplateView):
    template_name = 'accounts/myprofile.html'


