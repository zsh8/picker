from django.shortcuts import get_object_or_404
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from .models import StorageItem
from .serializers import StorageItemSerializer


class StorageItemLookupMixin(object):

    def get_object(self):
        """
        Overrides default get_object to use code and type
        attributes instead of pk for retrieving from db
        """
        code = self.kwargs.get('code')
        item_type = self.kwargs.get('item')

        return get_object_or_404(StorageItem, code=int(code), type=item_type)


class StorageItemListView(ListAPIView):
    queryset = StorageItem.objects.all()
    serializer_class = StorageItemSerializer


class StorageItemRetrieveView(StorageItemLookupMixin, RetrieveAPIView):
    queryset = StorageItem.objects.all()
    serializer_class = StorageItemSerializer


class StorageItemUpdateView(StorageItemLookupMixin, UpdateAPIView):
    queryset = StorageItem.objects.all()
    serializer_class = StorageItemSerializer
    http_method_names = ["put"]


class StorageItemCreateView(CreateAPIView):
    queryset = StorageItem.objects.all()
    serializer_class = StorageItemSerializer


class StorageItemDeleteView(StorageItemLookupMixin, DestroyAPIView):
    queryset = StorageItem.objects.all()
    serializer_class = StorageItemSerializer
