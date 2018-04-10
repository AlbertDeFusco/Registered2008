'''SQL table: Pennsylvania registered voters in 2008 by county'''

__version__ = '0.1'

from .main import read

def test():
    import unittest
    from .tests import TestStructure

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestStructure)

    runner = unittest.TextTestRunner()
    runner.run(suite)
