from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(username='User1', password='abc123')
        testuser.save()

        test_post = Post.objects.create(
            author=testuser,
            title='test_title',
            body='test_body'
        )

        test_post.save()

    def test_blog_content(self):
        post = Post.objects.first()
        author = f'{post.author.username}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'User1')
        self.assertEqual(title, 'test_title')
        self.assertEqual(body, 'test_body')

