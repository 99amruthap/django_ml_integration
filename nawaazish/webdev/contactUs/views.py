from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactUsForm
from .models import ContactUs


# Create your views here.

class ContactUsPageView(CreateView):
	model = ContactUs
	form_class = ContactUsForm
	template_name = 'contactUs/contactUsTemplate.html'
	success_url = '/'
