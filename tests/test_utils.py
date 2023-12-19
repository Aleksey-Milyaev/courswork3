import os
import json
from src.utils import get_operation, get_sorted_state, get_sorted_date


def test_get_operation():
    assert len(get_operation()) == 101

def test_get_sorted_state():
    operations = get_operation()
    assert len(get_sorted_state(operations)) == 85

def test_get_sorted_date():
    operations = get_operation()
    sorted_state = get_sorted_state(operations)
    assert get_sorted_date(sorted_state) == ['2019-12-08T22:46:21.935582','2019-12-07T06:17:14.634890','2019-11-19T09:22:25.899614','2019-11-13T17:38:04.800051','2019-11-05T12:04:13.781725',]