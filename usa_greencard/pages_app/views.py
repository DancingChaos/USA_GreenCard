from django.urls import path
from django.views.generic import TemplateView


class DvProgramView(TemplateView):
    template_name = 'pages_app/dv_program.html'


class ContactUsView(TemplateView):
    template_name = 'pages_app/contact.html'

