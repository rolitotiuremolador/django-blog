from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .forms import NewTopicForm
from .models import Forum, Topic, Post


def forum_view(req):
  forums = Forum.objects.all()
  return render(req, 'forum.html', {'forums':forums})

def forum_topics(req, pk):
  forum = get_object_or_404(Forum, pk=pk)
  return render(req, 'topics.html', {'forum': forum})

def new_topic(req, pk):
  forum = get_object_or_404(Forum, pk=pk)
  # user = User.objects.first() #TODO: get currently loggedin user
  if req.method == 'POST':
    subject = req.POST['subject']
    message = req.POST['message']
    # form = NewTopicForm(req.POST)
    user = User.objects.first()

    topic = Topic.objects.create(
      subject = subject,
      forum = forum,
      starter = user
    )

    post = Post.objects.create(
      message= message,
      topic = topic,
      created_by = user
    )
  
    return redirect('forum_topics', pk=forum.pk) #TODO: redirect to the created topic page.
  
  return render(req, 'new_topic.html', {'forum': forum})