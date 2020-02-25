from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from blog.models import BlogPost
from .forms import BlogPostModelForm #BlogPostForm


# CRUD - Create, Retrieve, Update, and Delete
def blog_post_list_view(req):
  p_title = "Blog List"
  template_name = "blog/list.html"
  # Version of Retrive - this could be a list or search
  qs = BlogPost.objects.all()
  context = {'objects': qs, 'ptitle': p_title}
  return render(req, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(req):
  # Create object, ? use a form
  form = BlogPostModelForm(req.POST or None)
  if form.is_valid():
    # obj = BlogPost.objects.create(**form.cleaned_data)
    obj = form.save(commit=False)
    obj.user = req.user
    obj.save()
    form = BlogPostModelForm()
  template_name = "blog/form.html" #"blog/create.html"
  p_title = "Create"
  context = {'ptitle':p_title, 'form':form}
  return render(req, template_name, context)

def blog_post_detail_view(req, slug):
  # 1 object -> detail view
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = "blog/detail.html"
  p_title = "Detail"
  context = {'object': obj, 'ptitle': p_title}
  return render(req, template_name, context)

def blog_post_update_view(req, slug):
  obj = get_object_or_404(BlogPost, slug=slug)
  form = BlogPostModelForm(req.POST or None, instance=obj)
  if form.is_valid():
    form.save()
  template_name = "blog/form.html"
  p_title = "Update"
  context = {'form': form, 'ptitle':p_title}
  return render(req, template_name, context)

def blog_post_delete_view(req, slug):
  obj = get_object_or_404(BlogPost, slug=slug)
  template_name = "blog/delete.html"
  if req.method == "POST":
    obj.delete()
    return redirect("/blog")
  context = {'object': obj}
  return render(req, template_name, context)