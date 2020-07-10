from django.urls import path
from .views import DvProgramView
from django.views.generic import TemplateView

app_name = "pages_app"

urlpatterns = [
    path("home/", TemplateView.as_view(template_name="pages_app/home.html"), name="home"),
    path("dv-program/", TemplateView.as_view(template_name="pages_app/dv_program.html"), name="dv-program"),
    path("contact/", TemplateView.as_view(template_name="pages_app/contact.html"), name="contact"),
    path("about/", TemplateView.as_view(template_name="pages_app/about.html"), name="about"),
    path("how-to-reg/", TemplateView.as_view(template_name="pages_app/how_to_reg.html"), name="how_to_reg"),
    path("requirements/", TemplateView.as_view(template_name="pages_app/requirements.html"), name="requirements"),
    path("green-card-process/", TemplateView.as_view(template_name="pages_app/green_card_process.html"), name="green_card_process"),
    path("advantages/", TemplateView.as_view(template_name="pages_app/advantages.html"), name="advantages"),
    path("private-entity/", TemplateView.as_view(template_name="pages_app/private_entity.html"), name="private_entity"),
    path("testimonials/", TemplateView.as_view(template_name="pages_app/testimonials.html"), name="testimonials"),
    path("terms-conditions/", TemplateView.as_view(template_name="pages_app/terms_conds.html"), name="terms_conds"),
    path("privacy-policy/", TemplateView.as_view(template_name="pages_app/privacy_policy.html"), name="privacy_policy"),
    path("eligible-countries/", TemplateView.as_view(template_name="pages_app/eligible_countries.html"), name="eligible_countries"),
    path("register/", TemplateView.as_view(template_name="pages_app/register.html"), name="register"),
]
