from unittest import TestCase

from assertions.posts_asertions import PostsAssertions
from factory.posts_factory import PostFactory
from service.todos_service import PostService


class BaseTest(TestCase):

    def test_should_get_all_posts(self):
        # when
        response = PostService.get_all_posts()
        # then
        assert PostsAssertions.is_get_all_posts_response_ok(response)

    def test_should_get_single_post(self):
        # when
        response = PostService.get_single_post(1)
        # then
        assert PostsAssertions.is_single_post_response_ok(response)

    def test_should_add_new_post(self):
        # given
        post = PostFactory.get_new_post()
        # when
        response = PostService.add_new_post(post)
        # then
        assert PostsAssertions.is_add_new_post_response_ok(post, response)

    def test_should_update_existing_post(self):
        # given
        post = PostFactory.get_new_post()
        # when
        response = PostService.update_existing_post(post_id=1, post=post)
        # then
        assert PostsAssertions.is_update_post_response_ok(post, response)

    def test_should_delete_posts(self):
        # when
        response = PostService.delete_single_post(1)
        # then
        assert PostsAssertions.is_delete_post_response_ok(response)
