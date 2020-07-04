from django.shortcuts import render
from .forms import QuestionForm
from .models import Question
from django.views.generic import CreateView, TemplateView

# Create your views here.

class QuestionFormCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question_form.html'
    success_url = 'success'

class SuccessView(TemplateView):
    template_name = 'success.html'

