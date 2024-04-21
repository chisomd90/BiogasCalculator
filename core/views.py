from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import BiogasProduction

def calculate_biogas(request):
    if request.method == 'POST':
        try:
            # Retrieve form data
            ratio_fvw = float(request.POST.get('ratio_fvw', 0))
            ratio_cow_manure = float(request.POST.get('ratio_cow_manure', 0))
            moisture_content = float(request.POST.get('moisture_content', 0))
            vs_content = float(request.POST.get('vs_content', 0))

            # Perform calculations
            total_vs = (ratio_fvw * vs_content + ratio_cow_manure * vs_content) / 100
            vs_dry_basis = total_vs * (1 - moisture_content / 100)
            biogas_production = vs_dry_basis * 0.037  # 37 mL/g

             # Save or update biogas production result in database
            biogas, created = BiogasProduction.objects.get_or_create(
                ratio_fvw=ratio_fvw,
                ratio_cow_manure=ratio_cow_manure,
                moisture_content=moisture_content,
                vs_content=vs_content,
                defaults={'biogas_production': biogas_production}
            )

            # If the biogas production was already present, update it
            if not created:
                biogas.biogas_production = biogas_production
                biogas.save()

            # Construct JSON response
            response_data = {
                'biogas_production': biogas_production,
                'response_message': f"The biogas production is {biogas_production:.5f} cubic meters."
            }
            return JsonResponse(response_data)

        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)  # Bad Request
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
    elif request.method == 'GET':
        # Render the HTML template for GET requests
        return render(request, 'BiogasCalculator/calculate.html')
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed
