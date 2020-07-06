from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView
from .models import JoinUs, ContactUs
from .forms import JoinUsForm, ContactUsForm

# Create your views here.


def about_show(request):
    return render(request, 'about.html', None)


def contact_show(request):
    return render(request, 'contact.html', None)


def donate_show(request):
    return render(request, 'donate.html', None)


def event_show(request):
    return render(request, 'event.html', None)


def gallery_show(request):
    return render(request, 'gallery.html', None)


def index_show(request):
    return render(request, 'index.html', None)


def crew_show(request):
    return render(request, 'meet-our-crew.html', None)


class JoinUsIndexCreateView(CreateView):
    model = JoinUs
    form_class = JoinUsForm
    template_name = 'index.html'
    success_url = '/'


class ContactUsCreateView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    second_form_class = JoinUsForm
    template_name = 'contact.html'
    success_url = 'contact/'




class CrewUsCreateView(CreateView):
    model = JoinUs
    form_class = JoinUsForm
    template_name = 'meet-our-crew.html'
    success_url = 'crew/'


class DonateCreateView(CreateView):
    model = JoinUs
    form_class = JoinUsForm
    template_name = 'donate.html'
    success_url = 'donate/'


class EventCreateView(CreateView):
    model = JoinUs
    form_class = JoinUsForm
    template_name = 'event.html'
    success_url = 'event/'


class AboutCreateView(CreateView):
    model = JoinUs
    form_class = JoinUsForm
    template_name = 'about.html'
    success_url = 'about/'


class GalleryCreateView(CreateView):
    model = JoinUs
    form_class = JoinUsForm
    template_name = 'gallery.html'
    success_url = 'gallery/'


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        join = JoinUsForm(self.request.GET or None)
        contact = ContactUsForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['join_form'] = join
        context['contact_form'] = contact
        return self.render_to_response(context)


class ContactFormView(FormView):
    form_class = ContactUsForm
    template_name = 'contact.html'
    success_url = reverse_lazy('join_us')

    def post(self, request, *args, **kwargs):
        question_form = self.form_class(request.POST)
        join_form = JoinUsForm()
        if question_form.is_valid():
            question_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    question_form=question_form,
                    join_form=join_form

                )
            )


class JoinFormView(FormView):
    form_class = JoinUsForm
    template_name = 'contact.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        answer_form = self.form_class(request.POST)
        contact_form = ContactUsForm()
        if answer_form.is_valid():
            answer_form.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
            )
        )
        else:
            return self.render_to_response(
                self.get_context_data(
                    join_form=answer_form,
                    contact_form=contact_form
            )
        )





