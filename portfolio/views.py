from django.views.generic import TemplateView, CreateView
from django.views import View
from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import redirect, reverse
import os
from django.contrib import messages
from portfolio.models import Contact


class LandingView(TemplateView):
    template_name = 'portfolio/index.html'


class ResumeView(View):
    """Load pdf version of resume"""
    def get(self, request):
        file_path = settings.MEDIA_ROOT + '/files/Ajawu David - Resume.pdf'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as resume_file:
                response = HttpResponse(resume_file.read(), 'application/pdf')
                response['Content-Disposition'] = 'filename=Ajawu David - Resume.pdf'
                # file.close()
                return response
        raise Http404


class ContactView(CreateView):
    model = Contact
    success_url = '/'
    fields = ['name', 'email', 'message']

    def form_valid(self, form):
        # Send Email function
        # send_email_delayed.delay(form.email_address, form.message, form.name, 'Contact')
        messages.success(self.request, 'Message saved successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'All fields are required')
        return redirect(reverse('portfolio:landing_page'))
