from django.http import JsonResponse
from .models import WasteCharacteristics, BiogasProduction

def calculate_biogas(request):
    if request.method == 'POST':
        # Retrieve form data
        ratio_fvw = float(request.POST.get('ratio_fvw', 75))
        ratio_cow_manure = float(request.POST.get('ratio_cow_manure', 25))

        # Retrieve waste characteristics from database
        characteristics = WasteCharacteristics.objects.first()  # Assuming only one entry in the database

        # Calculate biogas production
        moisture_content = characteristics.moisture_content
        vs_content = characteristics.vs_content
        total_vs = (ratio_fvw * vs_content + ratio_cow_manure * vs_content) / 100
        vs_dry_basis = total_vs * (1 - moisture_content / 100)
        biogas_production = vs_dry_basis * 0.037  # 37 mL/g

        # Save or update biogas production result in database
        biogas, created = BiogasProduction.objects.get_or_create(
            defaults={
                'ratio_fvw': ratio_fvw,
                'ratio_cow_manure': ratio_cow_manure,
                'biogas_production': biogas_production
            }
        )

        # Return the results as JSON response
        return JsonResponse({'biogas_production': biogas.biogas_production})

    # If the request method is not POST, return a 405 Method Not Allowed response
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)
