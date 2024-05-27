from django.contrib import admin
from .models import PercentageOfFat, PercentageOfAsh, PercentageOfProtein, PercentageOfMoisture, DeterminationOfTotalSolids, DeterminationOfVolatileSolids, PercentageOfFibre

admin.site.register(PercentageOfFat)
admin.site.register(PercentageOfAsh)
admin.site.register(PercentageOfProtein)
admin.site.register(PercentageOfMoisture)
admin.site.register(DeterminationOfTotalSolids)
admin.site.register(DeterminationOfVolatileSolids)
admin.site.register(PercentageOfFibre)
