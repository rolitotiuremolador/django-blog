from django.test import TestCase
from django.urls import reverse, resolve

from .views import forum_view, forum_topics
from .models import Forum

# Create your tests here.
class ForumViewTests(TestCase):
  def setUp(self):
    self.forum = Forum.objects.create(title="Programming Laguage", description="Desc")
    url = reverse('forum')
    self.response = self.client.get(url)

  def test_forum_view_status_code(self):
    self.assertEquals(self.response.status_code, 200)

  def test_forum_view_url_resolves_forum_view(self):
    view = resolve('/forum/')
    self.assertEquals(view.func, forum_view)

  def test_forum_view_contains_link_to_topics_page(self):
    forum_topics_url = reverse('forum_topics', kwargs={'pk':self.forum.pk})
    self.assertContains(self.response, 'href="{0}"'.format(forum_topics_url))

  def test_forum_topics_view_contains_link_back_to_forum_page(self):
    forum_topics_url = reverse('forum_topics',kwargs={'pk': 1})
    response = self.client.get(forum_topics_url)
    forum_page_url = reverse('forum')
    self.assertContains(response, 'href="{0}"'.format(forum_page_url))

class ForumTopicsTests(TestCase):
    def setUp(self):
        Forum.objects.create(title='Programming Language', description='Discussion about programming languages.')

    def test_forum_topics_view_success_status_code(self):
        url = reverse('forum_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_forum_topics_view_not_found_status_code(self):
        url = reverse('forum_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_forum_topics_url_resolves_forum_topics_view(self):
        view = resolve('/forum/1/')
        self.assertEquals(view.func, forum_topics)