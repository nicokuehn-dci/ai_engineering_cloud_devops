from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogViewTest(TestCase):

    # prepare some blogs
    def setUp(self):
        # reference: please look at our customermessages application in the group project
        self.post = Post.objects.create(title="Hello world", content="Test")

    def test_blog_context_contains_posts(self):
        # a client -> represents what a browser could do!
        response = self.client.get(reverse('blog')) # _> picks the name from the url conf
        # Do not hard code your URLs
        # response = self.client.get('/blog/')
        self.assertIn(self.post, response.context['posts'])
        self.assertContains(response, '<h1>List of posts</h1>')
        self.assertContains(response, '<li>Hello world</li>')

    def test_blog_post_detail_page(self):
        url = reverse('post_detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)