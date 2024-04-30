from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PercentageOfProtein

class CalculatePercentageOfFat(APIView):
    def post(self, request):
        # Parse request data
        weight_of_flask = request.data.get('weight_of_flask')
        weight_of_oil = request.data.get('weight_of_oil')
        weight_of_empty_flask = request.data.get('weight_of_empty_flask')
        weight_of_sample = request.data.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_flask, weight_of_oil, weight_of_empty_flask, weight_of_sample):
            return Response({'error': 'One or more parameters are missing in the request body'}, status=400)

        try:
            # Convert input data to float
            weight_of_flask = float(weight_of_flask)
            weight_of_oil = float(weight_of_oil)
            weight_of_empty_flask = float(weight_of_empty_flask)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = (((weight_of_flask + weight_of_oil) - weight_of_empty_flask) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_fat': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input data'}, status=400)
        

class CalculatePercentageOfAsh(APIView):
    def post(self, request):
        # Parse request data
        weight_of_crucible = request.data.get('weight_of_crucible')
        weight_of_ash = request.data.get('weight_of_ash')
        weight_of_sample = request.data.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_crucible, weight_of_ash, weight_of_sample):
            return Response({'error': 'One or more parameters are missing in the request body'}, status=400)

        try:
            # Convert input data to float
            weight_of_crucible = float(weight_of_crucible)
            weight_of_ash = float(weight_of_ash)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = (((weight_of_crucible + weight_of_ash) - weight_of_crucible) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_ash': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input data'}, status=400)

class CalculatePercentageOfProtein(APIView):
    def post(self, request):
        # Parse request data
        percentage_of_nitrogen = request.data.get('percentage_of_nitrogen')

        # Validate input parameters
        if percentage_of_nitrogen is None:
            return Response({'error': 'Query parameter "percentage_of_nitrogen" is missing'}, status=400)

        try:
            # Convert input data to float
            percentage_of_nitrogen = float(percentage_of_nitrogen)

            # Perform calculation
            result = percentage_of_nitrogen * PercentageOfProtein.CONVERSION_FACTOR

            # Return response
            return Response({'percentage_of_protein': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input data'}, status=400)

class CalculatePercentageOfMoisture(APIView):
    def post(self, request):
        # Parse request data
        weight_of_crucible = request.data.get('weight_of_crucible')
        weight_of_sample = request.data.get('weight_of_sample')
        weight_of_drymatter = request.data.get('weight_of_drymatter')

        # Validate input parameters
        if None in (weight_of_crucible, weight_of_sample, weight_of_drymatter):
            return Response({'error': 'One or more parameters are missing in the request body'}, status=400)

        try:
            # Convert input data to float
            weight_of_crucible = float(weight_of_crucible)
            weight_of_sample = float(weight_of_sample)
            weight_of_drymatter = float(weight_of_drymatter)

            # Perform calculation
            result = (((weight_of_crucible + weight_of_sample) - (weight_of_crucible + weight_of_drymatter)) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_moisture': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input data'}, status=400)

class CalculateDeterminationOfTotalSolids(APIView):
    def post(self, request):
        # Parse request data
        weight_of_crucible = request.data.get('weight_of_crucible')
        weight_of_sample = request.data.get('weight_of_sample')
        weight_of_dryresidue = request.data.get('weight_of_dryresidue')

        # Validate input parameters
        if None in (weight_of_crucible, weight_of_sample, weight_of_dryresidue):
            return Response({'error': 'One or more parameters are missing in the request body'}, status=400)

        try:
            # Convert input data to float
            weight_of_crucible = float(weight_of_crucible)
            weight_of_sample = float(weight_of_sample)
            weight_of_dryresidue = float(weight_of_dryresidue)

            # Perform calculation
            result = (((weight_of_crucible * weight_of_dryresidue) - weight_of_crucible) / weight_of_sample) * 100.0

            # Return response
            return Response({'determination_of_total_solids': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input data'}, status=400)

class CalculateDeterminationOfVolatileSolids(APIView):
    def post(self, request):
        # Parse request data
        weight_of_dryresidue = request.data.get('weight_of_dryresidue')
        weight_of_dryresidue_from_furnace = request.data.get('weight_of_dryresidue_from_furnace')
        weight_of_sample = request.data.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_dryresidue, weight_of_dryresidue_from_furnace, weight_of_sample):
            return Response({'error': 'One or more parameters are missing in the request body'}, status=400)

        try:
            # Convert input data to float
            weight_of_dryresidue = float(weight_of_dryresidue)
            weight_of_dryresidue_from_furnace = float(weight_of_dryresidue_from_furnace)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = ((weight_of_dryresidue - weight_of_dryresidue_from_furnace) / weight_of_sample) * 100.0

            # Return response
            return Response({'determination_of_volatile_solids': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input data'}, status=400)

class CalculatePercentageOfFibre(APIView):
    def post(self, request):
        # Parse request data
        weight_of_dryresidue = request.data.get('weight_of_dryresidue')
        weight_of_ash = request.data.get('weight_of_ash')
        weight_of_sample = request.data.get('weight_of_sample')

        # Validate input parameters
        if None in (weight_of_dryresidue, weight_of_ash, weight_of_sample):
            return Response({'error': 'One or more parameters are missing in the request body'}, status=400)

        try:
            # Convert input data to float
            weight_of_dryresidue = float(weight_of_dryresidue)
            weight_of_ash = float(weight_of_ash)
            weight_of_sample = float(weight_of_sample)

            # Perform calculation
            result = ((weight_of_dryresidue - weight_of_ash) / weight_of_sample) * 100.0

            # Return response
            return Response({'percentage_of_fibre': result}, status=200)
        except ValueError:
            return Response({'error': 'Invalid input data'}, status=400)
