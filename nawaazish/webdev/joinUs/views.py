from django.shortcuts import render
from .forms import JoinUsForm
from .models import JoinUs
from django.views.generic import CreateView, TemplateView

# Create your views here.

class JoinUsView(CreateView):
    model = JoinUs
    form_class = JoinUsForm
    template_name = 'joinUs/joinUsTemplate.html'
    success_url = '/'

# class SuccessView(TemplateView):
#     template_name = 'success.html'

