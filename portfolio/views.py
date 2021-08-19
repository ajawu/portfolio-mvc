from django.views.generic import TemplateView, FormView, DetailView
from django.views import View
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from portfolio.forms import ContactForm
import os
from portfolio.tasks import send_email_delayed
from django.contrib import messages
from portfolio.models import Project

import django.forms

class LandingView(TemplateView):
    template_name = 'portfolio/index.html'


class ResumeView(View):
    def get(self, request):
        file_path = settings.MEDIA_ROOT + '/files/Ajawu David - Resume.pdf'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as resume_file:
                response = HttpResponse(resume_file.read(), 'application/pdf')
                response['Content-Disposition'] = 'filename=Ajawu David - Resume.pdf'
                # file.close()
                return response
        raise Http404


class ContactView(FormView):
    form_class = ContactForm
    success_url = '/'
    template_name = 'portfolio/index.html'

    def form_valid(self, form):
        # Send Email function
        send_email_delayed.delay(form.email_address, form.message, form.name, 'Contact')
        messages.success(self.request, 'Message saved successfully.')
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'An error occurred while saving your message')
        return super().form_invalid(form)


class ProjectView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def fol(request):
    request.COOKIES.get()
