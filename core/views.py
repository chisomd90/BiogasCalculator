# from django.shortcuts import render
# from django.http import JsonResponse
# from django.core.exceptions import ValidationError
# from .models import PercentageOfFat, PercentageOfAsh, PercentageOfFibre, PercentageOfMoisture, PercentageOfProtein, PercentageOfCarbohydrate, DeterminationOfTotalSolids, DeterminationOfVolatileSolids

# def calculate_percentage_of_fat(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         weight_of_flask = request.POST.get('weight_of_flask')
#         weight_of_oil = request.POST.get('weight_of_oil')
#         weight_of_empty_flask = request.POST.get('weight_of_empty_flask')
#         weight_of_sample = request.POST.get('weight_of_sample')
        
#         try:
#             # Check if any form data is None
#             if None in (weight_of_flask, weight_of_oil, weight_of_empty_flask, weight_of_sample):
#                 raise ValueError("Form data cannot be None")

#             # Convert form inputs to integers
#             weight_of_flask = int(weight_of_flask)
#             weight_of_oil = int(weight_of_oil)
#             weight_of_empty_flask = int(weight_of_empty_flask)
#             weight_of_sample = int(weight_of_sample)
            
#             # Perform calculation
#             result = (((weight_of_flask + weight_of_oil) - weight_of_empty_flask) / weight_of_sample) * 100.0
            
#             # JSON response
#             response_data = {
#                 'message': 'Percentage of Fat calculation successful',
#                 'percentage_of_fat': result
#                 }
#             return JsonResponse(response_data)

#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_percentage_of_fat.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed
    

# def calculate_percentage_of_ash(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         weight_of_crucible = request.POST.get('weight_of_crucible')
#         weight_of_ash = request.POST.get('weight_of_ash')
#         weight_of_sample = request.POST.get('weight_of_sample')
        
#         try:
#             # Check if any form data is None
#             if None in (weight_of_crucible, weight_of_ash, weight_of_sample):
#                 raise ValueError("Form data cannot be None")
            
#             # Convert form inputs to integers
#             weight_of_crucible = int(weight_of_crucible)
#             weight_of_ash = int(weight_of_ash)
#             weight_of_sample = int(weight_of_sample)
            
#             # Perform calculation
#             result = (((weight_of_crucible + weight_of_ash) - weight_of_crucible) / weight_of_sample) * 100.0
            
#             # Create custom response message
#             response_data = {
#                 'message': 'Percentage of Ash calculation successful',
#                 'percentage_of_ash': result
#                 }
#             return JsonResponse(response_data)

#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_percentage_of_ash.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed
    


# def calculate_percentage_of_fibre(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         weight_of_dryresidue = request.POST.get('weight_of_dryresidue')
#         weight_of_ash = request.POST.get('weight_of_ash')
#         weight_of_sample = request.POST.get('weight_of_sample')
        
#         try:
#             # Check if any form data is None
#             if None in (weight_of_dryresidue, weight_of_ash, weight_of_sample):
#                 raise ValueError("Form data cannot be None")


#             # Convert form inputs to integers
#             weight_of_dryresidue = int(weight_of_dryresidue)
#             weight_of_ash = int(weight_of_ash)
#             weight_of_sample = int(weight_of_sample)
            
#             # Perform calculation
#             result = ((weight_of_dryresidue - weight_of_ash) / weight_of_sample) * 100.0
            
#             # Create custom response message
#             response_data = {
#                 'message': 'Percentage of Fibre calculation successful',
#                 'percentage_of_fibre': result
#             }
            
#             # Return JSON response
#             return JsonResponse(response_data)
#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_percentage_of_fibre.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed

# def calculate_percentage_of_moisture(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         weight_of_crucible = request.POST.get('weight_of_crucible')
#         weight_of_sample = request.POST.get('weight_of_sample')
#         weight_of_drymatter = request.POST.get('weight_of_drymatter')
        
#         try:
#             # Check if any form data is None
#             if None in (weight_of_crucible, weight_of_drymatter, weight_of_sample):
#                 raise ValueError("Form data cannot be None")
            

#             # Convert form inputs to integers
#             weight_of_crucible = int(weight_of_crucible)
#             weight_of_sample = int(weight_of_sample)
#             weight_of_drymatter = int(weight_of_drymatter)
            
#             # Perform calculation
#             result = (((weight_of_crucible + weight_of_sample) - (weight_of_crucible + weight_of_drymatter)) / weight_of_sample) * 100.0
            
#             # Create custom response message
#             response_data = {
#                 'message': 'Percentage of Moisture calculation successful',
#                 'percentage_of_moisture': result
#             }
            
#             # Return JSON response
#             return JsonResponse(response_data)
#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_percentage_of_moisture.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed

# def calculate_percentage_of_protein(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         percentage_of_nitrogen = request.POST.get('percentage_of_nitrogen')
        
#         try:
#             # Check if any form data is None
#             if None in (percentage_of_nitrogen):
#                 raise ValueError("Form data cannot be None")
#             # Convert form input to integer
#             percentage_of_nitrogen = int(percentage_of_nitrogen)
            
