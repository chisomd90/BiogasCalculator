# models.py
from django.db import models

class PercentageOfFat(models.Model):
    weight_of_flask = models.IntegerField()
    weight_of_oil = models.IntegerField()
    weight_of_empty_flask = models.IntegerField()
    weight_of_sample = models.IntegerField()

class PercentageOfMoisture(models.Model):
    weight_of_crucible = models.IntegerField()
    weight_of_sample = models.IntegerField()
    weight_of_drymatter = models.IntegerField()

class PercentageOfFibre(models.Model):
    weight_of_dryresidue = models.IntegerField()
    weight_of_sample = models.IntegerField()
    weight_of_ash = models.IntegerField()

class PercentageOfAsh(models.Model):
    weight_of_crucible = models.IntegerField()
    weight_of_ash = models.IntegerField()
    weight_of_sample = models.IntegerField()

class PercentageOfProtein(models.Model):
    CONVERSION_FACTOR = 6.25  # Constant value for conversion factor

    Percentage_of_nitrogen = models.IntegerField()

class PercentageOfCarbohydrate(models.Model):
    Percentage_of_ash = models.IntegerField()
    Percentage_of_protein = models.IntegerField()
    Percentage_of_moisture = models.IntegerField()
    Percentage_of_fat = models.IntegerField()
    Percentage_of_fibre = models.IntegerField()

class DeterminationOfTotalSolids(models.Model):
    weight_of_crucible = models.IntegerField()
    weight_of_sample = models.IntegerField()
    weight_of_dryresidue = models.IntegerField()

class DeterminationOfVolatileSolids(models.Model):
    weight_of_dryresidue = models.IntegerField()
    weight_of_dryresidue_from_furnace = models.IntegerField()
    weight_of_sample = models.IntegerField()