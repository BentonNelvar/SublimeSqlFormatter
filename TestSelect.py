import unittest
from FormatSql import FormatSql 

class TestSelect(unittest.TestCase):
    
    def setUp(self):
        self.formatSql = FormatSql()

    def test_select_all_from( self ):
        input = '  sElect * froM table ;'
        result = self.formatSql.format( input )
        self.assertEqual( result , 'SELECT\t\t*\n\tFROM\ttable;' )

if __name__ == '__main__':
    unittest.main()