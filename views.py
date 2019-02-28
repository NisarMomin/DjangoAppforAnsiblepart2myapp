# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.forms import NameForm
from django.shortcuts import render
#from django.views.generic import TemplateView
from myapp.forms import LoginForm

#class HomePageView(TemplateView):
def login(request):
    username = "NOT lOGGED IN"
    if request.method == "POST":
        #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = Loginform()
		
    return render(request, 'loggedin.html', {"username" : username})
 #   def get(self, request, **kwargs):
  #      return render(request, 'hello.html', context=None)

