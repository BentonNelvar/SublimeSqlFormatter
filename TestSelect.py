import unittest
from FormatSql import FormatSql 

class TestSelect(unittest.TestCase):
    
    def setUp(self):
        self.formatSql = FormatSql()

    def test_select_all_from_table( self ):
        input = '  sElect * froM table ;'
        result = self.formatSql.format( input )
        self.assertEqual( result , 'SELECT\t\t*\n\tFROM\ttable;' )

    def test_select_all_from_table_t( self ):
        input = 'select * from table t;'
        result = self.formatSql.format( input )
        self.assertEqual( result , 'SELECT\t\t*\n\tFROM\ttable AS t;' )

    def test_select_all_from_table_as_t( self ):
        input = 'select * from table as t;'
        result = self.formatSql.format( input )
        self.assertEqual( result , 'SELECT\t\t*\n\tFROM\ttable AS t;' )

    def test_select_t_all_from_table_t(self):
        input = 'select t.* from table as t;'
        result = self.formatSql.format( input )
        self.assertEqual( result , 'SELECT\t\tt.*\n\tFROM\ttable AS t;' )

    def test_select_t_c1_as_col1_t_c2_col2_from_table_t(self):
        input = 'select t.c1 as col1, t.c2 col2 from table as t;'
        result = self.formatSql.format( input )
        self.assertEqual( result , 'SELECT\t\tt.c1 AS col1,\n\t\t\tt.c2 AS col2\n\tFROM\ttable AS t;' )

    def test_select_t1_all_from_t1_select_t2_all_from_t2(self):
        input = 'select t1.* from t1; select t2.* from t2;'
        result = self.formatSql.format( input )
        self.assertEqual( result , 'SELECT\t\tt1.*\n\tFROM\tt1;\n\nSELECT\t\tt2.*\n\tFROM\tt2;' )

if __name__ == '__main__':
    unittest.main()