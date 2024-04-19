import json
from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from unittest.mock import MagicMock

from .models import BiogasProduction
from .views import calculate_biogas

class CalculateBiogasTestCase(TestCase):
    def test_post_request(self):
        # Create a POST request with mock form data
        post_data = {
            'ratio_fvw': '50.0',
            'ratio_cow_manure': '30.0',
            'moisture_content': '20.0',
            'vs_content': '80.0',
        }
        request = MagicMock()
        request.method = 'POST'
        request.POST = post_data

        # Call the view function with the mock request
        response = calculate_biogas(request)

        # Check if the response is a JSON response
        self.assertIsInstance(response, JsonResponse)

        # Check if the biogas production data is saved in the database
        biogas_production = BiogasProduction.objects.first()
        self.assertIsNotNone(biogas_production)

        # Check if the response contains the expected data
        expected_response_data = {
            'biogas_production': biogas_production.biogas_production,
            'response_message': f"The biogas production is {biogas_production.biogas_production:.2f} cubic meters."
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), json.dumps(expected_response_data))

    def test_get_request(self):
        # Create a GET request
        request = MagicMock()
        request.method = 'GET'

        # Call the view function with the mock request
        response = calculate_biogas(request)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

    def test_invalid_method(self):
        # Create a request with an invalid method
        request = MagicMock()
        request.method = 'PUT'

        # Call the view function with the mock request
        response = calculate_biogas(request)

        # Check if the response contains the expected error message
        expected_response_data = {'error': 'Method not allowed'}
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.content.decode('utf-8'), json.dumps(expected_response_data))
