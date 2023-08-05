from django.urls import path
from main.views import index, AboutTemplateView, ProductTemplateView, TestimonialsTemplateView, ContactFormView

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('products/', ProductTemplateView.as_view(), name='products'),
    path('testimonials/', TestimonialsTemplateView.as_view(), name='testimonials'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
]
