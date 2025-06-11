from datetime import date

import pytest

from pydanpak import Cashflows, total_cashflows


def test_total_cashflows():
    cf = Cashflows(cashflows={date(2023, 1, 1): 100.0, date(2023, 7, 1): -50.0})
    assert total_cashflows(cf) == 50.0


def test_empty_cashflows():
    cf = Cashflows(cashflows={})
    assert total_cashflows(cf) == 0.0 