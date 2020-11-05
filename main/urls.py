from django.urls import path
from django.contrib import admin
from.import views
from main import views
from django.views.generic import TemplateView

urlpatterns = [
        path('',views.home, name='rendering html file'),
        path(
        "about/",
        TemplateView.as_view(template_name="about_us.html"),name="about_us",),
        #path('about/', views.about),
        #path('test/',views.test)
        path("test/",TemplateView.as_view(template_name="test.html"),name="test",),
        path("contact-us/",views.ContactUsView.as_view(),name="contact_us"),
]
