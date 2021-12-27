from rest_framework import serializers
from search import models


class MedicineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicineData
        fields = ('autoid', 'sku_id', 'product_id', 'sku_name', 'price', 'manufacturer_name', 'salt_name', 'drug_form',
                  'pack_size',
                  'strength', 'product_banned_flag', 'unit', 'price_per_unit')

class MedicineListSerializer(serializers.ModelSerializer):
    result = MedicineDataSerializer()

    class Meta:
        model = models.MedicineData
        fields = ('result',)