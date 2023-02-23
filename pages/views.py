from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"
