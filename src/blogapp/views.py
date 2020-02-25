from django.shortcuts import render
from django.http import Http404, HttpResponse

from .forms import ContactForm, HomeForm

def home(req):
  template_name = "home.html"
  title = "home_page"
  context = {'title': title}
  return render(req, template_name, context)

def about(req):
  template_name = "about.html"
  title = "about_page"
  context = {'title': title}
  return render(req, template_name, context)

def contact(req):
  form = ContactForm(req.POST or None)
  if form.is_valid():
    print(form.cleaned_data)
    form = ContactForm()
  template_name = "contact.html" # or form.html...
  title = "contact_page"
  context = {'title': title, 'form': form}
  return render(req, template_name, context)