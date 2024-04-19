# models.py
from django.db import models

class BiogasProduction(models.Model):
    ratio_fvw = models.FloatField()  # Percentage
    ratio_cow_manure = models.FloatField()  # Percentage
    moisture_content = models.FloatField(null=True)  # Percentage - Nullable
    vs_content = models.FloatField(null=True)  # Percentage
    biogas_production = models.FloatField()  # mL/g
