from django.db import models


def item_default():
    return {'amount_multiplier': 0,
            'brand': '',
            'categ_id': None,
            'category_id': None,
            'description': '',
            'gross_weight': None,
            'id': None,
            'net_weight': None,
            'notes': False,
            'packaging': '',
            'related_products': [

            ],
            'requires_best_before_date': False,
            'requires_meat_info': False,
            'trade_item_unit_descriptor': '',
            'trade_item_unit_descriptor_name': '',
            'unit_name': '',
            'validation_status': ''}


class StorageItem(models.Model):
    amount = models.PositiveIntegerField(default=0)
    bbd = models.DateTimeField(null=True)
    comment = models.TextField(null=True, blank=True)
    country_of_disassembly = models.TextField(null=True, blank=True)
    country_of_rearing = models.TextField(null=True, blank=True)
    country_of_slaughter = models.TextField(null=True, blank=True)
    cutting_plant_registration = models.TextField(null=True, blank=True)
    code = models.PositiveBigIntegerField()
    type = models.TextField()
    item = models.JSONField(default=item_default)
    lot_number = models.TextField(null=True, blank=True)
    slaughterhouse_registration = models.TextField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['code', 'type'], name='unique_item')]
