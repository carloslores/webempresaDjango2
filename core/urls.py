from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about', core_views.about, name="about"),
    path('contact', core_views.contact, name="contact"),
    path('sample', core_views.sample, name="sample"),
    path('blog', core_views.blog, name="blog"),
    path('store', core_views.store, name="store"),
    path('services', core_views.services, name="services"),
]