"""Json placeholder tests"""

import unittest
import requests
from urllib.parse import urljoin
import json


class API(unittest.TestCase):

    base_url = 'https://jsonplaceholder.typicode.com/'

    def GET(self, path, data=None):
        response = requests.get(urljoin(self.base_url, path), json=data)
        return response

    def POST(self, path, data=None):
        response = requests.post(urljoin(self.base_url, path), json=data)
        return response

    def PUT(self, path, data=None):
        response = requests.post(urljoin(self.base_url, path), json=data)
        return response

    def PATCH(self, path, data=None):
        response = requests.post(urljoin(self.base_url, path), json=data)
        return response

    def DELETE(self, path, data=None):
        response = requests.delete(urljoin(self.base_url, path), json=data)
        return response

    # /posts	100 posts
    def test_posts_count(self):
        posts = self.GET('/posts').json()
        self.assertEqual(100, len(posts))

    def test_posts_creation_return(self):
        # results in successful creation of a post with a new id but nothing else
        # arguably weird behaviour, could have more validation
        post1 = self.POST('/posts').json()
        self.assertEqual(201, post1.status_code)

        # results in successful creation of a post with a new id with correct data, but same id
        post2_data = {
            "userId": 1,
            "title": "foo",
            "body": "bar"
        }

        # do some checks on submission
        post2 = self.POST('/posts', post2_data).json()
        for var in post2_data:
            self.assertEqual(post2_data[var], post2[var],
                             f"{var} not as expected")

    def test_posts_creation_count(self):
        initial_posts = self.GET('/posts').json()
        self.POST('/posts')
        final_posts = self.GET('/posts').json()
        self.assertGreater(len(final_posts), len(initial_posts),
                           "Post count has not increased")

    def test_posts_update(self):
        post1 = self.GET('/posts').json()[0]
        post1["title"] += " - updated"
        updated = self.PUT(f'/posts/{post1["id"]}', post1)
        # note: seem to get error rather than fake update back as docs would suggest
        self.assertEqual(post1, updated,
                         "Put did not update item as expected")

    def test_posts_patch_update(self):
        post1 = self.GET('/posts').json()[0]
        data = {'title': post1["title"] + " - updated"}
        updated = self.PATCH(f'/posts/{post1["id"]}', data).json()
        # note: seem to get error rather than fake update back as docs would suggest
        self.assertEqual(post1, updated, "Put did not update item as expected")

    def test_posts_delete(self):
        # get initial posts
        initial_posts = self.GET('/posts').json()
        post1 = initial_posts[0]
        var = f'/posts/{post1["id"]}'

        # delete and check success
        deleted = self.DELETE(f'/posts/{post1["id"]}')
        self.assertEqual(200, deleted.status_code,
                         "Delete did ntot return as expected")

        # check counts have decreased
        final_posts = self.GET('/posts').json()
        self.assertLess(len(final_posts), len(initial_posts),
                        "Post count has not decreased")

    # /comments	500 comments
    def test_comments_count(self):
        posts = self.GET('/comments').json()
        self.assertEqual(500, len(posts))

    # /albums	100 albums
    def test_albums_count(self):
        posts = self.GET('/albums').json()
        self.assertEqual(100, len(posts))

    # /photos	5000 photos
    def test_photos_count(self):
        posts = self.GET('/photos').json()
        self.assertEqual(5000, len(posts))

    # /todos	200 todos
    def test_todos_count(self):
        posts = self.GET('/todos').json()
        self.assertEqual(200, len(posts))

    # /users	10 users
    def test_users_count(self):
        posts = self.GET('/users').json()
        self.assertEqual(10, len(posts))


if __name__ == '__main__':
    unittest.main(exit=False)
