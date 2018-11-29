import json

import requests

from clients.client_utils import build_url


def get_posts(post_id=None):
    post_id = post_id if post_id is not None else ""
    return requests.get(build_url("/posts/{}").format(post_id))


def add_post(request_body):
    return requests.post(
        build_url("/posts"),
        data=json.dumps(request_body),
        headers={'Content-Type': 'application/json'}
    )


def put_post(request_body, post_id):
    return requests.put(
        build_url("/posts/{}".format(post_id)),
        data=json.dumps(request_body),
        headers={'Content-Type': 'application/json'}
    )


def delete_post(post_id):
    return requests.delete(build_url("/posts/{}").format(post_id))
