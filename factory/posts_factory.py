import random
import string


class PostFactory:

    @staticmethod
    def get_new_post():
        return {
            "title": PostFactory.__random_word(10),
            "body": PostFactory.__random_word(10),
            "userId": 1
        }

    @staticmethod
    def __random_word(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
