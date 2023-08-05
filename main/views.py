from django.shortcuts import render
from main.models import Company, Products, Testimonials, Contact
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from main.forms import ContactForm
from django.urls import reverse_lazy


def index(request):
    context = {
        'company':  Company.objects.first(),
        'products': Products.objects.all(),
        'testimonials': Testimonials.objects.all(),
    }
    return render(request, 'main/index.html', context=context)


class AboutTemplateView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context['company'] = Company.objects.first()
        return context


class ProductTemplateView(TemplateView):
    template_name = 'main/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductTemplateView, self).get_context_data()
        context['products'] = Products.objects.all()
        return context


class TestimonialsTemplateView(TemplateView):
    template_name = 'main/testimonials.html'

    def get_context_data(self, **kwargs):
        context = super(TestimonialsTemplateView, self).get_context_data()
        context['testimonials'] = Testimonials.objects.all()[1:]
        context['testimonials_main'] = Testimonials.objects.first()
        return context


class ContactFormView(CreateView):
    model = Contact
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:index')