#             # Perform calculation
#             result = percentage_of_nitrogen * PercentageOfProtein.CONVERSION_FACTOR
            
#             # Create custom response message
#             response_data = {
#                 'message': 'Percentage of Protein calculation successful',
#                 'percentage_of_protein': result
#             }
            
#             # Return JSON response
#             return JsonResponse(response_data)
#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_percentage_of_protein.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed

# def calculate_percentage_of_carbohydrate(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         percentage_of_ash = request.POST.get('percentage_of_ash')
#         percentage_of_protein = request.POST.get('percentage_of_protein')
#         percentage_of_moisture = request.POST.get('percentage_of_moisture')
#         percentage_of_fat = request.POST.get('percentage_of_fat')
#         percentage_of_fibre = request.POST.get('percentage_of_fibre')
        
#         try:
#             # Check if any form data is None
#             if None in (percentage_of_ash, percentage_of_fat, percentage_of_fibre, percentage_of_moisture, percentage_of_protein):
#                 raise ValueError("Form data cannot be None")
            
#             # Convert form inputs to integers
#             percentage_of_ash = int(percentage_of_ash)
#             percentage_of_protein = int(percentage_of_protein)
#             percentage_of_moisture = int(percentage_of_moisture)
#             percentage_of_fat = int(percentage_of_fat)
#             percentage_of_fibre = int(percentage_of_fibre)
            
#             # Perform calculation
#             result = 100 - (percentage_of_ash + percentage_of_fibre + percentage_of_fat + percentage_of_moisture + percentage_of_protein)
            
#             # Create custom response message
#             response_data = {
#                 'message': 'Percentage of Carbohydrate calculation successful',
#                 'percentage_of_carbohydrate': result
#             }
            
#             # Return JSON response
#             return JsonResponse(response_data)
#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_percentage_of_carbohydrate.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed
    

# def calculate_determination_of_total_solids(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         weight_of_crucible = request.POST.get('weight_of_crucible')
#         weight_of_sample = request.POST.get('weight_of_sample')
#         weight_of_dryresidue = request.POST.get('weight_of_dryresidue')
        
#         try:
#             # Check if any form data is None
#             if None in (weight_of_crucible, weight_of_dryresidue, weight_of_sample):
#                 raise ValueError("Form data cannot be None")
            
#             # Convert form inputs to integers
#             weight_of_crucible = int(weight_of_crucible)
#             weight_of_sample = int(weight_of_sample)
#             weight_of_dryresidue = int(weight_of_dryresidue)
            
#             # Perform calculation
#             result = (((weight_of_crucible * weight_of_dryresidue) - weight_of_crucible) / weight_of_sample) * 100.0
            
#             # Create custom response message
#             response_data = {
#                 'message': 'Determination of Total Solids calculation successful',
#                 'determination_of_total_solids': result
#             }
            
#             # Return JSON response
#             return JsonResponse(response_data)
#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_determination_of_total_solids.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed

# def calculate_determination_of_volatile_solids(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         weight_of_dryresidue = request.POST.get('weight_of_dryresidue')
#         weight_of_dryresidue_from_furnace = request.POST.get('weight_of_dryresidue_from_furnace')
#         weight_of_sample = request.POST.get('weight_of_sample')
        
#         try:
#             # Check if any form data is None
#             if None in (weight_of_dryresidue, weight_of_dryresidue_from_furnace, weight_of_sample):
#                 raise ValueError("Form data cannot be None")
            
#             # Convert form inputs to integers
#             weight_of_dryresidue = int(weight_of_dryresidue)
#             weight_of_dryresidue_from_furnace = int(weight_of_dryresidue_from_furnace)
#             weight_of_sample = int(weight_of_sample)
            
#             # Perform calculation
#             result = ((weight_of_dryresidue - weight_of_dryresidue_from_furnace) / weight_of_sample) * 100.0
            
#             # Create custom response message
#             response_data = {
#                 'message': 'Determination of Volatile Solids calculation successful',
#                 'determination_of_volatile_solids': result
#             }
            
#             # Return JSON response
#             return JsonResponse(response_data)
#         except ValueError as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Bad Request
#         except ValidationError as e:
#             return JsonResponse({'error': str(e)}, status=422)  # Unprocessable Entity (validation error)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)  # Internal Server Error
        
#     elif request.method == 'GET':
#         return render(request, 'BiogasCalculator/calculate_determination_of_volatile_solids.html')
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)  # Method Not Allowed

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PercentageOfFat, PercentageOfAsh, PercentageOfFibre, PercentageOfMoisture, PercentageOfProtein, PercentageOfCarbohydrate, DeterminationOfTotalSolids, DeterminationOfVolatileSolids
class CalculatePercentageOfFat(APIView):
    def get(self, request):
        # Parse query parameters
        weight_of_flask = request.query_params.get('weight_of_flask')
        weight_of_oil = request.query_params.get('weight_of_oil')
        weight_of_empty_flask = request.query_params.get('weight_of_empty_flask')
        weight_of_sample = request.query_params.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_flask, weight_of_oil, weight_of_empty_flask, weight_of_sample):
            return Response({'error': 'One or more query parameters are missing'}, status=400)

        try:
            # Convert query parameters to float
            weight_of_flask = float(weight_of_flask)
            weight_of_oil = float(weight_of_oil)
            weight_of_empty_flask = float(weight_of_empty_flask)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = (((weight_of_flask + weight_of_oil) - weight_of_empty_flask) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_fat': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input parameters'}, status=400)

