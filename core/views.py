from django.shortcuts import render
from .models import WasteCharacteristics, BiogasProduction

def calculate_biogas(request):
    if request.method == 'POST':
        # Retrieve form data
        ratio_fvw = float(request.POST['ratio_fvw'])
        ratio_cow_manure = float(request.POST['ratio_cow_manure'])

        # Retrieve waste characteristics from database
        characteristics = WasteCharacteristics.objects.first()  # Assuming only one entry in the database

        # Calculate biogas production
        moisture_content = characteristics.moisture_content
        vs_content = characteristics.vs_content
        total_vs = (ratio_fvw * vs_content + ratio_cow_manure * vs_content) / 100
        vs_dry_basis = total_vs * (1 - moisture_content / 100)
        biogas_production = vs_dry_basis * 0.037  # 37 mL/g

        # Save or update biogas production result in database
        biogas = BiogasProduction.objects.first()  # Assuming only one entry in the database
        if biogas:
            biogas.biogas_production = biogas_production
            biogas.save()
        else:
            BiogasProduction.objects.create(
                ratio_fvw=ratio_fvw,
                ratio_cow_manure=ratio_cow_manure,
                biogas_production=biogas_production
            )

        return render(request, 'BiogasCalculator/result.html', {'biogas_production': biogas_production})

    return render(request, 'BiogasCalculator/calculate.html')