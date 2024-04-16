# # In tests.py file of your Django app

# from django.test import TestCase, Client
# from django.urls import reverse
# from .models import WasteCharacteristics

# class BiogasCalculatorViewTestCase(TestCase):
#     def setUp(self):
#         # Create a waste characteristics object for testing
#         WasteCharacteristics.objects.create(moisture_content=79.35, vs_content=96)

#     def test_calculate_biogas_view(self):
#         # Create a client to simulate HTTP requests
#         client = Client()

#         # Simulate a POST request with input data
#         response = client.post(reverse('calculate_biogas'), {'ratio_fvw': 75, 'ratio_cow_manure': 25})

#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)

#         # Check if the response contains the expected biogas production value in JSON format
#         self.assertAlmostEqual(response.json()['biogas_production'], 2.322724, places=5)