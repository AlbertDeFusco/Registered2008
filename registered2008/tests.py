from .main import read
import unittest

from pandas.api.types import is_integer_dtype, is_string_dtype, is_float_dtype

class TestStructure(unittest.TestCase):
    def setUp(self):
        self.df = read()

        self.reference = {
            'county':is_string_dtype,
            'year': is_integer_dtype,
            'Total Voters': is_float_dtype
        }

    def test_columns(self):
        assert self.reference.keys() == set(self.df.columns), f'{self.reference.keys()} does not match {df.columns}'

    def test_dtypes(self):
        dtypes = self.df.dtypes
        for c, func in self.reference.items():
            assert func(dtypes[c]), f'{func} found dtype {dtypes[c]} for {c}.'
