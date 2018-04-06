from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve

class TestUrl(TestCase):
    client = Client()
    fixtures = ['data',]

    def test_create_url(self):

        #Get client response by URL
        response = self.client.get('/contact/create/')

        #Check if url is named 'create'
        self.assertEqual(response.resolver_match.url_name, 'create')

        #Check if page exists
        self.assertEqual(response.status_code, 200)

    def test_create_post_url(self):

        #Get client response by URL
        response = self.client.post('/contact/create-post/',{'name':'test','phone':'0927'})

        #Check if url is named 'create-post'
        self.assertEqual(response.resolver_match.url_name, 'create-post')

        #Check if redirected
        self.assertEqual(response.status_code, 302)

    def test_update_url(self):

        #Get client response by URL
        response = self.client.get('/contact/update/1/')

        #Check if url is named 'update'
        self.assertEqual(response.resolver_match.url_name, 'update')

        #Check if page exists
        self.assertEqual(response.status_code, 200)

    def test_update_post_url(self):

        #Get client response by URL
        response = self.client.post('/contact/update-post/1/',{'name':'test','phone':'0927'})

        #Check if url is named 'update-post'
        self.assertEqual(response.resolver_match.url_name, 'update-post')

        #Check if page exists
        self.assertEqual(response.status_code, 302)

    def test_delete_post_url(self):

        #Get client response by URL
        response = self.client.post('/contact/delete-post/1/')

        #Check if url is named 'delete-post'
        self.assertEqual(response.resolver_match.url_name, 'delete-post')

        #Check if page exists
        self.assertEqual(response.status_code, 302)
