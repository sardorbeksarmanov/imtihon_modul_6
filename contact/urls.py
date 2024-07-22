from django.urls import path
from .views import contact_view
from django.views.generic import TemplateView

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('contact_success/', TemplateView.as_view(template_name="contact_success.html"), name='contact_success'),
]
