# models.py
from django.db import models

class WasteCharacteristics(models.Model):
    moisture_content = models.FloatField()  # Percentage
    vs_content = models.FloatField()  # Percentage

class BiogasProduction(models.Model):
    ratio_fvw = models.FloatField()  # Percentage
    ratio_cow_manure = models.FloatField()  # Percentage
    biogas_production = models.FloatField()  # mL/g
