import sublime
import sublime_plugin
from FormatSql import FormatSql
  
class FormatSqlCommand( sublime_plugin.TextCommand ):
    
    def run( self , edit ):
        formatSql = FormatSql()
        regionAll = sublime.Region( 0 , self.view.size() )
        print( self.view.settings().get('syntax') )
        input = self.view.substr( regionAll )
        if not input:
            print( 'No text to parse' )
        else:
            output = formatSql.format( input )
            self.view.replace( edit , regionAll , output )
            self.view.set_syntax_file( 'Packages/SQL/SQL.tmLanguage' )