class CalculatePercentageOfAsh(APIView):
    def get(self, request):
        # Parse query parameters
        weight_of_crucible = request.query_params.get('weight_of_crucible')
        weight_of_ash = request.query_params.get('weight_of_ash')
        weight_of_sample = request.query_params.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_crucible, weight_of_ash, weight_of_sample):
            return Response({'error': 'One or more query parameters are missing'}, status=400)

        try:
            # Convert query parameters to float
            weight_of_crucible = float(weight_of_crucible)
            weight_of_ash = float(weight_of_ash)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = (((weight_of_crucible + weight_of_ash) - weight_of_crucible) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_ash': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input parameters'}, status=400)

class CalculatePercentageOfProtein(APIView):
    def get(self, request):
        # Parse query parameters
        percentage_of_nitrogen = request.query_params.get('percentage_of_nitrogen')

        # Validate input parameters
        if percentage_of_nitrogen is None:
            return Response({'error': 'Query parameter "percentage_of_nitrogen" is missing'}, status=400)

        try:
            # Convert query parameter to float
            percentage_of_nitrogen = float(percentage_of_nitrogen)

            # Perform calculation
            result = percentage_of_nitrogen * PercentageOfProtein.CONVERSION_FACTOR

            # Return response
            return Response({'percentage_of_protein': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input parameters'}, status=400)

class CalculatePercentageOfMoisture(APIView):
    def get(self, request):
        # Parse query parameters
        weight_of_crucible = request.query_params.get('weight_of_crucible')
        weight_of_sample = request.query_params.get('weight_of_sample')
        weight_of_drymatter = request.query_params.get('weight_of_drymatter')

        # Validate input parameters
        if None in (weight_of_crucible, weight_of_sample, weight_of_drymatter):
            return Response({'error': 'One or more query parameters are missing'}, status=400)

        try:
            # Convert query parameters to float
            weight_of_crucible = float(weight_of_crucible)
            weight_of_sample = float(weight_of_sample)
            weight_of_drymatter = float(weight_of_drymatter)

            # Perform calculation
            result = (((weight_of_crucible + weight_of_sample) - (weight_of_crucible + weight_of_drymatter)) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_moisture': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input parameters'}, status=400)

class CalculateDeterminationOfTotalSolids(APIView):
    def get(self, request):
        # Parse query parameters
        weight_of_crucible = request.query_params.get('weight_of_crucible')
        weight_of_sample = request.query_params.get('weight_of_sample')
        weight_of_dryresidue = request.query_params.get('weight_of_dryresidue')

        # Validate input parameters
        if None in (weight_of_crucible, weight_of_sample, weight_of_dryresidue):
            return Response({'error': 'One or more query parameters are missing'}, status=400)

        try:
            # Convert query parameters to float
            weight_of_crucible = float(weight_of_crucible)
            weight_of_sample = float(weight_of_sample)
            weight_of_dryresidue = float(weight_of_dryresidue)

            # Perform calculation
            result = (((weight_of_crucible * weight_of_dryresidue) - weight_of_crucible) / weight_of_sample) * 100.0

            # Return response
            return Response({'determination_of_total_solids': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input parameters'}, status=400)

class CalculateDeterminationOfVolatileSolids(APIView):
    def get(self, request):
        # Parse query parameters
        weight_of_dryresidue = request.query_params.get('weight_of_dryresidue')
        weight_of_dryresidue_from_furnace = request.query_params.get('weight_of_dryresidue_from_furnace')
        weight_of_sample = request.query_params.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_dryresidue, weight_of_dryresidue_from_furnace, weight_of_sample):
            return Response({'error': 'One or more query parameters are missing'}, status=400)

        try:
            # Convert query parameters to float
            weight_of_dryresidue = float(weight_of_dryresidue)
            weight_of_dryresidue_from_furnace = float(weight_of_dryresidue_from_furnace)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = ((weight_of_dryresidue - weight_of_dryresidue_from_furnace) / weight_of_sample) * 100.0

            # Return response
            return Response({'determination_of_volatile_solids': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input parameters'}, status=400)

class CalculatePercentageOfFibre(APIView):
    def get(self, request):
        # Parse query parameters
        weight_of_dryresidue = request.query_params.get('weight_of_dryresidue')
        weight_of_ash = request.query_params.get('weight_of_ash')
        weight_of_sample = request.query_params.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_dryresidue, weight_of_ash, weight_of_sample):
            return Response({'error': 'One or more query parameters are missing'}, status=400)

        try:
            # Convert query parameters to float
            weight_of_dryresidue = float(weight_of_dryresidue)
            weight_of_ash = float(weight_of_ash)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = ((weight_of_dryresidue - weight_of_ash) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_fibre': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input parameters'}, status=400)

