import logging

from clients.todos_client import get_posts, add_post, put_post, delete_post
from logger.logging_utils import log_entry


class PostService:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    @staticmethod
    def get_all_posts():
        call = get_posts()
        log_entry(url=call.request.url, http_method=call.request.method, response_code=call.status_code)
        return call

    @staticmethod
    def get_single_post(post_id):
        call = get_posts(post_id)
        log_entry(url=call.request.url,
                  http_method=call.request.method,
                  resp_body=call.json(),
                  response_code=call.status_code)
        return call

    @staticmethod
    def add_new_post(post):
        call = add_post(post)
        log_entry(url=call.request.url,
                  http_method=call.request.method,
                  req_body=call.request.body,
                  resp_body=call.json(),
                  response_code=call.status_code)
        return call

    @staticmethod
    def update_existing_post(post_id, post):
        post.update(id=post_id)
        call = put_post(post, post_id)

        log_entry(url=call.request.url,
                  http_method=call.request.method,
                  req_body=call.request.body,
                  resp_body=call.json(),
                  response_code=call.status_code)
        return call

    @staticmethod
    def delete_single_post(post_id):
        call = delete_post(post_id)
        log_entry(url=call.request.url, http_method=call.request.method, response_code=call.status_code)
        return call
