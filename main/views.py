from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from main import forms

# Create your views here.
def home(request):
     return render(request, "home.html", {})

#def about(request):
    #return render(request, "about_us.html")

#def test(request):
    #return render(request, "test.html")
class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
        return render(request,"contact_form.html")    
