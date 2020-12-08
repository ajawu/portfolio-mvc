from django.views.generic import TemplateView, FormView
from django.views import View
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail
import os


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

    # Fix to use celery worker for better performance
    def form_valid(self, form):
        # Send Email function
        send_response = send_mail('Portfolio Website Contact Form',
                                  form.message,
                                  'no-reply@mg.ajawudavid.tech',
                                  ['ajawudavid@gmail.com'])
        if send_response == 1:
            return JsonResponse({'success': True,
                                 'message': 'Thank you for reaching out. I will send you an email soon.'})
        else:
            return JsonResponse({'success': False,
                                 'message': 'Email could not be sent. Is the email address specified valid.'})

    def form_invalid(self, form):
        return JsonResponse({'success': False,
                             'errors': form.errors.as_json()})
