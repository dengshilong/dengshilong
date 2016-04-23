from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Post, Category, Page
# Create your tests here.
def create_post(title, slug, content, publish_time=None, categories=[], tags=[]):
    """
    Creates a post
    """
    post = Post.objects.create(title=title, slug=slug, content=content)
    if publish_time:
        post.publish_time = publish_time
    for category in categories:
        post.category.add(category)
    for tag in tags:
        post.tag.add(tag)
    post.save()
    return post

def create_page(title, slug, content):
    return Page.objects.create(title=title, slug=slug, content=content)

def create_category(name):
    return Category.objects.create(name=name)
class PostListTests(TestCase):
    def test_index_view_with_no_posts(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('blog.index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No post")
        self.assertQuerysetEqual(response.context['post_list'], [])
    def test_index_view_with_one_post(self):
        """
        Test with one post
        """
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02')
        response = self.client.get(reverse('blog.index'))
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])
    def test_index_view_with_two_post(self):
        """
        Test with two posts
        """
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02')
        create_post(title="newly-post", slug = "newly-post", content="test content", publish_time='2016-12-15 08:01:02')
        response = self.client.get(reverse('blog.index'))
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: newly-post>', '<Post: first post>'])
        
    def test_index_view_with_three_post(self):
        """
        Test with three posts
        """
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02')
        create_post(title="newly-post", slug = "newly-post", content="test content", publish_time='2016-12-15 08:01:02')
        create_post(title="oldest-post", slug = "oldest-post", content="test content", publish_time='2013-12-15 08:01:02')
        response = self.client.get(reverse('blog.index'))
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: newly-post>', '<Post: first post>', '<Post: oldest-post>'])
    """
    def test_index_view_with_pagination(self):
        page_number = 10
        for i in xrange(1, 2 * page_number + 1):
            title = "post%d" % i 
            create_post(title=title, slug=title, content="test content", publish_time='2014-12-%d 08:01:02' % i)
        result = []
        for i in xrange(page_number, 0, -1):
            result.append('<Post: post%d' % i) 
        response = self.client.get('/?page=2')
        self.assertQuerysetEqual(response.context['post_list'], result)
    """
             
class PostDetailTests(TestCase):
    def test_post_detail_view_with_one_post(self):
        """
        Test with one post
        """
        response = self.client.get('/2014/12/15/first-post/')
        self.assertEqual(response.status_code, 404)
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02')
        response = self.client.get('/2014/12/15/first-post/')
        self.assertEqual(response.context['post'].title, 'first post')

class PageDetailTests(TestCase):
    def test_page_detail_view_with_one_post(self):
        """
        Test with one page
        """
        response = self.client.get('/first-page/')
        self.assertEqual(response.status_code, 404)
        create_page(title="first page", slug = "first-page", content="test content")
        response = self.client.get('/first-page/')
        self.assertEqual(response.context['page'].title, 'first page')

class CategoryListTests(TestCase):
    def test_category_view_with_no_post(self):
        """
        Test with not post
        """
        response = self.client.get('/category/test/')
        self.assertEqual(response.status_code, 404)

    def test_category_view_with_one_post(self):
        """
        Test with one post
        """
        category = create_category('test')
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02', categories=[category])
        response = self.client.get('/category/test/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])

        response = self.client.get('/category/other/')
        self.assertEqual(response.status_code, 404)
    def test_category_view_with_two_category(self):
        """
        Test with one post with two category
        """
        category = create_category('test')
        
        second = create_category('other')
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02', categories=[category, second])
        response = self.client.get('/category/test/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])

        response = self.client.get('/category/other/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])
         
    def test_category_view_with_two_post(self):
        """
        Test with two post
        """
        category = create_category('test')
        create_post(title="newly post", slug = "first-post", content="test content", publish_time='2016-12-15 08:01:02', categories=[category])
        create_post(title="old post", slug = "newly-post", content="test content", publish_time='2015-12-15 08:01:02', categories=[category])
        response = self.client.get('/category/test/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: newly post>', '<Post: old post>'])

class TagListTests(TestCase):
    def test_tag_view_with_no_post(self):
        """
        Test with not post
        """
        response = self.client.get('/tag/test/')
        self.assertEqual(response.status_code, 200)

    def test_tag_view_with_one_post(self):
        """
        Test with one post
        """
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02', tags=['test'])
        response = self.client.get('/tag/test/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])

        response = self.client.get('/tag/other/')
        self.assertEqual(response.status_code, 200)
    def test_tag_view_with_two_tag(self):
        """
        Test with one post with two tag
        """
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02', tags=['test', 'other'])
        response = self.client.get('/tag/test/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])

        response = self.client.get('/tag/other/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])
         
    def test_tag_view_with_two_post(self):
        """
        Test with two post
        """
        create_post(title="newly post", slug = "first-post", content="test content", publish_time='2016-12-15 08:01:02', tags=['test'])
        create_post(title="old post", slug = "newly-post", content="test content", publish_time='2015-12-15 08:01:02', tags=['test'])
        response = self.client.get('/tag/test/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: newly post>', '<Post: old post>'])

class ArchiveListTests(TestCase):
    def test_archive_view_with_no_post(self):
        """
        Test with not post
        """
        response = self.client.get('/2014/12/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No post")
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_archive_view_with_one_post(self):
        """
        Test with one post
        """
        create_post(title="first post", slug = "first-post", content="test content", publish_time='2014-12-15 08:01:02')
        response = self.client.get('/2014/12/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: first post>'])

        response = self.client.get('/2014/11/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No post")
        self.assertQuerysetEqual(response.context['post_list'], [])
         
    def test_archive_view_with_two_post(self):
        """
        Test with two post
        """
        create_post(title="newly post", slug = "first-post", content="test content", publish_time='2014-12-16 08:01:02')
        create_post(title="old post", slug = "newly-post", content="test content", publish_time='2014-12-15 08:01:02')
        response = self.client.get('/2014/12/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: newly post>', '<Post: old post>'])



