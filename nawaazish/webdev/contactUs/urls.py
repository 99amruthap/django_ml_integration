from django.urls import path
from . import views

urlpatterns = [
		path("", views.contactUsPage, name="contactUsPage")
] 