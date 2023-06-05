import json

from rest_framework import serializers

from storage.models import StorageItem


class StorageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageItem
        exclude = ["id"]

    def to_representation(self, instance):
        """Puts type and code attributes inside the nested item dict
        and converts code to a string"""
        storage_item = super().to_representation(instance)
        code = storage_item.pop('code', None)
        item_type = storage_item.pop('type', None)
        storage_item['item']['code'] = str(code)
        storage_item['item']['type'] = item_type

        return storage_item

    def to_internal_value(self, data):
        """Convert trade_item_descriptor attribute to trade_item_descriptor.
        Puts code and type attributes outside the nested item.
        """

        try:
            # convert QueryDict to dict to be mutable
            data = data.dict()
        except AttributeError:
            pass

        nested_item = data.get('item') or {}
        if not isinstance(nested_item, dict):
            nested_item = json.loads(nested_item) or {}

        if 'trade_item_descriptor' in nested_item:
            nested_item['trade_item_unit_descriptor'] = nested_item['trade_item_descriptor']

        # support both nested and unnested code and type attributes
        data['code'] = nested_item.pop('code', data.get('code', None))
        data['type'] = nested_item.pop('type', data.get('type', ''))

        data['item'] = nested_item

        return super().to_internal_value(data)
