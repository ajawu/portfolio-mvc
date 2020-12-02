from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse,Http404
from django.conf import settings
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
