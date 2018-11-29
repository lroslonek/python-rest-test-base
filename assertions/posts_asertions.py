from assertions.AssertionException import AssertionException


class PostsAssertions:

    @staticmethod
    def is_get_all_posts_response_ok(response):
        if response.json()[0]['id'] == 1 \
                and len(response.json()) == 100 \
                and 'title' and 'body' and 'userId' in response.json()[0] \
                and len(response.json()[0]) == 4 \
                and response.status_code == 200:
            return True
        else:
            raise AssertionException("fetch all posts failed :(")

    @staticmethod
    def is_single_post_response_ok(response):
        if response.json()['id'] == 1 \
                and 'title' and 'body' and 'userId' in response.json() \
                and len(response.json()) == 4 \
                and response.status_code == 200:
            return True
        else:
            raise AssertionException("fetch single post failed :(")

    @staticmethod
    def is_add_new_post_response_ok(requested_post, response):
        if response.json()['id'] == 101 \
                and 'title' and 'body' and 'userId' in response.json() \
                and response.json()['title'] == requested_post['title'] \
                and response.json()['body'] == requested_post['body'] \
                and response.json()['userId'] == requested_post['userId'] \
                and len(response.json()) == 4 \
                and response.status_code == 201:
            return True
        else:
            raise AssertionException("add new post failed :(")

    @staticmethod
    def is_update_post_response_ok(requested_post, response):
        if response.json()['id'] == requested_post['id'] \
                and 'title' and 'body' and 'userId' in response.json() \
                and response.json()['title'] == requested_post['title'] \
                and response.json()['body'] == requested_post['body'] \
                and response.json()['userId'] == requested_post['userId'] \
                and len(response.json()) == 4 \
                and response.status_code == 200:
            return True
        else:
            raise AssertionException("update existing post failed :(")

    @staticmethod
    def is_delete_post_response_ok(response):
        if len(response.json()) == 0 and response.status_code == 200:
            return True
        else:
            raise AssertionException("delete post failed :(")

