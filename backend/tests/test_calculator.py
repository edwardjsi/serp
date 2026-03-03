from decimal import Decimal
import unittest
from backend.engine.calculator import (
    get_years_to_retirement,
    get_retirement_years,
    calculate_inflated_expense,
    calculate_corpus_required,
    calculate_asset_future_value,
    calculate_future_assets,
    calculate_deficit,
    calculate_fixed_sip,
    calculate_stepup_sip,
    project_wealth_pre_retirement,
    project_wealth_post_retirement
)

class TestCalculator(unittest.TestCase):
    
    def test_get_years_to_retirement(self):
        self.assertEqual(get_years_to_retirement(Decimal('30'), Decimal('60')), Decimal('30'))
        with self.assertRaises(ValueError):
            get_years_to_retirement(Decimal('60'), Decimal('30'))

    def test_get_retirement_years(self):
        self.assertEqual(get_retirement_years(Decimal('60'), Decimal('85')), Decimal('25'))
        with self.assertRaises(ValueError):
            get_retirement_years(Decimal('85'), Decimal('60'))

    def test_calculate_inflated_expense(self):
        annual_expense = Decimal('1200000') # 12L
        inflation = Decimal('0.06') # 6%
        years = Decimal('30')
        # 12L * (1.06^30) = ~68,92,139
        expected = annual_expense * ((Decimal('1') + inflation) ** years)
        result = calculate_inflated_expense(annual_expense, inflation, years)
        self.assertAlmostEqual(result, expected, places=2)

    def test_calculate_corpus_required(self):
        inflated_expense = Decimal('6892139')
        post_ret_return = Decimal('0.08') # 8%
        inflation = Decimal('0.06') # 6%
        n = Decimal('25')
        
        result = calculate_corpus_required(inflated_expense, post_ret_return, inflation, n)
        # Verify it's greater than 0
        self.assertTrue(result > Decimal('0'))
        
        # Test unsustainable withdrawal
        with self.assertRaises(ValueError):
            calculate_corpus_required(inflated_expense, Decimal('0.05'), Decimal('0.06'), n)

    def test_calculate_future_assets(self):
        assets = [Decimal('500000'), Decimal('1000000')]
        pre_ret_return = Decimal('0.10') # 10%
        years = Decimal('10')
        
        result = calculate_future_assets(assets, pre_ret_return, years)
        expected = Decimal('1500000') * ((Decimal('1.10')) ** years)
        self.assertAlmostEqual(result, expected, places=2)

    def test_calculate_deficit(self):
        corpus = Decimal('10000000')
        future_assets = Decimal('3000000')
        lumpsum = Decimal('1000000')
        
        self.assertEqual(calculate_deficit(corpus, future_assets, lumpsum), Decimal('6000000'))
        # Test negative deficit normalizes to 0
        self.assertEqual(calculate_deficit(corpus, Decimal('12000000'), Decimal('0')), Decimal('0'))

    def test_calculate_fixed_sip(self):
        deficit = Decimal('6000000')
        pre_ret_return = Decimal('0.12') # 12%
        years = Decimal('10')
        
        sip = calculate_fixed_sip(deficit, pre_ret_return, years)
        self.assertTrue(sip > Decimal('0'))
        
        # Test 0 deficit
        self.assertEqual(calculate_fixed_sip(Decimal('0'), pre_ret_return, years), Decimal('0'))

    def test_calculate_stepup_sip(self):
        deficit = Decimal('6000000')
        pre_ret_return = Decimal('0.12')
        step_up = Decimal('0.05')
        years = Decimal('10')
        
        sip = calculate_stepup_sip(deficit, pre_ret_return, step_up, years)
        self.assertTrue(sip > Decimal('0'))

    def test_wealth_projections(self):
        # Pre-retirement
        wealth = project_wealth_pre_retirement(Decimal('100000'), Decimal('0.10'), Decimal('50000'))
        self.assertEqual(wealth, Decimal('160000'))
        
        # Post-retirement
        remaining = project_wealth_post_retirement(Decimal('10000000'), Decimal('0.08'), Decimal('1000000'))
        self.assertEqual(remaining, Decimal('9800000'))

if __name__ == '__main__':
    unittest.main()
