# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.forms import NameForm
from django.shortcuts import render
#from django.views.generic import TemplateView
from myapp.forms import LoginForm
import subprocess
from subprocess import call, check_call
#call('echo "I like potatos"', shell=True)
#class HomePageView(TemplateView):
def login(request):
    username = "PACKAGE INSTALLED"
    password = "ALREADY"
    #call('ansible-playbook sahil.yml -l $username', shell=True)
    if request.method == "POST":
        #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            password = MyLoginForm.cleaned_data['password']
            call("echo " + password + "> pack", shell=True)
           # call(["echo", %k],shell=True)
            #call('echo MyLoginForm.cleaned_data['username']',shell=True)
            call("ansible-playbook sahil.yml -l " + username, shell=True)
    else:
        MyLoginForm = Loginform()
		
    return render(request, 'loggedin.html', {"username" : username,"password" : password})
 #   def get(self, request, **kwargs):
  #      return render(request, 'hello.html', context=None)

