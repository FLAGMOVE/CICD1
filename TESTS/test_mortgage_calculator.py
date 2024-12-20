import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from mortgage_calculator import calculate_monthly_payment

import pytest

def test_monthly_payment():
    assert calculate_monthly_payment(100000, 5, 30) == pytest.approx(536.82, rel=1e-2)
    assert calculate_monthly_payment(50000, 3, 15) == pytest.approx(345.29, rel=1e-2)
    assert calculate_monthly_payment(100000, 0, 30) == pytest.approx(277.78, rel=1e-2)
