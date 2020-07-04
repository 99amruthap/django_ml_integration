from django.urls import path
from . import views

urlpatterns = [
	path('join/', views.JoinUsView.as_view(), name='joinUsPage')
]