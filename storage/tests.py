import json

from django.test import TestCase
from django.test import Client
from rest_framework.test import APIClient
from django.urls import reverse
from .models import StorageItem


class StorageViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(StorageViewTests, cls).setUpClass()
        cls.client = Client()
        cls.test_item = StorageItem.objects.create(
            code='123', type='gtin')

    def test_StorageItemListView(self):
        # request all items
        response = self.client.get(reverse('storage:index'))
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.content)
        self.assertEqual(response[0]['item']['code'], '123')
        self.assertEqual(response[0]['item']['type'], 'gtin')

    def test_StorageItemRetrieveView(self):
        # request an existing item
        response = self.client.get(reverse('storage:detail', args=(
            self.test_item.type, self.test_item.code)))
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.content)
        self.assertEqual(response['item']['code'], '123')
        self.assertEqual(response['item']['type'], 'gtin')

        # request a non-existent item
        response = self.client.get(reverse('storage:detail', args=(
            'test_type', '999')))
        self.assertEqual(response.status_code, 404)

    def test_StorageItemUpdateView(self):

        # modify an existing item
        url = reverse('storage:edit', args=(
            self.test_item.type, self.test_item.code))
        response = self.client.put(
            url, {'code': 123, 'type': 'gtin',
                  'description': 'BIO Pommersche Gartenkr\u00e4uter 125g im Becher', 'amount': 124, 'bbd': '2023-06-10T00:00:00Z'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # modify a non-existent item
        url = reverse('storage:edit', args=('test_type', '999'))
        response = self.client.put(
            url, {'code': 123, 'type': 'gtin', 'amount': 124, 'bbd': None})
        self.assertEqual(response.status_code, 404)

        # modify with patch method
        url = reverse('storage:edit', args=('test_type', '999'))
        response = self.client.patch(
            url, {'code': 123, 'type': 'gtin', 'amount': 124, 'bbd': None})
        self.assertEqual(response.status_code, 405)

    def test_StorageItemCreateView(self):
        url = reverse('storage:create')

        # create a valid item
        response = self.client.post(
            url, {'amount': 124, 'bbd': '2023-06-10T00:00:00Z', 'item':
                  {'code': 456, 'type': 'test_type'}}, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # create an invalid item
        response = self.client.post(
            url, {'amount': 124, 'bbd': '2023-06-10',
                  'item': {'type': 'test_type'}},
            content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content,
                         b'{"code":["This field may not be null."]}')

    def test_StorageItemDeleteView(self):
        # delete an existing item
        response = self.client.delete(reverse('storage:delete', args=(
            self.test_item.type, self.test_item.code)))
        self.assertEqual(response.status_code, 204)

        # delete a non-existent item
        response = self.client.delete(
            reverse('storage:delete', args=('test_type', '999')))
        self.assertEqual(response.status_code, 404)
