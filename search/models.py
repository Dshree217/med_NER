from django.db import models

# Create your models here.
from django.db import models


class MedicineData(models.Model):
    autoid = models.AutoField(primary_key=True)
    sku_id = models.CharField(max_length=10, blank=True, null=True)
    product_id = models.CharField(max_length=10, blank=True, null=True)
    sku_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=50, blank=True, null=True)
    salt_name = models.CharField(max_length=300, blank=True, null=True)
    drug_form = models.CharField(max_length=20, blank=True, null=True)
    pack_size = models.CharField(db_column='Pack_size', max_length=25, blank=True, null=True)  # Field name made lowercase.
    strength = models.CharField(max_length=30, blank=True, null=True)
    product_banned_flag = models.CharField(max_length=10, blank=True, null=True)
    unit = models.CharField(max_length=30, blank=True, null=True)
    price_per_unit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'medicine_data'


