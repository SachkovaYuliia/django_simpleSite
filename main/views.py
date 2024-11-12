from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'main/home.html', {'title': 'Головна'})

def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})

class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакти'
        return context

class ServiceView(TemplateView):
    template_name = 'main/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Послуги'
        context['services'] = ['Консультація', 'Розробка', 'Підтримка']
        return context