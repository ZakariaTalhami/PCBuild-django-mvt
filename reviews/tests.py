from django.test import TestCase
from common.testing.custom_testcases import TemplateTestCase
from common.testing.object_factory import json_to_objects
from django.template import Context
from django.shortcuts import reverse
from reviews.models import Comment
from parts.models import Part
import os 

OBJECT_JSON_FILE = 'tests/test_objects/comments.json'
COMMENT_POST_NAMESPACE = 'comment-create'
DETAIL_VIEW_NAMESPACE = 'parts-memory-detail'


class CommentFilterTest(TemplateTestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        json_to_objects(os.path.join(dir, OBJECT_JSON_FILE))

    def test_iscommented_filter_true(self):
        parts = Part.objects.get(pk=1)
        comments = parts.comment_set.all()
        
        template = "{{ comments|iscommented:'1' }}"
        context = Context({'comments':comments})

        self.template_assert(
            filter_module="commentFilters",
            template=template,
            context=context,
            expected=str(True)
        )

    def test_iscommented_filter_false(self):
        parts = Part.objects.get(pk=2)
        comments = parts.comment_set.all()
        
        template = "{{ comments|iscommented:'1' }}"
        context = Context({'comments':comments})

        self.template_assert(
            filter_module="commentFilters",
            template=template,
            context=context,
            expected=str(False)
        )
        
class CommentViewTest(TestCase):

    def setUp(self):
        dir = os.path.dirname(__file__)
        json_to_objects(os.path.join(dir, OBJECT_JSON_FILE))

    def test_comment_creation(self):
        expected_redirect = reverse(DETAIL_VIEW_NAMESPACE, kwargs={ 'pk':1})
        old_comments_count = len(Comment.objects.all())
        post_data = {
            "owner": 1,
            "part": 2,
            "text": "sasda"
        }
        res = self.client.post(reverse(COMMENT_POST_NAMESPACE), post_data, HTTP_REFERER=expected_redirect)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(len(Comment.objects.all()), old_comments_count+1)
        self.assertRedirects(res, expected_redirect)

    def test_comment_creation_failed(self):
        expected_redirect = reverse(DETAIL_VIEW_NAMESPACE, kwargs={ 'pk':1})
        old_comments_count = len(Comment.objects.all())
        # part is already reviewed by the user
        post_data = {
            "owner": 1,
            "part": 1,
            "text": "sasda"
        }
        res = self.client.post(reverse(COMMENT_POST_NAMESPACE), post_data, HTTP_REFERER=expected_redirect)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(len(Comment.objects.all()), old_comments_count)
        self.assertRedirects(res, expected_redirect, status_code=400)
