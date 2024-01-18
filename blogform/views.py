from django.shortcuts import render
from django.views import View
from .forms import fileupload
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.
class profile_view(CreateView):
    template_name = 'blogform/form.html'
    model=UserProfile
    fields='__all__'
    success_url='/images'
class imageview(ListView):
    template_name='blogform/image.html'
    model=UserProfile
    context_object_name='images'