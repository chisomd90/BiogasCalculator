# from unittest import TestCase
# from .views import calculate_biogas_internal

# class BiogasCalculationTest(TestCase):

#     def test_default_ratios(self):
#         """Test biogas calculation with default ratios (75:25)"""
#         total_vs, biogas_production = calculate_biogas_internal()
#         expected_total_vs = (75 * 96 + 25 * 96) / 100  # 91
#         expected_biogas_production = 0.037 * (expected_total_vs * (1 - 79.35 / 100))  # 2.22

#         self.assertEqual(total_vs, expected_total_vs)
#         self.assertAlmostEqual(biogas_production, expected_biogas_production)

#     def test_custom_ratios(self):
#         """Test biogas calculation with custom ratios (60:40)"""
#         total_vs, biogas_production = calculate_biogas_internal(60, 40)
#         expected_total_vs = (60 * 96 + 40 * 96) / 100  # 86.4
#         expected_biogas_production = 0.037 * (expected_total_vs * (1 - 79.35 / 100))  # 2.09

#         self.assertEqual(total_vs, expected_total_vs)
#         self.assertAlmostEqual(biogas_production, expected_biogas_production)

#     def test_invalid_ratio_sum(self):
#         """Test error handling for invalid ratio sum (over 100)"""
#         with self.assertRaises(ValueError):
#             calculate_biogas_internal(80, 30)  # Ratio sum exceeds 100

#  # Run the tests
# if __name__ == '__main__':
#     unittest.main()
